
def main():
    with open("m4_input.txt", "r") as file:
        numbers = iter(map(int, file.read().split()))

    test_cases = next(numbers)

    for _ in range(test_cases):
        rows = next(numbers)
        cols = next(numbers)
        threshold = next(numbers)

        count = 0
        col = cols - 1

        for _ in range(rows):
            row = [next(numbers) for _ in range(cols)]

            while col >= 0 and row[col] >= threshold:
                col -= 1

            count += cols - 1 - col

        print(count)


if __name__ == "__main__":
    main()
