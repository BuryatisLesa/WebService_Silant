import { useState, useEffect } from "react";
import { useParams, useNavigate } from 'react-router-dom';
import { MachinesService } from "../../../Machines";

const machineService = new MachinesService();

function DetailModelEngine(){
    const {id} = useParams();
    const [modelEngine, setModelEngine] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        machineService.getEngine(id).then(result => setModelEngine(result.data))
            .catch(err => console.error("Ошибка загрузки данных модели!", err));
    }, [id]);


    if (!modelEngine) return <p>Загрузка данных...</p>;

    return (
        <>
        <div><button onClick={() => navigate("/")}>Назад</button></div>
        <div>Модель: {modelEngine.name}</div>
        <div>Описание: {modelEngine.descriptions}</div>
        </>
    )

}

export default DetailModelEngine;