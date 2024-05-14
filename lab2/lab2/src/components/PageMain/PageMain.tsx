import React from 'react';
import Fon from '../assets/images/Fon1200.png'

export function PageMain (){
    return(
        <div id="container" className="Font">
            <h1 id="Deviz">Запишитесь на бесплатную консультацию!</h1>
            <form className="form">
                <p id="P_zapis">Заполните анкету и мы свяжемся с вами:</p>
                <input id="LastName" className="input" type="text" placeholder="Ваша фамилия" />
                <input id="FirstName" className="input" type="text" placeholder="Ваше имя" />
                <input id="NumberTel" className="input" type="text" placeholder="Ваш номер телефона" />
                <input type="submit" id="buttonSend" value="Отправить"/>
            </form>
        </div>
    )
}
