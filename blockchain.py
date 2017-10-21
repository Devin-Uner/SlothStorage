import datetime
import sys
import random
import subprocess
import json

class Block(object):
	"""docstring for Block"""
	def __init__(self, data_=None, previous_hash_=None, adder_=None, difficulty_=None, block_repr=None):

		
		if block_repr != None:
			self.data = json.loads(block_repr)["data"]
			self.previous_hash = json.loads(block_repr)["previous_hash"]
			self.adder = json.loads(block_repr)["adder"]
			self.time = json.loads(block_repr)["time"]
			self.difficulty = json.loads(block_repr)["difficulty"]
			self.nonce = json.loads(block_repr)["nonce"]
			self.hash = json.loads(block_repr)["hash"]
		else:
			self.data = str(data_)
			self.previous_hash = str(previous_hash_)
			self.adder = str(adder_)
			self.time = str(datetime.datetime.now())
			self.difficulty = difficulty_

			self.nonce = 0
			self.hash = str(hash(self.data + self.previous_hash + self.adder + self.time + str(self.nonce)))+"x"*self.difficulty
			while(self.hash[:self.difficulty] != "8" * self.difficulty):
				self.nonce += random.randint(-1*sys.maxint, sys.maxint)
				self.hash = str(hash(self.data + self.previous_hash + self.adder + self.time + str(self.nonce)))+"x"*self.difficulty

			
			self.set_hash()

	def set_hash(self):
		self.hash = str(hash(self.data + str(self.previous_hash) + self.adder + self.time + str(self.nonce)))+"x"*self.difficulty

	def __repr__(self):
		return "\n--------" + ("VALID" if self.is_valid() else "INVALID") + "--------\ndata: " + self.data + "\nprevious hash: " + str(self.previous_hash) + "\nhash: " + self.hash + "\nadder: " + self.adder + "\ntime added: " + self.time + "\n----------------\n"

	def __str__(self):
		return json.dumps(self.get_dict())

	def get_dict(self):
		return {
				"data": self.data,
				"previous_hash": str(self.previous_hash),
				"adder": self.adder,
				"time": self.time,
				"difficulty": self.difficulty,
				"nonce": self.nonce,
				"hash": self.hash,
				}

	def is_valid(self):
		return self.hash[:self.difficulty] == "8"*self.difficulty



class Chain(object):
	"""docstring for Chain"""
	def __init__(self, difficulty_=None, chain_repr=None):
		if chain_repr==None:
			self.difficulty = difficulty_
			self.block_array = [Block("origin block", None, "root", difficulty_)]
		else:
			self.difficulty = json.loads(str(chain_repr))["difficulty"]
			self.block_array = []
			for block_repr in json.loads(str(chain_repr))["blocks"]:
				self.add_block(block_repr=block_repr)

	def add_block(self, message=None, user=None, block_repr=None):
		self.update_valid()
		if block_repr==None:
			self.block_array += [Block(message, self.block_array[-1].hash if len(self.block_array) > 0 else None, user, self.difficulty)]
		else:
			self.block_array += [Block(block_repr=block_repr)]


	def update_valid(self):
		for i in range(0, len(self.block_array)):
			self.block_array[i].previous_hash = self.block_array[i - 1].hash  if i > 0 else None
			self.block_array[i].set_hash()

	def __repr__(self):
		total = ""
		for block in self.block_array:
			total += repr(block)
		return total

	def __str__(self):
		total = []
		for block in self.block_array:
			total += [json.dumps(block.get_dict())]
		return json.dumps({"blocks": total, "difficulty": self.difficulty})

	def is_valid(self):
		self.update_valid()
		for block in self.block_array:
			if block.is_valid() == False:
				return False
		return True


# # make the BlockChain
# my_chain = Chain(3)
# my_chain.add_block("hello world!", "devin")
# my_chain.add_block("hello mike", "mikey")
# my_chain.add_block("devin is kool", "devin")

# # write the data to a file
# f = open("blockchain_data.txt", "w")
# f.write(str(my_chain))
# f.close()

# make a new one from the file
f = open("blockchain_data.txt", "r")
data = ""
for line in f:
	data += line
f.close()
new_chain = Chain(chain_repr=data)
# print repr(new_chain)


def reset():
	# query its neighbors for the correct values
	print "chain is currently invalid, attempting error correction"
	all_chains = {}
	# so for every line in the nodes.txt file, try to connect and read from it
	f = open("nodes.txt", "r")
	for line in f:
		chain = subprocess.check_output( ("ssh -i SlothStorageAWSKey.pem.txt " + str(line).replace("\n","") + " python blockchain.py " + str(0)).split())
		all_chains[chain] = all_chains.get(chain, 0) + 1
	f.close()
	all_chains["INVALID"] = 0
	best = sorted(all_chains.items(), key=lambda x:x[1])[-1][0]
	print "found best representation of uncorrupted data, resetting self"
	new_chain = Chain(chain_repr=best)
	f = open("blockchain_data.txt", "w")
	f.write(str(new_chain))
	f.close()


def write():
	# write the data to a file
	f = open("blockchain_data.txt", "w")
	f.write(str(new_chain))
	f.close()


def update_neighbors(new_block_repr):
	f = open("nodes.txt", "r")
	for line in f:
		command = "ssh -i SlothStorageAWSKey.pem.txt " + str(line).replace("\n","") + " python blockchain.py 0"
		print command
		output = subprocess.check_output(command.split(" "))
		if output != "INVALID CHAIN" and (len(Chain(chain_repr=output).block_array)==0 or Chain(chain_repr=output).block_array[-1].hash != json.loads(new_block_repr)["hash"]):
			command = "ssh -i SlothStorageAWSKey.pem.txt " + str(line).replace("\n","") + " python blockchain.py " + str(1) + " '" + new_block_repr + "'"
			print command
			output = subprocess.check_output( ("ssh -i SlothStorageAWSKey.pem.txt " + str(line).replace("\n","") + " python blockchain.py " + str(1) + " '" + new_block_repr + "'").split())


if not new_chain.is_valid():
	reset()

if int(sys.argv[1]) == 0: #print off all of the chains data in json format
	# check if its valid
	if new_chain.is_valid():
		print new_chain # if it is just print off its values
	else:
		print "INVALID CHAIN"
if int(sys.argv[1]) == 1: #add a block to the chain with a block_repr, need to have '' around the new block_repr
	new_chain.add_block(block_repr=sys.argv[2])
	new_chain.update_valid()
	write()
	update_neighbors(str(new_chain.block_array[-1]))
if int(sys.argv[1]) == 2: # add a new block to the chain from some data stuff
	new_chain.add_block(sys.argv[2], sys.argv[3])
	new_chain.update_valid()
	write()
	update_neighbors(str(new_chain.block_array[-1]))
if int(sys.argv[1]) == 3: #force reset
	reset()
if int(sys.argv[1]) == 4: #pretty print
	print repr(new_chain)

if not new_chain.is_valid():
	reset()











		