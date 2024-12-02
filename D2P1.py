def main():
    array = []
    answer_arr = []
    # Input processing
    with open(r"C:\Users\mpn42\PycharmProjects\AoC\AoC2024\Inputs\D2.txt", "r") as f:
        for line in f.read().strip().splitlines():
            array.append((line.split()))

    print(array)

    for i in range(len(array)):
        report_len = len(array[i])
        direction = int(array[i][0]) - int(array[i][1])
        if direction != 0:
            direction = direction/abs(direction)
            print(direction)
        else:
            continue

        for j in range(report_len - 1):
            diff = int(array[i][j]) - int(array[i][j+1])
            print(diff)
            if direction > 0:
                if 0 < diff < 4:
                    if j == report_len - 2:
                        answer_arr.append(i)
                else:
                    break
            elif direction < 0:
                if -4 < diff < 0:
                    if j == report_len - 2:
                        answer_arr.append(i)
                else:
                    break

        print(answer_arr)
        print(len(answer_arr))


if __name__ == "__main__":
    main()
