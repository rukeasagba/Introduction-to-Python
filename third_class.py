#Assignment

#Question 1

# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# n3 = int(input("Enter third number: "))
# total = n1 + n2 + n3
# average = total/3
# print(int(average))

#Question 2
# sentence = input("Write a sentence: ")
# print(sentence.capitalize())

#Question 2 main answer
# user_sentence = (input("enter any choice of your sentence")).lower()
# user_sentence_split = user_sentence.split(" ", 1 )
# first_word = user_sentence_split[0].upper()
# new_user_sentence = first_word+" "+user_sentence_split[1]
# print(new_user_sentence)

# #Question 2 alternative answer
# print('Enter a sentence below')
# answer = input(':>').split()
# answer[0] = answer[0].upper()
# print(f'Solution:\n{" ".join(answer)}')

# #Question 3
# study = "I am learning python"
# print(study.replace("I", "you"))

#Alternative Question 3
# study_2 = "I am learning python"
# print(study_2.replace("I am", "You are"))

#Question 4
# question = "I hope you had fun today in class."
# print(question.count("a"))

# def test_function():
#     print(4*2+2)

# test_function()


# def fun2(n:int):
#     print(n**2)

# fun2(3)

# def fun2(n:int):
#     return(n**2)

# print(fun2(4))

#Return marks the end of  function
# def fun2(n:int):
#     print("I am running")
#     return n**2
#     print("I just ran")

# print(fun2(4))

#Global variable
# result = 4

# def fun2(n:int):
#     return result*n

# print(fun2(4))

#Global Keyword
# def fun2(n:int):
#     global result
#     result = n**2
#     return result

# print(fun2(4))
# print(result)


# def fun3(a,b,c):
#     print(a,b,c)

# # fun3(1,2,3)
# # fun3(b=1, c=3, a=2)
# fun3(1, b=3, c=2)

#Classwork
def mean(arr):
    mean_value = sum(arr)/len(arr)
    return round(mean_value, 2)


print("Calculate your mean")
print("Enter your mean values separated by comma")
vals = input(":>").split(',')
# print(vals)
mapped = list(map(int,vals)) #convert map to list because map alone has no length function
# print(list(mapped))  #to show what was mapped you need to convert to a list
print(mean(mapped))


# print(mean([2,34,54,2,1,4]))



