/* trying to teach myself JavaScript by using the codewars site in combination with freecodecamp

*/

// reverses a given string
function solution(str){
    var new_str = '';
     
     for(var i = str.length - 1; i >=0; i--){
         new_str += str[i]
     }
     return new_str
}