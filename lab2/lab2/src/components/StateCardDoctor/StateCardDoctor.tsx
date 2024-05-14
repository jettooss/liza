import React, { useContext } from "react";
import { CardDoctor } from "../CardDoctor";
import { MessageContext } from "../MessageStore";

export default function StateCard() {
  const messages = useContext(MessageContext)

  return(
    <>
      {messages.messages !== null && (
        messages.messages.map(() => <CardDoctor />)
      )}
    </>
  );
}