def solution1(S):
    upper = set([letter.upper() for letter in S if letter.islower()])
    lower = set([letter for letter in S if letter.isupper()])
    intersection = upper & lower

    return max(intersection) if intersection else "NO"


def solution2(N):
    numbers = []
    if N % 2 != 0:
        numbers.append(0)
        N -= 1
    N = N // 2

    positive_numbers = list(range(1, N + 1))
    negative_numbers = list(range(-1, -(N + 1), -1))
    numbers.extend(positive_numbers)
    numbers.extend(negative_numbers)

    return numbers


def task2():
    res = []

    def nums(N):
        r = 1
        for i in range(N // 2):
            res.append(r)
            res.append(-r)
            r += 1

    def solution(N):
        if N % 2 == 0:
            nums(N)
        else:
            nums(N - 1)
            res.append(0)

        return res


def task3(A, B, C):
    def is_diverse(letter):
        return letter != ultimate or letter != penultimate

    def can_extend():
        return len(letters) > 1 or len(letters) == 1 and any(map(is_diverse, letters))

    def update_letter(letter, count):
        count -= 1
        if count <= 0:
            del letters[letter]
        else:
            letters[letter] = count

    ultimate, penultimate = '', ''

    letters = {}
    if A > 0: letters['a'] = A
    if B > 0: letters['b'] = B
    if C > 0: letters['c'] = C

    diverse_string = ""

    while can_extend():
        sorted_letters = sorted(list(letters.items()), key=lambda x: x[1], reverse=True)
        for letter, count in sorted_letters:
            if is_diverse(letter):
                diverse_string += letter
                penultimate, ultimate = ultimate, letter
                update_letter(letter, count)
                break

    return diverse_string


def main():
    # print(solution("Codility"))
    # print(solution2(4))
    print(task3(0,1,8))


if __name__ == '__main__':
    main()
    # import random
    #
    # print("TESTS")
    # for _ in range(1000000):
    #     num = random.randint(0, 100)
    #     numbers = solution2(num)
    #     assert sum(numbers) == 0
    #     assert len(numbers) == len(set(numbers))
