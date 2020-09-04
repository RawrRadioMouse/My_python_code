'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    var i;
    var vowels = 'aeiou';

    for (i = 0; i < s; i++)   {
        if (s.includes(vowels))
            console.log("dddd");
        
        }
}

Example above explained:

First, we set a variable before the loop starts (var i = 0;)
Then, we define the condition for the loop to run. As long as the variable is less than the length of the array (which is 4), the loop will continue
Each time the loop executes, the variable is incremented by one (i++)
Once the variable is no longer less than 4 (array's length), the condition is false, and the loop will end
