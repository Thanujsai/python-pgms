a=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
area=a*b
peri=2*(a+b)
if(area>peri):
    print("Area")
    print(area)
elif(area<peri):
    print("Peri")
    print(peri)
else:
    print("Eq")
    print(peri)