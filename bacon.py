#Small refresher about local variables 
# def spam():
#     eggs = "SPAMSPAM"
#     bacon()
#     print(eggs)

# def bacon():
#     ham = "hamham"
#     eggs= "BACONBACON"
#     print(ham, eggs)
# spam()

# pass

#Small refresher about Global variables

# def spam():
#     print(eggs)  # Prints 'GLOBALGLOBAL'
# eggs = 'GLOBALGLOBAL'
# spam()
# print(eggs)

# def spam():
#     eggs = "spam local"
#     print(eggs)

# def bacon():
#     eggs = "bacon local"
#     print(eggs) #bacon local
#     spam()
#     print(eggs) # bacon local

# eggs = 'global'
# bacon()
# print(eggs)

# def spam():
#     global eggs
#     eggs = "spam"

# eggs = 'global'
# spam()
# print(eggs)

# def spam():
#     global eggs
#     eggs = "global eggs variable"

# def bacon():
#     eggs = "local eggs variable"

# def ham():
#     eggs = "local eggs variable"
#     print(eggs)

# eggs = 'global'

# spam()
# print(eggs)

# def spam(divide_by):
#     try:
#         return 42 / divide_by
#     except ZeroDivisionError:
#         print("Error invalid argument")
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

# def spam(divide_by):
#     return 42 / divide_by
# try:
#     print(spam(2))
#     print(spam(12))
#     print(spam(0))
#     print(spam(1))
# except ZeroDivisionError:
#     print

def spam(divide_by):
    return 42 / divide_by

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')