def main():
    arr_1 = []
    arr_2 = []

    # Input processing
    with open(r"C:\Users\mpn42\PycharmProjects\AoC\AoC2024\Inputs\D1.txt", "r") as f:
        for val in f.read().strip().splitlines():

            a = val.split()[0]
            b = val.split()[1]

            arr_1.append(a)
            arr_2.append(b)

    s1 = sorted(arr_1)
    s2 = sorted(arr_2)

    total_dist = 0
    for i in range(len(s2)):
        total_dist = total_dist + abs(int(s1[i]) - int(s2[i]))

    print(total_dist)


if __name__ == "__main__":
    main()
