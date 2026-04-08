input_str = "acccdeee"

def summarize_string(input_str):
    alp = [0] * 26

    for i in input_str:
        alp[ord(i) - ord('a')] += 1

    result = ""

    for idx in range(len(alp)):
        if alp[idx] >= 1:
            if result != "":
                result += "/"
            alphabet = ord('a') + idx
            result += (chr(alphabet) + str(alp[idx]))

    return result

print(summarize_string(input_str))