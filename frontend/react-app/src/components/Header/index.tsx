import { Link } from 'react-router-dom';

 export function Header(){
    return (
        <header>
        <Link to="/registration">
            <button>Регистрация</button>
        </Link>
        <Link to="/login">
            <button>Авторизация</button>
        </Link>
        </header>
    )
}
