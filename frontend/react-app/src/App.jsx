import { useState } from 'react'
import './App.css'
import Main from './components/Main'
import { Header } from './components/Header'
import Login  from './components/Login'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import DetailMachine from './components/DetailMachine'
import DetailModelMachine from './components/DetailModelMachine'
import DetailModelEngine from './components/DetailModelEngine'
import DetailModelTransmission from './components/DetailModelTransmission'
import DetailModelDriveAxle from './components/DetailModelDriveAxle'

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/login" element={<Login />} />
        <Route path="/machines/:id" element={<DetailMachine/>} />
        <Route path="/model_machines/:id" element={<DetailModelMachine/>} />
        <Route path="/model_engines/:id" element={<DetailModelEngine/>} />
        <Route path="/model_transmissions/:id" element={<DetailModelTransmission/>} />
        <Route path="/model_drive_axles/:id" element={<DetailModelDriveAxle/>} />
      </Routes>
    </BrowserRouter>
  )
}

export default App;