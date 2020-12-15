import React, { Component } from 'react'
import Navbar from "./Navbar";
import GlobalStyles from './Global';

export class NavBar extends React.Component {
	constructor(props)
	{
		super(props);
		this.state = {navbarOpen: false};
		this.handleNavbar = this.handleNavbar.bind(this);
	}
	handleNavbar = () => {
		this.setState({ navbarOpen: !this.state.navbarOpen });
	}
	render() {
		return (
		<>
			<Navbar 
			navbarState={this.state.navbarOpen} 
			handleNavbar={this.handleNavbar}
			/>
			<GlobalStyles />
		</>
		)
	}
  }
