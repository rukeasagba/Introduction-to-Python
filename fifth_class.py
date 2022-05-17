# h=1
# while h<=10:
#     h+=1
#     print(h)


# h = 1
# while h<=10:
#     print(h)
#     h+=1

# import random
# print("Guess the computer's choice to win the prize.")
# a = [1,2,3,4,5,6,7]

# random.shuffle(a)
# trial = 3
# score = 0

# while trial > 0:
#     print("\nSelect a number from", a)
#     com_choice = random.choice(a)
#     user = int(input("Your choice\n:>"))
#     if user == com_choice:
#         print("You win")
#         score+=2
#         trial+=1
#         print(f"You have won an extra trial")
#         print(f"{trial} trial(s) left")
    
#     else:
#         if user > com_choice:
#             print("Too high")
#         else:
#             print("Too low")
#         trial-=1
#         print(f"{trial} trial(s) left")

# print(f"\nYou scored {score} points")
# print("Game over ):")


# Rock paper scissors game
# import random

# options = ["r", "p", "s"]
# trial = 3
# score = 0

# while trial >0:
#     print("""\nSelect R for rock, P for paper and S for scissors.""")
#     com_choice = random.choice(options)
#     player_choice = input(">").lower()
#     if player_choice in options :
#         if player_choice == options[0] and com_choice==options[2]:
#             print("You win")
#             print("Computer chose", com_choice)
#             trial+=1
#             score+=2
#         elif player_choice == options[2] and com_choice == options[1]:
#             print("You win")
#             print("Computer chose", com_choice)
#             trial+=1
#             score+=2
#         elif player_choice == options[1] and com_choice == options[0]:
#             print("You win")
#             print("Computer chose", com_choice)
#             trial+=1
#             score+=2
        
#         elif player_choice == com_choice:
#             print("It's a tie")
#         else:
#             print("You lose")
#             print("Computer chose", com_choice.title())
#             trial-=1
#     else:
#         print("Invalid input")
#         trial-=1


#     print(f"{trial} trials left")

# print("Game over")
# print("You scored", score)

# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]
# b[3] = 82
# print(b)

# a = [1,2,3,4,5,6,7,]
# print(a[2:5])

# for element in a:
#     print(element)

# a = [x**2 for x in range(10)]
# print(a)

#standard deviation 
# m = 0.728
# P = [1,2,4,7,8,9,10]
# c = [(x-m)**2 for x in P]
# print(sum(c))

# a = [x if x%2 == 0 else 0 for x in range(10)]
# print(a)



# n = int(input("Enter any number \n:>"))
# def prime_num(n):
#     if n > 1:
#    # check for factors
#        for i in range(2, n):
#            if (n % i) == 0:
#             return False
#        else:
#            return True

# prime_num = [n for n in range(98,176) if prime_num(n)]
# print(prime_num)

#Assignment 3
#Question 1

def Average(data): 
    avg = sum(data) / len(data) 
    return avg
  
data = [28,42,67,89,100] 
average = Average(data) 
  
print("The mean is", average)
    

#Question 2

def get_median(data):
    # sort the list
    data_sorted = data.sort()
    # find the median
    if len(data) % 2 != 0:
        # total number of values are odd
        # subtract 1 since indexing starts at 0
        m = int((len(data)+1)/2 - 1)
        return data[m]
    else:
        m1 = int(len(data)/2 - 1)
        m2 = int(len(data)/2)
        return (data[m1]+data[m2])/2
# create a list
data = [28,42,67,89,100] 
# get the median
print("The median is", get_median(data))

#Question 3

def variance(data):
# Number of observations
    n = len(data)
# Mean of the data
    mean = sum(data) / n
# Square deviations
    deviations = [(x - mean) ** 2 for x in data]
# Variance
    variance = sum(deviations) / n
    return variance

data = [28,42,67,89,100] 
print("The variance is", variance(data))


#Question 4

def stdev(data):
    var = variance(data)
    std_dev = (var)**0.5
    return std_dev

data = [28,42,67,89,100] 
print("The standard deviation is", stdev(data))


#Question 5

def skew(data):
    skew_data = 3*(Average(data) - get_median(data))/stdev(data)
    return skew_data

data = [28,42,67,89,100] 
print("The skew is", skew(data))

