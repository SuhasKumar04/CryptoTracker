import requests
import mysql.connector
from datetime import datetime
import matplotlib.pyplot as plt

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

def plotData():
    conn = mysql.connector.connect(comp)

    # Create a cursor
    cursor = conn.cursor()

    # Write an SQL query to select the data
    sql_query = "SELECT month, day, hour, minute, second, price FROM crypto_data"

    # Execute the query
    cursor.execute(sql_query)

    # Fetch the data
    data = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Extract data for plotting
    timestamps = []
    prices = []

    for row in data:
        month, day, hour, minute, second, price = row
        timestamp = f"{month}/{day} {hour}:{minute}:{second}"
        timestamps.append(timestamp)
        prices.append(price)

    # Create a line plot
    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, prices, marker='o')
    plt.title("Crypto Price Over Time")
    plt.xlabel("Timestamp")
    plt.ylabel("Price (USD)")
    plt.xticks(rotation=45)  # Rotate x-axis labels for readability

    # Display the plot
    plt.tight_layout()
    plt.show()



get_BitCoin_Price()
get_Ethereum_Price()
#plotData()
