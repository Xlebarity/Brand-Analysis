def average_rating(data): # Отчет по среднему рейтингу брендов
    ratings_sum = {}
    ratings_count = {}

    for item in data: # соберем сумму оценок 
        brand = item['brand']
        rating = float(item['rating'])
        ratings_sum[brand] = ratings_sum.get(brand, 0) + rating
        ratings_count[brand] = ratings_count.get(brand, 0) + 1

    result_rows = []
    for brand in ratings_sum:  # Вычислим средний рейтинг
        avg = ratings_sum[brand] / ratings_count[brand]
        result_rows.append([brand, round(avg, 2)])

    # отсортируем список по убыванию
    result_rows.sort(key=lambda x: x[1], reverse=True)

    return {
        'headers': ['Brand', 'Average Rating'],
        'rows': result_rows
    }

# Добавление отчета по средней цене, что бы быстро посмотреть среднюю цену
def average_price(data):
   
    prices_sum = {}
    prices_count = {}

    for item in data:
        brand = item['brand']
        price = float(item['price'])  
        prices_sum[brand] = prices_sum.get(brand, 0) + price
        prices_count[brand] = prices_count.get(brand, 0) + 1

    result_rows = []
    for brand in prices_sum:
        avg_price = prices_sum[brand] / prices_count[brand]
        result_rows.append([brand, round(avg_price, 2)])

    result_rows.sort(key=lambda x: x[1], reverse=True)

    return {
        'headers': ['Brand', 'Average Price'],
        'rows': result_rows
    }
REPORTS = {
    'average-rating': average_rating,
    'average-price': average_price,
    # сюда можно добавлять еще отчеты
}
def get_reporter(report_name): # Будем возращать функцию по имени
    
    return REPORTS.get(report_name)



