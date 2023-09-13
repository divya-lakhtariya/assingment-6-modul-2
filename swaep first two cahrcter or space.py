s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
if len(s1)==0 or len(s2)==0:
    print("enter strings.")
else:

    swappes1 = s2[:2] + s1[2:]
    swappes2 = s1[:2] + s2[2:]

    ans= swappes1 + " " + swappes2
    print("Result:",ans)
