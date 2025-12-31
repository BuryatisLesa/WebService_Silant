import {useState} from 'react';
import AccountsService from '../../../Accounts';

const newAccount = new AccountsService();

function Registration() {
    const [userName, setUserName] = useState("")
    const [userEmail, setUserEmail] = useState("")
    const [userPassword, setUserPassword] = useState("")

    const handlerButtonRegistration = (event) => {
        //Предотвращаем перезагрузку страницы
        event.preventDefault();

        if (userName.trim() === "" || userEmail.trim() === "" || userPassword.trim() === ""){
            alert("Заполните все поля!")
            return;
        } else {
            const dataUser = {
                username: userName,
                email: userEmail,
                password: userPassword
            };
            newAccount.registration(dataUser).then(() => {
                console.log("Пользователь создан")
                alert("Регистрация успешна!")
            }).catch((err => {
                console.error("Ошибка регистрации", err);
                alert("Ошибка при регистрации");
            }))
        }
    }

    return (
        <div>
            <h2>Страница регистрации</h2>
            <form onSubmit={handlerButtonRegistration}>
                <input 
                    value={userName} 
                    onChange={(e) => setUserName(e.target.value)} 
                    type="text" 
                    placeholder="Логин" 
                />
                <input 
                    value={userEmail} 
                    onChange={(e) => setUserEmail(e.target.value)} 
                    type="email" 
                    placeholder="Email" 
                />
                <input 
                    value={userPassword} 
                    onChange={(e) => setUserPassword(e.target.value)} 
                    type="password" 
                    placeholder="Пароль" 
                />
                <button type="submit">Создать аккаунт</button>
            </form>
        </div>
    );
}
export default Registration;
