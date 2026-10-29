from collections import Counter


def least_rot(s):
    n = len(s)
    s2 = s + s
    i, j, k = 0, 1, 0
    while i < n and j < n and k < n:
        a, b = s2[i + k], s2[j + k]
        if a == b:
            k += 1
            continue
        if a > b:
            i += k + 1
        else:
            j += k + 1
        if i == j:
            j += 1
        k = 0
    start = min(i, j)
    return s2[start:start + n]


def solve_case(readings):
    c = Counter(least_rot(r) for r in readings)
    return [len(c), max(c.values())] + sorted(c)


def main():
    data = open("m1_input.txt").read().split()
    p = 0
    T = int(data[p]); p += 1
    out = []
    for _ in range(T):
        K = int(data[p]); p += 1
        readings = [x.strip() for x in data[p:p + K]]
        p += K
        out.append(" ".join(map(str, solve_case(readings))))
    open("answers.txt", "w").write("\n".join(out) + "\n")
    print("\n".join(out))


main()