from .variousTypes import RoomType


class Room():
	
	def __init__(self, someType):
		self.type = someType

	
	def changeType(self, someType):
		self.type = someType
