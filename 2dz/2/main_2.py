import json


def write_order_to_json(item, quantity, price, buyer, date):
    """Запись в json"""

    with open('orders_2.json', 'r', encoding='utf-8') as f_out:
        data = json.load(f_out)

    with open('orders_2.json', 'w', encoding='utf-8', ) as f_in:
        orders_list = data['orders']
        order_info = {'item': item, 'quantity': quantity,
                      'price': price, 'buyer': buyer, 'date': date}
        orders_list.append(order_info)
        # используем параметр ensure_ascii=False
        # Если ensure_ascii = True, все не-ASCII символы в выводе будут экранированы
        # последовательностями \uXXXX, и результатом будет строка, содержащая только ASCII символы.
        # Если ensure_ascii = False, строки запишутся как есть.
        json.dump(data, f_in, indent=4, ensure_ascii=False)


# initialisation (чтобы не удалять данные при каждой новой проверке скрипта)
# with open('orders_2.json', 'w', encoding='utf-8') as f_in:
#     json.dump({'orders': []}, f_in, indent=4)


write_order_to_json('принтер', '10', '6700', 'Ivanov I.I.', '24.09.2017')
write_order_to_json('сканер', '20', '10000', 'Petrov P.P.', '11.01.2018')
write_order_to_json('компьютер', '5', '40000', 'Сидоров С.С.', '2.05.2019')
