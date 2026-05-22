def find_max_occurred_alphabet(string):
    alp = [0] * 26
    for ch in string:
        if not ch.isalpha():
            continue
        alp[ord(ch) - ord('a')] += 1

    max_count = alp[0]
    max_idx = 0

    for idx in range(1, len(alp)):
        if max_count < alp[idx]:
            max_count = alp[idx]
            max_idx = idx

    return chr(max_idx + ord('a'))


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))