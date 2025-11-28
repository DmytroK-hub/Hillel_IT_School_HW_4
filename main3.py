import random

length = random.randint(3, 10)
lst = [random.randint(0, 9) for _ in range(length)]
print("Початковий список:", lst)

first = lst[0]
third = lst[2]
second_from_end = lst[-2]

final_list = [first, third, second_from_end]
print("Фінальний список:", final_list)
