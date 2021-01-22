
''' 
CryptoBot
Version 1.2

"A smarter crypto bot for Discord channels" created by TechnoEquinox"

Requirements: 
    Python v3.6 (cryptocompare)

Changelog: 
- Added Discord integration which required a full rewrite of how data was access. Previous version stored data in local variables. This version utilizes function calls.

TODO:
- Add logging

Known Issues:
- Some coins may display statistics beyond two decimal places in certain conditions

'''

import sys
import cryptocompare
import math
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '?')

file = open('config.txt', 'r')
token = ''

try:
    token = file.readline()
except:
    print('An error occured opening "config.txt". Check that the file is in the same directory as "cryptobot.py"')


@client.event
async def on_ready():
    print("Bot is Online.")

@client.event
async def on_message(message):
    if message.content.startswith('?btc') or message.content.startswith('?BTC'):
        coin = 'BTC'
        raw = cryptocompare.get_price(coin, curr='USD',full=True) #raw_btc is a nested dictionary
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Bitcoin: $' + get_price_str(raw, coin) + ' (' +  get_day_price_change(price, open_price) + ')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```")
    elif message.content.startswith('?eth') or message.content.startswith('?ETH'):
        coin = 'ETH'
        raw = cryptocompare.get_price(coin, curr='USD',full=True) #raw_btc is a nested dictionary                                                                                                    
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Ethereum: $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```")
    elif message.content.startswith('?bch') or message.content.startswith('?BCH'):
        coin = 'BCH'
        raw = cryptocompare.get_price(coin, curr='USD',full=True) #raw_btc is a nested dictionary                                                                                                          
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Bitcoin Cash: $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) +'\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```")
    elif message.content.startswith('?lte') or message.content.startswith('?LTE'):
        coin = 'BCH'
        raw = cryptocompare.get_price(coin, curr='USD',full=True) #raw_btc is a nested dictionary                                                                                                          
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Litecoin: $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) +\
'\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```")
    elif message.content.startswith('?eos') or message.content.startswith('?EOS'):
        coin = 'EOS'
        raw = cryptocompare.get_price(coin, curr='USD',full=True) #raw_btc is a nested dictionary                                                                                                          
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'EOS $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) +\
'\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```")
    elif message.content.startswith('?bat') or message.content.startswith('?BAT'):
        coin = 'BAT'
        raw = cryptocompare.get_price(coin, curr='USD',full=True) #raw_btc is a nested dictionary                                                                                                          
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Basic Attention Token $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```")
    elif message.content.startswith('?xrp') or message.content.startswith('?XRP'):
        coin = 'XRP'
        raw = cryptocompare.get_price(coin, curr='USD',full=True) #raw_btc is a nested dictionary                                                                                                          
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'XRP $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```")
    elif message.content.startswith('?xlm') or message.content.startswith('?XLM'):
        coin = 'XLM'
        raw = cryptocompare.get_price(coin, curr='USD',full=True) #raw_btc is a nested dictionary                                                                                                          
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Stellar Lumens $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```")
    elif message.content.startswith('?etc') or message.content.startswith('?ETC'):
        coin = 'ETC'
        raw = cryptocompare.get_price(coin, curr='USD',full=True) #raw_btc is a nested dictionary                                                                                                          
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Ethereum Classic $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```")
    elif message.content.startswith('?zec') or message.content.startswith('?ZEC'):
        coin = 'ZEC'
        raw = cryptocompare.get_price(coin, curr='USD',full=True) #raw_btc is a nested dictionary                                                                                                          
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Zcash $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```")
    elif message.content.startswith('?zrx') or message.content.startswith('?ZRX'):
        coin = 'ZRX'
        raw = cryptocompare.get_price(coin, curr='USD',full=True) #raw_btc is a nested dictionary                                                                                                          
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = '0x $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```")
    elif message.content.startswith('?xtz') or message.content.startswith('?XTZ'):
        coin = 'XTZ'
        raw = cryptocompare.get_price(coin, curr='USD',full=True) #raw_btc is a nested dictionary                                                                                                          
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Tezos $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```")
    elif message.content.startswith('?help') or message.content.startswith('?HELP'):
        #BTC - ETH - BCH - LTC - EOS - BAT - XRP - XLM - ETC - ZEC - ZRX - XTZ
        channel = message.channel
        await channel.send("```CryptoBot v1.1\nCreated by TechnoEquinox\nPlease report bugs on Github: https://github.com/TechnoEquinox/CryptoBot\n\nKnown Issues:\n- Some coins may display values beyond two decimal places in certain conditions.\n\nCurrently Supported Currencies:\nBitcoin (BTC) - Ethereum (ETH) - Bitcoin Cash (BCH) - Litecoin (LTC) - EOS - Basic Attention Token (BAT) - XRP - Stellar Lumens (XLM) - Ethereum Classic (ETC) - Zcash (ZEC) - 0x (ZRX) - Tezos (XTZ)```")
    else:
        pass
        

        
def get_price_str(raw, coin):
    price = raw['RAW'][coin]['USD']['PRICE']
    return str(float(price))

def get_price(raw, coin):
    price = raw['RAW'][coin]['USD']['PRICE']
    return float(price)

def get_high_hour(raw, coin):
    high_hour = raw['RAW'][coin]['USD']['HIGHHOUR']
    return str(float(high_hour))

def get_low_hour(raw, coin):
    low_hour = raw['RAW'][coin]['USD']['LOWHOUR']
    return str(float(low_hour))

def get_high_day(raw, coin):
    high_day = raw['RAW'][coin]['USD']['HIGHDAY']
    return str(float(high_day))

def get_low_day(raw, coin):
    low_day = raw['RAW'][coin]['USD']['LOWDAY']
    return str(float(low_day))

def get_open_price(raw, coin):
    open_price = raw['DISPLAY'][coin]['USD']['OPEN24HOUR']
    open_price = open_price[2:] # substring off the $
    open_price = open_price.replace(',', "") # sanatize the string
    return float(open_price)

def get_day_price_change(price, open_price):
    day_price_change = round((((price - open_price) / open_price) * 100), 2)
    output = ''
    if day_price_change > 0:
        output = '+ ' + str(day_price_change) + '%'
    else:
        output = '- ' + str(abs(day_price_change)) + '%'
    return output
    
client.run(token)
    
