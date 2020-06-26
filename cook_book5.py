def create_dict_from_file(file_name):
    cook_dict = {}
    with open ('recipes.txt', encoding='utf-8') as f:
        for line in f:
            dish_name = f.readline()
            print(line.lower().strip())
            counter = int(f.readline())
            list_of_ingredient = [] # <временный список>
            for i in range(counter):
                temp_dict = {} #- временный словарь
                print(f.readline().lower())
                ingredients_list = (f.readline().rstrip().replace('|', '').split())
                #ingredient = f.readline() # вот так перемещаемся по файлу
                temp_dict['ingredient_name'] = ingredients_list[0] # <заполняем словарь с ингридиетом>
                temp_dict['quantity'] = ingredients_list[1]
                temp_dict['measure'] = ingredients_list[2]
                list_of_ingredient.append(temp_dict) #<добавляем словарь в список>
            cook_dict[dish_name] = list_of_ingredient
            f.readline() #- еще раз смещаетмся т.к. там пустая срока
    return cook_dict
create_dict_from_file('recipes.txt')