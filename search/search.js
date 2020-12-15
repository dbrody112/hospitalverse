import React, { useState } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Switch,
  Redirect
} from 'react-router-dom';
import {NavBar} from '../navbar/navbar_implementation';
import { Form, Input, Button } from 'semantic-ui-react';

const SearchForm = () => {
	const [street_address,setStreetAddress] = useState('');
	const [town,setTown] = useState('');
	const [state, setState] = useState('');
	const [zip,setZip] = useState('');
	const [radius,setRadius] = useState(30);
	const [success,setSuccess] = useState('');

	return(
	 <Form className = "rating-container">
	  <h1 className = "default">Search Form</h1>
      <Form.Field>
        <Input
        placeholder="Enter Street Address"
        value={street_address}
        onChange={event => setStreetAddress(event.target.value)}
        />
      </Form.Field>
	 
	  <Form.Field>
        <Input
        placeholder="Enter Town"
        value={town}
        onChange={event => setTown(event.target.value)}
        />
      </Form.Field>
	  
	  <Form.Field>
        <Input
        placeholder="Enter State"
        value={state}
        onChange={event => setState(event.target.value)}
        />
      </Form.Field>
	  
	  <Form.Field>
        <Input
        placeholder="Zip Code"
        value={zip}
        onChange={event => setZip(event.target.value)}
        />
      </Form.Field>
	  
	  <Form.Field>
	  <label>Radius (mi) (0-1000)</label>
        <Input
        placeholder="Enter Rating Out of 5"
		type = "range"
		min = "0"
		max = "1000"
		step = "10"
        value={radius}
        onChange={event => setRadius(event.target.value)}
        />
		<label>Current Radius: {radius} mi</label>
      </Form.Field>
	  <br/>
	  <br/>
      <Form.Field>
        <Button onClick= {async () => {
		  const new_street_address = street_address
		  const new_town = town;
		  const new_state = state;
		  const new_zip = zip;
		  const new_radius = radius;
          const response = await fetch('/users/hospital_search', {
            method: "POST",
            headers: {
              "Content_Type": "application/json"
            },
            body:
              JSON.stringify({street_address:new_street_address, town: new_town,zip:new_zip, radius:new_radius})
            })
          if (response.ok) {
            console.log("Response Worked! ");
			response.json().then(data=>{
				setSuccess(data.success)
				if(data.success === true)
				{
					localStorage.setItem('hospital_names', data.hospital_names);
					localStorage.setItem('hospital_ids', data.hospital_ids);
					localStorage.setItem('hospital_scores', data.hospital_scores);
					localStorage.setItem('haversines', data.haversines);
					localStorage.setItem('hospitals', data.hospitals);
				}
				});
        }
		}}>
        Submit</Button>
		<br/>
		<br/>
		{success==true? <Redirect to = "/filtered_hospitals"/>:<p className="alert"> Enter in the 
		correct information. If you only have limited information filling in only the state and city is fine. Note: All fields are case-sensitive.</p>}
		</Form.Field>
		

    </Form>
  );
};


export class HospitalSearch extends React.Component {
	render() {
	return(
		<div>
			<NavBar/>
			<SearchForm/>
		</div>
	  )
	}
}