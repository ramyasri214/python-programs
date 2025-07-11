# 1)Print all numbers from 1 to N using a loop.
# a=int(input("enter a value:"))
# sum=0
# for i in range(1,a+1):
#     sum=sum+i
# print(sum)

# 2)Print all even numbers from 1 to N.
# a=int(input("enter a value:"))
# for i in range(1,a+1):
#     if i%2==0:
#        print(i)

# 3)Print all odd numbers from 1 to N.

# a=int(input("enter a value:"))
# for i in range(1,a+1):
#     if i%2 !=0 :
#         print(i)

# 4)Calculate the sum of the first N natural numbers.
# n=int(input("enter a value:"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)


# another logic:
# n=int(input("enter a value:"))
# sum=n*(n+1)//2
# print(sum)

# 5)Print the multiplication table of a given number up to 10.


# for i in range(1,11):
#     print("5 * ",i,"=",5*i)

# 6)Count the number of digits in a given number.
# a=input("enter a value:")
# count=0
# for i in a:
#     count=count+1
# print(count)

# 7)Reverse a given integer number.
# num = int(input("Enter a number: "))
# reverse = 0
# while num != 0:
#     digit = num % 10            
#     reverse = reverse * 10 + digit  
#     num = num // 10            

# print("Reversed number is:", reverse)


# 8)Check whether a number is a palindrome or not.

# num=int(input("enter a value:"))
# original=num
# reverse=0
# while num >0:
#     digit=num %10
#     reverse=reverse*10+digit
#     num=num//10
# if original==reverse:
#     print("it is palindrome")
# else:
#     print("it is not a palindrome")

# 9)Check whether a number is a prime number.

# n = int(input("Enter a number: "))
# if n > 1:
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")
# else:
#     print("Not Prime")
# 10)Print all prime numbers between 1 and N.
# N = int(input("Enter a number: "))
# for num in range(2, N + 1):
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             break
#     else:
#         print(num, end=' ')
# 11)Find the factorial of a number using a loop.
# n=int(input("enter a value:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

# 12)Calculate a raised to the power b using a loop (without using **).
# a=int(input("enter a number:"))
# b=int(input("enter exponential number:"))
# result=1
# for i in range(b):
#     result *=a
# print(result)

# 13)Calculate the sum of digits of a given number.
# sum=0
# for i in range(1,6):
#     sum +=i
# print(sum)

# 14)Check whether a number is an Armstrong number or not (3-digit).
# num = int(input("Enter a 3-digit number: "))
# sum = 0
# temp = num

# while temp > 0:
#     digit = temp % 10
#     sum += digit ** 3
#     temp //= 10

# if sum == num:
#     print("amstrong number")
# else:
#     print(" not an Armstrong number")

# 15)Find the largest digit in a given number.

# num = int(input("Enter a number: "))
# max_digit = 0

# while num > 0:
#     digit = num % 10
#     if digit > max_digit:
#         max_digit = digit
#     num = num // 10

# print("Largest digit is:", max_digit)

# 16)Find the smallest digit in a given number.
# num = int(input("Enter a number: "))
# min_digit = 9  # Maximum possible digit

# while num > 0:
#     digit = num % 10
#     if digit < min_digit:
#         min_digit = digit
#     num = num // 10

# print("Smallest digit is:", min_digit)
