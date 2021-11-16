import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "SHLIMJDOG12U7GJA"
TWILIO_SID = "AC3e98ba123db2e5aa9c7ba6d531da0264"
TWILIO_AUTH_TOKEN = "f6550bfe97ba8e602ff4fd252aab15d0"
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
YESTERDAY_CLOSE_PRICE = data_list[0]['4. close']

DAY_BEFORE_YESTERDAY_CLOSE_PRICE = data_list[1]['4. close']


difference = float(YESTERDAY_CLOSE_PRICE) - float(DAY_BEFORE_YESTERDAY_CLOSE_PRICE)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(YESTERDAY_CLOSE_PRICE)) * 100)

NEWS_API_KEY = "0a8c6fd4b8ac4ad5a8cba2a090efce13"
if abs(diff_percent) > 1:
    news_params = {
        'apiKey': NEWS_API_KEY,
        'qInTitle': COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles']

    three_articles = articles[:3]

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}% \nHeadline: {article['title']}. \nBrief: {article['description']}\n"
                          for article in three_articles]

    for article in formatted_articles:
        print(article)
