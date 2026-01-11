import { useState, useEffect } from "react";
import { useParams, useNavigate } from 'react-router-dom';
import { MachinesService } from "../../../Machines";

const machineService = new MachinesService();

function DetailModelSteerAxle(){
    const {id} = useParams();
    const [modelSteerAxle, setModelSteerAxle] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        machineService.getSteerAxle(id).then(result => setModelSteerAxle(result.data))
            .catch(err => console.error("Ошибка загрузки данных модели!", err));
    }, [id]);


    if (!modelSteerAxle) return <p>Загрузка данных...</p>;

    return (
        <>
        <div><button onClick={() => navigate("/")}>Назад</button></div>
        <div>Модель: {modelSteerAxle.name}</div>
        <div>Описание: {modelSteerAxle.descriptions}</div>
        </>
    )

}

export default DetailModelSteerAxle;