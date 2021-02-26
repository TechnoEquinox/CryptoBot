''' 
CryptoBot
Version 2.0

"A smarter crypto bot for Discord channels" created by TechnoEquinox"

Requirements: 
    Python v3.6 (cryptocompare)

Changelog: 
- Added support for all tradable cryptocurrencies on Coinbase (U.S. region only)
- Added daily recap feature which will querry all coins on Coinbase to show the top 3 and bottom 3 coins over 24 hours
- Rewrote the launcher shell script to assist in inital setup
- Launcher now checks to make sure required dependencies are in the right place 
- Added a more helpful help menu 

Known Issues:
- U.S. is the only supported local at this time. Other locals will be added in later versions
- Server side logging of querries is currently broken

'''

import sys
import cryptocompare
import math
import discord
from discord.ext import commands
from datetime import date

client = commands.Bot(command_prefix = '?')


# File to write to for logging
log = open('log.txt', 'w')

# File to read from for Discord token
file = open('config.txt', 'r')
token = ''

try:
    token = file.readline()
except:
    print('An error occured opening "config.txt". Check that the file is in the same directory as "cryptobot.py"')

    
@client.event
async def on_ready():
    print("CryptoBot has successfully connected to your Discord server. Listening for commands...")
    #now = datetime.now()
    #dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    #log.write(dt_string + ": CryptoBot has successfully connected to your Discord server.")
    #print("Successfully wrote to log file!")

@client.event
async def on_message(message):
    if message.content.startswith('?btc') or message.content.startswith('?BTC'):
        coin = 'BTC'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Bitcoin: $' + get_price_str(raw, coin) + ' (' +  get_day_price_change(price, open_price) + ')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/BTCUSD/?exchange=COINBASE')
        print("User queried " + coin) # Logging
    elif message.content.startswith('?eth') or message.content.startswith('?ETH'):
        coin = 'ETH'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)                                                                                                   
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Ethereum: $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/ETHUSD/?exchange=COINBASE')
        print("User queried " + coin) # Logging
    elif message.content.startswith('?bch') or message.content.startswith('?BCH'):
        coin = 'BCH'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)                                                                                                          
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Bitcoin Cash: $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) +'\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/BCHUSD/?exchange=COINBASE')
        print("User queried " + coin) # Logging
    elif message.content.startswith('?lte') or message.content.startswith('?LTE'):
        coin = 'LTC'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)                                                                                                          
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Litecoin: $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/LTCUSD/?exchange=COINBASE')
        print("User queried " + coin) # Logging
    elif message.content.startswith('?eos') or message.content.startswith('?EOS'):
        coin = 'EOS'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)                                                                                                          
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'EOS $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) +\
'\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/EOSUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?bat') or message.content.startswith('?BAT'):
        coin = 'BAT'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)                                                                                                          
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Basic Attention Token $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/BATUSDC/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?xrp') or message.content.startswith('?XRP'):
        coin = 'XRP'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)                                                                                                          
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'XRP $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/XRPUSD/?exchange=BITFINEX')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?xlm') or message.content.startswith('?XLM'):
        coin = 'XLM'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)                                                                                                          
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Stellar Lumens $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/XLMUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?etc') or message.content.startswith('?ETC'):
        coin = 'ETC'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)                                                                                                           
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Ethereum Classic $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/ETCUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?zec') or message.content.startswith('?ZEC'):
        coin = 'ZEC'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)                                                                                                          
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Zcash $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/ZECUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?zrx') or message.content.startswith('?ZRX'):
        coin = 'ZRX'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)                                                                                                          
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = '0x $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/ZRXUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?xtz') or message.content.startswith('?XTZ'):
        coin = 'XTZ'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)                                                                                                          
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Tezos $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/XTZUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?comp') or message.content.startswith('?COMP'):
        coin = 'COMP'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)                                                                                                  
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Compound $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/COMPUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?uni') or message.content.startswith('?UNI'):
        coin = 'UNI'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)                                                                         
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Uniswap $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/UNIUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?aave') or message.content.startswith('?AAVE'):
        coin = 'AAVE'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Aave $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/AAVEUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?algo') or message.content.startswith('?ALGO'):
        coin = 'ALGO'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Algorand $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin)+ '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/ALGOUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?atom') or message.content.startswith('?ATOM'):
        coin = 'ATOM'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Cosmos $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin\
)+ '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/ATOMUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?bal') or message.content.startswith('?BAL'):
        coin = 'BAL'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Balancer $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin)+ '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/BALUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?band') or message.content.startswith('?BAND'):
        coin = 'BAND'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Band Protocol $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin)+ '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/BANDUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?bnt') or message.content.startswith('?BNT'):
        coin = 'BNT'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Bancor Network Token $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin)+ '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/BNTUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?bsv') or message.content.startswith('?BSV'):
        coin = 'BSV'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Bitcoin SV $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin)+ '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/BSVUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?cgld') or message.content.startswith('?CGLD'):
        coin = 'CGLD'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Celo $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin)+ '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/CGLDUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?cvc') or message.content.startswith('?CVC'):
        coin = 'CVC'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Civic $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin)+ '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/CVCUSDC/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?dai') or message.content.startswith('?DAI'):
        coin = 'DAI'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Dai $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin)+ \
'\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/DAIUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?dash') or message.content.startswith('?DASH'):
        coin = 'DASH'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Dash $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin)+ \
'\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/DASHUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?dnt') or message.content.startswith('?DNT'):
        coin = 'DNT'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'district0x $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin)+ '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/DNTUSDC/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?fil') or message.content.startswith('?FIL'):
        coin = 'FIL'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Filecoin $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin)+ '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/FILUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?grt') or message.content.startswith('?GRT'):
        coin = 'GRT'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'The Graph $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin)+ '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/GRTUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?knc') or message.content.startswith('?KNC'):
        coin = 'KNC'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Kyber Network $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin)+ '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/KNCUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?link') or message.content.startswith('?LINK'):
        coin = 'LINK'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Chainlink $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin)+ '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/LINKUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?lrc') or message.content.startswith('?LRC'):
        coin = 'LRC'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Loopring $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin)+ '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/LRCUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?mana') or message.content.startswith('?MANA'):
        coin = 'MANA'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Decentraland $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin)+ '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/MANAUSDC/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?mkr') or message.content.startswith('?MKR'):
        coin = 'MKR'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Maker $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin)+ '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/MKRUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?nmr') or message.content.startswith('?NMR'):
        coin = 'NMR'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Numeraire $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin)+ '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/NMRUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?nu') or message.content.startswith('?NU'):
        coin = 'NU'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'NuCypher $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin)+ '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/NUUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?omg') or message.content.startswith('?OMG'):
        coin = 'OMG'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'OMG Network $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin)+ '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/OMGUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?oxt') or message.content.startswith('?OXT'):
        coin = 'OXT'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Orchid $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/OXTUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?ren') or message.content.startswith('?REN'):
        coin = 'REN'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Ren $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/RENUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?rep') or message.content.startswith('?REP'):
        coin = 'REP'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Auger $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/REPUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?snx') or message.content.startswith('?SNX'):
        coin = 'SNX'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Synthetix Network Token $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/SNXUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?uma') or message.content.startswith('?UMA'):
        coin = 'UMA'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'UMA $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/UMAUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?wbtc') or message.content.startswith('?WBTC'):
        coin = 'WBTC'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'Wrapped Bitcoin $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw, coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/WBTCUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?yfi') or message.content.startswith('?YFI'):
        coin = 'YFI'
        raw = cryptocompare.get_price(coin, curr='USD',full=True)
        channel = message.channel
        price = get_price(raw, coin)
        open_price = get_open_price(raw, coin)
        results = 'yearn.finance $' + get_price_str(raw, coin) + ' (' + get_day_price_change(price, open_price) +')\n\n1HR High: $' + get_high_hour(raw, coin) + '\n1HR Low: $' + get_low_hour(raw,coin) + '\n\n24HR High: $' + get_high_day(raw, coin) + '\n24HR Low: $' + get_low_day(raw, coin)
        await channel.send("```" + results + "```" + 'https://www.tradingview.com/symbols/YFIUSD/?exchange=COINBASE')
        print("User queried " + coin) #Logging
    elif message.content.startswith('?help') or message.content.startswith('?HELP'):
        #BTC - ETH - BCH - LTC - EOS - BAT - XRP - XLM - ETC - ZEC - ZRX - XTZ - COMP - UNI
        channel = message.channel
        await channel.send("```CryptoBot v2.0\nCreated by TechnoEquinox\nPlease report bugs on Github: https://github.com/TechnoEquinox/CryptoBot\n\nKnown Issues:\n-U.S.A. is the only supported local at this time. Other locals will be added in later versions.\n-Server side logging of querries is broken\n\nHow To Use:\n-To querry the price data on a coin: ?[coin symbol]\n-To querry Daily Recap: ?recap or ?RECAP \n\nCurrently Supported Currencies:```" + "https://help.coinbase.com/en/coinbase/trading-and-funding/cryptocurrency-trading-pairs/supported-cryptocurrencies")
        print("User queried ?help")
    elif message.content.startswith('?recap') or message.content.startswith('?RECAP') or message.content.startswith('?Recap'):
        coin = 'Daily Recap'
        channel = message.channel
        today = date.today()
        d = today.strftime("%B %d, %Y")
        output = calc_recap() # Call function, given string output
        await channel.send("```Daily Recap of the " + d + " Crypto Markets\n" + output + "```")
        
        
        
        print("User queried " + coin)
    else:
        pass
        
def get_price_str(raw, coin):
    price = raw['RAW'][coin]['USD']['PRICE']
    return str(float(price))

def get_price(raw, coin):
    price = raw['RAW'][coin]['USD']['PRICE']
    return round(float(price), 2)

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
    return round(float(open_price), 2)

def get_day_price_change(price, open_price):
    day_price_change = round((((price - open_price) / open_price) * 100), 2)
    output = ''
    if day_price_change > 0:
        output = '+ ' + str(day_price_change) + '%'
    else:
        output = '- ' + str(abs(day_price_change)) + '%'
    return output

def calc_recap():
    # Initalize lists
    coins = ['BTC', 'ETH', 'BCH', 'LTC', 'EOS', 'BAT', 'XRP', 'XLM', 'ETC', 'ZEC', 'ZRX', 'XTZ', 'COMP', 'UNI']
    coins_price = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    coins_change = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    price = 0
    cnt = 0
    
    # Get price now and open price, perform percent change and store in list[]
    # Itterate in one loop for better efficiency
    # TODO: This operation takes a long time due to the amount of data it has to go through, look into better runtime
    for x in range(len(coins)):
        var = coins[x]
        raw = cryptocompare.get_price(var, curr='USD',full=True)

        price = get_price(raw, var)
        coins_price[x] = price
        
        open_price = get_open_price(raw, var)

        price_change = round((((price - open_price) / open_price) * 100), 2)
        coins_change[x] = price_change
        
    # Check for biggest gains
    while cnt < 14:
        for x in range(len(coins)-1):
            if coins_change[x] < coins_change[x+1]:
                # Switch values so greater value is moved up the list
                dummy = coins_change[x] # Holds the var that will be switched
                coins_change[x] = coins_change[x+1]
                coins_change[x+1] = dummy
                
                dummy = coins_price[x] # Holds the var that will be switched
                coins_price[x] = coins_price[x+1]
                coins_price[x+1] = dummy
                
                dummy = coins[x]
                coins[x] = coins[x+1]
                coins[x+1] = dummy
        cnt = cnt + 1

    #Pull first 3 and last 3 from the list for best performing and worst performing
    #List is sorted so best performer is in front and least performer is last
    #Return a string with this data formatted

    output = "Top Performing Currencies:\n\n" + str(coins[0]) + ": $" + str(coins_price[0]) + " (" + str(coins_change[0]) + " %)\n" + str(coins[1]) + ": $" + str(coins_price[1]) + " (" + str(coins_change[1]) + " %)\n" + str(coins[2]) + ": $" + str(coins_price[2]) + " (" + str(coins_change[2]) + " %)\n\nWorst Performing Currencies:\n\n" + str(coins[-1]) + ": $" + str(coins_price[-1]) + " (" + str(coins_change[-1]) + " %)\n" + str(coins[-2]) + ": $" + str(coins_price[-2]) + " (" + str(coins_change[-2]) + " %)\n" + str(coins[-3]) + ": $" + str(coins_price[-3]) + " (" + str(coins_change[-3]) + " %)"

    return output
    
client.run(token)
    
