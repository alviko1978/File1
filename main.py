# Читаем файл и создаем словарь со списком блюд и перечнем продуктов
with open("recept.txt", "rt", encoding="utf-8") as file:
    menu = {}
    for line in file:
        menu_name = line.strip()
        number_ingr = int(file.readline())
        ingredient = []
        for _ in range(number_ingr):
            rec = file.readline().strip().split(' | ')
            name, number, unit = rec
            ingredient.append({"name": name, "number": number, "unit": unit})
        file.readline()
        name = menu_name
        menu[name] = ingredient
print(menu)
# Формируем на экране меню для заказа блюд
print("Наше меню сегодня:")
punkt_menu = 1
for key, values in menu.items():
    print(f'{punkt_menu}. "{key}"')
    punkt_menu+=1
# Формируем список блюд для заказа(для удобства работы с программой список из порядковых значений меню)
zakaz = []
print("Введите названия блюд для заказа, если все выбрали, нажмите 0: ")
number_zakaz = int(input())
while number_zakaz !=0 and number_zakaz <= len(menu):
    zakaz.append(number_zakaz)
    number_zakaz = int(input("Следующее блюдо: "))
print("Заказ принят")
# Сортируем и откидываем лишние номера блюд при повторном вводе
zakaz = list(set(zakaz))
# Формируем список из названия блюд по их цифровым номерам
list_key = list(menu.keys())
list_zakaz = []
for i in zakaz:
    list_zakaz.append(list_key[i-1])
# Вводим количество персон
number_pers = int(input("Введите количество персон: "))

# #Функция формирования словаря со списком продуктов и их количества для покупки из расчета количества персон


def shop_list(dishes, person_count):
    grocery_dict = {}  # Создаем пустой словарь для хранения списка покупок
    for _dish in dishes:
        for ingredient in menu[_dish]:
            ingredient_list = dict([(ingredient['name'], {'number': int(ingredient['number']) * person_count,'unit': ingredient['unit']})])
            if grocery_dict.get(ingredient['name']) == 'None':
                _merger = (int(grocery_dict[ingredient['name']]['number']) +
                           int(ingredient_list[ingredient['name']]['number']))
                grocery_dict[ingredient['name']]['number'] = _merger
            else:
                grocery_dict.update(ingredient_list)
    return grocery_dict


print(shop_list(list_zakaz, number_pers))