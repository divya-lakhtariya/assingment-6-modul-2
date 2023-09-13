str1 = input("Enter main string: ") 
str2 = input("Enter the insert string: ")
a= int(input("Enter midel string: ")) 

str1 =str1[:a]+str2+str1[a:] 

print(str1) 
