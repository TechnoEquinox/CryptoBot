red=`tput setaf 1`
background=`tput setab 7`
reset=`tput sgr 0`

echo -e "${red}CryptoBot v1.2.1\nCreated by: TechnoEquinox\nPlease report bugs on Github: ${background}https://github.com/TechnoEquinox/CryptoBot${reset}"

echo "${red}Launching Script..."
cd ~/CryptoBot
python3.6 cryptobot.py
