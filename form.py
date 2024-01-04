name=input("enter your name:")
id=(input("enter your id:"))
m1=int(input("enter your mark 1:"))
m2=int(input("enter your mark 2:"))
m3=int(input("enter your mark 3:"))
total=m1+m2+m3
avg=total/3


print("***student details***")
print("name:",name,"\nid:",id,"\nmark1",m1,"\nmark2:",m2,"\nmark3:",m3,"\ntotal:",total,"average\n:",avg)



if avg>=90:
    print("grade:a+")
elif avg>=80:
    print("grade:a")
elif avg>=70:
    print("grade:b+")
elif avg>=60:
    print("grade:b")
elif avg>=50:
    print("grade:c+")
elif avg>=40:
    print("grade:c")
     
else:
    print("fail")
