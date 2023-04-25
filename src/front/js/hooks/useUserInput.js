import React from "react";

import { useState } from "react";

const useUserInput = (initialValue = {}) => {
    
    const [userInput, setUserInput] = useState({});

    const handleUserInput = (event) => {

        const target = event.target

        setUserInput((prev) => {
            const newUserInput = {...prev}
            newUserInput[target.name] = target.value;
            return newUserInput;
        })

    }

    const handleUserSelectDate = (event) => {

        const target = event.target

        setUserInput((prev) => {
            const newUserInput = {...prev}
            newUserInput[target.name] = target.selected;
            return newUserInput;
        })

    }

    const handleUserRadio = (event) => {
        
        const target = event.target
        
        setUserInput((prev) => {
            const newUserInput = {...prev}
            if(target.value) newUserInput[target.placeholder] = target.name;
            console.log(newUserInput)
            return newUserInput;
        })
    }

    const handleUserCheck = ({target}) => {

        setUserInput((prev) => {
            const newUserInput = {...prev}
            newUserInput[target.name] = target.checked;
            return newUserInput;
        })
    } 

    const resetInput = (newValue = initialValue) => setUserInput(newValue);

    return {
        userInput,
        resetInput,
        handleUserInput,
        handleUserSelectDate,
        handleUserRadio,
        handleUserCheck,
    }
}

export default useUserInput;