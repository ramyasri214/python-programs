1) sum of odd numbers, from 1 to 10?
sum=0
for i in range(1,11):
    if i%2 !=0:
        sum=sum+i
print(sum)

2) Sum of even numbers from 1 to 10?
sum=0
for i in range(1,11):
    if i%2==0:
        sum=sum+i
print(sum)


3) sum of numbers from I to 10?

sum=0
for i in range(1,11):
    sum=sum+i
print(sum)

4) Find the Greatest of two numbers

a=int(input("enter a value:"))
b=int(input("enter a  value:"))
c=[a,b]
d=c[0]
for num in c:
    if num>d:
        d=num
print(d)

5) Find the Greatest of three numbers
a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
c=[a,b,c]
d=c[0]
for num in c:
    if num>d:
        d=num
print(d)


6) print 1 to 10 Prime numbers


for num in range(2, 11):
    is_prime = True
    for i in range(2, int(num** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")


7) Find the Leap Year

year=int(input("enter year"))
if(year %4==0 and year %100 !=0 or year %400==0 ):
    print("this is leapm year")
else:
    print("not a leap year")