red=`tput setaf 1`
green=`tput setaf 2`
background=`tput setab 7`
reset=`tput sgr 0`

echo -e "CryptoBot v2.0\nCreated by: TechnoEquinox\n${red}Please report bugs on Github: ${background}https://github.com/TechnoEquinox/CryptoBot${reset}"

echo -e "Checking for required dependencies..."

# check to see if the cryptocompare package is installed                                                                                                                                              
if python3 -V; then
    echo -e "Python 3 was found."
else
    echo -e "${red}Python3 was not found. ${reset}"
    echo -e "Installing Python 3..."
    sudo apt-get install python3.6 # TODO: Test and see if root privilages are needed here
fi

# check to see if pip3 is installed
if pip3 --version; then
    echo -e "pip3 was found."
else
    echo -e "${red}pip3 was not found. ${reset}"
    echo -e "Installing pip3..."
    sudo apt-get -y install python3-pip # TODO Test and see if root privilages are needed here
fi

# check to see if the Discord package is installed
if python3 -c 'import discord; exit()'; then
    echo -e "The Discord package was found found."
else
    echo -e "${red}The Discord package was not found. ${reset}"
    echo -e "Installing Discord python3 package..."
    python3 -m pip install -U discord.py # TODO: Test and see if root privilages are needed here                                                                                                                
fi

# check to see if the cryptocompare package is installed
if python3 -c 'import cryptocompare; exit()'; then
    echo -e "The cryptocompare package was found found."
else
    echo -e "${red}The cryptocompare package was not found. ${reset}"
    echo -e "Installing cryptocompare..."
    pip3 install cryptocompare # TODO: Test and see if root privilages are needed here
fi


cd ~/CryptoBot_dev
# Check for local file to find country 
echo -e "Checking for local file..."
LOCAL_FILE=~/CryptoBot_dev/local.txt
if ! [ -f "$LOCAL_FILE" ]; then
    echo -e "${red}$LOCAL_FILE does not exist. Creating...${reset}"
    touch ~/CryptoBot_dev/local.txt
    echo "Created $LOCAL_FILE"
    echo -e "Input your geographical region to see more accurate data.\n(Coinbase supported regions: US, EU, UK, AU, CA, SG)"
    read region
    echo "Writing region to $LOCAL_FILE..."
    echo $region > ~/CryptoBot_dev/local.txt
    echo "${red}$LOCAL_FILE is now ready to be used. Relaunch the script to run.${reset}"
    exit 1
fi
    
echo -e "Checking for config file..."
# Checks if config.txt is not present
# Prompts for token after creating file
FILE=~/CryptoBot_dev/config.txt
if ! [ -f "$FILE" ]; then
    echo -e "${red}$FILE does not exist. Creating...${reset}"
    touch ~/CryptoBot_dev/config.txt
    echo "Created $FILE"
    echo "Input your Bot's secret token from Discord. (Can be found at: https://discord.com/developers/)"
    echo "Secret token: "
    read token_secret
    echo "Writing token to $FILE..."
    echo $token_secret > ~/CryptoBot_dev/config.txt
    echo "${red}$FILE is now ready to be used. Relaunch the script to run.${reset}"
    exit 1
fi

echo -e "${green}$FILE exists. Running the script...${reset}\n*\n*\n*\n"
python3.6 cryptobot.py
