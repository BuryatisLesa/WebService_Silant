import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export default class AccountsService {
    registration(userData) {
        const url = `${API_URL}/api/registration/`;
        return axios.post(url, userData);
    }

    authorization(userData){
        const url = `${API_URL}/api/login/`;
        return axios.post(url, userData)
    }
}
