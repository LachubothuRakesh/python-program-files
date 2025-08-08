str="welcome" #basic's of string
print(str[0])
print(str[0:3])
print(str[-2])

str="welcometojava" #methods (capitalize,title,isalpha)
print(str.capitalize())
print(str.title())
print(str.isalpha())

str="welcome" #index
print(str.index("m"))

str="welcome" #rindex
print(str.rindex("e"))

str="welcome" #find
print(str.find("e"))

str="welcome" #rfind
print(str.rfind("e"))

str="welcometopython" #count
print(str.count("p"))

str="welcometopython" #starts with
print(str.startswith("w"))

str="welcometopython" #ends with
print(str.endswith("n"))

str="welcometopython" #replace
print(str.replace("welcometopython","welcometojava"))

str="  welcometopython    " #strip
print(str.strip())

str="  welcometopython    " #leftstrip
print(str.lstrip())

str="  welcometopython    " #rightstrip
print(str.rstrip())

str="welcometopython" #join
print("/".join(str))

li="welcome,to,python" #split
print(li.split(","))

str="welcometopython"
print(str.isdigit())
print(str.islower())
print(str.isalpha())
print(str.isalnum())
print(str.isspace())

str="123welcometopython"
print(str.isalnum())