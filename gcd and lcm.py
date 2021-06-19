# cook your dish here
n=int(input("Enter the number of test cases:"))
for i in range(n):
    a,b=map(int,input("Enter the numbers:").split())
    if(a>b):
        num=a
        den=b
    else:
        num=b
        den=a
    rem=num%den
    while(rem!=0):
        num=den
        den=rem
        rem=num%den
    hcf=den
    lcm=(a*b)//hcf
    print(hcf,lcm)