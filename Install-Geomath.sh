#!/bin/bash


echo "DIGITE 1 PARA INSTALAR PELO GITHUB, DIGITE 2 PARA INSTAALAR PELO PIP!"
read inputUser
if [ $inputUser = "1" ]; then
	git clone https://github.com/vmesel/GeoMath.git
else
	pip install geomath
fi


