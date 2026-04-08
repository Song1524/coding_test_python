input = "111011"


def find_count_to_turn_out_to_all_zero_or_all_one(string):

    group_zero = 0
    group_one = 0

    if string[0] == "0":
        group_zero += 1
    else:
        group_one += 1

    for i in range(1, len(string)):
        if string[i] != string[i - 1]:
            if string[i] == "0":
                group_zero += 1
            else:
                group_one += 1

    return min(group_zero, group_one)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)