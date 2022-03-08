import json


def write_order_to_json(item: str, quantity: str, price: str, buyer: str, date: str) -> None:
    """
    Writing function arguments to json file (in dictionary format)
    :param item: good
    :param quantity: quantity
    :param price: price
    :param buyer: buyer
    :param date: date in string format
    :return None: result - writing to a json file
    """

    with open('orders_1.json', 'r', encoding='utf-8') as f_out:
        data = json.load(f_out)

    with open('orders_1.json', 'w', encoding='utf-8') as f_in:
        orders_list = data['orders']
        order_info = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': date
        }
        orders_list.append(order_info)
        json.dump(data, f_in, indent=4)


# # initialisation (чтобы при отладке не удалять данные)
# with open('orders_1.json', 'w', encoding='utf-8') as f_in:
#     json.dump({'orders': []}, f_in, indent=4)

# Вот здесь важный момент. С латиницей все хорошо. Но стоит указать строку с кириллицей
# и в json-файле получим
# "item": "\u043f\u0440\u0438\u043d\u0442\u0435\u0440",
write_order_to_json('printer', '10', '6700', 'Иванов I.I.', '24.09.2017')
write_order_to_json('scaner', '20', '10000', 'Petrov P.P.', '11.01.2018')
write_order_to_json('computer', '5', '40000', 'Sidorov S.S.', '2.05.2019')
