import React, { useState } from 'react';
import {
  BrowserRouter as Router,
  Route,
  Switch,
} from 'react-router-dom';
import {NavBar} from '../navbar/navbar_implementation';

export class About extends React.Component {
	render() {
	return(
		<div className = "about-container">
			<NavBar/>
			<h1>Why?</h1>
			<h3> The reason for this app is because of the state that the United States is in. Not only has the current president, Donald Trump,
			forwarded policies that legalize healthcare discrimination for LGBTQIA+ but a study has shown that 1 in 5 in LGBTQIA+ are uncomfortable 
			on getting healthcare because of fear of discrimination. Under this pandemic healthcare is a need right now so this app is to save some 
			LGBTQIA+ lives!!!</h3>
			<h1>Functionality</h1>
			<h3> There are three functions here and I will list them below:</h3>
			<ul><li><h3>Profile: Set your sexual orientation and age (optionally) to be an anonymous user in data visualizations representing your sexuality in your rating.
			This can be very important because different sexualities may be treated differently</h3></li>
			<br/>
			<br/>
			<li><h3>Review: This is an important function of the app where users can review hospitals both numerically and verbally. Please be aware that any activity on this webapp,
			regardless of the section is completely anonymous.</h3></li>
			<br/>
			<br/>
			<li><h3>Search: This is the main goal of the app where users can find hospitals near their location and access valuable information on them regarding LGBTQ-friendliness.
			The more ratings there are the more accurate it becomes</h3></li></ul>
		</div>
	  )
	}
}