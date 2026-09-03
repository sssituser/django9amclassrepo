import React from "react";
import { useParams,useNavigate,Link } from "react-router-dom";
import axios from 'axios'
export default function Del(){
    const {id} = useParams()
    
    let navi = useNavigate()
    
    function dell(event){
        event.preventDefault()
        axios.delete(`http://localhost:8000/employees/${id}/`)
        .then(()=>{
            alert("Record deleted")
            navi("/employees")
        })
        .catch((error)=>{
            alert(error)
        })
       }
    
    return(
        <React.Fragment>
            <div className="container mt-5">
                <div className="row justify-content-center">
                    <div className="col-md-4">
                        <div className="card mt-5 ">
                          <div className="card-body shadow-lg bg-primary text-white text-center">
                            <form onSubmit={dell}>
                                <p className="h1">Do You Want to Delete ?</p>
                                <button className="btn btn-danger btn-md">Yes</button>
                                <Link to={'/employees'} className="btn btn-md btn-warning">Cancel</Link>
                            </form>
                          </div>
                          
                        </div>
                    </div>
                </div>
            </div>
        </React.Fragment>
    )
}