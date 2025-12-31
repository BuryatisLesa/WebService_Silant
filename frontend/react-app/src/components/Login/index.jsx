import {useState} from 'react';
import AccountsService from '../../../Accounts';
import { useNavigate } from 'react-router-dom';

const accountsService = new AccountsService();

function Login() {
    const [userName, setUserName] = useState("")
    const [userPassword, setUserPassword] = useState("")
    const navigate = useNavigate();

    const handlerButtonAuthorization = (event) => {
        //Предотвращаем перезагрузку страницы
        event.preventDefault();


        if (userName.trim() === "" || userPassword.trim() === ""){
            alert("Заполните все поля!")
            return;
        }
        const dataUser = {
            username: userName,
            password: userPassword
            };
        accountsService.authorization(dataUser).then((response) => {
            console.log("Пользователь авторизован", response.data)
            localStorage.setItem("token", response.data.token);
            alert("Успешный вход");
            navigate('/');
        }).catch((err => {
                const errorMessage = err.response?.data?.[0] || "Ошибка авторизации";
                console.error("Ошибка:", err);
                alert(errorMessage);
        }))
    }

    return (
        <div>
            <h2>Страница Авторизации</h2>
            <form onSubmit={handlerButtonAuthorization}>
                <input 
                    value={userName} 
                    onChange={(e) => setUserName(e.target.value)} 
                    type="text" 
                    placeholder="Логин" 
                />
                <input 
                    value={userPassword} 
                    onChange={(e) => setUserPassword(e.target.value)} 
                    type="password" 
                    placeholder="Пароль" 
                />
                <button type="submit">Войти</button>
            </form>
        </div>
    );
}
export default Login;
