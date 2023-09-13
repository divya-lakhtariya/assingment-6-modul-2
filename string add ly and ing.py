s= input("Enter a string: ")


if len(s)>= 3:
    
    if s[-3:] == 'ing':
        
         s1=s[:-3] + 'ly'

    else:
        
        s1 = s + 'ing'
else:
    s1 =s


print("Modified string:",s1)




