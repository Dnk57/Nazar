# TODO Напишите функцию для поиска индекса товара
def fruit_(fruit_list, product):
    for i in items_list:
        if product == i:
            return items_list.index(i)
        elif items_list.index(i) == len(items_list)-1 and product != i:
            return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = fruit_(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
