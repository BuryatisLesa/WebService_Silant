import {useState, useEffect, act} from 'react'
import Search from '../Search'
import { TableMachines } from '../TableMachines';
import TableTI from '../TableTI';
import TableComplaint from '../TableComplaint/index.jsx';
import { MachinesService, TechnicalInspectService, ComplaintService } from '../../../Machines.jsx';
import Management from '../Management/index.jsx';

const machineService = new MachinesService();
const technicalInspectService = new TechnicalInspectService();
const complaintService = new ComplaintService();

function Main (){
    const [machineData, setMachineData] = useState([]);
    const token = localStorage.getItem("token");
    const [tiData, setTI] = useState([]);
    const [complaintData, setComplaint] = useState([]);


    // Состояние для активной вкладки
    const [activeTab, setActiveTab] = useState('machines');

    // получение данных о машинах
    const loadInitialData = () => {
        machineService.getMachines().then(res => setMachineData(res.data));
    };

    // получение данных о ТО
    const getTechnicalInspection = () => {
        technicalInspectService.getTI()
            .then((result) => {
                setTI(result.data);
            })
            .catch((error) => {
                console.error("Ошибка авторизации или загрузки ТО", error);
            });
    };

    // получение данных Рекламации
    const getComplaint = () => {
        complaintService.getComplaint()
            .then((result) => {
                setComplaint(result.data);
            })
            .catch((error) => {
                console.error("Ошибка авторизации или загрузки Рекламации", error);
            });
    };

    useEffect(() => {
        // загрузка данных связанный с пользователем
        loadInitialData();
        getTechnicalInspection();
        getComplaint();
    }, [token]);

    return (    
        <main>
            {token ? (
                <>  
                    {/*Кнопки переключение таблиц*/}
                    <div className='tabs-nav'>
                        <button onClick={() => { setActiveTab('machines')}}>Общая информация</button>
                        <button onClick={() => { setActiveTab('ti')}}>ТО</button>
                        <button onClick={() => { setActiveTab('complaints')}}>Рекламация</button>
                        <button onClick={() => { setActiveTab('manager')}}>Управление</button>
                    </div>
                    <div className='tab-content'>
                        {activeTab === 'machines' && (
                            <>
                                <h2>Список ваших машин</h2>
                                <TableMachines data={machineData} />
                            </>
                        )}
                        {activeTab === 'ti' && (
                            <>
                                <h2>Техническое обслуживание</h2>
                                <TableTI data={tiData} />
                            </>
                        )}
                        {activeTab === 'complaints' && (
                            <>
                                <h2>Рекламации</h2>
                                <TableComplaint data={complaintData} />
                            </>
                        )}
                        {activeTab === 'manager' && (
                            <>
                                <h2>Справочники</h2>
                                <Management/>
                            </>
                        )}
                    </div>
                </>
            ) : (
                // Если токена нет, показываем поиск для анонимов
                <Search />
            )}
        </main>
    );
}

export default Main;