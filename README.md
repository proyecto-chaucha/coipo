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
C:\coipo>python blockchain.py 4
Block #0

> Verbose: {'hash': '75cb20507f10ba0e25d1440045f84e40', 'height': 0, 'timestamp': 1507872083.6958768, 'n': 1, 'data': [123.456], 'previousblockhash': '0'}
> Packed: b'75cb20507f10ba0e25d1440045f84e40\x00\x00\x00\x00?\x89\xecT\x13x\xd6A\x01\x00\x00\x00w\xbe\x9f\x1a/\xdd^@0'

Block #1

> Verbose: {'hash': '6c4f57a95ab43a447083b6cdb9d8a0bd', 'height': 1, 'timestamp': 1507872083.6958768, 'n': 3, 'data': [39297.97842706353, 62871.74976145796, 57982.552574572], 'previousblockhash': '75cb20507f10ba0e25d1440045f84e40'}
> Packed: b'6c4f57a95ab43a447083b6cdb9d8a0bd\x01\x00\x00\x00?\x89\xecT\x13x\xd6A\x03\x00\x00\x00\xecEFO?0\xe3@\xb8\xbd\x0b\xfe\xf7\xb2\xee@k\xde\xb0\xae\xd1O\xec@75cb20507f10ba0e25d1440045f84e40'

Block #2

> Verbose: {'hash': 'c9f0d85851634b1438afb0cea8b72901', 'height': 2, 'timestamp': 1507872083.6958768, 'n': 4, 'data': [14191.398899271044, 76824.98079584673, 62141.311592661965, 97967.57021489395], 'previousblockhash': '6c4f57a95ab43a447083b6cdb9d8a0bd'}
> Packed: b'c9f0d85851634b1438afb0cea8b72901\x02\x00\x00\x00?\x89\xecT\x13x\xd6A\x04\x00\x00\x00\xc4\x9d!\x0f\xb3\xb7\xcb@\\\xfcV\xb1\x8f\xc1\xf2@\x9a,\x91\xf8\xa9W\xee@\x13\xa7\x99\x1f\xf9\xea\xf7@6c4f57a95ab43a447083b6cdb9d8a0bd'

Block #3

> Verbose: {'hash': '3546b9b008231489442b2a76ec030f01', 'height': 3, 'timestamp': 1507872083.6958768, 'n': 5, 'data': [92335.60187598539, 64168.39044798297, 88142.9693653524, 55160.1053871766, 68605.79710889491], 'previousblockhash': 'c9f0d85851634b1438afb0cea8b72901'}
> Packed: b'3546b9b008231489442b2a76ec030f01\x03\x00\x00\x00?\x89\xecT\x13x\xd6A\x05\x00\x00\x00\x98\xb6H\xa1\xf9\x8a\xf6@\xb5\xc4\x8c~\x0cU\xef@g>\x85\x82\xef\x84\xf5@\x9d\xedT_\x03\xef\xea@\xb0A\xf5\xc0\xdc\xbf\xf0@c9f0d85851634b1438afb0cea8b72901'

Block #4

> Verbose: {'hash': 'c5b1e12efd2f03816f3141388d642fd0', 'height': 4, 'timestamp': 1507872083.6958768, 'n': 4, 'data': [12755.648236527864, 86291.8490459989, 22117.057505280784, 96386.86116813589], 'previousblockhash': '3546b9b008231489442b2a76ec030f01'}
> Packed: b'c5b1e12efd2f03816f3141388d642fd0\x04\x00\x00\x00?\x89\xecT\x13x\xd6A\x04\x00\x00\x00\xa0\x1fj\xf9\xd2\xe9\xc8@\xe1A\xb1\x95=\x11\xf5@\x14\xa1*\xaeC\x99\xd5@@=X\xc7-\x88\xf7@3546b9b008231489442b2a76ec030f01'

FIN
```