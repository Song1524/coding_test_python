finding_target = 1
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, array):
    # 이 부분을 채워보세요!
    # array.sort()
    # start = 0
    # end = len(array) - 1
    #
    # while start <= end:
    #     mid = (start + end) // 2
    #
    #     if array[mid] == target:
    #         return True
    #     elif array[mid] < target:
    #         start = mid + 1
    #     elif array[mid] > target:
    #         end = mid - 1

    if target in array:
        return True

    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)