import { useState, useEffect } from "react";
import { useParams, useNavigate } from 'react-router-dom';
import { MachinesService } from "../../../Machines";

const machineService = new MachinesService();

function DetailModelTransmission(){
    const {id} = useParams();
    const [modelTransmission, setModelTransmission] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        machineService.getTransmission(id).then(result => setModelTransmission(result.data))
            .catch(err => console.error("Ошибка загрузки данных модели!", err));
    }, [id]);


    if (!modelTransmission) return <p>Загрузка данных...</p>;

    return (
        <>
        <div><button onClick={() => navigate("/")}>Назад</button></div>
        <div>Модель: {modelTransmission.name}</div>
        <div>Описание: {modelTransmission.descriptions}</div>
        </>
    )

}

export default DetailModelTransmission;