import chess
import numpy
def DMap(board):
	X = [-DValue(board,x,0) for x in range(64)]
	Y = [-DValue(board,x,1) for x in range(64)]
	return X,Y

def DValue(board,a,side):
	attackers = board.attackers(side,a)
	points = 0
	iter_b = [x.split() for x in str(board).split('\n')]
	iter_att = numpy.array([map(int,x.replace('.','0').split()) for x in str(attackers).split('\n')])
	for x in range(8):
		for y in range(8):
			if iter_att[x][y]:
				points+=getpoints(iter_b[x][y])
	return points

def getpoints(piece):
	points_dic = {'p':100,'k':60000,'q':929,'r':479,'n':280,'b':320}
	return points_dic[piece.lower()]
			
b = chess.Board()
x,y = DMap(b)

