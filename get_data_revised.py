''' 
CryptoBot
Version 1.1

"A smarter crypto bot for Discord channels" created by TechnoEquinox"

Requirements: 
    Python v3.6 (cryptocompare)

Changelog: 
- Improves and optimizes the querries of new coin data to be handled in one method dynamically

'''

import sys
import cryptocompare
import math


def get_info(coin):
    raw = cryptocompare.get_price(coin, curr='USD',full=True) #raw_btc is a nested dictionary
    price = raw['RAW'][coin]['USD']['PRICE'] #navigate nested dictionary like this
    high_hour = raw['RAW'][coin]['USD']['HIGHHOUR']
    low_hour = raw['RAW'][coin]['USD']['LOWHOUR']
    high_day = raw['RAW'][coin]['USD']['HIGHDAY']
    low_day = raw['RAW'][coin]['USD']['LOWDAY']
    open_price = raw['DISPLAY'][coin]['USD']['OPEN24HOUR']

    price = float(price)
    
    open_price = open_price[2:] # substring off the $
    open_price = open_price.replace(',', "") # sanatize the string
    open_price = float(open_price) # convert to float

    day_price_change = round((((price - open_price) / open_price) * 100), 2)
    
    if day_price_change > 0:
        print(coin, " $", price, " (+", day_price_change, "%) ")
    else:
        print(coin, " $", price, " (", day_price_change, "%) ")

    print("1HR High: $", high_hour)
    print("1HR Low: $", low_hour)
    print("24HR High: $", high_day)
    print("24HR Low: $", low_day)


coin_to_search = input("Enter the ticker symbol of the crypto currency you want to research: ")
print("\n")

if coin_to_search == 'BTC' or coin_to_search == 'ETH' or coin_to_search == 'BCH' or coin_to_search == 'LTC' or coin_to_search == 'EOS' or coin_to_search == 'BAT' or coin_to_search == 'XRP' or coin_to_search == 'XLM' or coin_to_search == 'ETC' or coin_to_search == 'ZEC' or coin_to_search == 'ZRX' or coin_to_search == 'XTZ':
    get_info(coin_to_search)
elif coin_to_search == 'help' or coin_to_search == 'Help' or coin_to_search == 'HELP':
    print("Current supported assets: \nBTC - ETH - BCH - LTC - EOS - BAT - XRP - XLM - ETC - ZEC - ZRX - XTZ")
else:
    print("Sorry this crypto currency either cannot be found or is not supported at this time. (Try 'help')")


exit(0)




    
