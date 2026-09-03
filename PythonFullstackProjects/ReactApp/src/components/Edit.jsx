import React, { useEffect, useState }  from "react";
import axios from 'axios'
import { Link,useNavigate, useParams } from "react-router-dom";

export default function Edit(){
    let {id} = useParams()
    let navi = useNavigate()
    
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

    function updateEmployee(event){
        event.preventDefault()
        axios.put(`http://localhost:8000/employees/${id}/`,emp)
        .then(()=>
            {
                alert("Record updated")
                navi("/employees")
            })
        .catch((error)=>{alert(error)})
    }
    


    function updateInput(event){
        
        setEmployee(
          {
            ...emp,
            [event.target.name]:event.target.value
          }
        )
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
                        <div className="card-header text-center bg-dark text-white">
                                <p className="h1">Edit Employee Here</p>
                        </div>
                        <div className="card-body">
                            <form action="" onSubmit={updateEmployee}>
                                <div className="form-group">
                                    <label htmlFor="" className="form-label">Employee ID</label>
                                    <input type="number" name="EmployeeId" onChange={updateInput} value={emp.EmployeeId} min={'1111'} max={'9999'} className="form-control" placeholder="Employee ID"/>
                                </div>
                                  <div className="form-group">
                                    <label htmlFor="" className="form-label">Employee Name</label>
                                    <input type="text"  name="EmployeeName" onChange={updateInput} value={emp.EmployeeName} className="form-control" placeholder="Employee Name"/>
                                </div>
                                  <div className="form-group">
                                    <label htmlFor="" className="form-label">Employee Salary</label>
                                    <input type="number" name="EmployeeSalary" onChange={updateInput} value={emp.EmployeeSalary} max={'200000'} min='30000' className="form-control" placeholder="Employee Salary"/>
                                </div>
                               
                               <button className="btn btn-primary btn-md w-100">Update</button>

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