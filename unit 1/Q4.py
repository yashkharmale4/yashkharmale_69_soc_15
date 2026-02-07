A= {"name": "Yash","roll_no": 69,"course": "Python"}
print(A["name"])

 #updating
A.update({"class":"soc15"})
print(A)

A["course"]= "java"
print(A)

#add
A["dob"]="442007"
print(A)

#removing
del A["name"]
print(A)

#mearge\
B={"name":"adi","roll":"2","couse":"python"}
C=A|B
print(C)