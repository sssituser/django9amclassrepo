import React, { useEffect, useState }  from "react";
import axios from 'axios'
import { Link,useNavigate, useParams } from "react-router-dom";

export default function Find(){
    let {id} = useParams()
    
    
    let[emp,setEmployee]=useState({
        "EmployeeId":"",
        "EmployeeName":"",
        "EmployeeSalary":""
    });
  
    function getEmployeeById(){
        axios.get(`http://localhost:8000/employees/${id}/`)
        .then((res)=>{
            setEmployee(res.data)
        })
        .catch((error)=>{
            alert(error)
        })
    }
 
   useEffect(()=>{
    getEmployeeById()
   },[])
   

    return(
        <React.Fragment>
           
           
            <div className="container mt-5">
                <div className="row d-flex justify-content-center">
                   
                   <div className="col-md-5">
                     <div className="card">
                        <div className="card-header  text-center bg-primary text-white">
                                <p className="h1 ">Employee Infomation</p>
                        </div>
                        <div className="card-body">
                            <form action="" >
                                <div className="form-group">
                                    <label htmlFor="" className="form-label">Employee ID</label>
                                    <input type="number" name="EmployeeId" value={emp.EmployeeId} min={'1111'} max={'9999'} className="form-control" placeholder="Employee ID"/>
                                </div>
                                  <div className="form-group">
                                    <label htmlFor="" className="form-label">Employee Name</label>
                                    <input type="text"  name="EmployeeName"  value={emp.EmployeeName} className="form-control" placeholder="Employee Name"/>
                                </div>
                                  <div className="form-group">
                                    <label htmlFor="" className="form-label">Employee Salary</label>
                                    <input type="number" name="EmployeeSalary"  value={emp.EmployeeSalary} max={'200000'} min='30000' className="form-control" placeholder="Employee Salary"/>
                                </div>
                               
                               
                                <Link to={`/edit/${emp.EmployeeId}/`} className="btn btn-warning btn-md w-100">Edit</Link>
                                <Link to='/employees' className="btn btn-success btn-md w-100">Employees</Link>
                                
                            </form>
                        </div>
                    </div>
                   </div>
                </div>
            </div>




        </React.Fragment>
    )
}