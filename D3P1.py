
def main():
    array = []

    p1 = 0
    p2 = 0
    # Input processing
    with open(r"C:\Users\mpn42\PycharmProjects\AoC\AoC2024\Inputs\D3.txt", "r") as f:
        for line in f.read().splitlines():
            array.append(line.split('mul'))

    print(array)


    for i in range(len(array)):
        for j in range(len(array[i])):

            wrk = []
            if array[i][j].find('(') == 0 and array[i][j].find(',') != -1 and array[i][j].find(')') != -1:
                wrk.clear()

                wrk = array[i][j].split(',')

                wrk[0] = wrk[0][wrk[0].find('(') +1:]

                wrk[1] = wrk[1][:wrk[1].find(')')]

                if wrk[0].isnumeric() and wrk[1].isnumeric():
                    print('IS valid: ', array[i][j])

                    p1 += int(wrk[0]) * int(wrk[1])
                else:
                    print('NOT valid: ', array[i][j])
            else:
                print('NOT valid: ', array[i][j])
    print(p1)







    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
