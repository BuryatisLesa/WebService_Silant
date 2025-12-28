import {useState, useEffect} from 'react'
import MachinesService from '../../../Machines';
import { TableMachines } from '../TableMachines';


const machineService = new MachinesService();

function Search(){
    const [searchQuery, setSearchQuery] = useState("");
    const [machineData, setMachineData] = useState([]);

    const getMachineData = (query) => {
        machineService.getMachines(query).then((result => {
            setMachineData(result.data);
        }))
        .catch((error => {
            console.log(`Ошибка загрузки данных с сервера ${error}`)
        }))
    }
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