function showTime(){
    // getting hours, minutes and seconds. initializing at AM.
    var date = new Date();
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var seconds = date.getSeconds();
    var am_pm = "AM";
    
    // ensuring that midnight is displayed as 12:xxAM and not 00:xxAM
    if(hours == 0){
        hours = 12;
    }
    
    // forcing the clock off 24 hour, using AM/PM instead
    if(hours>12){
        hours = hours - 12;
        am_pm = "PM";
    }
    
    // appending a 0 to the clock display if only single digit so clock maintains xx:xx format
    hours = (hours < 10) ? '0' + hours : hours;
    minutes = (minutes < 10) ? '0' + minutes : minutes;
    seconds = (seconds < 10) ? '0' + seconds : seconds;
    
    // putting the time variable together which will be displayed
    var time = hours + ':' + minutes + ':' + seconds + ' ' + am_pm;
    
    // adding time to the div
    document.getElementById("MyClockDisplay").innerText = time;
    document.getElementById("MyClockDisplay").textContent = time;
    
    // showing every second
    setTimeout(showTime, 1000);
}

// calling function
showTime();