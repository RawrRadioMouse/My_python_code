/*

Complete the reverseString function; it has one parameter, . You must perform the following actions:

Try to reverse string  using the split, reverse, and join methods.
If an exception is thrown, catch it and print the contents of the exception's message on a new line.
Print s  on a new line. If no exception was thrown, then this should be the reversed string; if an exception was thrown, this should be the original string.


/*
 * Complete the reverseString function
 * Use console.log() to print to stdout.
 */
function reverseString(s) {
    try{
        var sArray = s.split(""); //turn  the string into an array by splitting it up
        var sReverse = sArray.reverse(); //reverse the values in the array
        var s = sReverse.join(""); //put the string back together
    }
    catch(err) {
        console.log(err.message);
    }
        console.log(s) ;
}   
