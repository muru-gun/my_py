a = float(input("Enter 1st number : "))
b = float(input("Enter 2nd number : "))
c = float(input("Enter 3rd number : "))

if a!=b and a!=c and c!=b: #to make sure all numbers are different
    if a>b and a>c: 
        print("The 1st number '", a, "' is greater")

    elif b>a and b>c:
        print("The 2nd number '", b, "' is greater")

    elif c>a and c>a:
        print("The 3rd number '", c, "' is greater")

elif a==b and a!=c:  #to check if any two numbers are same
    if c>a:
        print("The 3rd number '", c, "' is greater")
    else:
        print("The 1st number '", a, "' and the 2nd number '", b, "' are equal and greater.")

elif a==c and a!=b:  #to check if any two numbers are same
    if b>a:
        print("The 2nd number '", b, "' is greater")
    else:
        print("The 1st number '", a, "' and the 3rd number '", c, "' are equal and greater.")

elif b==c and a!=b:  #to check if any two numbers are same
    if a>b:
        print("The 1st number '", a, "' is greater")
    else:
        print("The 2nd number '", b, "' and the 3rd number '", c, "' are equal and greater.")

else:
    print("All the numbers are equal")