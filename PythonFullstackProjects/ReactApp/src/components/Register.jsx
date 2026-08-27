import React, { useEffect, useState } from "react";
import {Link} from 'react-router-dom'
import axios   from 'axios'
export default function Register(){
    let[employees,setEmployees]=useState([]);

    function getEmployees(){
        axios.get("http://localhost:8000/employees/")
        .then((response)=>{
            setEmployees(response.data)
        })
        .catch((er)=>{
            alert(er)
        })
    }
    useEffect(()=>{
        getEmployees()
    },[])
    return(
        <React.Fragment>
           <div className="container mt-5">
            <div className="row d-flex justify-content-center mt-5">
                <pre>{JSON.stringify(employees)}</pre>
                <div className="col-md-5">
                        <div className="card mt-5 shadow-lg animated jello">
                            <div className="card-header bg-primary text-white text-center">
                                <p className="h2">Register Here</p>
                            </div>
                            <div className="card-body bg-white ">
                            <div className="form-group">
                                <label className="form-label">Employee ID</label>
                                <input type="number" className="form-control" placeholder="Employee ID" />
                            </div>

                             <div className="form-group">
                                <label className="form-label">Employee Name</label>
                                <input type="text" className="form-control" placeholder="Employee Name" />
                            </div>
                             <div className="form-group">
                                <label className="form-label">Employee Salary</label>
                                <input type="number" className="form-control" placeholder="Employee Salary" />
                            </div>
                            <div className="form-group">
                                <button className="btn btn-outline-primary btn-sm">Register</button>
                                <Link to='/' className="btn btn-sm btn-outline-amber float-right">List</Link>
                            </div>
                        </div>
                        </div>
                        
                </div>
            </div>
           </div>
        </React.Fragment>
    )
}