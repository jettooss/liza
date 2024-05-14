import React from "react";

export default function Stars(){
    return(
        <div className="AllStars">
            <div className="Stars">
                <input id="Riting5" className="Item" type="radio" value="5"/>
                <label htmlFor="Riting5"/>
                <input id="Riting4" className="Item" type="radio" value="4"/>
                <label htmlFor="Riting4"/>
                <input id="Riting3" className="Item" type="radio" value="3"/>
                <label htmlFor="Riting3"/>
                <input id="Riting2" className="Item" type="radio" value="2"/>
                <label htmlFor="Riting2"/>
                <input id="Riting1" className="Item" type="radio" value="1"/>
                <label htmlFor="Riting1"/>
            </div>
        </div>
        )
    }