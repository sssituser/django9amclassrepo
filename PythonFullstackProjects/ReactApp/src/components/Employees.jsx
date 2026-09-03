import React,{useEffect, useState} from "react";
import axios from 'axios';
import {Link} from 'react-router-dom'
export default function Employees(){
    let[employees,setEmployees]=useState([]);
  
    function getEmployees(){
        axios.get("http://localhost:8000/employees/")
        .then((res)=>{
            setEmployees(res.data)
        })
        .catch((error)=>{
            alert(error)
        })
    }

    useEffect(()=>{
        getEmployees()
    },[]);


    return(
        <React.Fragment>           
            {
                employees.length>0  ? 

                <div className="container">
                      <table className="table table-bordered table-hover table-striped text-center">
                    <thead  className="bg-primary text-white ">
                        <tr>
                            <th>
                                Employee ID
                            </th>
                            <th>
                                Employee Name
                            </th>
                            <th>
                                Employee Salary
                            </th>
                            <th>
                                Actions
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            employees.map((emp)=>{
                               return(
                                <tr>
                                    <td>{emp.EmployeeId}</td>
                                    <td>{emp.EmployeeName}</td>
                                    <td>{emp.EmployeeSalary}</td>
                                    <td>
                                        <Link to={`/find/${emp.EmployeeId}`} className="mr-3">
                                            <i className="fa fa-eye fa-2x text-secondary"></i>
                                        </Link>
                                         <Link to={`/edit/${emp.EmployeeId}`} className="mr-3">
                                            <i className="fa fa-2x fa-pen text-info"></i>
                                        </Link>
                                         <Link to={`/delete/${emp.EmployeeId}`} className="mr-3">
                                            <i className="fa fa-2x fa-trash-alt text-danger"></i>
                                        </Link>
                                      
                                    </td>
                                </tr>
                               )
                            })
                        }
                    </tbody>

                </table>
              
                </div>
              


                :
                <p className="h1 text-danger text-center">Employee Not Found</p>
            }


        </React.Fragment>
    )
}