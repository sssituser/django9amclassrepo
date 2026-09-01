import React,{useState,useEffect} from  'react'
import axios from 'axios';
export default function Employees(){
    let[employees,setEmployees]=useState([]) ;
    function getEmployees(){
        axios.get("http://localhost:8000/employees/")
        .then((res)=>{
            setEmployees(res.data)
        })
        .catch((error)=>{
            alert(error)
        })
    }
    useEffect(()=>
        {
            getEmployees()
        },[])

    return(
        <React.Fragment>
            <p className="h1 text-center">Employees Information</p>
            
            <div className="row d-flex justify-content-center">
                <div className="col-md-5">
                {
                    employees.length>0 ?
                <p className="text-center text-danger">Emploees found</p>
                :
                <p className="lead text-center text-success">Employees not found</p>
                }
                </div>
            </div>
        </React.Fragment>
    )
}