#gameplan: solve, valid, find_empty, startmenu, gameloop, settings
import pygame
import random

b1 = [
[0, 0, 0, 2, 6, 0, 7, 0, 1],
[6, 8, 0, 0, 7, 0, 0, 9, 0],
[1, 9, 0, 0, 0, 4, 5, 0, 0],
[8, 2, 0, 1, 0, 0, 0, 4, 0],
[0, 0, 4, 6, 0, 2, 9, 0, 0],
[0, 5, 0, 0, 0, 3, 0, 2, 8],
[0, 0, 9, 3, 0, 0, 0, 7, 4],
[0, 4, 0, 0, 5, 0, 0, 3, 6],
[7, 0, 3, 0, 1, 8, 0, 0, 0]
]

b2 = [
[1, 0, 0, 4, 8, 9, 0, 0, 6],
[7, 3, 0, 0, 5, 0, 0, 4, 0],
[4, 6, 0, 0, 0, 1, 2, 9, 5],
[3, 8, 7, 1, 2, 0, 6, 0, 0],
[5, 0, 1, 7, 0, 3, 0, 0, 8],
[0, 4, 6, 0, 9, 5, 7, 1, 0],
[9, 1, 4, 6, 0, 0, 0, 8, 0],
[0, 2, 0, 0, 4, 0, 0, 3, 7],
[8, 0, 3, 5, 1, 2, 0, 0, 4]
]

b3 = [
    [5, 3, 0, 0, 7, 0, 9, 0, 2],
    [6, 0, 2, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 2, 0, 6, 0],
    [8, 0, 9, 0, 6, 0, 4, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 8, 0, 6],
    [0, 6, 0, 5, 0, 7, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

b4 = [
[0, 2, 0, 0, 0, 4, 3, 0, 0],
[9, 0, 0, 0, 2, 0, 0, 0, 8],
[0, 0, 0, 6, 0, 9, 0, 5, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 7, 2, 5, 0, 3, 6, 8, 0],
[6, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 8, 0, 2, 0, 5, 0, 0, 0],
[1, 0, 0, 0, 9, 0, 0, 0, 3],
[0, 0, 9, 8, 0, 0, 0, 6, 7]
]

b5 = [
[2, 0, 6, 3, 0, 4, 0, 5, 0],
[8, 0, 4, 0, 6, 2, 0, 0, 3],
[0, 1, 3, 8, 0, 5, 2, 0, 0],
[0, 0, 0, 0, 2, 0, 3, 9, 0],
[5, 0, 7, 4, 0, 0, 6, 2, 1],
[0, 3, 2, 0, 0, 6, 0, 0, 0],
[0, 2, 0, 0, 0, 9, 1, 4, 0],
[6, 0, 1, 2, 5, 0, 8, 0, 9],
[0, 0, 0, 0, 0, 1, 0, 0, 2]
]
boards = [b1, b2, b3, b4, b5]
board = []
def reset_board():
    global board, strikes
    strikes = 0
    index = random.randint(0, len(boards)-1)
    board = [i[:] for i in boards[index]]
    if len(boards) > 1:
        del boards[index]

def valid(bo, num, pos):
	#check horizontal
    if num in bo[pos[0]]:
    	return False
    #check vertical
    for i in range(len(bo)):
    	if num == bo[i][pos[1]]:
    		return False
    #check box
    br, bc = pos[0] // 3, pos[1] // 3
    for i in range(3):
    	for j in range(3):
    		if bo[br*3+i][bc*3+j] == num:
    			return False
    return True


def find_empty(bo):
	for i in range(len(bo)):
		for j in range(9):
			if bo[i][j] == 0:
				return (i, j)
	return False

def solve(bo, solving):
	keys = pygame.key.get_pressed()
	if not find_empty(bo):
		return True
	pos = find_empty(bo)
	for a in range(1, 10):
		if solving:
			checking_animation(a, pos)
			if keys[pygame.K_s]:
				solving = False
		if valid(bo, a, pos):
			bo[pos[0]][pos[1]] = a
			if solving:
				solving_animation(pos)

			if solve(bo, solving):
				return True
			bo[pos[0]][pos[1]] = 0
			if solving:
				back_animation(pos)
	
	return False

def checking_animation(num, pos):
	global squares
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	font = pygame.font.Font('freesansbold.ttf', 30)
	win.fill(grey)
	draw_grid()
	for i in squares:
		if i.gridpos == pos:
			text = font.render(str(num), True, white)
			win.blit(text, (i.tx, i.ty))
	print_board(win, ww, board)
	pygame.time.delay(60)
	pygame.display.update()
			

def back_animation(pos):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	hl = pygame.Surface((60, 60))
	hl.fill(red)
	hl.set_alpha(50)
	for i in squares:
		if i.gridpos == pos:
			win.blit(hl, (i.x, i.y))
	pygame.time.delay(80)
	pygame.display.update()

def solving_animation(pos):
	global squares
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	
	win.fill(grey)
	draw_grid()
	hl = pygame.Surface((60, 60))
	hl.fill(green)
	hl.set_alpha(50)
	for i in squares:
		if i.gridpos == pos:
			win.blit(hl, (i.x, i.y))
	print_board(win, ww, board)
	pygame.time.delay(250)
	pygame.display.update()

#pygame stuff

pygame.init()
ww = 540
win = pygame.display.set_mode((ww, ww))
pygame.display.set_caption('Sudoku Solver')
font = pygame.font.Font('freesansbold.ttf', 32)
f2 = pygame.font.Font('freesansbold.ttf', 10)

white = (255, 255, 255)
grey = (20, 20, 20)
black = (0, 0, 0)
green = (0, 200, 0)
red = (200, 0, 0)

def draw_smenu(win, ww, mp):
	win.fill(grey)
	title = font.render('Sudoku Solver', True, white)
	win.blit(title, (ww//4+22, ww//4))

	pygame.draw.rect(win, white, (ww//2-50, ww//2, 100, 25), 2)
	b1t = f2.render('New Game', True, white)
	win.blit(b1t, (ww//2-50+25, ww//2+9))
	
	pygame.draw.rect(win, white, (ww//2-50, ww//2+50, 100, 25), 2)
	b2t = f2.render('Continue Game', True, white)
	win.blit(b2t, (ww//2-50+15, ww//2+59))

	pygame.draw.rect(win, white, (ww//2-50, ww//2+100, 100, 25), 2)
	b3t = f2.render('Exit', True, white)
	win.blit(b3t, (ww//2-9, ww//2+109))

	wtl = pygame.Surface((100, 25))
	wtl.fill(white)
	wtl.set_alpha(50)
	if ww//2-50 <= mp[0] <= ww//2-50+100 and ww//2 <= mp[1] <= ww//2+25:
		win.blit(wtl, (ww//2-50, ww//2))

	if ww//2-50 <= mp[0] <= ww//2-50+100 and ww//2+50 <= mp[1] <= ww//2+75:
		win.blit(wtl, (ww//2-50, ww//2+50))

	if ww//2-50 <= mp[0] <= ww//2-50+100 and ww//2+100 <= mp[1] <= ww//2+125:
		win.blit(wtl, (ww//2-50, ww//2+100))


	pygame.display.update()

def startmenu(win, ww):
	run = True
	while run:
		mouse_pos = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if ww//2-50 <= mouse_pos[0] <= ww//2-50+100 and ww//2+50 <= mouse_pos[1] <= ww//2+75:
					gameloop()
				if ww//2-50 <= mouse_pos[0] <= ww//2-50+100 and ww//2 <= mouse_pos[1] <= ww//2+25:
					reset_board()
					gameloop()
				if ww//2-50 <= mouse_pos[0] <= ww//2-50+100 and ww//2+100 <= mouse_pos[1] <= ww//2+125:
					pygame.quit()
					quit()
		
		draw_smenu(win, ww, mouse_pos)
		
class square():
	def __init__(self, x, y, num):
		self.x = x
		self.y = y
		self.l = 60
		self.gridpos = (self.y//self.l, self.x//self.l)
		self.num = num
		self.tx = self.x+22
		self.ty = self.y+18

	def is_cursor(self):
		mp = pygame.mouse.get_pos()
		if self.x <= mp[0] <= self.x+self.l and self.y <= mp[1] <= self.y+self.l:
			return True
	
	def is_clicked(self):
		mp = pygame.mouse.get_pos()
		if self.x <= mp[0] <= self.x+self.l and self.y <= mp[1] <= self.y+self.l:
			if pygame.mouse.get_pressed()[0]:
				return True

squares = [] #list of squares on the grid
strikes = 0 #number of incorrect guesses

def update_squares(board):
	global squares
	squares = [square(j*60, i*60, board[i][j]) for i in range(9) for j in range(9)]
	
def print_board(win, ww, board):
	update_squares(board)
	global squares
	font = pygame.font.Font('freesansbold.ttf', 30)
	for i in squares:
		if i.num != 0:
			text = font.render(str(i.num), True, white)
			win.blit(text, (i.tx, i.ty))
	
def draw_grid():
	for i in range(1, ww//60):
		pygame.draw.line(win, white, (i*60, 0), (i*60, ww))
		if i % 3 == 0:
			pygame.draw.line(win, white, (i*60, 0), (i*60, ww), 4)
	for i in range(1, ww//60):
		pygame.draw.line(win, white, (0, i*60), (ww, i*60))
		if i % 3 == 0:
			pygame.draw.line(win, white, (0, i*60), (ww, i*60), 4)

def correct(pos):
	hl = pygame.Surface((60, 60))
	hl.fill(green)
	hl.set_alpha(40)
	win.blit(hl, (pos[0], pos[1]))
	print_board(win, ww, board)
	draw_grid()
	pygame.display.update()
	pygame.time.delay(150)

def incorrect(pos):
	global strikes
	hl = pygame.Surface((60, 60))
	hl.fill(red)
	hl.set_alpha(40)
	win.blit(hl, (pos[0], pos[1]))
	print_board(win, ww, board)
	draw_grid()
	crosses()
	pygame.display.update()
	pygame.time.delay(150)
	strikes += 1


def input_num(selected, keys, bosolved):
	for i in squares:
		if (i.x, i.y, i.l, i.l) == selected[1] and i.num == 0:
			if keys[pygame.K_1]:
				if bosolved[i.gridpos[0]][i.gridpos[1]] == 1:
					i.num = 1
					board[i.gridpos[0]][i.gridpos[1]] = 1
					correct((i.x, i.y))
				else:
					incorrect((i.x, i.y))
			elif keys[pygame.K_2]:
				if bosolved[i.gridpos[0]][i.gridpos[1]] == 2:
					i.num = 2
					board[i.gridpos[0]][i.gridpos[1]] = 2
					correct((i.x, i.y))
				else:
					incorrect((i.x, i.y))
			elif keys[pygame.K_3]:
				if bosolved[i.gridpos[0]][i.gridpos[1]] == 3:
					i.num = 3
					board[i.gridpos[0]][i.gridpos[1]] = 3
					correct((i.x, i.y))
				else:
					incorrect((i.x, i.y))
			elif keys[pygame.K_4]:
				if bosolved[i.gridpos[0]][i.gridpos[1]] == 4:
					i.num = 4
					board[i.gridpos[0]][i.gridpos[1]] = 4
					correct((i.x, i.y))
				else:
					incorrect((i.x, i.y))
			elif keys[pygame.K_5]:
				if bosolved[i.gridpos[0]][i.gridpos[1]] == 5:
					i.num = 5
					board[i.gridpos[0]][i.gridpos[1]] = 5
					correct((i.x, i.y))
				else:
					incorrect((i.x, i.y))
			elif keys[pygame.K_6]:
				if bosolved[i.gridpos[0]][i.gridpos[1]] == 6:
					i.num = 6
					board[i.gridpos[0]][i.gridpos[1]] = 6
					correct((i.x, i.y))
				else:
					incorrect((i.x, i.y))
			if keys[pygame.K_7]:
				if bosolved[i.gridpos[0]][i.gridpos[1]] == 7:
					i.num = 7
					board[i.gridpos[0]][i.gridpos[1]] = 7
					correct((i.x, i.y))
				else:
					incorrect((i.x, i.y))
			elif keys[pygame.K_8]:
				if bosolved[i.gridpos[0]][i.gridpos[1]] == 8:
					i.num = 8
					board[i.gridpos[0]][i.gridpos[1]] = 8
					correct((i.x, i.y))
				else:
					incorrect((i.x, i.y))
			elif keys[pygame.K_9]:
				if bosolved[i.gridpos[0]][i.gridpos[1]] == 9:
					i.num = 9
					board[i.gridpos[0]][i.gridpos[1]] = 9
					correct((i.x, i.y))
				else:
					incorrect((i.x, i.y))


def crosses():
	global strikes
	for s in range(strikes):
		pygame.draw.line(win, red, (ww-s*20-10, ww-15), (ww-s*20-10-10, ww-5))
		pygame.draw.line(win, red, (ww-s*20-10, ww-5), (ww-s*20-10-10, ww-15))


def gameloop():
	global squares
	selected = [False, ()]
	run = True
	
	bosolved = [i[:] for i in board]
	solve(bosolved, False)

	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		win.fill(grey)

		hl = pygame.Surface((60, 60))
		hl.set_alpha(40)

		
		#input
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			solve(board, True)
		if keys[pygame.K_s]:
			solve(board, False)
		if keys[pygame.K_ESCAPE]:
			run = False
		for i in squares:
			if i.is_cursor():
				hl.fill(white)
				win.blit(hl, (i.x, i.y))
			if i.is_clicked():
				hl.fill(black)
				win.blit(hl, (i.x, i.y))
				selected = [True, (i.x, i.y, i.l, i.l)]
				

		if selected[0]:
			pygame.draw.rect(win, white, (selected[1]), 6)

		input_num(selected, keys, bosolved)

		#printboard
		print_board(win, ww, board)

		#draw grid
		draw_grid()

		#Xs for incorrect
		crosses()

		pygame.display.update()


startmenu(win, ww)