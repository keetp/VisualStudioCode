/* trying to teach myself JavaScript by using the codewars site in combination with freecodecamp


freecodecamp stuff follows. basic syntax exercises completed before attempting the following. codewars stuff found in CodeWars.js
*/

// recursion practice
// implementation of recursion to replace a loop. function to be changed is as follows:

// multiplying the first n elements of an array, arr.
function multiply(arr, n) {
    var product = 1;
    for(var i = 0; i <= n; i++){
        product *= arr[i];
    }
}   return product;

// implemented with recursion. note that 
// multiply(arr, n) == multiply(arr, n - 1) * arr[n - 1]

function multiply(arr, n) {
    // base case
    if (n <= 0){
        return 1;
    } else {
        return (multiply(arr, n-1) * arr[n-1])
    }
}   

// similar function which uses recursion to calculate sum

function sum(arr, n) {
    // base case
    if (n <= 0){
        return 0;
    } else {
        return (sum(arr, n-1) + arr[n-1])
    }
}
