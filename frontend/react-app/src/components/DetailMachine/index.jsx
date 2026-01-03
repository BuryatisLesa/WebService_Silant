    import { useState, useEffect } from "react";
    import { useParams, useNavigate } from 'react-router-dom';
    import { MachinesService } from "../../../Machines";

    const machineService = new MachinesService();

    function DetailMachine(){
        const { id } = useParams();
        const [machine, setMachine] = useState(null);
        const navigate = useNavigate();


        useEffect(() => {
            machineService.getMachine(id)
            .then(result => setMachine(result.data))
            .catch(err => console.error("Ошибка загрузки машины", err));
        }, [id]);

        console.log(machine)

        if (!machine) return <p>Загрузка данных...</p>;

        return(
            <>
                <div><button onClick={() => navigate("/")}>Назад</button></div>
                <div>
                    <b>Зав. № машины:</b><span>{machine.unique_machine_number}</span>
                </div>
                <div>
                    Модель техники: {machine.model_machine_info?.name}
                </div>
                <div>
                    Модель двигателя: {machine.model_engine_info?.name}
                </div>
                <div>
                    Зав. № двигателя: {machine.number_engine}
                </div>
                <div>
                    Модель трансмиссии: {machine.model_transmission_info?.name}
                </div>
                <div>
                    Зав. № трансмиссии: {machine.number_transmission}
                </div>
                <div>
                    Модель ведущего моста: {machine.model_drive_axle_info?.name}
                </div>
                <div>
                    Зав. № ведущего моста: {machine.number_drive_axle}
                </div>
                <div>
                    Модель управляемого моста: {machine.model_steer_axle_info?.name}
                </div>
                <div>
                    Зав. № управляемого моста: {machine.number_steer_axle}
                </div>
                <div>
                    Договор поставки №, дата: {machine.number_supply_contract}
                </div>
                <div>
                    Дата отгрузки с завода: {machine.date_shipment_with_factory}
                </div>
                <div>
                    Грузополучатель: {machine.cargo_recipient}
                </div>
                <div>
                    Адрес поставки: {machine.delivery_address}
                </div>
                <div>
                    Комплектация: {machine.configuration}
                </div>
                <div>
                    Клиент: {machine.client_info?.username}
                </div>
                <div>
                    Сервисная компания: {machine.service_company_info?.name}
                </div>
            </>
        )
    }

    export default DetailMachine;