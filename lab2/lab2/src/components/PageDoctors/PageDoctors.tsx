import React, { useState } from "react";
import { CardDoctor } from "../CardDoctor/CardDoctor";

export function PageDoctors() {

    const [cards, setCards] = useState(Array.from({ length: 20 }, () => <div><CardDoctor /></div>));

    const addMoreCards = () => {
        const newCards = Array.from({ length: 20 }, () => <div><CardDoctor /></div>);
        setCards([...cards, ...newCards]);
    };

    return (
        <div>
            <h1 id="Profi">Наши профессионалы</h1>
            <div className="Cards AllCard">
                {cards}
            </div>
            <button onClick={addMoreCards} className="ButtonMore">Показать ещё</button>
        </div>
    )
}
