import time


def check_words(r, c, arr):
    count = 0
    base = arr[r][c]
    # Check U
    if base + arr[r - 1][c] + arr[r - 2][c] + arr[r - 3][c] == 'XMAS':
        count += 1
    # Check UR
    if base + arr[r - 1][c + 1] + arr[r - 2][c + 2] + arr[r - 3][c + 3] == 'XMAS':
        count += 1
    # Check R
    if base + arr[r][c + 1] + arr[r][c + 2] + arr[r][c + 3] == 'XMAS':
        count += 1
    # Check DR
    if base + arr[r + 1][c + 1] + arr[r + 2][c + 2] + arr[r + 3][c + 3] == 'XMAS':
        count += 1
    # Check D
    if base + arr[r + 1][c] + arr[r + 2][c] + arr[r + 3][c] == 'XMAS':
        count += 1
    # Check DL
    if base + arr[r + 1][c - 1] + arr[r + 2][c - 2] + arr[r + 3][c - 3] == 'XMAS':
        count += 1
    # Check L
    if base + arr[r][c - 1] + arr[r][c - 2] + arr[r][c - 3] == 'XMAS':
        count += 1
    # Check UL
    if base + arr[r - 1][c - 1] + arr[r - 2][c - 2] + arr[r - 3][c - 3] == 'XMAS':
        count += 1
    return count


def main():
    array = []

    p1 = 0

    # Input processing
    with open(r"C:\Users\mpn42\PycharmProjects\AoC\AoC2024\Inputs\D4.txt", "r") as f:
        first_line = f.readline()

        text_len = len('XMAS')
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

    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col] == 'X':

                p1 += check_words(row, col, array)

    print(p1)



if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")
