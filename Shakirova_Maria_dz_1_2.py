list_cub = []
sum_num = 0

for i in range(1, 1000, 2):
    list_cub.append(i ** 3)
for ind, val in enumerate(list_cub):
    sum_digit = 0
    while val:
        sum_digit += val % 10
        val //= 10
    if sum_digit % 7 == 0:
        sum_num += list_cub[ind]
    list_cub[ind] += 17
print(sum_num)

sum_num = 0

for ind, val in enumerate(list_cub):
    sum_digit = 0
    while val:
        sum_digit += val % 10
        val //= 10
    if sum_digit % 7 == 0:
        sum_num += list_cub[ind]
print(sum_num)