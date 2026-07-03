str1 = "rahulshettyacademy.com"
str = "mgsystech.com"
str2 = "mgsys"
str3 = " Good "

print(str[1])        # print any char
print(str[0:5])      # substring from main string
print(str1+str)      # concatenation
print(str2 in str)   # substring check

var = str.split(".") # split the string from where we want
print(var)
print(var[0])

print(str3.strip())  # Remove the blank spaces/white spaces from string.
str3.lstrip()
print(str3.lstrip()) # Remove only left spaces/white spaces from string
str3.rstrip()
print(str3.rstrip()) # # Remove only right spaces/white spaces from string
