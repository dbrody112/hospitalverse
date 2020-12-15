import React, { useState } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Switch,
  Redirect
} from 'react-router-dom';
import {NavBar} from '../navbar/navbar_implementation';
import { Form, Input, Button } from 'semantic-ui-react';

export const Filtered= () =>{
	
	const hospitals = localStorage.getItem("hospitals").split("$,");
	
	const [success,setSuccess] = useState('');
	/*localStorage.setItem('zip_code',data.zip_code);
							localStorage.setItem('phone_number',data.phone_number);
							localStorage.setItem('hospital_name',data.hospital_name);
							localStorage.setItem('website',data.website);
							localStorage.setItem("mapsUrl",data.mapsUrl);
							localStorage.setItem("mapsUrl",data.mapsUrl);*/
	
	return(
		<div>
			
			<NavBar/>
			<br/>
			
			{hospitals.map(name=>(
				
				<div className = "search-container">
				<Button className = "about-container" onClick = {async () => {
				const hospital_id = name.split(",")[2];
				console.log(hospital_id);
				const response = await fetch('/hospital_chosen', {
				method: "POST",
				headers: {
					"Content_Type": "application/json"
					},
					body:
						JSON.stringify({hospital_id:hospital_id})
					})
				if (response.ok) {
					console.log("Response Worked! ");
					response.json().then(data=>{
						setSuccess(data.success)
						if(data.success === true)
						{
							localStorage.setItem("street_address",data.street_address);
							localStorage.setItem("town",data.town);
							localStorage.setItem("state",data.state);
							localStorage.setItem('zip_code',data.zip_code);
							localStorage.setItem('phone_number',data.phone_number);
							localStorage.setItem('hospital_name',name.split(",")[1]);
							localStorage.setItem('website',data.website);
							localStorage.setItem("mapsUrl",data.mapsUrl);
							localStorage.setItem("total_score",data.total_score);
							localStorage.setItem("total_score",data.total_score);
							localStorage.setItem("non_discrimination_and_staff_training", data.non_discrimination_and_staff_training)
							localStorage.setItem("sub_patient_non_discrimination", data.sub_patient_non_discrimination);
							localStorage.setItem("sub_visitation_non_discrimination", data.sub_visitation_non_discrimination);
							localStorage.setItem("sub_employment_non_discrimination",data.sub_employment_non_discrimination);
							localStorage.setItem("sub_staff_training", data.sub_staff_training);
							localStorage.setItem("patient_services_and_support", data.patient_services_and_support);
							localStorage.setItem("employee_benefits_and_policies", data.employee_benefits_and_policies);
							localStorage.setItem("sub_employee_policies_and_benefits", data.sub_employee_policies_and_benefits);
							localStorage.setItem("sub_transgender_inclusive_health_insurance", data.sub_transgender_inclusive_health_insurance);
							localStorage.setItem("responsible_citizenship", data.responsible_citizenship);
							localStorage.setItem("patient_and_community_engagement",data.patient_and_community_engagement);
						}
					});
					console.log(success)
				}
				else {
					console.log("Title not found")
				}
				}}>
					<h3>{name.split(",")[1]}</h3>
					<h3>{(parseFloat(name.split(",")[0])*0.62137119).toFixed(2)} miles away</h3>
					<h3>Score: {name.split(",")[3].split('$')[0] == -1? 'N/A':(parseFloat(name.split(",")[3].split('$')[0])).toFixed(2)}</h3>
					<h3>Average Rating (Out of 5): {name.split(",")[4].split('$')[0]}</h3>
					#<h3>Average Rating (Out of 5): {(parseInt(name.split(",")[4].split('$')[0])).toFixed(0)}</h3> (update but committed late)
				</Button>
				{success === true ? <Redirect to = '/hospital_page'/>:<br/>}
				<br/>
				</div>
			))}
			
		</div>
	)
};
