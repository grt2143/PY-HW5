#3-Создайте два списка — один с названиями языков программирования, другой — с числами
#  от 1 до длины первого.['python', 'c#'] [1,2]
#Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из
#  номера и языка, написанного большими буквами. [(1,'PYTHON'), (2,'C#')]
#Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет 
# в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется
#  на сумму очков. [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
#[(1,'PYTHON'), (102,'C#')] Если нет — удаляется. Суммой очков называется сложение порядковых номеров 
# букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
#Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
#Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком

from functools import reduce

with open('file.txt', encoding='utf-8') as file:
    languages = file.read().split('\n')

numbers = list(range(1, len(languages)+1))

new_list =list(zip(numbers, [word.upper() for word in languages]))
print(new_list)

def filter_list(new_list):
    result_list = []
    result = 0
    for number, language in new_list:
        sum_of_points = reduce(lambda a,b: a+b, [ord(char) for char in language])
        if sum_of_points % number == 0:
            result += sum_of_points
            result_list.append((sum_of_points, language))
    del new_list
    return result_list
print(filter_list(new_list))