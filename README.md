# CryptoBot v2.0
A Discord Bot written in Python 3 that provides price data about supported Crypto Currencies. This script is intended to be a simple tool used for those interested
in keeping track of the most popular cryptocurrencies without the need to leave Discord. The bot provides the current price, 24 hour percent change, 1 hour high and
lows, and 24 hour high and lows. 

Setup is easy and is explained in the documentation below. New features will continued to be developed as the code is maintained. Please feel free to submit
any bugs you have found. 

## Changelog
- Added support for all tradable cryptocurrencies on Coinbase (U.S. region only)
- Added daily recap feature which will querry all coins on Coinbase to show the top 3 and bottom 3 coins over 24 hours
- Rewrote the launcher shell script to assist in inital setup
- Launcher now checks to make sure required dependencies are in the right place 
- Added a more helpful help menu 

## Setup and Configuration
1: Log into `www.discord.com/developers/` with your Discord credentials 

2: Create a new Application for the bot. Feel free to add a custom name for your bot and add a custom avatar image. 

3: Navigate to the 'Bot' menu and create a new bot. Click "Click to Reveal Token" to reveal your bot's token. Copy the token as we will need it in the next steps. **Keep this token a secret.**

If you need additional help getting this information, RealPython has a great guide that will walk you through the process. `https://realpython.com/how-to-make-a-discord-bot-python/`

4: Log into the machine you wish to run this script off of. We recommend running this script on Ubuntu 18.04 or later. This script has not been tested on other distributions but should continue to work as long as Python 3 is installed. 

5. Clone this repository using the git command: `git clone https://github.com/TechnoEquinox/CryptoBot`

6. Enter the `CryptoBot/` directory and run the launcher: `./cryptobot.sh`

7. Follow the set up process that is prompted.

## Running CryptoBot
If you've successfully followed the **Setup and Configuration** without any errors, then you can run the file with the following command:
`python3 cryptobot.py`

## Usage
Using CryptoBot is easy! The prefix used to talk to the Bot is the '?'. After the '?', input the ticker symbol of the currency you wish to research. 

**Example:** `?btc` or `?BTC`

If you want to querry the daily recap, use the recap command and the bot will handle the rest!

**Example** `?recap` or `?RECAP`

If you need help, use the `?help` command. 

Find a list of all the supported cryptocurrencies here: 
https://help.coinbase.com/en/coinbase/trading-and-funding/cryptocurrency-trading-pairs/supported-cryptocurrencies
