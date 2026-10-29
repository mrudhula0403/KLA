
def solve(arr):
    balance = 0
    first = {0: 0}  # balance -> earliest prefix position

    best_len = 0
    best_start = -1
    best_end = -1

    for i, bit in enumerate(arr, start=1):
        if bit == 1:
            balance += 1
        else:
            balance -= 1

        if balance in first:
            start = first[balance] + 1
            end = i
            length = end - start + 1

            if (length > best_len or
                (length == best_len and
                 (best_start == -1 or start < best_start))):
                best_len = length
                best_start = start
                best_end = end
        else:
            first[balance] = i

    if best_len == 0:
        return "0 -1 -1"

    return f"{best_len} {best_start} {best_end}"


def main():
    with open("m3_input.txt", "r") as file:
        data = list(map(int, file.read().split()))

    p = 0
    T = data[p]
    p += 1

    answers = []

    for _ in range(T):
        n = data[p]
        p += 1

        arr = data[p:p + n]
        p += n

        answers.append(solve(arr))

    result = "\n".join(answers)

    with open("answers3.txt", "w") as file:
        file.write(result + "\n")

    print(result)


if __name__ == "__main__":
    main()
