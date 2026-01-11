import { useState, useEffect, useRef } from 'react';
import { ComplaintService, MachinesService } from "../../../Machines";

const complaintService = new ComplaintService();
const machineService = new MachinesService();

function TableComplaint({ data }) {
    const [editRowId, setEditRowId] = useState(null);
    const [formData, setFormData] = useState({});
    
    // Фильтрация
    const [activeFilter, setActiveFilter] = useState({
        failedUnits: [],
        methodsRestoration: [],
        machines: [],
        serviceCompanies: []
    });

    // Состояния для справочников
    const [options, setOptions] = useState({
        failedUnits: [],
        methodsRestoration: [],
        machines: [],
        serviceCompanies: []
    });

    const userRole = localStorage.getItem('role');
    const canEdit = ['manager', 'service_company'].includes(userRole);

    // Загрузка справочников при монтировании компонента
    useEffect(() => {
        Promise.all([
            complaintService.getFailedUnits(),
            complaintService.getMethodsRestoration(),
            machineService.getMachines(),
            machineService.getServiceCompanies()
        ])
        .then(([units, methods, machines, companies]) => {
            setOptions({
                failedUnits: units.data.results || units.data || [],
                methodsRestoration: methods.data.results || methods.data || [],
                machines: machines.data.results || machines.data || [],
                serviceCompanies: companies.data.results || companies.data || []
            });
            console.log(data)
        })
        .catch(err => console.error("Ошибка загрузки справочников рекламаций:", err));
    }, []);

    if (!data || data.length === 0) {
        return <p style={{marginTop: "20px"}}>Записей Рекламации не найдено</p>;
    }
    const startEdit = (item) => {
        setEditRowId(item.id);
        setFormData({
            ...item,
            // Мапим объекты в ID для выпадающих списков
            failed_unit: item.failed_unit_info?.id || item.failed_unit,
            method_restoration: item.method_restoration_info?.id || item.method_restoration,
            machine: item.machine_info?.id || item.machine,
            service_company: item.service_company_info?.id || item.service_company
        });
    }
    
    const handlerSave = (id) => {
        // Отправляем formData
        complaintService.updateComplaint(id, formData)
            .then(() => {
                alert("Данные рекламации обновлены");
                setEditRowId(null);
                window.location.reload();  // Перезагрузка страницы, после обновления данных
            })
            .catch(err => {
                console.error("Ошибка обновления:", err.response?.data || err);
                alert("Ошибка при сохранении: " + JSON.stringify(err.response?.data || "Ошибка сервера"));
            });
    }

    const RenderSelect = ({ name, value, list, labelField = "name" }) => (
        <select 
            value={value || ""} 
            style={{ width: "100%" }}
            onChange={e => setFormData({
                ...formData,
                [name]: e.target.value ? Number(e.target.value) : null
            })}
        >
            <option value="">Выберите...</option>
            {list.map(obj => (
                <option key={obj.id} value={obj.id}>
                    {obj[labelField]}
                </option>
            ))}
        </select>
    );

    const Filter = ({ name, category, data, selectedValues, onChange, onReset }) => {
        const formRef = useRef(null);

        return (
            <div className="filter-group" style={{ margin: '10px 0', border: '1px solid #ccc', padding: '10px' }}>
                <strong>{name}</strong>
                <form ref={formRef} onReset={() => onReset(category)}>
                    {data && data.map((item) => (
                        <label key={item.id} style={{ display: 'block' }}>
                            <input
                                type="checkbox"
                                value={item.id}
                                checked={selectedValues.includes(String(item.id))}
                                onChange={() => onChange(category, item.id)}
                            />
                            {item.name}
                        </label>
                    ))}
                    <button type="reset" style={{ marginTop: '5px' }} disabled={selectedValues.length === 0}>
                        Сбросить {name}
                    </button>
                </form>
            </div>
        );
    };

    const handleFilterChange = (category, id) => {
        setActiveFilter(prev => {
            const currentCategory = prev[category];
            const stringId = String(id);
            const newValues = currentCategory.includes(stringId)
                ? currentCategory.filter(item => item !== stringId)
                : [...currentCategory, stringId];
            
            return { ...prev, [category]: newValues };
        });
    };

    const handleFilterReset = (category) => {
        setActiveFilter(prev => ({ ...prev, [category]: [] }));
    };

    return (
        <>
        <div className="filters-container" style={{ display: 'flex', gap: '20px' }}>
            <Filter 
                name="Узел отказа" 
                category="failedUnits"
                data={options.failedUnits} 
                selectedValues={activeFilter.failedUnits}
                onChange={handleFilterChange}
                onReset={handleFilterReset}
            />
            <Filter 
                name="Метод восстановления" 
                category="methodsRestoration"
                data={options.methodsRestoration} 
                selectedValues={activeFilter.methodsRestoration}
                onChange={handleFilterChange}
                onReset={handleFilterReset}
            />
        </div>
        <table border="1" style={{ width: "100%", marginTop: "20px", borderCollapse: "collapse" }}>
            <thead>
                <tr style={{ backgroundColor: "#f2f2f2" }}>
                    <th>Дата отказа</th>
                    <th>Наработка</th>
                    <th>Узел отказа</th>
                    <th>Описание</th>
                    <th>Способ восст.</th>
                    <th>Запчасти</th>
                    <th>Дата восст.</th>
                    <th>Простой</th>
                    <th>Машина</th>
                    {canEdit && <th>Действие</th>}
                </tr>
            </thead>
            <tbody>
                {data
                    .filter(item => {
                        // Фильтр по узлу отказа
                        const failUnitMath = activeFilter.failedUnits.length === 0 || 
                            activeFilter.failedUnits.includes(String(item.failed_unit_info?.id));

                        // Фильтр методу восстановления
                        const methodsRestorationMath = activeFilter.methodsRestoration.length === 0 || 
                            activeFilter.methodsRestoration.includes(String(item.method_restoration_info?.id));
                        return failUnitMath && methodsRestorationMath;
                    })
                    .map((item) => (
                    <tr key={item.id}>
                        {editRowId === item.id ? (
                            <>
                
                                <td>
                                    <input type="date" value={formData.date_failure || ""} 
                                        onChange={e => setFormData({...formData, date_failure: e.target.value})} />
                                </td>
                                <td>
                                    <input type="number" value={formData.running_hours || ""} 
                                        onChange={e => setFormData({...formData, running_hours: e.target.value})} />
                                </td>
                                <td>
                                    <RenderSelect name="failed_unit" value={formData.failed_unit} list={options.failedUnits} />
                                </td>
                                <td>
                                    <input type="text" value={formData.description_failed || ""} 
                                        onChange={e => setFormData({...formData, description_failed: e.target.value})} />
                                </td>
                                <td>
                                    <RenderSelect name="method_restoration" value={formData.method_restoration} list={options.methodsRestoration} />
                                </td>
                                <td>
                                    <input type="text" value={formData.spare_parts_usage || ""} 
                                        onChange={e => setFormData({...formData, spare_parts_usage: e.target.value})} />
                                </td>
                                <td>
                                    <input type="date" value={formData.date_restoration || ""} 
                                        onChange={e => setFormData({...formData, date_restoration: e.target.value})} />
                                </td>
                                <td>{item.time_stop} дн.</td>
                                <td>
                                    <RenderSelect 
                                        name="machine" 
                                        value={formData.machine} 
                                        list={options.machines} 
                                        labelField="unique_machine_number" 
                                    />
                                </td>
                                <td>
                                    <button onClick={() => handlerSave(item.id)}>ОК</button>
                                    <button onClick={() => setEditRowId(null)}>Отмена</button>
                                </td>
                            </>
                        ) : (
                            <>
                                <td>{item.date_failure}</td>
                                <td>{item.running_hours}</td>
                                <td>{item.failed_unit_info?.name || "—"}</td>
                                <td>{item.description_failed}</td>
                                <td>{item.method_restoration_info?.name || "—"}</td>
                                <td>{item.spare_parts_usage}</td>
                                <td>{item.date_restoration}</td>
                                <td>{item.time_stop} дн.</td>
                                <td>{item.machine_info?.unique_machine_number}</td>
                                {canEdit && (
                                    <td>
                                        <button onClick={() => startEdit(item)}>Редактировать</button>
                                    </td>
                                )}
                            </>
                        )}
                    </tr>
                ))}
            </tbody>
        </table>
        </>
    );
    
}

export default TableComplaint;
