import requests
import math

def telegram_bot_sendtext(bot_message):
    """sends the article via telegram"""
    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

#specified stock of the user
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

#Api endpoint and Api key of the stock market and articles respectively
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "your key"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "your key"

#specify the time frame
YESTERDAY = "2025-12-05"
DAY_BEFORE_YESTERDAY = "2025-12-01"

#parameters for various Api's
STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
news_parameters = {
    "q": COMPANY_NAME,
    "from": DAY_BEFORE_YESTERDAY,
    "to": YESTERDAY,
    "apikey": NEWS_API_KEY
}

#Goal: When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print the first 3 articles

# get the stock data and stock price for yesterday closing price and a day before yesterday closing price with the API
stock_response = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMS)
stock_data = stock_response.json()
stock_date = stock_data["Time Series (Daily)"]
yesterday_price = float(stock_date[YESTERDAY]["4. close"])
day_before_yesterday_price = float(stock_date[DAY_BEFORE_YESTERDAY]["4. close"])

#work out the difference between them and get the percentage
difference = yesterday_price - day_before_yesterday_price

#stock indicator(mail)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
percentage_change = math.floor((difference / day_before_yesterday_price) * 100)

#get the first three articles for the specified stock and format them
news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_data = news_response.json()
articles = news_data["articles"][:3]
formated_article = [(f"{STOCK}:{up_down}{abs(percentage_change)}%\nHeadline: {news_item["title"]}"
                     f"\nBrief: {news_item["description"]}") for news_item in articles]

#refer to Goal...
#Send each article as a separate message via Telegram.
if percentage_change <= -5 or percentage_change >= 5:
    for article in formated_article:
        message = telegram_bot_sendtext(article)
        print(message)