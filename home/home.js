import React, { useState } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Switch,
} from 'react-router-dom';
import {NavBar} from '../navbar/navbar_implementation';

export class Home extends React.Component {
	render() {
	return(
		<div>
			<NavBar/>
			<img src = "https://hospital-bucket.s3.us-east-2.amazonaws.com/lgbtq_self_care.webp"/>
			<h3 className = "default">("https://driveforwardfoundation.org/wp-content/uploads/2020/03/coronavirus-Crisis-1.png")</h3>
			<img src = "https://hospital-bucket.s3.us-east-2.amazonaws.com/lgbtq_discrim.jpg"/>
			<h3  className = "default">("https://mediad.publicbroadcasting.net/p/kunr/files/styles/x_large/public/201911/revised_insta_audiogram.jpg")</h3>
		</div>
	  )
	}
}
	