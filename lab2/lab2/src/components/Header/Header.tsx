import React from 'react';
import Logo500NotFoneWhite from '../../assets/images/Logo500NotFoneWhite.png'

export function Header (){
    return(
        <header style={{ backgroundColor: "#1a8acc" }}>
            <nav>
                <div className="MainMenu">
                    <div className="Logo">
                        <img src={Logo500NotFoneWhite} id="mainLogo" width="50%" height="50%"/>
                    </div>
                    <div className="DivUl">
                        <ul className="mainUl">
                            <li><a href="/">Главная</a></li>
                            <li><a href="">Услуги</a></li>
                            <li><a href="">Цены</a></li>
                            <li><a href="/doctors">Врачи</a></li>
                            <li><a href="">Контакты</a></li>
                            <li><a href="">Запись на приём</a></li>
                        </ul>
                    </div>
                </div>
            </nav>
        </header>
    );
}
