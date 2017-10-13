# coipo
Experimento Blockchain en Python utilizando como base de desarrollo el script [Snakecoin](https://gist.github.com/aunyks/8f2c2fd51cc17f342737917e1c2582e2).

## Modo de uso:

Ejecuta el script **blockchain.py** con [Python 3.6](https://www.python.org), incluyendo la cantidad de bloques que deseas generar.

```
python blockchain.py [cantidad de bloques]
```

Automaticamente el script generará transacciones, creará bloques con sus respectivos hashes y entregará en pantalla el resultado.

## Ejemplo:

```
C:\coipo>blockchain.py 4
Block #0
{'hash': '90e4c708f82029a3f5d79da6b97843da', 'height': 0, 'timestamp': 1507871005.8566692, 'n': 1, 'data': 123.456, 'previousblockhash': '0'}

Block #1
{'hash': '451f06ffaeef60786651433c4ede5d9e', 'height': 1, 'timestamp': 1507871005.8566692, 'n': 4, 'data': [13122.322698373324, 59913.01273632884, 62132.8152003053, 97694.28095929835], 'previousblockhash': '90e4c708f82029a3f5d79da6b97843da'}

Block #2
{'hash': '882d118cff57dda84427f1c157c6c213', 'height': 2, 'timestamp': 1507871005.8566692, 'n': 1, 'data': [94378.06577589802], 'previousblockhash': '451f06ffaeef60786651433c4ede5d9e'}

Block #3
{'hash': 'fd41c2e938ea6223afc523826f03f7ff', 'height': 3, 'timestamp': 1507871005.8566692, 'n': 5, 'data': [39213.74385322358, 39446.675587020574, 53746.775946413996, 90589.57639552676, 69233.97350841446], 'previousblockhash': '882d118cff57dda84427f1c157c6c213'}

Block #4
{'hash': '9820eba4995c0246a07d7955f71bd09b', 'height': 4, 'timestamp': 1507871005.8566692, 'n': 3, 'data': [28787.1528008594, 68297.59952194573, 94060.04395769224], 'previousblockhash': 'fd41c2e938ea6223afc523826f03f7ff'}

FIN
```