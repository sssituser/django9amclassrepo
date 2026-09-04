import axios from "axios";
import React, { useEffect, useState } from "react";
import { useParams,Link } from "react-router-dom";


export default function Find(){
    let {id} = useParams();
    let[employee,setEmployee]=useState({})
    function getEmployeeById(){
        axios.get(`http://localhost:8000/employees/${id}/`)
        .then((res)=>{setEmployee(res.data)})
        .catch((err)=>{alert(err)})
    }
    useEffect(()=>{getEmployeeById()})

    return(
        <React.Fragment>
            <div className="container mt-5">
                <div className="row justify-content-center">
                    <div className="col-md-6">
                        <div className="card mt-5">
                            <div className="card-header bg-success text-center text-white">
                                <p className="h3">Employee Inforamtion</p>
                            </div>
                            <div className="card-body">
                                <div className="row justify-content-center">
                                    <div className="col ">
                                       <p className="h3"> Employee ID</p>
                                    </div>
                                    <div className="col">
                                       <p className="h3"> {employee.EmployeeId}</p>
                                    </div>
                                </div>
                                 <div className="row justify-content-center">
                                    <div className="col ">
                                       <p className="h3"> Employee Name</p>
                                    </div>
                                    <div className="col">
                                       <p className="h3"> {employee.EmployeeName}</p>
                                    </div>
                                </div>
                                <div className="row justify-content-center">
                                    <div className="col ">
                                       <p className="h3"> Employee Salary</p>
                                    </div>
                                    <div className="col">
                                       <p className="h3"> {employee.EmployeeSalary}</p>
                                    </div>
                                </div>
                            </div>
                            <div className="card-footer">
                                <Link to='/employees' className="btn btn-md btn-secondary w-100">EmployeeList</Link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </React.Fragment>
    )
}