import React from 'react';
import Doctor from "../../assets/images/Log150.png"
import Stars from "../Stars/Stars";

export function CardDoctor() {
    return (
        <div>
            <div className="ImageCard">
                <img src={Doctor} />
            </div>
            <div className="RatingCard">
                <Stars />
            </div>
            <div className="DescriptionCard">
                <h6>Валерьева Валерия Валерьевна</h6>
                <p>Стоматолог-терапевт</p>
                <button id="Button">Подробнее</button>
            </div>
        </div>
    )
}

