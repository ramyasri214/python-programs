1) Reverse a String Without Using [::-1]:
Reverse a string using a loop or recursion.
a="ramyasri"
sub=" "
for char in a:
    sub=char+sub;
print(sub)

2)Count Frequency of an Element in a List:
Input a list and an element; count how many times the element appears
r=[1,2,3,2,3,2,3,3,2,2,3]
value=2
count=0
for i in r:
    if i ==value:
        count=count+1
print(count)

3)Print First N Prime Numbers:
Take N as input and print the first N prime numbers
n = int(input("Enter how many prime numbers to print: "))
count = 0
num = 2
while count < n:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
        count += 1
    num += 1
print(num)

4)Remove Duplicates from a List:
Given a list, return a new list without duplicates (maintain order)

lst = [1, 2, 2, 3, 1, 4, 5, 3]
a= []

for i in lst:
    if i not in a:
        a.append(i)

print("List without duplicates:", a)

5)
FizzBuzz:
For numbers from 1 to N, print:

“Fizz” if divisible by 3

“Buzz” if divisible by 5

“FizzBuzz” if divisible by both

Else print the number itself

N=int(input("enter a value:"))
for i in range(1,N+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

    

