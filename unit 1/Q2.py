A={1,2,3,4,5}
B={5,6,7,8,9}

# using loop
for i in A:
 print(i)

# to check if the element exist in set 
print("2" in A)

# union
C=A.union(B)
print (C)

#intersection
D=A.intersection(B)
print (D)


#differance
E=A.difference(B)
print (E)
