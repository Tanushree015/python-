# loops

'''ticket = 16
if ticket >= 18:
    print("allowed")
else:
    print("denied")'''

'''amount = int(input("enter the amount: "))
if amount >= 1000:
    print("discount is applies")
else:
    print("no discount")'''


'''marks=int(input("enter the marks: "))
if marks>=90:
    print("grade A")
elif marks>=80 and marks<=90:
    print("grade B")
elif marks>=50 and marks<=80:
    print("grade C")
else:
    print("fail")'''


'''balance =int(input("enter the balance:"))
if balance >= 5000:
    print("withdrawal successfull")
elif balance >=1000 and balance <=4999:
    print("insufficient balance for large withdrawal")


elif balance >=1000:
    print("low balance")
else:
    print("no balance")'''


'''signal=input("enter the signal: ")

if signal== "red":
    print("stop")
elif signal== "yellow":
    print("ready")
elif signal== "green":
    print("go")
else:
    print("invalid signal")'''


'''username ="user"

if username=="admin":
    print("login successfull")
else:
    print("login failed")'''

'''number=int(input("enter the number: "))
if number%2==0:
    print("even number")

else:
    print("odd number")'''



'''ticket =int(input("enter the ticket: "))
if ticket <=5:
    print("ticket price is free")
elif ticket>=5 and ticket<=17:
    print("ticket price is 100")

elif ticket>=18:
    print("ticket price is 200")
else:
    print("invalid ticket")'''

'''password=input("enter the password: ")
if password=="python123":
    print("acess granted")
else:
    print("Acess denied")
'''

'''number=int(input("enter the number: "))
if number>0:
    print("positive")
elif number<0:
    print("negative")

else:
    print("zero")'''


'''num1=int(input("enter first number: "))
num2=int(input("enter second number:"))

if num1>num2:
    print("first number is greater")
elif num1<num2:
    print("second number is greater")
else:
    print("both numbers are equal")


# while loop

num=1

while num<=10:
    print(num)
    num=num+1




num = 10

while num>=1:
    print(num)
    num=num-1

num =0
while num <=10:
    
        print(num)
        num=num+2

num=5
while num<=30:
    print(num)
    num=num+5


num=1
while num<=10 :

    print(num)
    num=num+2



for i in range(3, 31, 3):
    print(i)

for i in range(1, 6):
    print(i * i)


marks=int(input("enter the attendence: "))
if marks>=75:
    print("allowed for the exam")
else:
    print("not allowed for the exam")



for i in range(1,11):
    print(i)


for students in range (1,6):
    print("student",students)



for orders in range(1,8):
    print("processing order",orders)

marks=[23,45,67,89,90,34,56,78,12,34]
for i in marks:
    if i>=50:
        print(i,"pass")
    else:
        print(i,"fail")
        


numbers = [12, 7, 8, 15, 20, 3, 10]
for num in numbers:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")

numbers = [12, 7, 8, 15, 20, 3, 10]
for num in numbers:
    if num % 2 == 0:
        print(num, "is even")
        
numbers = [12, 7, 8, 15, 20, 3, 10]

count = 0

for num in numbers:
    if num % 2 == 0:
        print(num, "is even")
        count = count + 1

print("Total even numbers:", count)


sum=0
for i in range(1,11):
    sum=sum+i
    print(sum)

numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
   total=total+num
   print(total)
   
    