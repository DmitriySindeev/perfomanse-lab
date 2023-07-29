import sys

def min_moves(nums):
    target = round(sum(nums) / len(nums)) # Находим число, к которому нужно приравнять элементы массива
    moves = 0

    for num in nums:
        moves += abs(num - target)

    return moves

if __name__ == "__main__":
    # Считываем аргумент командной строки - имя файла
    input_file = sys.argv[1]

    # Считываем числа из файла
    with open(input_file, "r") as f:
        nums = [int(line.strip()) for line in f]

    # Вычисляем минимальное количество ходов
    result = min_moves(nums)

    # Выводим результат
    print(result)