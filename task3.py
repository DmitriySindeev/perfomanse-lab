import json
import sys

def fill_values(tests, values):
    for test in tests:
        test_id = test["id"]
        if "values" in test:
            fill_values(test["values"], values)
        if "value" in test:
            for value in values:
                if value["id"] == test_id:
                    test["value"] = value["value"]
                    break

if __name__ == "__main__":
    # Считываем аргументы командной строки
    tests_file = sys.argv[1]
    values_file = sys.argv[2]
    report_file = sys.argv[3]

    # Считываем структуру tests.json из файла
    with open(tests_file, "r") as f:
        data = json.load(f)
        tests = data["tests"]

    # Считываем результаты прохождения тестов из values.json
    with open(values_file, "r") as f:
        values_data = json.load(f)
        values = values_data["values"]

    # Заполняем поля value в структуре tests.json на основе результатов values.json
    fill_values(tests, values)

    # Записываем полученный отчёт в файл report.json
    with open(report_file, "w") as f:
        json.dump(data, f, indent=2)