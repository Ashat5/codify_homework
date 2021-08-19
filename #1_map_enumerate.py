#Ashat_Polvanov

#Условие программы:
#В магазине есть список разных продуктов, у каждого продукта есть название, цена, уникальный номер. 
#Сперва пользователю нужно отобразить весь список продуктов с их информацией, после нужно сказать чтобы он ввел
#название товара, если такой товар есть предложить пользователю купить этот товар, и ввести сумму если введенная 
#сумма меньше цены которая указана на товар то нужно уведомить его что у вас не хватает денег чтобы купить, иначе 
#сказать ему что вы получили товар.


products_list = [{
    'name' : 'bread',
    'price' : 25,
    'id' : 1
},
{   'name' : 'milk',
    'price' : 50,
    'id' : 2
},
{   'name' : 'meat',
    'price' : 500,
    'id' : 3
},
{   'name' : 'potatoes',
    'price' : 30,
    'id' : 4
},
{   'name' : 'cheese',
    'price' : 600,
    'id' : 5
}]
print('PRODUCT LIST:')
for product in products_list:
    print('*' * 40)
    for i in product:
        print(i,product[i])
user_input = ''
continue_word = ''
while user_input == '' or user_input == None:
    user_input = input('Enter the name of the product you want to buy: ')
    try:
        if user_input == '' or user_input == None:
            raise Exception ("Error! You didn't enter anything!")
        else:
            for product in products_list:
                
                if user_input in product['name']:
                    user_input = user_input.lower()
                    users_product = product
                    print('This product is available.')
                    continue_word = input('If you want to buy this product enter "yes", to select another product press any key: ')
                    if continue_word == 'yes':
                        break
                    else:
                        user_input = ''
                        break
            else:
                print('This product is out of stock.')
                continue_word = input('To select another product press any key, to exit the store type "exit": ')
                if continue_word != 'exit':
                    user_input = ''                        
                else:
                    continue
    except Exception as e:
        print(e)
other_enter = continue_word
while other_enter != 'exit':
    try:   
        user_price = int(input('Enter payment for the product: '))
            
        if user_price == '' or user_price == None:
            raise Exception ("Error! You didn't enter anything!")
    except Exception as e:
        print(e)
    except ValueError as e:
        print('Value Error', e)

    if user_price >= users_product['price']:
        print("You bought the product!")
        break
    else:
        print("Not enough funds!")
        other_enter = input('If you want to enter a different amount press any key,\
 if you want to exit the store enter "exit": ')












