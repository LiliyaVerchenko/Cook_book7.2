from pprint import pprint

def create_dict_from_file(file):
    cook_dict = {}
    with open ('recipes.txt', encoding='utf-8') as f:
        for line in f:
            dish_name = line.lower().strip()
            counter = int(f.readline())
            list_of_ingredient = [] # <временный список>
            for i in range(counter):
                temp_dict = {} #- временный словарь
                ingredients_list = f.readline().strip().split('|')
                #ingredient = f.readline() # вот так перемещаемся по файлу
                temp_dict['ingredient_name'] = ingredients_list[0].strip() # <заполняем словарь с ингридиетом>
                temp_dict['quantity'] = ingredients_list[1].strip()
                temp_dict['measure'] = ingredients_list[2].strip()
                list_of_ingredient.append(temp_dict) #<добавляем словарь в список>
            cook_dict[dish_name] = list_of_ingredient
            f.readline() #- еще раз смещаетмся т.к. там пустая срока
    #pprint(cook_dict)
    return cook_dict
create_dict_from_file('recipes.txt')

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_dict = create_dict_from_file('recipes.txt')
    for dish in dishes:
        for ingredients in cook_dict[dish]:
            quantity = int(ingredients['quantity']) * person_count
            if ingredients['ingredient_name'] not in shop_list:
                shop_list[ingredients['ingredient_name']] = {'measure': ingredients['measure'], 'quantity': quantity}
            else:
                shop_list[ingredients['ingredient_name']]['quantity'] += int(ingredients['quantity']) * person_count
    return shop_list

def input_data():
    dishes = input('Введите перечень блюд (через запятую) ').lower().split(', ')
    person_count = int(input('Введите количество персон '))
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    pprint(shop_list)
input_data()