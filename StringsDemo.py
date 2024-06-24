str = "Anurodh.Ramesh.More"
str1 = 450
str2 = "Anurodh"

print(str[0:7])

##print(str+str1)  -- normal concatenation
print("{} {}".format(str,str1))  # concatenation of int and str


print(str.__contains__(str2))   #method 1
print(str2 in str)  #method2  substing check

print(str.split("."))
print(str.split(".")[0])

str3 = " House "
print(str3.lstrip())
print(str3.strip())
print(str3.rstrip())

