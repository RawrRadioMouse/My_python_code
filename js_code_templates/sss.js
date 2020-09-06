/*
Complete the vowelsAndConsonants function in the editor below. It has one parameter, a string, , consisting of lowercase English alphabetic letters (i.e., a through z). The function must do the following:

First, print each vowel in  on a new line. The English vowels are a, e, i, o, and u, and each vowel must be printed in the same order as it appeared in .
Second, print each consonant (i.e., non-vowel) in  on a new line in the same order as it appeared in .

 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    var i;
    var vowels = 'aeiou';
    var consonants = [];
    for (i in s)   {
        if (vowels.includes(s[i])){
            console.log(s[i]);
        }
    else {
        consonants += s[i] + '\n';
    }
    }
console.log(consonants);
}

/*
Example above explained:

First, we set a variable before the loop starts (var i = 0;)
Then, we define the condition for the loop to run. As long as the variable is less than the length of the array (which is 4), the loop will continue
Each time the loop executes, the variable is incremented by one (i++)
Once the variable is no longer less than 4 (array's length), the condition is false, and the loop will end
/*
