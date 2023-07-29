import sys

def point_position(center_x, center_y, radius, point_x, point_y):
    distance = ((point_x - center_x) ** 2 + (point_y - center_y) ** 2) ** 0.5
    if distance == radius:
        return 0  # Точка лежит на окружности
    elif distance < radius:
        return 1  # Точка внутри окружности
    else:
        return 2  # Точка снаружи окружности

if __name__ == "__main__":
    # Считываем аргументы командной строки
    center_file = sys.argv[1]
    points_file = sys.argv[2]

    # Считываем координаты центра окружности и радиус из файла
    with open(center_file, "r") as f:
        center_x, center_y = map(float, f.readline().split())
        radius = float(f.readline())

    # Считываем координаты точек из файла и выводим их положение относительно окружности
    with open(points_file, "r") as f:
        for line in f:
            point_x, point_y = map(float, line.split())
            position = point_position(center_x, center_y, radius, point_x, point_y)
            print(position)