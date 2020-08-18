import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import { Widget, addResponseMessage, addLinkSnippet, addUserMessage, renderCustomComponent, toggleInputDisabled } from 'react-chat-widget';
import 'react-chat-widget/lib/styles.css';
import Chat from './ChatWindow';
import axios from 'axios';
import { Link, DateSelector } from './AppintmentLink';
import DatePicker from "react-datepicker";


class App extends Component {
  
  state = {
    stage : 1,
    ipMsg : "",
    opMsg : "",
    flow : null,    
    uname : "",
    email : "",
    phone : "",
    date : new Date()
    
  }

  componentDidMount=()=>{
    // this.setState({stage:1})
    renderCustomComponent(Link,{handleBook: this.setFlow_Stage});
    toggleInputDisabled();
    
  }

  setFlow_Stage = () =>{
    // this.setState({flow:"appt", stage:1},);
    this.handleChatFlow();
  }

  handleChatFlow = () =>{
    if (this.state.stage === 1){
        addResponseMessage("Please Enter your user name");
        toggleInputDisabled();
    }

  }

   handleNewUserMessage = (newMessage) => {
    console.log("New Message : "+newMessage);
    if(this.state.stage === 1){
      this.setState({uname:newMessage, stage : 2})
      addResponseMessage("Please Enter your Email ID");
      
    }
    else if(this.state.stage === 2){
      this.setState({email:newMessage, stage : 3})
      addResponseMessage("Please Enter your Contact Number");
    }
    else if(this.state.stage === 3){
      this.setState({phone:newMessage, stage : 4});
      // addResponseMessage("Please Select Date & Time for Appointment");   
      // renderCustomComponent(<DatePicker />) 
      renderCustomComponent(DateSelector,{startDate : this.state.date,changeTime :this.handleTimechange, selectTime : this.handleTimechange, callService: this.callService});     
      // addResponseMessage(<DateSelector />);
    }  
    else if(this.state.stage === 4){
      this.setState({stage : 5});
    }
    console.log(JSON.stringify(this.state)); 
    // , this.callService()
    // Now send the message throught the backend API
  };
  handleTimechange = (date) =>{
      this.setState({date : date},
        console.log("New State : "+ JSON.stringify(this.state))
        );
  }

  callService = () =>{
    // this.handleTimechange(dt);
    let params = {
      msg : "newMessage",
      stage : this.state.stage,
      uname : this.state.uname,
      email : this.state.email,
      phone : this.state.phone,
      year : this.state.date.getFullYear(),
      month : this.state.date.getMonth()+1,
      date : this.state.date.getDate(),
      hours : this.state.date.getHours(),
      mins : this.state.date.getMinutes()  
    }
    axios.post("http://localhost:7002/chat", params)
    .then(
      res=>{
        console.log(JSON.stringify(res))
       
        
        addResponseMessage("Booking");
      }
    
    )
  }
  
  render (){
    
    return (
    <div className="App">
      {/* <Chat/> */}
      <Widget 
        handleNewUserMessage = {this.handleNewUserMessage}
        title = "Appointment Scheduler"
        subtitle = "Welcome to Scheduling Bot"
      />
      
    </div>
  );
  }
}

export default App;
