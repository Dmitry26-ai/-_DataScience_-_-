import math
#                                     Задача 1:
#Написать функцию на языке Python, аргументом которой является 
#целочисленный массив (список, элементами которого является тип данных int).
#Функция должна обработать целочисленный массив и вернуть только уникальные
#значения (без дубликатов)  для данного массива c сортировкой по возрастанию.

def function_1(a):
    b = set(a)
    print(list(b))

#function_1([1, 1, 2, 4, 3, 6, 7, 3, 2, 1, 8, 9, 3])

#                                     Задача 2:
# Напишите функцию, которая принимает на вход два вектора (2 списка) и рассчитывает
# косинусное расстояние полученных векторов и выводит результат вычисления в консоль. 
# Реализуйте проверку для валидности расчета косинусного расстояния между 2-мя векторами, 
# в случае если проверка не прошла, вывести в консоль причину почему рассчитать расстояние 
# между 2-мя векторами невозможно.

def function_2(a, b):

    for i in (a + b):
        if type(i) != int:
            print("Вектор содержит не числовые значения")
            return False
        
    if len(a) != len(b):
        print("Размерности векторов не совпадают")
        return False
    
    if (a[0] and a[1] and a[2]) == 0 or (b[0] and b[1] and b[2]) == 0:
        print("Один из векторов является нулевым вектором")
        return False
    
    axb = a[0] * b[0] + a[1] * b[1] + a[2] * b[2] 
    la = math.sqrt(a[0]**2 + a[1]**2 + a[2]**2)
    lb = math.sqrt(b[0]**2 + b[1]**2 + b[2]**2)
    print(axb/(la*lb))

#function_2([1,-1], [2,-2,2])
#function_2([-1,1,-1], [2,"-2",2])
#function_2([0,0,0], [2,-2,2])
#function_2([-1,1,-1], [2,-2,2])

#                                       Задача 3:
# Реализуйте функцию принимающую 2 аргумента - 2-е даты. Результатом вычисления функции 
# должна быть разница между 2-й датой и 1-й датов в днях. В случае если разница принимает 
# негативное значение вывести в консоль абсолютное значение разницы в днях. 
# Используем стандартный модуль Python для работы с датами datetime (без внешних библиотек).

from datetime import date

def main(date1, date2):

    delta = str(date2 - date1)
    answer = delta[:-13]
    print(f'Разница между {date2} и {date1}: {abs(int(answer))} дней.')

#main(date(2020, 10, 2), date(2020, 10, 30))

#                                       Задача 4:
# Реализуйте двусвязный список используя синтаксис языка Python. Вам необходимо создать класс (либо несколько классов), 
#который (которые) будет (будут) представлять структуру данных - связный список.
# Связный список — это набор элементов данных, называемых узлами. В односвязном списке каждый узел содержит значение 
#и ссылку на следующий узел. В двусвязном списке каждый узел также содержит ссылку на предыдущий узел.
# Реализуйте узел для хранения значения и указателей на следующий и предыдущий узлы. 
# Затем реализуйте список, который содержит ссылки на первый и последний узел и предлагает интерфейс, подобный массиву,
#для добавления и удаления элементов, какие методы должны быть реализованы:
#           push() - записывает значение в конец списка
#           pop() - удаляет значение с конца списка
#           shift() - удаляет значение в начале списка
#           unshift() - записывает значение в начало списка

class DoublyLinkedListNode:
    def __init__(self, value, previous, next):
        self.value = value
        self.previous = previous
        self.next = next   

class DoublyLinkedList:
    head = None
    tail = None
    def __repr__(self):
        return f"DoublyLinkedList: {self.to_list()}"
    
    def to_list(self):
            result = []
            current = self.head
            while current:
                result.append(current.value)
                current = current.next
            return result
    
    # Добавление элемента в конец списка
    def push(self, value):
        new_node = DoublyLinkedListNode(value, None, None)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # Удаление последнего элемента и его возвращение
    def pop(self):
        if not self.tail:
            return None
        value = self.tail.value
        self.tail = self.tail.previous
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return value

    # Удаление первого элемента и его возвращение
    def shift(self):
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.previous = None
        else:
            self.tail = None
        return value

    # Добавление элемента в начало списка
    def unshift(self, value):
        new_node = DoublyLinkedListNode(value, None, None)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

# list = DoublyLinkedList()

# list.push(1)
# list.push(2)
# list.push(3)

# print(list.pop())  # 3
# print(list.shift())  # 1
# list.unshift(4)
# print(list)
            
#                                         Задача 5:
# Существует массив поисковых запросов, например:
# search_queries = [“watch new movies”, “coffee near me”, “how to find the determinant”, 
#“python”, “data science jobs in UK”, “courses for data science”, “taxi”, “google”, “yandex”,
#“bing”,”foreign exchange rates USD/BYN”, “Netflix movies watch online free”,  “Statistics courses online from top universities”]
# Необходимо реализовать функцию, которая принимает на вход данные массива поисковых запросов и возвращает распределение поисковых
#запросов по количеству слов в каждом из запросов в процентах. 
    # Результат должен выглядеть следующим образом:
    # 1 слово : 10%
    # 2 слова:  40%
    # 4 слова:  45%
    # 5 слов:    5%

def calculate_query_distribution(search_queries):
    word_count_distribution = {}
    total_queries = len(search_queries)

    for query in search_queries:
        word_count = len(query.split())
        if word_count in word_count_distribution:
            word_count_distribution[word_count] += 1
        else:
            word_count_distribution[word_count] = 1

    distribution_in_percent = {word_count: round((count / total_queries) * 100, 2) for word_count, count in word_count_distribution.items()}
    distribution_in_percent = sorted(distribution_in_percent.items())
    
    for i in range(len(distribution_in_percent)):
        if (distribution_in_percent[i])[0] == 1:
            print(f'{(distribution_in_percent[i])[0]} слово: {(distribution_in_percent[i])[1]} %')
            i += 1
        elif (distribution_in_percent[i])[0] in (2, 3, 4):
            print(f'{(distribution_in_percent[i])[0]} слова: {(distribution_in_percent[i])[1]} %')
            i += 1
        elif (distribution_in_percent[i])[0] in (5, 6, 7):
            print(f'{(distribution_in_percent[i])[0]} слов: {(distribution_in_percent[i])[1]} %')
            i += 1
        else:
            print('Очень много слов...')

search_queries = ['watch new movies', 'coffee near me', 'how to find the determinant', 
    'python', 'data science jobs in UK', 'courses for data science', 'taxi', 'google', 'yandex',
    'bing', 'foreign exchange rates USD/BYN', 'Netflix movies watch online free',  'Statistics courses online from top universities']

#calculate_query_distribution(search_queries)
