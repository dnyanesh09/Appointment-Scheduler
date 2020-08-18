import React, { useState } from 'react';
import './AppointmentLink.css'
import DatePicker from "react-datepicker";
 
import "react-datepicker/dist/react-datepicker.css";            

export const Link = (props) =>{
    return(
        <div className="app1">
            {/* <a href="/#" onClick= {props.handleBook}>Book</a> */}
            <button onClick= {props.handleBook} className="app1" >Book An Appointment</button>
        </div>
    )
}

export const DateSelector = (props) =>{
    const [startDate, setStartDate] = useState(new Date());

    // setDate = (date) =>{
    //     setStartDate(date);
    //     props.selectTime(date);
    // }

    
    return(
        <div className="app1">
            <p>Please Select Date and Time for Appointment</p>
            <DatePicker 
                // selected = {startDate}
                // onChange={date => setStartDate(date)}
                selected = {startDate}
                onChange = { date => {setStartDate(date); props.selectTime(date)} }
                
                // onChangeRaw = {date =>props.selectTime(date)}
                // onSelect = {date => props.selectTime(date)}
                // onSelect = {props.selectTime(startDate)}
                showTimeSelect
                // scrollableYearDropdown
                showYearDropdown
                showMonthDropdown
                dropdownMode = "select"
                dateFormat="yyyy/MM/dd H:mm "
                // timeFormat = "h:mm"
                // tim
                minDate = {new Date()}
                isClearable
                placeholderText= "Appointment Date and Time"
                // onCalendarClose = {startDate =>props.selectTime(startDate)}            
            />
            <button onClick={props.callService}>Book My Appointment</button>
        </div>
    )
}