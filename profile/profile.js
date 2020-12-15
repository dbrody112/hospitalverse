import React, { useState } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Switch,
  Redirect
} from 'react-router-dom';
import {NavBar} from '../navbar/navbar_implementation';

import { Form, Input, Button,Radio,Select,TextArea} from 'semantic-ui-react';

export const ProfileForm = () => {
	
	const [sexualOrientation,setSexualOrientation] = useState('');
	const [age, setAge] = useState('');
	const [success,setSuccess] = useState(''); 
	const [username,setUsername] = useState('')
	const [old_password, setOldPassword] = useState('')
	const [new_password, setPassword] = useState('')
	const [empty, setEmpty] = useState(true)
	const [authorized, setAuthorized] = useState(false)
	
	return(
	 <Form className = "rating-container">
	  <h1 className = "default">Update Optional Fields</h1>
      <Form.Field>
        <Input
        placeholder="Enter Sexual Orientation (optional)"
        value={sexualOrientation}
        onChange={event => setSexualOrientation(event.target.value)}
        />
      </Form.Field>
	  <br/>
	  <br/>
	  <Form.Field>
	  <label>Age</label>
        <Input
		type = "range"
		min = "0"
		max = "100"
		step = "1"
        value={age}
        onChange={event => setAge(event.target.value)}
        />
		<label>{age}</label>
      </Form.Field>
	  <Button onClick= {async () => {
          const new_age = age
		  const new_sexualOrientation = sexualOrientation
		  const username = localStorage.getItem("username");
          const response = await fetch("/update/optional", {
            method: "POST",
            headers: {
              "Content_Type": "application/json"
            },
            body:
              JSON.stringify({username:username, age:new_age,sexual_orientation:new_sexualOrientation})
            })
          if (response.ok) {
            console.log("Response Worked! ");
			response.json().then(data=>{setEmpty(data.empty)});
			console.log(empty)
          }
          else {
            console.log("Title not found")
			
          }
        }}>
        Update</Button>
		{empty == false ? <h3 className = "default">process went through!!</h3>:<br/>}
	  <br/>
	  <p className = "default">-----------------------------------------------------------------------------</p>
	  <br/>
	  <h1 className = "default">Update Credentials</h1>
      <Form.Field>
	  <Form.Field>
        <Input
        placeholder="Enter Username"
        value={username}
        onChange={event => setUsername(event.target.value)}
        />
      </Form.Field>
	  <Form.Field>
        <Input
		type = "password"
        placeholder="Enter Old Password"
        value={old_password}
        onChange={event => setOldPassword(event.target.value)}
        />
      </Form.Field>
	  <Form.Field>
        <Input
		type = "password"
        placeholder="Enter New Password"
        value={new_password}
        onChange={event => setPassword(event.target.value)}
        />
      </Form.Field>
        <Button onClick= {async () => {
          const newPassword = new_password
		  const oldPassword = old_password
		  const username = localStorage.getItem("username");
          const response = await fetch('/update/password', {
            method: "POST",
            headers: {
              "Content_Type": "application/json"
            },
            body:
              JSON.stringify({username:username, new_password:newPassword,old_password:oldPassword})
            })
          if (response.ok) {
            console.log("Response Worked! ");
			response.json().then(data=>{setAuthorized(data.authorized)});
			console.log(authorized)
          }
          else {
            console.log("Title not found")
			
          }
        }}>
        Update</Button>
		{authorized == true ? <h3 className = "default">process went through!!</h3>:<br/>}
		
		</Form.Field>

    </Form>
  );
};


export class Profile extends React.Component {
	render() {
	return(
		<div>
			<NavBar/>
			<ProfileForm/>
		</div>
	  )
	}
}