import React, { useState } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Switch,
  Redirect
} from 'react-router-dom';
import {NavBar} from '../navbar/navbar_implementation';
import { Form, Input, Button,Radio,Select,TextArea} from 'semantic-ui-react';
import 'semantic-ui-css/semantic.min.css';



const RatingForm = () => {
	const [hospitalName,setHospitalName] = useState('');
	const [rating,setRating] = useState(2);
	const [review, setReview] = useState('');
	const [success, setSuccess] = useState('');
	return(
	 <Form className = "rating-container">
	  <h1 className = "default">Rating Form</h1>
      <Form.Field>
        <Input
        placeholder="Enter Hospital Name"
        value={hospitalName}
        onChange={event => setHospitalName(event.target.value)}
        />
      </Form.Field>
	  <br/>
	  <br/>
	  <Form.Field>
	  <label>Rating Out of 5 </label>
        <Input
        placeholder="Enter Rating Out of 5"
		type = "range"
		min = "0"
		max = "5"
		step = "1"
        value={rating}
        onChange={event => setRating(event.target.value)}
        />
		<label>Current Rating: {rating}</label>
      </Form.Field>
	   <br/>
	  <br/>
	  <Form.Field control={TextArea} placeholder="Enter Verbal Review (optional)"
	  
        value={review}
        onChange={event => setReview(event.target.value)}>
        <Input
    
        />
      </Form.Field>
	  <label>This is the {review}</label>
      <Form.Field>
        <Button onClick= {async () => {
          const hospital_name = hospitalName;
		  const new_rating = rating;
		  const new_review = review;
		  const username = localStorage.getItem("username");
          const response = await fetch("/user/rating", {
            method: "POST",
            headers: {
              "Content_Type": "application/json"
            },
            body:
              JSON.stringify({username:username, hospital_name: hospital_name,rating:new_rating, review:new_review})
            })
          if (response.ok) {
            console.log("Response Worked! ");
			response.json().then(data=>{setSuccess(data.success)});
			console.log(success)
          }
          else {
            console.log("Title not found")
          }
        }}>
        Submit</Button>
		{success === true ? <Redirect to = "/success"/>:<p className = "default">jkvguergvyrgvrey</p>}
		</Form.Field>

    </Form>
  );
};


export const Rating = () => {
	 return(
	 <div>
		<NavBar/>
		<RatingForm/>
	</div>
	)
};
	