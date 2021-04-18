/* small javascript stopwatch project. working on getting better at js.

includes a start, stop and reset button. */

// run app on page load

window.onload = function() {

    // initializing time variables and fetching buttons
    var seconds = 0;
    var msec = 0;
    var appendMsec = document.getElementById('msec');
    var appendSeconds = document.getElementById('seconds');
    var startButton = document.getElementById('start-button');
    var stopButton = document.getElementById('stop-button');
    var resetButton = document.getElementById('reset-button');
    var interval;

    // start button
    startButton.onclick = function(){

        clearInterval(interval);
        interval = setInterval(startTimer, 10);
    }

    // stop button
    stopButton.onclick = function(){

        clearInterval(interval);
    }

    // reset button
    resetButton.onclick = function(){

        clearInterval(interval);
        msec = '00';
        seconds = '00';
        appendMsec.innerHTML = msec;
        appendSeconds.innerHTML = seconds;
    }

    // function to start timer
    function startTimer() {
        
        // starting the time count
        msec++;

        /* following chain of if statements determine the time and append the appropriate information to the 
        stop watch display */

        // millisecond display
        if(msec < 9){
            appendMsec.innerHTML = '0' + msec;
        }

        if(msec > 9){
            appendMsec.innerHTML = msec;
        }

        // moving to seconds
        if(msec > 99){
            console.log('seconds')
            seconds++;
            appendSeconds.innerHTML = '0' + seconds;
            msec = 0; // reinitializing
            appendMsec.innerHTML = '0' + 0;
        }

        if(seconds > 9){
            appendSeconds.innerHTML = seconds;
        }
    }


}   