#!/bin/bash

echo -n "Checking dependencies... "

for name in node python3 pip3
do
  [[ $(which $name 2>/dev/null) ]] || { echo -en "\n$name needs to be installed. Use 'sudo apt-get install $name'";deps=1; }
done

[[ $deps -ne 1 ]] && echo "OK" || { echo -en "\nInstall the above and rerun this script\n";exit 1; }

echo "Installing python libraries... "
pip3 install pygame
echo "OK"
