from .variousTypes import RoomType


class Room():
	
	def __init__(self, someType, position):
		self.type = someType
		self.position = position

	
	def changeType(self, someType):
		self.type = someType
