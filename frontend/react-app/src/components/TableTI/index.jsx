import { TechnicalInspectService, MachinesService } from "../../../Machines";
import { useState, useEffect } from 'react';

const tiService = new TechnicalInspectService();
const machineService = new MachinesService(); 

function TableTI({ data }) {
    const [editRowId, setEditRowId] = useState(null);
    const [formData, setFormData] = useState({});
    const [options, setOptions] = useState({
        typesTI: [],
        machines: [],
        serviceCompanies: []
    });

    const userRole = localStorage.getItem('role');
    const canEdit = ['client', 'manager', 'service_company'].includes(userRole);

    // Загрузка справочников
    useEffect(() => {
        Promise.all([
            tiService.getTypesTI(),
            machineService.getMachines(),
            machineService.getServiceCompanies()
        ])
        .then(([types, machines, companies]) => {
            setOptions({
                typesTI: types.data.results || types.data || [],
                machines: machines.data.results || machines.data || [],
                serviceCompanies: companies.data.results || companies.data || []
            });
        })
        .catch(err => console.error("Ошибка загрузки:", err));
    }, []);

    const startEdit = (item) => {
        setEditRowId(item.id);
        setFormData({
            ...item,
            // Передаем ID для работы select (из полей которые НЕ _info)
            type_ti: item.type_ti_info?.id || item.type_ti,
            machine: item.machine_info?.id || item.machine,
            service_company: item.service_company_info?.id || item.service_company
        });
    }

    const handlerSave = (id) => {
        // Подготавливаем данные: убираем лишние вложенные объекты _info перед отправкой
        const { type_ti_info, machine_info, service_company_info, ...payload } = formData;

        tiService.updateTI(id, payload)
            .then(() => {
                alert("Данные обновлены");
                setEditRowId(null);
                window.location.reload(); 
            })
            .catch(err => {
                console.error("Ошибка обновления:", err.response?.data);
                alert("Ошибка при сохранении: " + JSON.stringify(err.response?.data || "Ошибка сервера"));
            });
    }

    const RenderSelect = ({ name, value, list, labelField = "name" }) => (
        <select 
            value={value || ""} 
            style={{ width: "100%", padding: "4px" }}
            onChange={e => {
                const val = e.target.value;
                setFormData({
                    ...formData, 
                    [name]: val ? Number(val) : null
                });
            }}
        >
            <option value="">Выберите...</option>
            {list && list.map(obj => (
                <option key={obj.id} value={obj.id}>
                    {obj[labelField] || `ID: ${obj.id}`}
                </option>
            ))}
        </select>
    );

    return (
        <table border="1" style={{ width: "100%", marginTop: "20px", borderCollapse: "collapse" }}>
            <thead>
                <tr style={{ backgroundColor: "#f2f2f2" }}>
                    <th>Вид ТО</th>
                    <th>Дата проведения</th>
                    <th>Наработка (м/час)</th>
                    <th>№ заказ-наряда</th>
                    <th>Машина (Зав. №)</th>
                    <th>Сервисная компания</th>
                    {canEdit && <th>Действие</th>}
                </tr>
            </thead>
            <tbody>
                {data.map((item) => (
                    <tr key={item.id}>
                        {editRowId === item.id ? (
                            <>
                                <td>
                                    <RenderSelect 
                                        name="type_ti" 
                                        value={formData.type_ti} 
                                        list={options.typesTI} 
                                        labelField="name"
                                    />
                                </td>
                                <td>
                                    <input 
                                        type="date" 
                                        value={formData.date_service || ""} 
                                        onChange={e => setFormData({...formData, date_service: e.target.value})}
                                    />
                                </td>
                                <td>
                                    <input 
                                        type="number" 
                                        value={formData.running_hours || ""} 
                                        onChange={e => setFormData({...formData, running_hours: e.target.value})}
                                    />
                                </td>
                                <td>
                                    <input 
                                        type="text" 
                                        value={formData.order || ""} 
                                        onChange={e => setFormData({...formData, order: e.target.value})}
                                    />
                                </td>
                                <td>
                                    <RenderSelect 
                                        name="machine" 
                                        value={formData.machine} 
                                        list={options.machines} 
                                        labelField="unique_machine_number" 
                                    />
                                </td>
                                <td>
                                    <RenderSelect 
                                        name="service_company" 
                                        value={formData.service_company} 
                                        list={options.serviceCompanies} 
                                        labelField="name"
                                    />
                                </td>
                                <td style={{ textAlign: "center" }}>
                                    <button onClick={() => handlerSave(item.id)}>ОК</button>
                                    <button onClick={() => setEditRowId(null)} style={{ marginLeft: "5px" }}>Отмена</button>
                                </td>
                            </>
                        ) : (
                            <>
                                <td>{item.type_ti_info?.name || "—"}</td>
                                <td>{item.date_service}</td>
                                <td>{item.running_hours}</td>
                                <td>{item.order}</td>
                                <td>{item.machine_info?.unique_machine_number || "—"}</td>
                                <td>{item.service_company_info?.name || "—"}</td>
                                {canEdit && (
                                    <td style={{ textAlign: "center" }}>
                                        <button onClick={() => startEdit(item)}>Редактировать</button>
                                    </td>
                                )}
                            </>
                        )}
                    </tr>
                ))}
            </tbody>
        </table>
    );
}

export default TableTI;
