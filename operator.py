
num=int(input("enter a number"))
   if(num%2)==0:
    
    print(num,"is even")
else:
    print(num,"is odd")


#h c f two number.using loop
x=18
y=12
if x>y:
    smaller=y
else:
        smaller=x
for i in range(1,smaller+1):
        if((x%i==0)and(y%i==0)):
            hcf=i
print(hcf)
