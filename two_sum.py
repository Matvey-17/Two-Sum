list_digit = [7, 4, 3, 1, 2]
target = 9

seen = {}

for i in range(len(list_digit)):
    if list_digit[i] > target:
        continue
    
    pr_res = target - list_digit[i]
    
    if list_digit[i] in seen:
        print(i, seen[list_digit[i]])
        break
    
    seen[pr_res] = i  

else:
    print('Не найдено')

