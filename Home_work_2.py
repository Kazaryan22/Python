# задача 1

# a = [1 , 'July' , 4.56 , 23 , None]
# print (type (a))

# Задача 2
# a = input("List: ")
# new_list = a.split()
#
# for i in range(len(new_list) // 2):
#     k1 , k2 = 2 * i, 2 * i + 1
#     new_list[k1], new_list[k2] = new_list[k2], new_list[k1]
# print(new_list)

 #Задача 3
# month = input('enter number of month:  ')
#
# a, b, c, d = 'зима', "весна", "лето", "осень"
#
# m_dict = {'1': a, '2': a, '3': b, '4': b, '5': b, '6': c, '7': c, '8': c, '9':d, '10':d, '11': d, '12': a}
# print({m_dict[month]})
#
# month_list = [a, a, b, b, b, c, c, c, d, d, d, a]
# print(month_list[int(month) -1])

 #Задача 4
# input_string = input("Введите предложение из нескольких слова: ")
#
# words = input_string.split()
#
# for num, word in enumerate(words):
#     print(f'#{num} - {word[:10]}')

 #Задача 5
# my_list = [8, 8, 7, 7, 6, 5, 4, 3]
# raiting = int(input("Enter raiting number: "))
# a = False
#
# for  index, elem in enumerate(my_list):
#     if elem > raiting:
#         my_list.insert(index, raiting)
#         a = True
#         break
# if not a:
#     my_list.append(raiting)
# print(my_list)

 #Задача 6
#  items = [
#     (1, {'Наименование': "Телевизор", "Цена": "50000", "Количество": "2", "единицы": "штуки"}),
#     (2, {'Наименование': "Ноутбук", "Цена": "50000", "Количество": "2", "единицы": "штуки"}),
#     (3, {'Наименование': "Смартфон", "Цена": "10000", "Количество": "4", "единицы": "штуки"})
# ]
#  list_a = []
#  for numbers, prod_dict in items:
#      for key, value in prod_dict.items():
#          if not list_a.get(key)
#              list_a(key) = [value]
#      else:
#          list_a(key).append(value)
#
#     print(list_a)

