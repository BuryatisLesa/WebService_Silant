import { useState, useEffect } from "react";
import { useParams, useNavigate } from 'react-router-dom';
import { MachinesService } from "../../../Machines";

const machineService = new MachinesService();

function DetailModelMachine(){
    const {id} = useParams();
    const [modelMachine, setModelMachine] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        machineService.getModel(id).then(result => setModelMachine(result.data))
            .catch(err => console.error("Ошибка загрузки данных модели!", err));
    }, [id]);


    if (!modelMachine) return <p>Загрузка данных...</p>;

    return (
        <>
        <div><button onClick={() => navigate("/")}>Назад</button></div>
        <div>Модель: {modelMachine.name}</div>
        <div>Описание: {modelMachine.descriptions}</div>
        </>
    )

}

export default DetailModelMachine;