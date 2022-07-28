#1- Напишите программу, удаляющую из текста все слова,
# содержащие ""абв"".'абвгдейка - это передача' 
# = >" - это передача"

text = 'абвгдейка - это передача'
print(text)

def delete_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

new_text = delete_words(text)
print (new_text)