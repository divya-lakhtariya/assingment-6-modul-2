s= input("Enter a string: ")

if len(s) % 4 == 0:
    reverse=s[::-1]
    print("Reversed string:", reverse)
else:
    print("String length is not a multiple of 4.")
