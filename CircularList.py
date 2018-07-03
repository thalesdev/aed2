#encoding:utf-8

class CircularList:
	def __init__(self, pos_head, arrangement):
		self.__head = pos_head
		self.__arrangement = arrangement
		self.__list_index = arrangement.newList()
		self.__size = 0
		self.__tail = pos_head
		self.__end = pos_head
		if (self.__arrangement.size()-1) < pos_head and pos_head < 0:
			raise Exception("Posição inicial invalida.")
		if (self.__arrangement.memory()[pos_head] is not None):
			raise Exception("Posição já está ocupada.")
	def head(self):
		return self.__head
	def tail(self):
		return self.__tail
	def pos_end(self):
		return self.__end
	def set_pos_end(self, pos):
		self.__end = pos
	def set_tail(self, tail):
		self.__tail = tail
	def arrangement(self):
		return self.__arrangement
	def push_back(self, item):
		return self.__push(item, "backward")
	def push_foward(self, item):
		return self.__push(item, "forward")
	def push_center(self, item):
		return self.__push(item, "center")
	def __push(self , item , direction="backward"):
		tail = self.tail()
		head = self.head()
		ag_pos  = (self.arrangement().size()-1)
		if direction == "backward":
			dp = tail - head
			if self.arrangement().memory()[tail] is not None:
					raise Exception("Não há mais espaço disponivel.")
			self.set_pos_end(tail)
			if dp >= 0:
				if tail < ag_pos:
					self.arrangement().memory()[tail] = item
					tail+=1
					self.set_tail(tail)
				elif tail == ag_pos:
					self.arrangement().memory()[tail] = item
					if self.arrangement().memory()[0] is None:
						self.set_tail(0)
			else:
				if  head-(tail+1) > 0:
					self.arrangement().memory()[tail] = item
					self.set_tail(tail+1)
				elif head==(tail+1):
					self.arrangement().memory()[tail] = item
	
	def search(self, data):
		dp = self.pos_end() - self.head()
		if dp>0:
			for j,value in enumerate(self.arrangement().memory()[self.head():self.tail()]):
				if value == data:
					return j
		else:
			for j,value in enumerate(self.arrangement().memory()[self.head():]):
				if value == data:
					return j
			for j,value in enumerate(self.arrangement().memory()[:self.tail()]):
				if value == data:
					return (self.arrangement().size()-1)-self.head()+j
		raise Exception("Elemento não encontrado na lista.")

	def __remove(self, index):
		dp = self.pos_end() - self.head()
		if dp>=0 or (dp<0 and self.pos_end() >= index <= self.head() ):
			for j in range(index, self.pos_end()):
				self.arrangement().memory()[j] = self.arrangement().memory()[j+1]
			self.arrangement().memory()[self.pos_end()] = None
		else:
			for j in range(index, self.arrangement().size()-1):
				self.arrangement().memory()[j] = self.arrangement().memory()[j+1]
			self.arrangement().memory()[self.arrangement().size()-1] = None
			if self.pos_end() > 0:
				self.arrangement().memory()[self.arrangement().size()-1]  = self.arrangement().memory()[0]
			for j in range(0, self.tail()):
				self.arrangement().memory()[j] = self.arrangement().memory()[j+1]
		self.set_pos_end(self.pos_end()-1 if self.pos_end() > 0 else self.arrangement().size()-1)
		self.set_tail(self.tail()-1 if self.tail() > 0 else self.arrangement().size()-1)
	def __parse_id(self, id):
		index = id
		index = index+self.head() if (index+self.head())<=(self.arrangement().size()-1) else (index+self.head())-(self.arrangement().size()-1)
		return index
	def remove(self, data):
		index = self.__parse_id(self.search(data))
		self.__remove(index) 
	def remove_by_id(self, index):
		self.__remove(self.__parse_id(index)) 
	def __str__(self):
		dp = self.tail() - self.head()
		if dp>=0:
			_list = self.__arrangement.memory()[self.head():self.tail()]
		else:
			_list_1 = self.__arrangement.memory()[self.head():]
			_list_2 = self.__arrangement.memory()[:self.tail()+1 if dp ==-1 else self.tail()]
			_list = _list_1+_list_2
		return "Lista {} <{}>".format(self.__list_index,str(_list))



class Arrangement:
	def __init__(self, size):
		self.__list = [None]*size
		self.__size = size
		self.__lists = 0
	def newList(self):
		c = self.get_list_counter()
		self.set_list_counter(c+1)
		return c+1
	def size(self):
		return self.__size
	def insert(self,index, node):
		self.__list[index] = node
	def memory(self):
		return self.__list
	def __str__(self):
		return "Arranjo <{}>".format(str(self.__list))
	def get_list_counter(self):
		return self.__lists
	def set_list_counter(self, n):
		self.__lists = n
		

if __name__ == "__main__":
	arranjo = Arrangement(20)
	lista_circular = CircularList(15,arranjo)
	for j in range(0,8):
		lista_circular.push_back(j)

	print(lista_circular)
	print(arranjo)
	lista_circular.remove_by_id(1)
	print(lista_circular)
	print(arranjo)

