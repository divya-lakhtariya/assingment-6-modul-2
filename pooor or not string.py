s= input("Enter a string: ")

a= s.find('not')
b= s.find('poor')

if a!= -1 and b!= -1 and b>a:
    s =s[:a] + 'good' +s[b+4:]

print("Result:",s)
