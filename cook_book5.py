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
                temp_dict['ingredient_name'] = ingredients_list[0].strip() # <заполняем словарь
                temp_dict['quantity'] = ingredients_list[1].strip()
                temp_dict['measure'] = ingredients_list[2].strip()
                list_of_ingredient.append(temp_dict) #<добавляем словарь в список>
            cook_dict[dish_name] = list_of_ingredient
            f.readline() #пустая срока
    pprint(cook_dict)
    return cook_dict
create_dict_from_file('recipes.txt')