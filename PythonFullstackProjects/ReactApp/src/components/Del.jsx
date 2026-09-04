import axios from "axios";
import React, { useEffect, useState } from "react";
import { useParams,Link,useNavigate } from "react-router-dom";


export default function Del(){
    let navi = useNavigate()
    let {id} = useParams();
   
    function delEmployeeById(event){
        event.preventDefault()
        axios.delete(`http://localhost:8000/employees/${id}/`)
        .then(()=>{
            alert("Employee Deleted")
            navi('/employees')
        })
        .catch((er)=>{alert(er)})
    }

      

    return(
        <React.Fragment>
            <div className="container mt-5">
                <div className="row justify-content-center">
                    <div className="col-md-6">
                        <div className="card mt-5">
                            <div className="card-header bg-default text-center text-danger">
                                <p className="h3">Do You Want To Delete Employee ? </p>
                            </div>
                            {/* <div className="card-body">
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
                            </div> */}
                            <div className="card-footer">
                              <form action="" onSubmit={delEmployeeById}>
                                <button className="btn btn-md btn-danger w-100">YES</button>
                              <Link to='/employees' className="btn btn-md btn-secondary w-100">NO</Link>
                              </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </React.Fragment>
    )
}