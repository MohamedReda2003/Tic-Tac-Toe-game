import pygame, sys
import numpy as np
import random
import time 
# import tkinter as tk
# from tkinter import messagebox
# import pdb


class TicTacToe:
    pygame.init()
    WIDTH = 600
    HEIGHT = 600
    LINE_WIDTH = 15
    WIN_LINE_WIDTH = 15
    BOARD_ROWS = 3
    BOARD_COLS = 3
    SQUARE_SIZE = 200
    CIRCLE_RADIUS = 60
    CIRCLE_WIDTH = 15
    CROSS_WIDTH = 25
    SPACE = 55
    # pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()
    
    RED = (255, 0, 0)
    BG_COLOR = (20, 200, 160)
    LINE_COLOR = (23, 145, 135)
    CIRCLE_COLOR = (239, 231, 200)
    CROSS_COLOR = (66, 66, 66)
    
    screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
    pygame.display.set_caption( 'TIC TAC TOE' )
    screen.fill( BG_COLOR )
    
    board = np.zeros( (BOARD_ROWS, BOARD_COLS) )
    
    def draw_lines(self):
    	
    	pygame.draw.line( self.screen, self.LINE_COLOR, (0, self.SQUARE_SIZE), (self.WIDTH, self.SQUARE_SIZE), self.LINE_WIDTH )
    	
    	pygame.draw.line( self.screen, self.LINE_COLOR, (0, 2 * self.SQUARE_SIZE), (self.WIDTH, 2 * self.SQUARE_SIZE), self.LINE_WIDTH )
    
    	pygame.draw.line( self.screen, self.LINE_COLOR, (self.SQUARE_SIZE, 0), (self.SQUARE_SIZE, self.HEIGHT), self.LINE_WIDTH )
    
    	pygame.draw.line( self.screen, self.LINE_COLOR, (2 * self.SQUARE_SIZE, 0), (2 * self.SQUARE_SIZE, self.HEIGHT), self.LINE_WIDTH )
    
    def draw_figures(self):
    	for row in range(self.BOARD_ROWS):
    		for col in range(self.BOARD_COLS):
    			if self.board[row][col] == 2:
    				pygame.draw.circle( self.screen, self.CIRCLE_COLOR, (int( col * self.SQUARE_SIZE + self.SQUARE_SIZE//2 ), int( row * self.SQUARE_SIZE + self.SQUARE_SIZE//2 )), self.CIRCLE_RADIUS, self.CIRCLE_WIDTH )
    			elif self.board[row][col] == 1:
    				pygame.draw.line( self.screen, self.CROSS_COLOR, (col * self.SQUARE_SIZE + self.SPACE, row * self.SQUARE_SIZE + self.SQUARE_SIZE - self.SPACE), (col * self.SQUARE_SIZE + self.SQUARE_SIZE - self.SPACE, row * self.SQUARE_SIZE + self.SPACE), self.CROSS_WIDTH )	
    				pygame.draw.line( self.screen, self.CROSS_COLOR, (col * self.SQUARE_SIZE + self.SPACE, row * self.SQUARE_SIZE + self.SPACE), (col * self.SQUARE_SIZE + self.SQUARE_SIZE - self.SPACE, row * self.SQUARE_SIZE + self.SQUARE_SIZE - self.SPACE), self.CROSS_WIDTH )
    
    def mark_square(self,row, col, player):
    	self.board[row][col] = player
    
    def available_square(self,row, col):
    	return self.board[row][col] == 0
    
    def is_board_full(self):
    	for row in range(self.BOARD_ROWS):
    		for col in range(self.BOARD_COLS):
    			if self.board[row][col] == 0:
    				return False
    
    	return True
    
    def check_win(self,player):
    	for col in range(self.BOARD_COLS):
    		if self.board[0][col] == player and self.board[1][col] == player and self.board[2][col] == player:
    			self.draw_vertical_winning_line(col, player)
    			return True
    
    	for row in range(self.BOARD_ROWS):
    		if self.board[row][0] == player and self.board[row][1] == player and self.board[row][2] == player:
    			self.draw_horizontal_winning_line(row, player)
    			return True
    
    	if self.board[2][0] == player and self.board[1][1] == player and self.board[0][2] == player:
    		self.draw_asc_diagonal(player)
    		return True
    
    	if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
    		self.draw_desc_diagonal(player)
    		return True
    
    	return False
    
    def draw_vertical_winning_line(self,col, player):
    	posX = col * self.SQUARE_SIZE + self.SQUARE_SIZE//2
    
    	if player == 1:
    		color = self.CIRCLE_COLOR
    	elif player == 2:
    		color = self.CROSS_COLOR
    
    	pygame.draw.line( self.screen, color, (posX, 15), (posX, self.HEIGHT - 15), self.LINE_WIDTH )
    
    def draw_horizontal_winning_line(self,row, player):
    	posY = row * self.SQUARE_SIZE + self.SQUARE_SIZE//2
    
    	if player == 1:
    		color = self.CIRCLE_COLOR
    	elif player == 2:
    		color = self.CROSS_COLOR
    
    	pygame.draw.line( self.screen, color, (15, posY), (self.WIDTH - 15, posY), self.WIN_LINE_WIDTH )
    
    def draw_asc_diagonal(self,player):
    	if player == 1:
    		color = self.CIRCLE_COLOR
    	elif player == 2:
    		color = self.CROSS_COLOR
    
    	pygame.draw.line( self.screen, color, (15, self.HEIGHT - 15), (self.WIDTH - 15, 15), self.WIN_LINE_WIDTH )
    
    def draw_desc_diagonal(self,player):
    	if player == 1:
    		color = self.CIRCLE_COLOR
    	elif player == 2:
    		color = self.CROSS_COLOR
    
    	pygame.draw.line( self.screen, color, (15, 15), (self.WIDTH - 15, self.HEIGHT - 15), self.WIN_LINE_WIDTH )
    
    def restart(self):
    	self.screen.fill( self.BG_COLOR )
    	self.draw_lines()
    	for row in range(self.BOARD_ROWS):
    		for col in range(self.BOARD_COLS):
    			self.board[row][col] = 0
    
    def tic_tac_toe_2_players(self):
        screen.fill(self.BG_COLOR)
        self.draw_lines()
        player=1
        game_over=False
        running =True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # pygame.quit()
                    self.restart()
                    self.main_menu()
                    # sys.exit()
                    running=False
                if event.type== pygame.MOUSEBUTTONDOWN and not game_over:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]
                    clicked_row = int(mouseY // self.SQUARE_SIZE)
                    clicked_col = int(mouseX // self.SQUARE_SIZE)
                    
                    if self.available_square( clicked_row, clicked_col ):
                        self.mark_square( clicked_row, clicked_col, player )
                        if self.check_win( player ):
                            game_over=True
                        player = player % 2 + 1
                        self.draw_figures()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.restart()
                        player=1
                        game_over=False
                        
            pygame.display.update()
                    
                    
                    
      
        
      
        
      
        
      
    def tic_tac_toe_against_computer(self):
        screen.fill(self.BG_COLOR)
        self.draw_lines()
        player=1
        game_over=False
        running=True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # pygame.quit()
                    self.restart()
                    self.main_menu()
                    # sys.exit()
                    break
                
                if event.type == pygame.MOUSEBUTTONDOWN and not game_over and player%2==1:
                    mouseX =event.pos[0]
                    mouseY=event.pos[1]
                    clicked_row=int(mouseY//self.SQUARE_SIZE)
                    # print(mouseY)
                    # print(clicked_row)
                    
                    clicked_col=int(mouseX//self.SQUARE_SIZE)
                    print(f'[{clicked_row},{clicked_col}]')
                    if self.available_square(clicked_row, clicked_col):
                        self.mark_square(clicked_row, clicked_col, player)
                        if self.check_win(player):
                            game_over=True
                        player=player % 2+1
                        self.draw_figures()
                if player%2==0 and not game_over:
                    # time.sleep(1)
                    try:
                        squares=[]
                        rows=[0,1,2]
                        columns=[0,1,2]
                        for r in rows:
                            for c in columns:
                                to_click=[r,c]
                                squares.append(to_click)
                        squares_that_are_available=[]
                        for square in squares:
                            if self.available_square(square[0], square[1]):
                                squares_that_are_available.append(square)
                        print(len(squares_that_are_available))
                        chosen_square=random.choice(squares_that_are_available)
                        print(chosen_square)
                        self.mark_square(chosen_square[0], chosen_square[1],player)
                        if self.check_win(player):
                            game_over=True
                        player=player%2+1
                        self.draw_figures()
                    except :
                        pass
                    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            self.restart()
                            player=0
                            game_over=False
            pygame.display.update()
        
    
    def main_menu(self):
        buttons = [
            Button(WIDTH // 4, HEIGHT // 2 - 50, WIDTH // 2, 50, GRAY, "2 Players", self.tic_tac_toe_2_players),
            Button(WIDTH // 4, HEIGHT // 2 + 50, WIDTH // 2, 50, GRAY, "Player vs Computer", self.tic_tac_toe_against_computer),
        ]

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in buttons:
                        if button.rect.collidepoint(event.pos):
                            button.action()

            screen.fill(WHITE)
            for button in buttons:
                button.draw()

            pygame.display.flip()
            self.clock.tick(10)
            






WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
WIDTH = 600
HEIGHT = 600
TITLE = "Tic Tac Toe"
# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))



class Button:
    def __init__(self, x, y, width, height, color, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.action = action

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, BLACK)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)
        


        

# Define the two_players function
# def two_players():
    
#     tic_tac_toe = TicTacToe()
#     screen.fill(tic_tac_toe.BG_COLOR)
#     tic_tac_toe.tic_tac_toe_2_players()
    
    # Implement the game logic for two players here

# Define the player_vs_computer function
# def player_vs_computer():
#     tic_tac_toe = TicTacToe()
#     screen.fill(tic_tac_toe.BG_COLOR)
#     tic_tac_toe.tic_tac_toe_against_computer()


game=TicTacToe()
game.main_menu()





