import curses

from common.variousTypes import RoomType
from common.shelter import Shelter

KEY_ESCAPE = 27


class Game():
	
	def __init__(self, address, delay, shelterSize=(30, 10), roomSize=(5, 4)):
		self.delay = delay
		self.doShow = True
		self.roomSize = roomSize
		self.shelterSize = shelterSize
		self.shelter = Shelter(shelterSize)
		self.minSizeX = shelterSize[0] * roomSize[0] + 30
		self.minSizeY = shelterSize[1] * roomSize[1] + 10
		self.mouse = {'y': None, 'x': None, 'state': None}
	
	def start(self):
		'''
		Def : Start the game by calling the curses wrapper.
		'''
		
		try:
			curses.wrapper(self.mainLoop)
		finally:
			curses.endwin()
	
	
	def dealInputs(self, screen):
		event = screen.getch()
		if event in [ord("q"), KEY_ESCAPE]:
			self.doShow = False
		if event == curses.KEY_MOUSE:
			(idd, x, y, z, bstate) = curses.getmouse()
			self.mouse['y'] = y
			self.mouse['x'] = x
			self.mouse['state'] = bstate
	
	
	def addColors(self):
		assert curses.COLORS == 256
		curses.use_default_colors()
		curses.init_pair(RoomType.unknown, 11, 236)
		curses.init_pair(RoomType.stair,   11, 255)
		curses.init_pair(RoomType.water,   11, 21)
		curses.init_pair(RoomType.kitchen, 11, 112)
		curses.init_pair(RoomType.storage, 11, 214)
		curses.init_pair(RoomType.steam,   11, 202)
	
	
	def mainLoop(self, screen):
		
		self.addColors()
		curses.noecho()
		curses.curs_set(0)
		screen.nodelay(1)
		
		screen.keypad(1) # added for test
		curses.mousemask(1) # added for test
		
		hx = self.shelterSize[0] * self.roomSize[0] + 2
		hy = self.shelterSize[1] * self.roomSize[1] + 2
			
		while self.doShow:
			
			self.dealInputs(screen)
			self.shelter.update()
			
			(dy, dx) = screen.getmaxyx()
						
			if dx >= self.minSizeX and dy >= self.minSizeY:
				
				lx = dx - hx
				ly = dy - hy
			
				win1 = curses.newwin(hy, lx,  0,  0) # character info
				win2 = curses.newwin(ly, lx, hy,  0) # something unknown
				win3 = curses.newwin(hy, hx,  0, lx) # shelter view
				win4 = curses.newwin(ly, hx, hy, lx) # shelter info
	
				windows = {win1 : self.drawCharacterInformationWindow,
					        win2 : self.drawLogWindow,
					        win3 : self.drawShelterWindow,
					        win4 : self.drawShelterInformationWindow}
			
				for win, func in windows.items():
					win.box()
					func(win)
					win.refresh()
			
			else:
				screen.addstr(0, 0, 'Please resize your terminal')
				
			curses.napms(self.delay)
	
	
	def drawCharacterInformationWindow(self, win):
		win.addstr(1, 1, 'Character information')
	
	
	def drawShelterWindow(self, win):
		for room in self.shelter.rooms:
			self.drawRoom(win, room)
	
	
	def drawShelterInformationWindow(self, win):
		win.addstr(1, 1, 'Shelter information')
	
	
	def drawLogWindow(self, win):
		win.addstr(1, 1, 'Log')
		mouseStr = 'mouse: {} {} {}'.format(self.mouse['x'], self.mouse['y'], self.mouse['state'])
		win.addstr(2, 1, mouseStr)
	
	
	def drawRoom(self, win, room):
		offx = room.position[0] * self.roomSize[0] + 1
		offy = room.position[1] * self.roomSize[1] + 1
		for i in range(self.roomSize[0]):
			for j in range(self.roomSize[1]):
				win.addstr(j + offy, i + offx, ' ', curses.color_pair(room.type))
			
	
