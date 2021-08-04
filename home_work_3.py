
# 1
# def func_1 (a, b):
#     if a == 0 or b == 0:
#         print('Деление на ноль!')
#     else:
#         return a / b
#
# print(func_1(45, 0))

# 2
# def user_func (FIO, year, city, mobile, email):
#     print (f'{FIO} {year} {city} {mobile} {email}')
#
# n = input("Enter you name and surname: ")
# y = input("Enter your year of the birth: ")
# c = input("Enter your city: ")
# m = input("Enter your mobile phone: ")
# e = input("Enter your email: ")
#
# user_func(n=FIO, y=year, c=city, m=mobile, e=email)
# print(user_func())

#3
# def my_func(a, b, c):
#     sum_nums = a + b + c
#     return sum_nums - min(a, b, c)
#
# a = int(input('Input a: '))
# b = int(input('Input b: '))
# c = int(input('Input c: '))
#
# x = my_func(a, b, c)
#
# print(x)

#4
#
# def my_func(x, y):
#     degree = x ** abs(y)
#     return degree
# x =int(input('Enter any number:  '))
# y= int(input('Enter any negative number: '))
# a = my_func(x, y)
# print(a)

#5
# def sum_nums (nums_str, stopp):
#     num_list = nums_str.split(' ')
#     sum_list = 0
#     for i in num_list:
#         if i == stopp:4
#             break
#             print("EXIT!")
#         sum_list += int(i)
#
#     return sum_list
#
# stopp = "*"
# finish = False
# s= 0
# while not finish:
#     nums_list = input("Enter numbers sepparated by a space or * to exit: ")
#     s += sum_nums(nums_str, stopp)
#     finish = stopp in nums_str
#     print(f"Summ is {s}")

#6
# def int_func(text):
#     word = text[0].upper() + text[1: ].lower()
#     return  word
#
# print(int_func('world'))
#
# string = input('Enter words sepparated by a space: ')
# for word in string.split(" "):
#     print(f'{int_func(word)} ', end= " ")
