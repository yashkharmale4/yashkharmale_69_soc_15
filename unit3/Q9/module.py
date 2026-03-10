import shapes

print("1-circle")
print("2-rectriangle")
print("3-triangle")

A=int(input("enter your choice "))

if A==1:
 r=float(input("enter the radius"))
 print(shapes.cr(r))
elif A==2:
 l=float(input("enter the lenth"))
 w=float(input("enter the width"))
 print("rectrangle",shapes.rec(l,w))
elif A==3:
 l=float(input("enter the lenth"))
 w=float(input("enter the width"))
 print("traiangle",shapes.tra(l,w))
else:
 print("invalid input")