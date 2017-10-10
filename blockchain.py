# Snakecoin
# https://gist.github.com/aunyks/8f2c2fd51cc17f342737917e1c2582e2

# Proyecto Chaucha - 2017

import hashlib as hasher
from time import time
from struct import pack, unpack

# Definición del sintaxis de bloque
class Block:
	def __init__(self, index, timestamp, data, previousblockhash):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previousblockhash = previousblockhash
		self.hash = self.blockHash()
	
	# Creación de hash de bloque
	def blockHash(self):
		sha = hasher.sha256()
		block_template = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previousblockhash)
		sha.update(block_template.encode('utf-8'))
		return sha.hexdigest()

	# Compresión de tamaño de bloque
	def blockPack(self):
		packedIndex = pack('L', self.index)
		packedTimestamp = pack('d', self.timestamp)

	# Presentación de información en formato JSON
	def verbose(self):
		return {
				'hash' : self.hash,
				'index' : self.index,
				'timestamp' : self.timestamp,
				'data' : self.data,
				'previousblockhash' : self.previousblockhash
				}

# Genesis Block
def genesisBlock():
	return Block(0, time(), 'Genesis Block', '0')

# Generación de bloques
def blockCreate(lastBlock):
	index = lastBlock.index + 1
	timestamp = int(time())
	data = 'Hey! Im block ' + str(index)
	hash = lastBlock.hash
	return Block(index, timestamp, data, hash)

def main():
	# Iniciar blockchain con el Genesis Block
	blockchain = [genesisBlock()]
	previous_block = blockchain[0]

	num_of_blocks_to_add = 20

	# Generar 20 bloques
	for i in range(0, num_of_blocks_to_add):
		block_to_add = blockCreate(previous_block)
		blockchain.append(block_to_add)
		previous_block = block_to_add

	# Mostrar el resultado
	print(Block.verbose(blockchain[5]))

if __name__ == '__main__':
	main()