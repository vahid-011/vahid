#simple calculator using elif ladder



num1=int(input("enter a number: " ))
num2=int(input("enter a  number: "))
choice=int(input("enter your choice:\n 1:Addition\n 2:Subtraction\n 3:Multiply\n 4:Division \n "))




if choice==1:
    sum=num1+num2
    print("sum=",sum)
elif choice==2:
    sub=num1-num2
    print("sub",sub)
elif choice==3:
    product=num1*num2
    print("product =",product)
elif choice==4:
    result=num1/num2
    print("Quatient = ",result)
    
else:
    print("invalid syntax")

