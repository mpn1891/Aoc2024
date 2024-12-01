def main():

    arr_1 = []
    arr_2 = []

    # Input processing
    with open(r"C:\Users\mpn42\PycharmProjects\AoC\AoC2024\Inputs\D1.txt", "r") as f:
        for val in f.read().strip().splitlines():

            a = val.split()[0]
            b = val.split()[1]

            arr_1.append(int(a))
            arr_2.append(int(b))

    s1 = sorted(arr_1)

    sim_score = 0
    for i in range(len(s1)):
        sim_score += s1[i] * arr_2.count(s1[i])

    print(sim_score)


if __name__ == "__main__":
    main()
