s=("123")

# weapply the any() function to the filter method to the isalnum method with s variable as the argument
if any(filter(str.isalnum,s)):
    print("True")
else:
    print("False")
if any(filter(str.isalpha,s)):
    print("True")
else:
    print("False")
if any(filter(str.isdigit,s)):
    print("True")
else:
    print("False")
if any(filter(str.islower,s)):
    print("True")
else:
    print("False")
if any(filter(str.isupper,s)):
    print("True")
else:
    print("False")
