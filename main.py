import requests
import mysql.connector
from datetime import datetime

# local database config, this is different for everyone due to local preferences
comp = mysql.connector.connect(
    host='localhost',
    user='root',
    password='tree',
    port='3306',
    database='crypto'
)


def get_BitCoin_Price():
    try:
        # source the crypto values are pulling from
        source = "https://api.coingecko.com/api/v3/simple/price"

        parameters = {
            "ids": "bitcoin",
            "vs_currencies": "usd"
        }

        request = requests.get(source, params=parameters)

        # 200 means source was valid
        if request.status_code == 200:
            # Parse the JSON response
            data = request.json()
            bitcoin_price_usd = data['bitcoin']['usd']
            print(f"Bitcoin Price (USD): ${bitcoin_price_usd}")

            bitcoin_price = float(bitcoin_price_usd)
            cursor = comp.cursor()
            timeStamp = datetime.now()  # date along with time retrieved

            hour = timeStamp.hour
            second = timeStamp.hour
            month = timeStamp.month
            day = timeStamp.day
            min = timeStamp.minute
            year = timeStamp.year

            statement = "INSERT INTO bitcoin_livedata (Month, Day, year, Hour, Min, Second, Price) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (month, day, year, hour, min, second, bitcoin_price)
            cursor.execute(statement, values)
            comp.commit()
            cursor.close()


        else:
            print(f"Request failed with status code: {request.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")


def get_Ethereum_Price():
    try:
        # source the crypto values are pulling from
        source = "https://api.coingecko.com/api/v3/simple/price"

        parameters = {
            "ids": "ethereum",
            "vs_currencies": "usd"
        }

        request = requests.get(source, params=parameters)

        # 200 means source was valid
        if request.status_code == 200:
            # Parse the JSON response
            data = request.json()
            ethereum_price_usd = data['ethereum']['usd']
            print(f"Ethereum Price (USD): ${ethereum_price_usd}")

            ethereum_price = float(ethereum_price_usd)
            cursor = comp.cursor()
            timeStamp = datetime.now()  # date along with time retrieved

            hour = timeStamp.hour
            second = timeStamp.hour
            month = timeStamp.month
            day = timeStamp.day
            min = timeStamp.minute
            year = timeStamp.year

            statement = "INSERT INTO ethereum (Month, Day, year, Hour, Min, Second, Price) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (month, day, year, hour, min, second, ethereum_price)
            cursor.execute(statement, values)
            comp.commit()
            cursor.close()
            comp.close()

        else:
            print(f"Request failed with status code: {request.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")




get_BitCoin_Price()
get_Ethereum_Price()
