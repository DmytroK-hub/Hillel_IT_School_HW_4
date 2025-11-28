lst = [0, 3, 6, 2, 9, 8, 2]

if lst:
    even_index_elements = lst[0::2]
    sum_even = sum(even_index_elements)
    last_element = lst[-1]
    result = sum_even * last_element
else:
    result = 0

print(result)
