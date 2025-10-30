import pytest
from main import read_csv_files
from reporters import average_rating


def test_read_csv_files(tmp_path):  # проверка что файл читает CSV файл
    data = """name,brand,price,rating
iPhone 15,apple,999,4.9
Galaxy S21,samsung,799,4.8
Redmi Note,xiaomi,199,4.6
"""
    file_path = tmp_path / "test.csv"
    file_path.write_text(data)

    result = read_csv_files([str(file_path)])
    assert len(result) == 3
    assert result[0]["name"] == "iPhone 15"
    assert result[1]["brand"] == "samsung"


def test_average_rating():
    data = [
        {"name": "item1", "brand": "apple", "price": "999", "rating": "4.9"},
        {"name": "item2", "brand": "apple", "price": "899", "rating": "4.7"},
        {"name": "item3", "brand": "samsung", "price": "799", "rating": "4.8"},
    ]
    report = average_rating(data)
    assert report["headers"] == ["Brand", "Average Rating"]
    # Проверяем, что для apple средний рейтинг 4.8
    apple_rating = next(row for row in report["rows"] if row[0] == "apple")[1]
    assert abs(apple_rating - 4.8) < 0.01
