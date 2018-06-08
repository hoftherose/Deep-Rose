import chess, chess.pgn
import os
import board as chessboard
import keyboard as kb
import matplotlib.pyplot as plt
import time
import sysconfig
dist_suffix = sysconfig.get_config_var("SO")
import sys
sys.path.insert(0,'./')
import play
import random


p = "Desktop/Chess/images/bpawn.png"
r = "Desktop/Chess/images/brook.png"
n = "Desktop/Chess/images/bknight.png"
b = "Desktop/Chess/images/bbishop.png"
q = "Desktop/Chess/images/bqueen.png"
k = "Desktop/Chess/images/bking.png"
P = "Desktop/Chess/images/wpawn.png"
R = "Desktop/Chess/images/wrook.png"
N = "Desktop/Chess/images/wknight.png"
B = "Desktop/Chess/images/wbishop.png"
Q = "Desktop/Chess/images/wqueen.png"
K = "Desktop/Chess/images/wking.png"

size = 60

maxd = random.randint(1, 2)
secs = random.random()
func = play.get_model_from_pickle('model.pickle')
#playerA = play.Human()
#playerA = play.Sunfish(secs=secs)
#playerA = play.Computer(func, maxd=maxd)
playerA = play.Sunfish(secs=secs)
playerB = play.Computer(func, maxd=maxd)
turn = True
gn_current = chess.pgn.Game()

def choose_move():
	global turn,playerA,playerB,gn_current
	if turn:
		gn_current = playerA.move(gn_current)
	else:
		gn_current = playerB.move(gn_current)
	turn = not(turn)
	
def run_game():
	choose_move()				
if __name__ == '__main__':
	fptr = open('output.txt', 'w')
	chessboard.draw_board1(gn_current.board())
	while not(gn_current.board().is_checkmate()):
		run_game()
		chessboard.draw_board(gn_current.board())
		print(gn_current.board())
	if turn:
		print('Gana blanco')
	else:
		print('Gana negro')

	fptr.write(str(components) + '\n')

	fptr.close()



