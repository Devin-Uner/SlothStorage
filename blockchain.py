import datetime
import sys
import random

class Block(object):
	"""docstring for Block"""
	def __init__(self, data_, previous_hash_, adder_, difficulty_):
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
		self.hash = str(hash(self.data + self.previous_hash + self.adder + self.time + str(self.nonce)))+"x"*self.difficulty

	def __repr__(self):
		return "\n--------" + ("VALID" if self.is_valid() else "INVALID") + "--------\ndata: " + self.data + "\nprevioud hash: " + self.previous_hash + "\nhash: " + self.hash + "\nadder: " + self.adder + "\ntime added: " + self.time + "\n----------------\n"

	def is_valid(self):
		return self.hash[:self.difficulty] == "8"*self.difficulty



class Chain(object):
	"""docstring for Chain"""
	def __init__(self, difficulty_):
		self.difficulty = difficulty_
		self.block_array = [Block("origin block", None, "root", difficulty_)]

	def add_block(self, message, user):
		self.update_valid()
		if not self.block_array[-1].is_valid:
			raise ReferenceError("the previous block was invalid, please consolt the chain before adding")
		self.block_array += [Block(message, self.block_array[-1].hash, user, self.difficulty)]


	def update_valid(self):
		self.block_array[0].set_hash()
		for i in range(1, len(self.block_array)):
			self.block_array[i].previous_hash = self.block_array[i - 1].hash
			self.block_array[i].set_hash()

	def __repr__(self):
		total = ""
		for block in self.block_array:
			total += str(block)
		return total

my_chain = Chain(3)
my_chain.add_block("hello world!", "devin")
my_chain.add_block("hello mike", "mikey")

my_chain.block_array[1].data = "HAHAHA im evil :)"

my_chain.update_valid()

print my_chain



		