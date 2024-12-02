

def check_report(ls):
    in_order = (ls == sorted(ls) or ls == sorted(ls, reverse=True))
    asc_or_desc_val_check = True
    for i in range(len(ls)-1):
        diff = abs(ls[i]-ls[i+1])
        if diff < 1 or diff > 3:
            asc_or_desc_val_check = False

    return in_order and asc_or_desc_val_check


def main():
    array = []

    p1 = 0
    p2 = 0
    # Input processing
    with open(r"C:\Users\mpn42\PycharmProjects\AoC\AoC2024\Inputs\D2.txt", "r") as f:
        for line in f.read().strip().splitlines():
            array.append(list(map(int, line.split())))

    print(array)
    for i in range(len(array)):
        check = check_report(array[i])
        if check:
            p1 += 1
        check_p2 = False
        for j in range(len(array[i])):
            temp_list = array[i][:j] + array[i][j+1:]
            if check_report(temp_list):
                check_p2 = True

        if check_p2:
            p2 += 1

    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
