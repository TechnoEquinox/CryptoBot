# CryptoBot v1.2
A Discord Bot written in Python 3 that provides price data about supported Crypto Currencies. This script is intended to be a simple tool used for those interested
in keeping track of the most popular cryptocurrencies without the need to leave Discord. The bot provides the current price, 24 hour percent change, 1 hour high and
lows, and 24 hour high and lows. 

Setup is easy and is explained in the documentation below. New features will continued to be developed as the code is maintained. Please feel free to submit
any bugs you have found. 

## Changelog
- Fixed an issue that caused an out of context '?' to be read as invalid input
- Added better handling of the bot token so it does not need to be put into the source code
- Updated the `?help` command with relevant version number and link to GitHub page

## Setup and Configuration
1: Log into `www.discord.com/developers/` with your Discord credentials 

2: Create a new Application for the bot. Feel free to add a custom name for your bot and add a custom avatar image. 

3: Navigate to the 'Bot' menu and create a new bot. Click "Click to Reveal Token" to reveal your bot's token. Copy the token as we will need it in the next steps. **Keep this token a secret.**

If you need additional help getting this information, RealPython has a great guide that will walk you through the process. `https://realpython.com/how-to-make-a-discord-bot-python/`

4: Log into the machine you wish to run this script off of. We recommend running this script on Ubuntu 18.04 or later. This script has not been tested on other distributions but should continue to work as long as Python 3 is installed. 

5: Verify Python 3 is installed using
`python3 --version`

If it is not installed, install using
`sudo apt install python3`

6: Install the cryptocompare python package. This is used to query price data for the script:
`pip3 install cryptocompare`

7: Install the Discord API:
`pip3 install -U discord.py`

8: Install CryptoBot by cloning the repository:
`git clone https://github.com/TechnoEquinox/CryptoBot`

9: Navigate to the created CryptoBot directory and run the following command:
`touch config.txt`

Open this file in your text editor and paste the token from Discord into this file. Leave the text on the first line and do not add anything else other than the token to this file. 

## Running CryptoBot
If you've successfully followed the **Setup and Configuration** without any errors, then you can run the file with the following command:
`python3 cryptobot.py`

## Usage
Using CryptoBot is easy! The prefix used to talk to the Bot is the '?'. After the '?', input the ticker symbol of the currency you wish to research. 

**Example:** `?btc` or `?BTC`

If you need help, use the `?help` command. 

This is the current list of supported currencies with more to be added in the future:
- Bitcoin (BTC) 
- Ethereum (ETH) 
- Bitcoin Cash (BCH) 
- Litecoin (LTC)
- EOS 
- Basic Attention Token (BAT) 
- XRP 
- Stellar Lumens (XLM) 
- Ethereum Classic (ETC) 
- Zcash (ZEC) 
- 0x (ZRX) 
- Tezos (XTZ)
