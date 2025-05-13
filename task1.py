input_str = input("Введите список чисел через запятую: ")
num_list = [int(num) for num in input_str.split(",")]

even_numbers = [num for num in num_list if num % 2 == 0]

max_num = num_list[0]
min_num = num_list[0]
for num in num_list:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

sorted_list = num_list.copy()
n = len(sorted_list)
for i in range(n):
    for j in range(0, n-i-1):
        if sorted_list[j] > sorted_list[j+1]:
            sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]

print("Четные числа:", even_numbers)
print("Максимальное число:", max_num)
print("Минимальное число:", min_num)
print("Отсортированный список:", sorted_list)