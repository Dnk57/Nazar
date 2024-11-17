import csv
import json
from collections import OrderedDict

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

indent = 4
ensure_ascii = False


def task(filename: str, delimiter=',', line_terminator='\n') -> str:
    # Чтение данных из CSV файла
    with open(INPUT_FILENAME, "r", encoding='utf-8', newline='') as json_str:
        reader = csv.DictReader(json_str, delimiter=delimiter, lineterminator=line_terminator)

        # Сериализация данных в формате JSON
        data = [OrderedDict(row) for row in reader]

    # Преобразование в JSON
    json_output = json.dumps(data, indent=indent, ensure_ascii=ensure_ascii)
    return json_output


if __name__ == '__main__':
    # Преобразование и запись результата в файл
    json_result = task(INPUT_FILENAME)
    with open(OUTPUT_FILENAME, "w", encoding='utf-8') as output_f:
        output_f.write(json_result)

    # Для проверки результата
    with open(OUTPUT_FILENAME, "r", encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")
