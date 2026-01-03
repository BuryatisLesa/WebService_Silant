import { useState, useEffect } from "react";
import { useParams, useNavigate } from 'react-router-dom';
import { MachinesService } from "../../../Machines";

const machineService = new MachinesService();

function DetailModelDriveAxle(){
    const {id} = useParams();
    const [modelDriveAxle, setModelDriveAxle] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        machineService.getDriveAxle(id).then(result => setModelDriveAxle(result.data))
            .catch(err => console.error("Ошибка загрузки данных модели!", err));
    }, [id]);


    if (!modelDriveAxle) return <p>Загрузка данных...</p>;

    return (
        <>
        <div><button onClick={() => navigate("/")}>Назад</button></div>
        <div>Модель: {modelDriveAxle.name}</div>
        <div>Описание: {modelDriveAxle.descriptions}</div>
        </>
    )

}

export default DetailModelDriveAxle;