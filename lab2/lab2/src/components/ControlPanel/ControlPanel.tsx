import React, { useContext } from 'react';
import { MessageContext } from '../MessageStore/MessageStore';

export function ControlPanel() {
    const state = useContext<any>(MessageContext);

    return (
        <div className="control_panel">
            <div className="buttons">
                <input type="button" onClick={
                    ()=>{
                        var m = {NameDoctor: "Валерьева Валерия Валерьевна", Post: "Стоматолог-терапевт"}
                        state.add(m)
                    }
                } value="NEW"/>
                <input type="button" value="DELETE" onClick={e=>{
                    state.dropAt(0)
                }}/>
            </div>
        </div>
    );
}
