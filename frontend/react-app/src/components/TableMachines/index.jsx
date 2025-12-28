import { Component, useState, useEffect } from "react";

export function TableMachines({data}) {
    return (
        <table>
            <thead>
                <tr>
                    <th>Модель техники</th>
                    <th>Модель двигателя</th>
                    <th>Модель трансмиссии</th>
                    <th>Модель ведущего моста</th>
                    <th>Модель управляемого моста</th>
                </tr>
            </thead>
            <tbody>
            {data.map((machine) => (
                <tr key={machine.id}>
                <td>{machine.model_machine?.name}</td> 
                <td>{machine.model_engine?.name}</td>
                <td>{machine.model_transmission?.name}</td>
                <td>{machine.model_drive_axle?.name}</td>
                <td>{machine.model_steer_axle?.name}</td>
                </tr>
            ))}
            </tbody>

        </table>
    )
}