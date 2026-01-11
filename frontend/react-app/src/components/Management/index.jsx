import { MachinesService} from "../../../Machines";
import { useState, useEffect } from "react";

const machineService = new MachinesService();


function Management(){
    // Состояния для справочников
    const [options, setOptions] = useState({
        models: [], engines: [], transmissions: [], driveAxles: [], steerAxles: [],
        typeTI: [], serviceCompany: [], failUnit: [], methodRestoration: [],
    });


    useEffect(() => {
        Promise.all([
            machineService.getModels(),
            machineService.getEngines(),
            machineService.getTransmissions(),
            machineService.getDriveAxles(),
            machineService.getSteerAxles(),
            machineService.getTypeTI(),
            machineService.getServiceCompanies(),
            machineService.getFailedUnits(),
            machineService.getMethodsRestoration(),
        ]).then(([m, e, t, da, sa, tti, sc, fu, mr]) => {
            console.log(tti.data)
            setOptions({
                models: m.data, 
                engines: e.data, 
                transmissions: t.data, 
                driveAxles: da.data, 
                steerAxles: sa.data,
                typeTI: tti.data,
                serviceCompany: sc.data,
                failUnit: fu.data,
                methodRestoration: mr.data,
            });
        }).catch(err => console.error("Ошибка загрузки справочников", err));
    }, []);

    // вспомогательный компонент для отображение справочников
    const RenderSection = ({title, data}) => {
        return (
            <div style={{ marginBottom: "20px" }}>
                <strong style={{ fontSize: "1.2em", color: "#333" }}>{title}</strong>
                <ul>
                    {data.map((item) => (
                        <li key={item.id}>
                            <strong>{item.name}</strong> 
                            {item.description && <span> — {item.description}</span>}
                        </li>
                    ))}
                </ul>
            </div>
        );
    };

    return (
        <>
        <RenderSection title="Модель техники" data={options.models}></RenderSection>
        <RenderSection title="Модель двигателя" data={options.engines}></RenderSection>
        <RenderSection title="Модель трансмиссии" data={options.transmissions}></RenderSection>
        <RenderSection title="Модель ведущего моста" data={options.driveAxles}></RenderSection>
        <RenderSection title="Модель управляемого моста" data={options.steerAxles}></RenderSection>
        <RenderSection title="Модель вид ТО" data={options.typeTI}></RenderSection>
        <RenderSection title="Сервисные компании" data={options.serviceCompany}></RenderSection>
        <RenderSection title="Узел отказа" data={options.failUnit}></RenderSection>
        <RenderSection title="Метод восстановления" data={options.methodRestoration}></RenderSection>
        </>
    )
};

export default Management;