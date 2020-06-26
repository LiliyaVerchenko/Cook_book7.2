def cook_book_all():
    dish_list = []
    cook_book = {}
    cook_book_1 = []
    with open ('recipes.txt', encoding='utf-8') as f:
        while True:
            title = f.readline().rstrip()  # 1 строка
            number_of_ingredients = f.readline().rstrip() # 2 строка
            n = int(number_of_ingredients)
            cook_book[title] = dish_list
            for i in range(0,n):
                ingredients_list = (f.readline().rstrip().replace('|', '').split())
                ingredients_dict = {}
                ingredients_dict['ingredient_name'] = ingredients_list[0]
                ingredients_dict['quantity'] = ingredients_list[1]
                ingredients_dict['measure'] = ingredients_list[2]
                dish_list.append(ingredients_dict)
            #print(cook_book)
            f.readline()  # пустая строка
            if not title:
                break
            cook_book_1.append(cook_book)
            print(cook_book_1)
cook_book_all()
