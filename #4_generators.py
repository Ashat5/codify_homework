#Ashat_Polvanov

# 1. Реализовать функцию range с помощью генератора.

def my_range_function(start, end, step):
    x = start
    while True:
        try:
            if x == end:
                raise Exception ('Конечный порог достигнут!')
            yield x
            x += step 
        except StopIteration:
            print('Хватит генерировать!')   
        except Exception as e:
            print (e)
            break

my_range = my_range_function(0,10,1)
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))
print(next(my_range))



# 2. Реализовать функцию enumerate с помощью генератора.

def my_enumerate_function(object):
    index = 0
    for i in object:
        yield index, i
        index += 1

my_list = ['apple', 'banana', 'cherry']
my_enumerate = my_enumerate_function(my_list)
print(next(my_enumerate))
print(next(my_enumerate))
print(next(my_enumerate))


# 3. Реализовать функцию map с помощью генератора.

def my_map_function(object, function):
    for i in object:
        i = function(i)
        yield i
        
            
i = 0
my_list = [1,2,3,4,5]
def my_func(i):
    i = i ** 2
    return i


my_map = my_map_function(my_list, my_func)
print(next(my_map))
print(next(my_map))
print(next(my_map))


    