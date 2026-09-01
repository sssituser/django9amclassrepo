
import React from "react";
import {BrowserRouter,Routes,Route}  from 'react-router-dom'
import Home from "./components/Home";
import Register from "./components/Register";
import About from "./components/About";
import Contact from "./components/Contact";
import Navbar from "./components/Navbar";
import Employees from "./components/Employees";
import Find from "./components/Find";
import Edit from "./components/Edit";
import Del from "./components/Del";

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
        <Route path="/employees"  element={<Employees/>} />

        <Route path="/find/:id"  element={<Find/>} />
        <Route path="/edit/:id"  element={<Edit/>} />
        <Route path="/delete/:id"  element={<Del/>} />        
      </Routes>
      </BrowserRouter>
    </React.Fragment>
  )
}