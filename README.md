# GeoMath [![Build Status](https://travis-ci.org/vmesel/GeoMath.svg?branch=master)](https://travis-ci.org/vmesel/GeoMath) [![PyPI version] (https://badge.fury.io/py/geomath.svg)](https://badge.fury.io/py/geomath)

![image](imgs/geomath.png)


GeoMath é uma biblioteca que possibilita a todos usuários a implementarem e trabalharem com Geometria Analítica em Python 3.X. Esta biblioteca é gratuita e está garantida na licença GNU GPLv3, portanto você pode baixar, redistribuir e modificar a vontade, mas sempre citando a fonte dos códigos.

A biblioteca é dividida em algumas classes:

- Pontos: Uma classe que define, cria e calcula vários formatos de informação com pontos;
- Linha: Como eu posso juntar dois pontos? É simples, use uma linha;
- Figuras: Você quer criar uma figura com estes pontos? Adicione-os dentro da figura.

PS: A biblioteca ainda está em processo de tradução, portanto pode ser que você veja alguns termos em inglês, mas uma rápida googlada te ajudará a entende-los.

## Como usar?

```
from geomath.point import Point
from geomath.line import Line
P1 = Point(0,0) # We create a Point
P2 = Point(4,4) # We create another Point
L1 = Line()
L1.create(P1,P2)
L1.equation() #irá retornar a equação da linha
```

A biblioteca é muito simples de ser usada, os exemplos e guia de uso estão disponíveis em [GeoMath.co](http://geomath.co), e a documentação está disponível [neste link](https://geomath.readthedocs.io/).

## Como instalar?

Existem 2 formas simples de ter o GeoMath instalado e rodando em seu computador:

- do Python PyPi
- do github(not recommended)

###Instalando do PyPi

``` pip install geomath ```

###Instalando do Github

``` git clone https://www.github.com/vmesel/GeoMath.git ```


Pronto! Agora você pode ser um geometro!

##[TODO](/todo.md)
