import React, { useState} from 'react';
import { Form, Input, Button } from 'semantic-ui-react';
import 'semantic-ui-css/semantic.min.css';
import {Redirect} from 'react-router-dom';

export const Login = ()  => {
  const [username, setUsername] = useState(''); //  Empty String
  const [user_password,setPassword] = useState('')
  const [title,setTitle] = useState('')
  const[verified,setVerified] = useState('')
  return (
    <Form className = "login-container">
	  <img src = "https://hospital-bucket.s3.us-east-2.amazonaws.com/hospitalverse.png" width = "260" height = "120"/>
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
        placeholder="Enter Password"
        value={user_password}
        onChange={event => setPassword(event.target.value)}
        />
      </Form.Field>
      <Form.Field>
	  
        <Button onClick= {async () => {
          const user = username;
		  const new_password = user_password;
          const response = await fetch("/user", {
            method: "POST",
            headers: {
              "Content_Type": "application/json"
            },
            body:
              JSON.stringify({
			  username: user,user_password:new_password})
            })
          if (response.ok) {
            console.log("Response Worked! ");
            
            
          }
          else {
            console.log("Title not found")
            
          }
        }}>
        Sign Up</Button>
		<Button onClick = {async () => {
          const user = username;
		  const new_password = user_password;
          const response = await fetch("/user/verify", {
            method: "POST",
            headers: {
              "Content_Type": "application/json"
            },
            body:
              JSON.stringify({
			  username: user,user_password:new_password})
            })
          if (response.ok) {
            console.log("Response Worked! ");
			response.json().then(data=>{
				setVerified(data.authorized)
				console.log(data)
				if(data.authorized===true)
				{
					
					localStorage.setItem('access_token', data.access_token);
					localStorage.setItem('username', data.username);
				}
				});
          }
          else {
            console.log("Title not found") 
          }
		   console.log(verified);
        }}> Sign In </Button>
		{verified === true ? <Redirect to='/home' /> :<Redirect to='/' />}
		
      </Form.Field>
	  {verified !== '' ? <p className = 'alert'>Incorrect username and/or password </p>:<p> </p>}
	  <p className = 'default'>Please enter a username (an email) and a password. If you do not already have an account sign up but if you do have one sign in. Note that passwords are not stored and 
	  any and all actions made on this webapp will be anonymous. It is preferred to use an unidentifying email for username. </p>
    </Form>
  );
};