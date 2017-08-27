st = input()
counter = {}
str_list = []
max_num = 1
for s in str(st):
    if s in counter:
        counter[s] += 1
        if counter[s] > max_num:
            max_num = counter[s]
    else:
        counter[s] = 1
        str_list.append(s)
str_list.sort()
aux_dict = {}
second = 0
third = 0
for s, n in counter.items():
    if n == max_num:
        if n not in aux_dict:
            aux_dict[n] = [s]
        else:
            aux_dict[n].append(s)
    elif second < n or second == n:
        if third < n < second:
            third = second
        if second != n:
            second = n
        if n not in aux_dict:
            aux_dict[n] = [s]
        else:
            aux_dict[n].append(s)
    elif third < n or third == n:
        if third != n:
            third = n
        if n not in aux_dict:
            aux_dict[n] = [s]
        else:
            aux_dict[n].append(s)

result = aux_dict[max_num]
len_result = len(result)
if len_result < 3:
    second_list = aux_dict[second]
    if len_result == 1:
        if len(second_list) > 1:
            second_list.sort()
            second_list = second_list[:2]
            result += second_list
        else:
            result += second_list
            aux_dict[third].sort()
            result += aux_dict[third][0]
    else:
        result += second_list[0]
elif len_result > 3 or len_result == 3:
    result.sort()
    result = result[:3]
for r in result:
    print(r + ' ' + str(counter[r]))
