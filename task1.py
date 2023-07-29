import sys

def circular_array_path(n, m):
    array = list(range(1, n+1)) * 2  # Создаем массив с повторяющимися элементами от 1 до n
    path = []  # Инициализируем пустой путь
    start_index = 0  # Устанавливаем начальный индекс

    while len(path) < n:  # Пока длина пути меньше n
        path.append(array[start_index])  # Добавляем элемент в путь
        start_index = (start_index + m - 1) % n  # Обновляем индекс в соответствии с правилом
        if start_index == 0:  # Если вернулись к начальному индексу, выходим из цикла
            break

    return path

if __name__ == "__main__":
    # Считываем аргументы командной строки
    n = int(sys.argv[1])
    m = int(sys.argv[2])

    result = circular_array_path(n, m)
    print(''.join(map(str, result)))