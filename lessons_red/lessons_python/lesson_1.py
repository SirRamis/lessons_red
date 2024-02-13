# Данные множества
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}

# 1. Найдем значения, которые встречаются в обоих множествах:
intersection = set1.intersection(set2)
print("Значения, которые встречаются в обоих множествах:", intersection)

# 2. Найдем значения, которые не встречаются в обоих множествах:
symmetric_difference = set1.symmetric_difference(set2)
print("Значения, которые не встречаются в обоих множествах:", symmetric_difference)

# 3. Проверим, являются ли эти множества подмножествами друг друга:
is_subset_1_to_2 = set1.issubset(set2)
is_subset_2_to_1 = set2.issubset(set1)

print("set1 является подмножеством set2:", is_subset_1_to_2)
print("set2 является подмножеством set1:", is_subset_2_to_1)
