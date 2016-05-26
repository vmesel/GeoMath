#!/bin/bash


echo "TYPE 1 TO INSTALL VIA GITHUB CLONING, TYPE 2 TO INSTALL BY PIP!"
read inputUser
if [ $inputUser = "1" ]; then
	echo "Cloning the repository locally, so you can start developing"
	git clone https://github.com/vmesel/GeoMath.git
else
	echo "Installing geomath library, it will be available via PyPi"
	pip install geomath
fi


