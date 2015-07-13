from random import choice # TODO remove this when not needed anymore

from common.variousTypes import RoomType
from .room import Room


class Shelter():

	def __init__(self, size):
		self.size = size
		self.rooms = []
		for i in range(self.size[0]):
			for j in range(self.size[1]):
				room = Room((i, j))
				self.rooms.append(room)
	
	def update(self):
		for room in self.rooms:
			if room.position[1] == 0:
				room.changeType(RoomType.water)
			else:
				room.changeType(choice(range(2, 7))) # TODO remove this, just a test
