# coipo
Experimento Blockchain en Python utilizando como base de desarrollo el script [Snakecoin](https://gist.github.com/aunyks/8f2c2fd51cc17f342737917e1c2582e2).

## Modo de uso:

Ejecuta el script **blockchain.py** con Python 3.6, incluyendo la cantidad de bloques que deseas generar.

```
python blockchain.py [cantidad de bloques]
```

Automaticamente el script generará transacciones, creará bloques con sus respectivos hashes y entregará en pantalla el resultado.

## Ejemplo:

```
C:\coipo>blockchain.py 4
Block #0
{'hash': '45d909f5fc0b0968a5ff1326620ad358', 'height': 0, 'timestamp': 150787068
7.6261067, 'data': 123.456, 'n': 1, 'previousblockhash': '0'}


Block #1
{'hash': '85c62520314142a788b4ea9842951ec5', 'height': 1, 'timestamp': 150787068
7.6261067, 'data': [68231.22745131716, 58148.46920219712], 'n': 2, 'previousbloc
khash': '45d909f5fc0b0968a5ff1326620ad358'}


Block #2
{'hash': '818abe8343d67c533424919081c6d1bb', 'height': 2, 'timestamp': 150787068
7.6261067, 'data': [88964.82613856552], 'n': 1, 'previousblockhash': '85c6252031
4142a788b4ea9842951ec5'}


Block #3
{'hash': 'b2d5c5637f65f9e66952116ae8b81539', 'height': 3, 'timestamp': 150787068
7.6261067, 'data': [29176.304833827224, 58411.000334397184, 77085.80915241255, 3
6014.99994471835], 'n': 4, 'previousblockhash': '818abe8343d67c533424919081c6d1b
b'}


Block #4
{'hash': '7c11c6b981a223c1f54c49bb76877fa2', 'height': 4, 'timestamp': 150787068
7.6261067, 'data': [40927.396798802845, 44776.007651747605], 'n': 2, 'previousbl
ockhash': 'b2d5c5637f65f9e66952116ae8b81539'}


FIN
```