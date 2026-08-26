
import React from "react";
import {BrowserRouter,Routes,Route}  from 'react-router-dom'
import Home from "./components/Home";
import Register from "./components/Register";
import About from "./components/About";
import Contact from "./components/Contact";
import Navbar from "./components/Navbar";

export default function App(){
  return(
    <React.Fragment>
      <BrowserRouter>
      <Navbar/>
      <Routes>
        <Route path="/"  element={<Home/>} />
        <Route path="/register"  element={<Register/>} />
        <Route path="/about"  element={<About/>} />
         <Route path="/contact"  element={<Contact/>} />
      </Routes>
      </BrowserRouter>
    </React.Fragment>
  )
}