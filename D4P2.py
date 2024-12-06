import time


def check_words(r, c, arr, a_count):
    base = arr[r][c]

    # Check UR
    if base + arr[r - 1][c + 1] + arr[r - 2][c + 2] == 'MAS':
        a_count[r - 1][c + 1] += 1

    # Check DR
    if base + arr[r + 1][c + 1] + arr[r + 2][c + 2] == 'MAS':
        a_count[r + 1][c + 1] += 1

    # Check DL
    if base + arr[r + 1][c - 1] + arr[r + 2][c - 2] == 'MAS':
        a_count[r + 1][c - 1] += 1

    # Check UL
    if base + arr[r - 1][c - 1] + arr[r - 2][c - 2] == 'MAS':
        a_count[r - 1][c - 1] += 1


def main():
    array = []

    p2 = 0
    # Input processing
    with open(r"C:\Users\mpn42\PycharmProjects\AoC\AoC2024\Inputs\D4.txt", "r") as f:
        first_line = f.readline()

        text_len = len('MAS')
        width = len(first_line) - 1 + text_len * 2
        test_str = '.'
        topbot_line = test_str * width
        for i in range(text_len):
            array.append(topbot_line)
        f.seek(0, 0)
        for line in f.read().splitlines():
            line = test_str * text_len + line + test_str * text_len
            array.append(line)

        for j in range(text_len):
            array.append(topbot_line)

    r_copy = len(array)
    c_copy = len(array[0]) if array else 0
    a_list = [[0 for _ in range(c_copy)] for _ in range(r_copy)]

    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col] == 'M':
                check_words(row, col, array, a_list)

    for ls in a_list:
        for val in ls:
            if val == 2:
                p2 += 1
    print(p2)


if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")
