import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import chess

P = img.imread("./images/wpawn.png")
R = img.imread("./images/wrook.png")
N = img.imread("./images/wknight.png")
B = img.imread("./images/wbishop.png")
Q = img.imread("./images/wqueen.png")
K = img.imread("./images/wking.png")
p = img.imread("./images/bpawn.png")
r = img.imread("./images/brook.png")
n = img.imread("./images/bknight.png")
b = img.imread("./images/bbishop.png")
q = img.imread("./images/bqueen.png")
k = img.imread("./images/bking.png")
empty = img.imread("./images/empty.png")
boardimg = img.imread('./images/chessb.jpg')
mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
table = []

def draw_board(board):
	global p,r,n,b,q,k,P,R,N,B,Q,K,table,boardimg
	letter_piece = {"p":p,"r":r,"n":n,"b":b,"q":q,"k":k,"P":P,"R":R,"N":N,"B":B,"Q":Q,"K":K,".":empty}
	l = str(board)
	iter_board = [x.split() for x in l.split('\n')]
	for row in range(8):
		for col in range(8):
			piece = letter_piece[iter_board[col][row]]
			table[row*8+col].set_data(piece[::-1])
	plt.pause(.1)
	plt.draw()

def draw_board1(board):
	global p,r,n,b,q,k,P,R,N,B,Q,K,table,boardimg
	plt.ion()
	letter_piece = {"p":p,"r":r,"n":n,"b":b,"q":q,"k":k,"P":P,"R":R,"N":N,"B":B,"Q":Q,"K":K,".":empty}
	fig = plt.imshow(boardimg[::])
	fig.axes.get_xaxis().set_visible(False)
	fig.axes.get_yaxis().set_visible(False)
	l = str(board)
	iter_board = [x.split() for x in l.split('\n')]
	for row in range(8):
		for col in range(8):
			piece = letter_piece[iter_board[col][row]]
			topx = (86+(7-row)*50)
			topy = (92+(7-col)*50)
			extent = topx,topx-50,topy,topy-50
			tbfig = plt.imshow(piece[::-1],extent = extent)
			tbfig.axes.get_xaxis().set_visible(False)
			tbfig.axes.get_yaxis().set_visible(False)
			table.append(tbfig)
	plt.xlim(0,478)
	plt.ylim(0,480)
	plt.show()
	
"""
def draw_piece(row,col,piece):
	global size
	topx = (86+row*50)
	topy = (92+col*50)
	extent = topx,topx-50,topy,topy-50
	fig = plt.imshow(piece[::-1],extent = extent)
	fig.axes.get_xaxis().set_visible(False)
	fig.axes.get_yaxis().set_visible(False)


I = img
fog, ax = plt.subplots()
im = x.imshow('img.png')

for i in range:
	plt.pause(.3)
	im.set_data(img)
	plt.draw()"""
