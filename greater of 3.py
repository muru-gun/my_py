a = float(input("Enter 1st number : "))
b = float(input("Enter 2nd number : "))
c = float(input("Enter 3rd number : "))

if a>b and a>c:
    print("The 1st number '", a, "' is greater")

elif b>a and b>c:
    print("The 2nd number '", b, "' is greater")

elif c>a and c>a:
    print("The 3rd number '", c, "' is greater")

elif a==b and a==c:
    print("All the numbers are equal")