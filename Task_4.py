#. 4-Реализовать RLE алгоритм. реализовать модуль сжатия и 
# восстановления данных.
# a) входные и выходные данные хранятся в отдельных текстовых файлах


with open('file1.txt', 'r', encoding='utf-8') as file:
    data = file.readline()
    print(data)

def encode_data(data):
    encoding = ""  
    i = 0
    while i < len(data):          # подсчитываем количество вхождений символа
        count = 1
        while i + 1 < len(data) and data[i] == data[i + 1]:
            count = count + 1
            i = i + 1          # добавляет к результату текущий символ и его количество
        encoding += str(count) + data[i]
        i = i + 1
    return encoding
print(encode_data(data))


with open('file2.txt', 'r', encoding='utf-8') as file:
    data = file.readline()
    print(data)

def decode_data(data):
    decoding = ""             
    count = ""
    for char in data:
        if char.isdigit():
            count += char
        else:
            decoding += char * int(count)
            count = " "
    return decoding
print(decode_data(data))