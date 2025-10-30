import argparse
import csv
from collections import defaultdict
from tabulate import tabulate
from reporters import get_reporter

#обработка командных аргументов для запуска скрипта через терминал
def parse_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument(
        "--report", required=True
    )
    return parser.parse_args()

# для чтения файла products.csv
def read_csv_files(file_paths):
    data = []
    for path in file_paths:
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    return data

def main():
    args = parse_args()

    data = read_csv_files(args.files)

    # функция для получения формирования отчета
    report_func = get_reporter(args.report)
    if report_func is None:
        print(f"Отчет '{args.report}' не найден.")
        return

    report_data = report_func(data)

    # Выводим в таблице
    headers = report_data["headers"]
    rows = report_data["rows"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    main()
