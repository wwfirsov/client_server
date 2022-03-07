VAR_1 = 'attribute'
VAR_2 = 'класс'
VAR_3 = 'функция'
VAR_4 = 'type'

WORDS = [VAR_1, VAR_2, VAR_3, VAR_4]

# Вариант 1
for word in WORDS:
    try:
        bytes(word, 'ascii')
    except UnicodeEncodeError:
        print(f'Слово "{word}" невозможно записать в виде байтовой строки')

# Вариант 2
for word in WORDS:
    try:
        word.encode('ascii')
    except UnicodeEncodeError:
        print(f'Слово "{word}" невозможно записать в виде байтовой строки')

# Вариант 3
for word in WORDS:
    try:
        expr_obj = f"b'{word}'"
        eval(expr_obj)
    except SyntaxError:
        print(f'Слово "{word}" невозможно записать в виде байтовой строки')