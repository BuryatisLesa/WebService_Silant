import {useState} from 'react'
import { MachinesService} from '../../../Machines.jsx';
import { TableMachines } from '../TableMachines';


const machineService = new MachinesService();


function Search(){
    const [searchQuery, setSearchQuery] = useState(""); // Данные с инпута
    const [machineData, setMachineData] = useState([]); // Данные о машинах с сервера

    // Обращение к серверу и получение данных
    const getMachineData = (query) => {
        machineService.getMachines(query).then((result => {
            setMachineData(result.data);
        }))
        .catch((error => {
            console.log(`Ошибка загрузки данных с сервера ${error}`)
        }))
    }

    // Обработка действия кнопки поиска
    const handlerButtonClick = () => {
        const cleanQuery = searchQuery.trim();
        if (cleanQuery === ""){
            alert("Введите номер машины!")
            return;
        } else {
            getMachineData(cleanQuery)
        }
    }

    return (
        <>
        <div>
            <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
            />
            <button onClick={handlerButtonClick}>Найти машину</button>
        </div>
        <div>
            <TableMachines data={machineData}></TableMachines>
        </div>
        </>
    )}
export default Search;