from .variousTypes import RoomType


class Room():
	
	def __init__(self, position):
		self.position = position
		self.type = RoomType.unknown
	
	def changeType(self, someType):
		self.type = someType
