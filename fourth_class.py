# def factorial(n):
#     if n==1:
#         return 1
#     if n==0:
#         return 1
#     recurse = n * factorial(n-1)
#     print(recurse)
#     return recurse


# factorial(5)


# print('x')
# if 4 > 5:
#     print(7)
# print(4)



# print('boy')
# if 4 > 5:
#     print(7)
# else:
#     print(8)
# print(4)

# score = int(input("Enter your exam score:\n:>"))
# print(type(score))


# if score <= 100:
#     if score >= 90:
#         print('A')
#     elif score >= 80:
#         print('B')
#     elif score >= 70:
#         print('C')
#     elif score >= 60:
#         print('D')
#     elif score >= 50:
#         print('E')
#     elif score >= 40:
#         print('F')
#     else:
#         print('Comrade go learn work!')
# else:
#     print('Even me no do reach that one!')

# my_str = "this is a lovely string"
# a = list(map(lambda f:f.upper(), my_str))
# print("".join(a))

# help("keywords")


# import random
# print("Guess the computer's choice to win the prize.")
# a = [1, 2, 3, 4, 5, 6, 7]
# print("Select a number from", a)
# # random.shuffle(a)
# # print(a)
# # b = random.sample(a, 3)
# random.shuffle(a)
# com_choice = random.choice(a)
# user = int(input("Your choice\n:>"))
# if user == com_choice:
#     print("You win")
# else:
#     if user > com_choice:
#         print("Too high")
#     else:
#         print("Too low")
#     print("You lose")

#Classwork
#Build rock paper scissors game
#Rock wins scissors, scissors wins paper, paper wins rock
#You are playing against computer
#If they choose the same things, print it's a tie

# import random
# print("You are playing against the computer to win a prize")
# a = ["rock", "paper", "scissors"]
# print("Select an option from", a)
# random.shuffle(a)
# com_choice = random.choice(a)
# user = input("Your choice\n:>")
# if user == "rock" and com_choice == "scissors":
#     print("You win")
# elif user == "scissors" and com_choice == "paper":
#     print("You win")
# elif user == "paper" and com_choice == "rock":
#     print("You win")
# elif user == com_choice:
#     print(" It is a tie")
# else:
#     print("You lose")


#Classwork Correction
# import random

# options = ["r", "p", "s"]
# print("""Select R for rock, P for paper and S for scissors.""" )
# com_choice = random.choice(options)
# player_choice = input(">").lower()
# if player_choice in options:
#     if player_choice == options[0] and com_choice ==options[2]:
#         print("You win")
#         print("Computer chose", com_choice)
#     elif player_choice == options[2] and com_choice == options[1]:
#         print("You win")
#         print("Computer chose", com_choice)
#     elif player_choice == options[1] and com_choice == options[0]:
#         print("You win")
#         print("Computer chose", com_choice)
#     elif player_choice == com_choice:
#         print("It's a tie")
#     else:
#         print("You lose")
#         print("Computer chose", com_choice.title())
# else:
#     print("Invalid point")

#For loop
# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# for i in range(10):
#     if i == 5:
#         continue
#     print(i)


#Classwork2
# for i in range(90, 120):
#     if i % 2 == 0:
#         continue
#     print(i)


# for i in (1,2,3,4,15,22,21,33,50,55,72,66,95):
#     if i % 5 == 0 or i % 3 == 0:
#         print(i)

#Classwork correction to include count
# a = 0
# for i in range (90, 120):
#     if i%2 == 1:
#         a+=1
#         print(i)
# print(" ")
# print(a)
# print(" ")

# b = [1,2,3,4,15,22,21,33,50,55,72,66,95]
# c = 0
# for i in b:
#     if i%3==0 or i%5==0:
#         print(i)
#         c+=1
# print(" ")
# print(c)

#Assignment
n = int(input("Enter any number \n:>"))
if n > 1:
   # check for factors
   for i in range(2, n):
       if (n % i) == 0:
           print("False")
           break
   else:
       print("True")
       
#If the input number is equal to 1, then it is not prime
else:
   print("False, it is not a prime number.")
    


