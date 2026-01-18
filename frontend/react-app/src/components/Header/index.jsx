import style from './style.module.css';
import { useNavigate } from 'react-router-dom';

 export function Header(){
    const navigate =  useNavigate();
    const username = localStorage.getItem("username");
    const role = localStorage.getItem("role")

    const handlerLogout =  () => {
        // localStorage.removeItem("username");
        // localStorage.removeItem("token");
        // localStorage.removeItem("role");
        localStorage.clear();
        navigate("/login");
    }
    return (
        <header className={style["header"]}>
            <nav className={style["header__navbar"]}>
            <div className={style["header__logo"]}>
                <h1>SILANT</h1>
                </div>
            {username ? (
                <div className={style["header__user"]}>
                    <span className={style["header__username"]}>
                        Привет, <strong>{username}/{role}</strong>!</span>
                    <button
                    className={style["header__button-logout"]}
                    onClick={handlerLogout}>
                        Выйти
                    </button>
                </div>
            ) : (
                <button className={style["header__button-login"]} onClick={() => navigate('/login')}>Войти</button>
            )}
            </nav>
            <div className={style['header__welcome-text']}>
                <h3>Электронная сервисная книжка "Мой Силант"</h3>
            </div>
        </header>
    )
}
