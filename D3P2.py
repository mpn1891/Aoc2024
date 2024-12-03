import time


def main():
    array = []

    p2 = 0
    # Input processing
    with open(r"C:\Users\mpn42\PycharmProjects\AoC\AoC2024\Inputs\D3.txt", "r") as f:
        for line in f.read().splitlines():
            array.append(line.split('mul'))

    do = True
    for i in range(len(array)):
        for j in range(len(array[i])):

            if array[i][j].find('(') == 0 and array[i][j].find(',') != -1 and array[i][j].find(')') != -1 and do:

                wrk = array[i][j].split(',')
                wrk[0] = wrk[0][wrk[0].find('(') + 1:]
                wrk[1] = wrk[1][:wrk[1].find(')')]

                if wrk[0].isnumeric() and wrk[1].isnumeric():
                    p2 += int(wrk[0]) * int(wrk[1])

            if array[i][j].find('''don't()''') != -1:
                do = False
            if array[i][j].find('''do()''') != -1:
                do = True
    print(p2)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")