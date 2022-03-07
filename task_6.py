from chardet import detect

LINES_LST = ['сетевое программирование', 'сокет', 'декоратор']
with open('test.txt', 'w') as file:
    for line in LINES_LST:
        file.write(f'{line}\n')
file.close()

# узнаем кодировку файла
with open('test.txt', 'rb') as file:
    CONTENT = file.read()
ENCODING = detect(CONTENT)['encoding']
print(ENCODING)

# открываем файл в правильной кодировке
with open('test.txt', 'r', encoding=ENCODING) as file:
    CONTENT = file.read()
print(CONTENT)