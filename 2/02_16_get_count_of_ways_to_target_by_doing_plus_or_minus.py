numbers = [1, 1, 1, 1, 1]
target_number = 3

count = 0

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    # 구현해보세요!
    global count

    dfs(array, 0, 0, target)

    return count


def dfs(arry, index, sum, target):
    global count

    if index == len(arry):
        if sum == target:
            count += 1
        return

    dfs(arry, index + 1, sum + arry[index], target)
    dfs(arry, index + 1, sum - arry[index], target)


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!