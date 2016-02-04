from random import choice # TODO remove this when not needed anymore

from common.variousTypes import RoomType
from .room import Room
import numpy as np

class Shelter():

	def __init__(self, size):
		self.size = size
		self.rooms = np.empty((self.size[0] self.size[1]), dtype=np.object)
	
	def update(self, roomTypes):
		for key, roomType in roomTypes.items():
			(i, j) = [int(a) for a in key.split(',')]
			self.rooms[i][j] = Room(roomType)
