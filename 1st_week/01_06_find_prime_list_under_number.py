input = 20

def find_prime_list_under_number(number):
    prime = []

    for i in range(2, number + 1):
        for j in prime:
            if i % j == 0:
                break
        else:
            prime.append(i)

    return prime

result = find_prime_list_under_number(input)
print(result)