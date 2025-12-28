import axios from "axios"

const API_URL = "http://127.0.0.1:8000/"

export default class MachinesService{
    getMachines(query = ""){
        // Если query есть, добавляем параметр поиска, если нет — запрашиваем весь список
        const url = query 
            ? `${API_URL}/api/machines/?search=${query}` 
            : `${API_URL}/api/machines/`;

        return axios.get(url)
    }
    getMachine(id){
        //Получить конкретную запись о машине по id
        const url = `${API_URL}/api/machines/${id}/`
        return axios.get(url)
    }   
    createMachine(machineData){
        const url = `${API_URL}/api/machines/`
        return axios.post(url, machineData)
    }
}