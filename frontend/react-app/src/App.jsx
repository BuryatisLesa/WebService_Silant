import { useState } from 'react'
import './App.css'
import Main from './components/Main'
import { Header } from './components/Header'
import Registration  from './components/Registration'
import Login  from './components/Login'
import { BrowserRouter, Routes, Route } from 'react-router-dom'

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/login" element={<Login />} />
        <Route path="/registration" element={<Registration />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App