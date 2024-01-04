num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
choice=int(input("enter your choice:\n 1.subtraction\n 2.addition\n 3.multiplication\n 4.division\n"))
if choice==1:
    result=num1-num2
    print("result",result)
elif choice==2:
    result=num1+num2
    print("result",result)
elif choice==3:
    result=num1*num2
    print("result",result)
elif choice==4:
    result=num1/num2
    print("result",result)
else:
    print("invalid syntax")
