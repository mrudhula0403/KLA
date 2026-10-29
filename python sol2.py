
def solve(h):
    n = len(h)
    l, r = 0, n - 1

    max_coolant = 0
    best_left = 0
    best_right = n - 1

    while l < r:
        width = r - l
        water_height = min(h[l], h[r])
        capacity = width * water_height

        if (capacity > max_coolant or
            (capacity == max_coolant and
             (l < best_left or
              (l == best_left and r < best_right)))):
            max_coolant = capacity
            best_left = l
            best_right = r

        if h[l] < h[r]:
            l += 1
        else:
            r -= 1

    return max_coolant, best_left + 1, best_right + 1


def main():
    with open("m2_input.txt", "r") as file:
        data = file.read().split()

    p = 0
    T = int(data[p])
    p += 1

    out = []

    for _ in range(T):
        n = int(data[p])
        p += 1

        h = list(map(int, data[p:p + n]))
        p += n

        max_coolant, left, right = solve(h)
        out.append(f"{max_coolant} {left} {right}")

    with open("answers2.txt", "w") as file:
        file.write("\n".join(out) + "\n")

    print("\n".join(out))


if __name__ == "__main__":
    main()
