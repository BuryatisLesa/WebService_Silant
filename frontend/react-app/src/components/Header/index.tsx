import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';

 export function Header(){
    const navigate =  useNavigate();
    const username = localStorage.getItem("username");

    const handlerLogout =  () => {
        localStorage.clear();
        navigate("/login");
    }
    return (
        <header>
            {username ? (
                <div>
                    <span>Привет, <strong>{username}</strong>!</span>
                    <button onClick={handlerLogout}>Выйти</button>
                </div>
            ) : (
                <button onClick={() => navigate('/login')}>Войти</button>
            )}
        </header>
    )
}
