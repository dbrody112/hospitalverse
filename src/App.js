import React, { useState } from 'react';
import logo from './logo.svg';
import {
  BrowserRouter as Router,
  Route,
  Switch,
} from 'react-router-dom';
import './App.css';
import {Login} from './components/home/searchForm';
import {NavBar} from './components/navbar/navbar_implementation';
import {Home} from './components/home/home';
import {HospitalSearch} from './components/search/search';
import {Profile} from './components/profile/profile';
import {Rating} from './components/rating/rating';
import {RatingSuccess} from './components/rating/rating_success';
import {About} from './components/about/about';
import {Filtered} from './components/search/filtered_hospitals'
import {HospitalPage} from './components/search/hospital_page'
//get rid of navbar for final proj

function App() {
  return (
  <Router>
    <div className="App">
      <header className="App-header">
	  
        
		<Switch>
			<Route exact path = "/" component = {Login} />
			<Route path = "/home" component = {Home} />
			<Route path = "/search" component = {HospitalSearch}/>
			<Route path = "/profile" component = {Profile}/>
			<Route path = "/rating" component = {Rating}/>
			<Route path = "/success" component = {RatingSuccess}/>
			<Route path = "/about" component = {About} />
			<Route path = "/filtered_hospitals" component = {Filtered}/>
			<Route path = "/hospital_page" component = {HospitalPage}/>
		</Switch>

      </header>
    </div>
	</Router>
  );
}

export default App;
