/*
Backreferences match the same text as previously matched by a capturing group. EG the 1$ is matching the what we found one occurence ago (the starting char)
/*/


function regexVar() {

    var re = /^([aeiou]).*\1$/
    /*
     * Declare a RegExp object variable named 're'
     * It must match a string that starts and ends with the same vowel (i.e., {a, e, i, o, u})
     */
    
    
    /*
     * Do not remove the return statement
     */
    return re;
}
