import { useState, useEffect, useRef } from 'react';
import { MachinesService } from '../../../Machines.jsx';
import { Link } from 'react-router-dom';


const machineService = new MachinesService(); 

export function TableMachines({ data }) {
    const [editRowId, setEditRowId] = useState(null);
    const [formData, setFormData] = useState({});

    const [activeFilter, setActiveFilter] = useState({
        models: [], engines: [], transmissions: [], driveAxles: [], steerAxles: []
    });
    
    // Состояния для справочников
    const [options, setOptions] = useState({
        models: [], engines: [], transmissions: [], driveAxles: [], steerAxles: []
    });

    const userRole = localStorage.getItem('role');
    const canEdit = ['manager'].includes(userRole);

    useEffect(() => {
        Promise.all([
            machineService.getModels(),
            machineService.getEngines(),
            machineService.getTransmissions(),
            machineService.getDriveAxles(),
            machineService.getSteerAxles(),
            machineService.getClients(),
        ]).then(([m, e, t, da, sa, c]) => {
            setOptions({
                models: m.data, 
                engines: e.data, 
                transmissions: t.data, 
                driveAxles: da.data, 
                steerAxles: sa.data,
                clients: c.data,
            });
        }).catch(err => console.error("Ошибка загрузки справочников", err));
    }, []); 

    const startEdit = (item) => {
        setEditRowId(item.id);
        // Превращаем объекты в ID для работы <select>
        setFormData({
            ...item,
            model_machine: item.model_machine_info?.id || item.model_machine,
            model_engine: item.model_engine_info?.id || item.model_engine,
            model_transmission: item.model_transmission_info?.id || item.model_transmission,
            model_drive_axle: item.model_drive_axle_info?.id || item.model_drive_axle,
            model_steer_axle: item.model_steer_axle_info?.id || item.model_steer_axle,
            clients: item.client_info?.id || item.client,
        });
    };
    
    const handlerSave = (id) => {
        machineService.updateMachine(id, formData)
        .then((response) => {
            console.log("Успешно обновлено:", response.data);
            
            // Выключаем режим редактирования
            setEditRowId(null);
            
            // Перезагружаем страницу для обновления данных в таблице
            window.location.reload();
        })
        .catch((err) => {
            console.error("Детали ошибки:", err.response?.data);
            
            const errorMsg = err.response?.data?.detail || "Ошибка при сохранении";
            alert("Произошла ошибка: " + errorMsg);
        });
};

    // Компонент для отрисовки <select> чтобы не дублировать код
    const RenderSelect = ({ name, value, list, labelField = 'name' }) => (
        <select 
            value={value || ""} 
            onChange={e => setFormData({
                ...formData, 
                [name]: e.target.value ? Number(e.target.value) : null 
            })}
        >
            <option value="">Выберите...</option>
            {list && list.map(obj => (
                <option key={obj.id} value={obj.id}>
                    {obj[labelField] || obj.name || `ID: ${obj.id}`}
                </option>
            ))}
        </select>
    );

    const CreateMachine = () => (
        <div>
            <input>Зав. № машины</input>
            <RenderSelect name="model_machine" value={formData.model_machine} list={options.models} />
            <RenderSelect name="model_engine" value={formData.model_engine} list={options.engines} />
            <input>№ Двигателя</input>
            <RenderSelect name="model_transmission" value={formData.model_transmission} list={options.transmissions} />
            <input>Зав. № трансмиссии</input>
            <RenderSelect name="model_drive_axle" value={formData.model_drive_axle} list={options.driveAxles} />
            <input>Зав. № ведущего моста</input>
            <RenderSelect name="model_steer_axle" value={formData.model_steer_axle} list={options.steerAxles} />
            <input>Зав. № управляемого моста</input>
        </div>

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
            name="Модель техники" 
            category="models"
            data={options.models} 
            selectedValues={activeFilter.models}
            onChange={handleFilterChange}
            onReset={handleFilterReset}
        />
        <Filter 
            name="Двигатель" 
            category="engines"
            data={options.engines} 
            selectedValues={activeFilter.engines}
            onChange={handleFilterChange}
            onReset={handleFilterReset}
        />
        <Filter 
            name="Трансмиссии" 
            category="transmissions"
            data={options.transmissions} 
            selectedValues={activeFilter.transmissions}
            onChange={handleFilterChange}
            onReset={handleFilterReset}
        />
        <Filter 
            name="Ведущий мост" 
            category="driveAxles"
            data={options.driveAxles} 
            selectedValues={activeFilter.driveAxles}
            onChange={handleFilterChange}
            onReset={handleFilterReset}
        />
        <Filter 
            name="Управляемый мост" 
            category="steerAxles"
            data={options.steerAxles} 
            selectedValues={activeFilter.steerAxles}
            onChange={handleFilterChange}
            onReset={handleFilterReset}
        />
    </div>
        <table border="1" style={{ width: "100%", marginTop: "20px", borderCollapse: "collapse" }}>
            <thead>
                <tr style={{ backgroundColor: "#f2f2f2" }}>
                    <th>Зав. № машины</th>
                    <th>Модель техники</th>
                    <th>Модель двигателя</th>
                    <th>Зав. № двигателя</th>
                    <th>Модель трансмиссии</th>
                    <th>Зав. № трансмиссии</th>
                    <th>Модель ведущий мост</th>
                    <th>Зав. № ведущего моста</th>
                    <th>Модель управляемого мост</th>
                    <th>Зав. № управляемого моста</th>
                    {canEdit &&
                    <>
                    <th>Договор поставки №, дата</th>
                    <th>Дата отгрузки с завода</th>
                    <th>Грузополучатель</th>
                    <th>Адрес поставки</th>
                    <th>Комплектация</th>
                    <th>Клиент</th>
                    <th>Действие</th>
                    </>
                    }
                </tr>
            </thead>
            <tbody>
                {data
                    .filter(machine => {
                        // Фильтр по моделям техники
                        const modelMatch = activeFilter.models.length === 0 || 
                            activeFilter.models.includes(String(machine.model_machine_info?.id));

                        // Фильтр по двигателям
                        const engineMatch = activeFilter.engines.length === 0 || 
                            activeFilter.engines.includes(String(machine.model_engine_info?.id));

                        // Фильтр по трансмиссиям
                        const transmissionMatch = activeFilter.transmissions.length === 0 || 
                            activeFilter.transmissions.includes(String(machine.model_transmission_info?.id));

                        // Фильтр по ведущим мостам
                        const driveAxleMatch = activeFilter.driveAxles.length === 0 || 
                            activeFilter.driveAxles.includes(String(machine.model_drive_axle_info?.id));

                        // Фильтр по управляемым мостам
                        const steerAxleMatch = activeFilter.steerAxles.length === 0 || 
                            activeFilter.steerAxles.includes(String(machine.model_steer_axle_info?.id));

                        // Машина показывается только если прошла ВСЕ проверки (логическое И)
                        return modelMatch && engineMatch && transmissionMatch && driveAxleMatch && steerAxleMatch;
                    })
                    .map((machine) => (
                    <tr key={machine.id}>
                        {editRowId === machine.id ? (
                            <>  
                                {/* № Зав.техники*/}
                                <td>
                                    <input 
                                        type="text" 
                                        value={formData.unique_machine_number || ""} 
                                        onChange={e => setFormData({...formData, unique_machine_number: e.target.value})}
                                    />
                                </td>

                                {/* Модель техники */}
                                <td><RenderSelect name="model_machine" value={formData.model_machine} list={options.models} /></td>

                                {/* Модель двигателя */}
                                <td><RenderSelect name="model_engine" value={formData.model_engine} list={options.engines} /></td>

                                {/* № Зав.двигателя*/}
                                <td>
                                    <input 
                                        type="text" 
                                        value={formData.number_engine || ""} 
                                        onChange={e => setFormData({...formData, number_engine: e.target.value})}
                                    />
                                </td>

                                {/* Модель трансмисиии*/}
                                <td><RenderSelect name="model_transmission" value={formData.model_transmission} list={options.transmissions} /></td>

                                {/* № Зав.трансмиссии*/}
                                <td>
                                    <input 
                                        type="text" 
                                        value={formData.number_transmission || ""} 
                                        onChange={e => setFormData({...formData, number_transmission: e.target.value})}
                                    />
                                </td>

                                {/* Модель управляемого моста */}
                                <td><RenderSelect name="model_drive_axle" value={formData.model_drive_axle} list={options.driveAxles} /></td>

                                {/* № управляемого моста */}
                                <td>
                                    <input 
                                        type="text" 
                                        value={formData.number_drive_axle || ""} 
                                        onChange={e => setFormData({...formData, number_drive_axle: e.target.value})}
                                    />
                                </td>

                                {/* Модель ведущего моста */}
                                <td><RenderSelect name="model_steer_axle" value={formData.model_steer_axle} list={options.steerAxles} /></td>

                                {/* № ведущего моста */}
                                <td>
                                    <input 
                                        type="text" 
                                        value={formData.number_steer_axle || ""} 
                                        onChange={e => setFormData({...formData, number_steer_axle: e.target.value})}
                                    />
                                </td>

                                {/* Договор поставки №, дата */}
                                <td>
                                    <input 
                                        type="text" 
                                        value={formData.number_supply_contract || ""} 
                                        onChange={e => setFormData({...formData, number_supply_contract: e.target.value})}
                                    />
                                </td>

                                {/* Дата отгрузки с завода */}
                                <td>
                                    <input 
                                        type="date" 
                                        value={formData.date_shipment_with_factory || ""} 
                                        onChange={e => setFormData({...formData, date_shipment_with_factory: e.target.value})}
                                    />
                                </td>

                                {/* Грузополучатель */}
                                <td>
                                    <input 
                                        type="text" 
                                        value={formData.cargo_recipient || ""} 
                                        onChange={e => setFormData({...formData, cargo_recipient: e.target.value})}
                                    />
                                </td>

                                {/* Адрес поставки */}
                                <td>
                                    <input 
                                        type="text" 
                                        value={formData.date_shipment_with_factory || ""} 
                                        onChange={e => setFormData({...formData, date_shipment_with_factory: e.target.value})}
                                    />
                                </td>

                                {/* Комплектация */}
                                <td>
                                    <input 
                                        type="text" 
                                        value={formData.configuration || ""} 
                                        onChange={e => setFormData({...formData, configuration: e.target.value})}
                                    />
                                </td>

                                {/* Клиент */}
                                <td><RenderSelect name="client" value={formData.client} list={options.clients} labelField="username" /></td>

                                <td>
                                    <button onClick={() => handlerSave(machine.id)}>ОК</button>
                                    <button onClick={() => setEditRowId(null)}>Отмена</button>
                                </td>
                            </>
                        ) : (
                            <>
                                {/* № Зав.техники*/}
                                <td>
                                    <Link to={`/machines/${machine.id}`}>
                                        {machine.unique_machine_number}
                                    </Link>
                                </td>
                                {/* Модель техники*/}
                                <td>
                                    <Link to={`/model_machines/${machine.model_machine}`}>
                                        {machine.model_machine_info?.name}
                                    </Link>
                                    </td>
                                {/* Модель двигателя*/}
                                <td>
                                    <Link to={`/model_engines/${machine.model_engine}`}>
                                        {machine.model_engine_info?.name}
                                    </Link>
                                </td>
                                {/* № Зав.двигателя*/}
                                <td>{machine.number_engine}</td>
                                {/* Модель трансмисии */}
                                <td>
                                    <Link to={`/model_transmissions/${machine.model_transmission}`}>
                                    {machine.model_transmission_info?.name}
                                    </Link>
                                </td>
                                {/* № Зав.трансмиссии */}
                                <td>{machine.number_transmission}</td>
                                {/* Модель управляемого моста */}
                                <td>
                                    <Link to={`/model_drive_axles/${machine.model_drive_axle}`}>
                                        {machine.model_drive_axle_info?.name}
                                    </Link>
                                </td>
                                {/* № Зав.управляемого моста */}
                                <td>{machine.number_drive_axle}</td>
                                {/* Модель ведущего моста */}
                                <td>
                                    <Link to={`/model_steer_axles/${machine.model_steer_axle}`}>
                                        {machine.model_steer_axle_info?.name}
                                    </Link>
                                </td>
                                {/* № Зав.ведущего моста */}
                                <td>{machine.number_steer_axle}</td>

                                {canEdit && 
                                <>
                                {/* Договор поставки №, дата */}
                                <td>{machine.number_supply_contract}</td>
                                {/* Дата отгрузки с завода */}
                                <td>{machine.date_shipment_with_factory}</td>
                                {/* Грузополучатель */}
                                <td>{machine.cargo_recipient}</td>
                                {/* Адрес поставки */}
                                <td>{machine.delivery_address}</td>
                                {/* Комплектация */}
                                <td>{machine.configuration}</td>
                                {/* Клиент */}
                                <td>{machine?.client_info.username}</td>
                                <td><button onClick={() => startEdit(machine)}>Редактировать</button></td>
                                </>
                                }
                            </>
                        )}
                    </tr>
                ))}
            </tbody>
        </table>
    </>
    );
}
