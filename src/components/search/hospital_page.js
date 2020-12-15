import React, { useState } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Switch,
  Redirect
} from 'react-router-dom';
import {NavBar} from '../navbar/navbar_implementation';
import { Form, Input, Button } from 'semantic-ui-react';

export const HospitalPage = () =>{
	
	
	const street_address = localStorage.getItem("street_address");
	const town = localStorage.getItem("town");
	const state = localStorage.getItem("state");
	const zip_code = localStorage.getItem('zip_code');
	const phone_number = localStorage.getItem('phone_number');
	const hospital_name = localStorage.getItem('hospital_name');
	const website = localStorage.getItem('website');
	const mapsUrl = localStorage.getItem("mapsUrl");
	const total_score = localStorage.getItem("total_score");
	const non_discrimination_and_staff_training= localStorage.getItem("non_discrimination_and_staff_training")
	const sub_patient_non_discrimination = localStorage.getItem("sub_patient_non_discrimination");
	const sub_visitation_non_discrimination = localStorage.getItem("sub_visitation_non_discrimination");
	const sub_employment_non_discrimination = localStorage.getItem("sub_employment_non_discrimination");
	const sub_staff_training=localStorage.getItem("sub_staff_training");
	const patient_services_and_support = localStorage.getItem("patient_services_and_support");
	const employee_benefits_and_policies = localStorage.getItem("employee_benefits_and_policies");
	const sub_employee_policies_and_benefits = localStorage.getItem("sub_employee_policies_and_benefits");
	const sub_transgender_inclusive_health_insurance = localStorage.getItem("sub_transgender_inclusive_health_insurance");
	const responsible_citizenship = localStorage.getItem("responsible_citizenship");
	const patient_and_community_engagement = localStorage.getItem("patient_and_community_engagement");
	
	const [success,setSuccess] = useState('');
	return(
		<div className = "search-container">
			
			<NavBar/>
			<br/>
			<h1>{hospital_name} ----- Score: {total_score}</h1>
			
			<h2>Address</h2>
			<h3>{street_address}</h3>
			<h3>{town}, {state}, {zip_code}</h3>
			<h2>Phone Number</h2>
			<h3>{phone_number}</h3>
			<a href = {website}><h2>Website</h2></a>
			<h3>({website})</h3>
			<a href = {mapsUrl}><h2>Google Maps URL</h2></a>
			<h3> ({mapsUrl})</h3>
			<h1>Criteria</h1>
			<h5>(pulled from the Human Rights Campaign Healthcare Equality Index)</h5>
			<h2>Non-Discrimination & Staff Training ------------- {non_discrimination_and_staff_training}</h2>
			<h3>The Non-Discrimination and Staff Training criteria represents the foundational policies and practices in providing 
			LGBTQ-inclusive patient centered care. These questions assess whether a facility has LGBTQ-inclusive policies and whether the 
			facility shares these policies with the public and its patients and staff. In order to most effectively implement these policies, 
			we also require training for staff in LGBTQ-inclusive care. All questions in this section are scored and must be met in order to receive full credit: up to 40 points.</h3>
			<h2>Breakdown</h2>
			<div><h3>Patient Non-Discrimination : {sub_patient_non_discrimination}</h3><h4> <li>Patient Non-Discrimination Policy is LGBTQ-inclusive</li> <li>Patient Non-Discrimination Policy is communicated</li></h4></div>
			<br/>
			<div><h3>Visitation Non-Discrimination : {sub_visitation_non_discrimination}</h3><h4><li>Visitation Policy is LGBTQ-inclusive</li><li>Visitation Policy is communicated</li></h4></div>
			<br/>
			<div><h3>Employment Non-Discrimination : {sub_employment_non_discrimination}</h3><h4><li>Employment Non-Discrimination Policy is LGBTQ-inclusive</li><li>Employment Non-Discrimination Policy is communicated</li></h4></div>
			<br/>
			<div><h3>Staff Training : {sub_staff_training}</h3><h4><li>LGBTQ staff training requirement was met</li><li>LGBTQ staff training options were communicated</li></h4></div>
			<br/>
			<h2> Patient Services & Support -------------  {patient_services_and_support}</h2>
			<h3>The questions in this criteria all relate to best practices in the provision of Patient Services & 
			Support—this could include providing LGBTQ clinical services, hiring a patient advocate for transgender patients, 
			collecting sexual orientation and gender identity data in health records or providing training on 
			LGBTQ inclusive medical decision making options, and more. In order to receive full credit (30 points) for this criteria, 
			a facility must have implemented 11 or more of the recommended best practices. A facility may receive partial credit (15 points) for this 
			criteria if it has implemented 6 to 10 of the best practices.</h3>
			<h2>Employee Benefits & Policies:  -------------  {employee_benefits_and_policies}</h2>
			<h3>The Employee Benefits and Policies criteria focuses on creating an LGBTQ-inclusive workplace for healthcare facilities’ 
			employees—these efforts include equal benefits for LGBTQ employees, transgender-inclusive health insurance benefits, 
			employee resource groups, LGBTQ-inclusive hiring efforts, employee transition support, and more. This criterion is divided into 
			two scored subsections. In order to receive full credit (15 points) for the first subsection, a facility must have implemented 7 
			or more of the recommended best practices. A facility may receive partial credit (10 points) for this criteria if it has implemented 
			4 to 6 of the best practices. The second subsection is related to the provision of transgender healthcare benefits for employees and is worth 5 points.</h3>
			<h2>Breakdown</h2>
			<div><h3>Employee Policies and Benefits : {sub_employee_policies_and_benefits}</h3><h4> <li>Employee Policies and Benefits</li></h4></div>
			<br/>
			<div><h3>Transgender Inclusive Health Insurance : {sub_transgender_inclusive_health_insurance}</h3><h4> <li>Employee Policies and Benefits</li></h4></div>
			<br/>
			<h2>Patient & Community Engagement   ------------- {patient_and_community_engagement}</h2>
			<h3>The Patient & Community Engagement criteria focuses on community outreach and promotion to let the LGBTQ community know that healthcare facilities are a welcoming and affirming setting, 
			working toward LGBTQ inclusion. Efforts to promote community inclusion may include, meeting with local LGBTQ groups, sponsoring a local pride event, developing LGBTQ focused marketing materials, 
			and more. In order to receive full credit (10 points) for this section, a facility must have implemented 4 or more of the recommended best practices. A facility may receive partial credit (5 points) 
			for this criteria if it has implemented 2 to 3 of the best practices.</h3>
			<h2>Responsible Citizenship  ------------- {responsible_citizenship}</h2>
			<h3>This section focuses on known activity that would undermine LGBTQ equality or patient care. Healthcare facilities will have 25 points deducted from their score for a large-scale official or public anti-LGBTQ blemish on their recent records. Scores on this criterion are based on information that has come to HRC Foundation’s attention related to topics including but not limited to:revoking inclusive LGBTQ policies or practices;
facilitating the continued practice of healthcare providers that provide or promote LGBTQ related treatment or services to that have been discredited by mainstream medical and mental health organizations, including, but not limited to, “conversion therapy”;
engaging in proven practices that are contrary to the facility's written LGBTQ patient or employment policies;
or directing charitable contributions or other public support to organizations whose primary mission includes advocacy against LGBTQ equality or care.</h3>

		</div>
	)
}
	
