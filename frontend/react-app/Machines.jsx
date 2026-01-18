import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

class MachinesService{
    getMachines(query = "") {
        const token = localStorage.getItem("token");
        
        // Формируем URL: если есть query, добавляем поиск
        const url = query 
            ? `${API_URL}/api/machines/?search=${query}`
            : `${API_URL}/api/machines/`;

        return axios.get(url, {
            headers: token ? { 'Authorization': `Token ${token}` } : {}
        });
    }
    getMachine(id){
        //Получить конкретную запись о машине по id
        const url = `${API_URL}/api/machines/${id}/`;
        return axios.get(url);
    }   
    createMachine(machineData){
        const url = `${API_URL}/api/machines/`;
        return axios.post(url, machineData);
    }
    
    updateMachine(id, data) {
    const token = localStorage.getItem("token");
    const url = `${API_URL}/api/machines/${id}/update/`;
    return axios.put(url, data, {
        headers: {
            'Authorization': `Token ${token}`,
            'Content-Type': 'application/json'
        }
    })
    }

    // Справочники
    getModels() { return axios.get(`${API_URL}/api/model_machines/`); }
    getModel(id) { return axios.get(`${API_URL}/api/model_machines/${id}/`); }
    getEngines() { return axios.get(`${API_URL}/api/model_engines/`); }
    getEngine(id) { return axios.get(`${API_URL}/api/model_engines/${id}/`); }
    getTransmissions() { return axios.get(`${API_URL}/api/model_transmissions/`); }
    getTransmission(id) { return axios.get(`${API_URL}/api/model_transmissions/${id}/`); }
    getDriveAxles() { return axios.get(`${API_URL}/api/model_drive_axles/`); }
    getDriveAxle(id) { return axios.get(`${API_URL}/api/model_drive_axles/${id}/`); }
    getSteerAxles() { return axios.get(`${API_URL}/api/model_steer_axles/`); }
    getSteerAxle(id) { return axios.get(`${API_URL}/api/model_steer_axles/${id}/`); }
    getServiceCompanies() { return axios.get(`${API_URL}/api/service_companies/`); }
    getServiceCompany(id) { return axios.get(`${API_URL}/api/service_companies/${id}/`); }
    getClients() { return axios.get(`${API_URL}/api/clients/`); }
    getFailedUnits() { return axios.get(`${API_URL}/api/failed_units/`); }
    getMethodsRestoration() { return axios.get(`${API_URL}/api/method_restorations/`); }
    getTypeTI() { return axios.get(`${API_URL}/api/type_technical_inspections/`); }

}

class TechnicalInspectService {
    getTI() {
        const token = localStorage.getItem("token"); // Берем токен из хранилища
        const url = `${API_URL}/api/technical_inspections/`;

        return axios.get(url, {
            headers: {
                'Authorization': `Token ${token}` // Передаем токен в заголовке
            }
        });
    }

    updateTI(id, updateData) {
        const token = localStorage.getItem("token");
        const url = `${API_URL}/api/technical_inspections/${id}/update/`;

        // В axios.post вторым аргументом идут данные, а третьим — конфиг с заголовками
        return axios.put(url, updateData, {
            headers: {
                'Authorization': `Token ${token}`,
                'Content-Type': 'application/json'
            }
        });
    }
    getTypesTI() { 
        return axios.get(`${API_URL}/api/type_technical_inspections/`); 
    }
}


class ComplaintService {
    getComplaint() {
        const token = localStorage.getItem("token"); // Берем токен из хранилища
        const url = `${API_URL}/api/complaints/`;

        return axios.get(url, {
            headers: {
                'Authorization': `Token ${token}` // Передаем токен в заголовке
            }
        });
    }
    updateComplaint(id, updateData){
        const token = localStorage.getItem("token");
        const url = `${API_URL}/api/complaints/${id}/update/`;

        // В axios.post вторым аргументом идут данные, а третьим — конфиг с заголовками
        return axios.put(url, updateData, {
            headers: {
                'Authorization': `Token ${token}`,
                'Content-Type': 'application/json'
            }
        });
    }
    getFailedUnits() { 
        return axios.get(`${API_URL}/api/failed_units/`); 
    }
    getMethodsRestoration() { 
        return axios.get(`${API_URL}/api/method_restorations/`); 
    }
}

export { MachinesService, TechnicalInspectService, ComplaintService};

