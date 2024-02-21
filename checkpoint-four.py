from decimal import Decimal
import math

#Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
my_list = [1, 3, 56, 2]
my_tuple = (1, 4, 6, 8)
float_number = 1.3
integer_number = 34
decimal = Decimal(2.58)
my_dictionary = { "james" : 23, "bily" : 55, "isabelle" : 85}

#Exercise 2: Round your float up.
print(math.ceil(float_number))

#Exercise 3: Get the square root of your float.
print(math.sqrt(float_number))

#Exercise 4: Select the first element from your dictionary.
first_key = list(my_dictionary.keys())[0]
first_value = list(my_dictionary.values())[0]
first_element = first_key + ' : ' + str(first_value)
print(first_element)


#Exercise 5: Select the second element from your tuple.
print(my_tuple[1])

#Exercise 6: Add an element to the end of your list.
my_list.append(7)
print(my_list)

#Exercise 7: Replace the first element in your list.
my_list[0] = 99
print(my_list)

#Exercise 8: Sort your list alphabetically.
letter_list = ["g", "r", "z", "a"]
letter_list.sort()
print(letter_list)

#Exercise 9: Use reassignment to add an element to your tuple.
new_tupple = my_tuple + (15, )
print(new_tupple)