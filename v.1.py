# Import requests, BeautifulSoup and csv libraries
import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the website
url = "https://shitcoins.club/"

# Send a GET request to the website and get the response
response = requests.get(url)

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    # Parse the response content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the tbody element with id "atm_table_tbody"
    tbody = soup.find("tbody", id="atm_table_tbody")

    # Find all the tr elements in the tbody element
    rows = tbody.find_all("tr")

    # Create a list to store the cryptocurrency data
    data = []

    # Loop through each row element and extract the cryptocurrency name and prices
    for row in rows:
        # Find all the td elements in the row
        cells = row.find_all("td")
      
        # Get the text of each cell as a string
        name = cells[0].text.strip()
        buy_price = cells[1].text.strip()
        sell_price = cells[2].text.strip()

        # Check if the name is one of BTC, ETH, LTC or USDT
        if name in ["BTC", "ETH", "LTC", "USDT"]:
            # Print the name and prices of each cryptocurrency
            print(name, buy_price, sell_price)

            # Append the name and prices to the data list as a tuple
            data.append((name, buy_price, sell_price))

    # Open a file named "cryptocurrency_data.csv" in write mode
    with open("cryptocurrency_data.csv", "w") as file:
        # Create a csv writer object
        writer = csv.writer(file)

        # Write a header row with column names "Name", "Buy Price" and "Sell Price"
        writer.writerow(["Name", "Buy Price", "Sell Price"])

        # Write the data list to the file as rows
        writer.writerows(data)
else:
    # Print an error message if the response status code is not 200 (OK)
    print("Error: Unable to access the website")
