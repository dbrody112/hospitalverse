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

export const RatingSuccess = () => {
	 return(
	 <div>
		<NavBar/>
		<h1 className = "large">SUCCESS!!!</h1>
	</div>
	)
};
