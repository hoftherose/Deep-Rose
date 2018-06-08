import DEFMap
import numpy
import sys
import os
import multiprocessing
import itertools
import random
import h5py
import chess.pgn
	

def read_games(fn):
	f = open(fn)
	while True:
		try:
			g = chess.pgn.read_game(f)
		except KeyboardInterrupt:
			raise
		except:
			print('error')
			continue
		if not g:
			break
		yield g


def bb2array(b, flip=False):
	tables = []
	for piece in range(1,7):
		for color in range(2):
			x = numpy.array([map(int,x.replace('.','0').split()) for x in str(b.pieces(piece,flip^color)).split('\n')]).flatten()
			tables.append(x)
	return tables


def parse_game(g):
	rm = {'1-0': 1, '0-1': -1, '1/2-1/2': 0}
	r = g.headers['Result']
	if r not in rm:
		print('error in results')
		return None
	y = rm[r]
	# print >> sys.stderr, 'result:', y

	# Generate all boards
	gn = g.end()

	gns = []
	moves_left = 0
	while gn:
		gns.append((moves_left, gn, gn.board().turn == 0))
		gn = gn.parent
		moves_left += 1

#	print len(gns)
#	if len(gns) < 10:
#		print g.end()

	gns.pop() # remove first position

	moves_left, gn, flip = random.choice(gns)

	b = gn.board()
	x = bb2array(b)
	b_parent = gn.parent.board()
	x_parent = bb2array(b_parent, flip=(not flip))
	if flip:
		y = -y

	# generate a random board
#	moves = list(b_parent.legal_moves)
#	move = random.choice(moves)
#	b_parent.push(move)
	defmapx,defmapy = DEFMap.DMap(b)

	#x_random = bb2array(b_parent, flip=flip)

#	if moves_left < 3:
#		print moves_left, 'moves left'
#		print 'winner:', y
#		print g.headers
#		print b
#		print 'checkmate:', g.end().board().is_checkmate()
	
	# print x
	# print x_parent
	# print x_random
	return (x, x_parent, defmapx, defmapy, moves_left, y)
	"""x_random,"""

def read_all_games(fn_in, fn_out):
	g = h5py.File(fn_out, 'w')
	X = g.create_dataset('x', (0, 12, 64), dtype='b', maxshape=(None, 12, 64), chunks=True)
	Xp = g.create_dataset('xp', (0, 12, 64), dtype='b', maxshape=(None, 12, 64), chunks=True)
	Xd = g.create_dataset('xd', (0, 64), dtype='b', maxshape=(None, 64), chunks=True)
	Xa = g.create_dataset('xa', (0, 64), dtype='b', maxshape=(None, 64), chunks=True)

	Y = g.create_dataset('y', (0,), dtype='b', maxshape=(None,), chunks=True)
	M = g.create_dataset('m', (0,), dtype='b', maxshape=(None,), chunks=True)
	size = 0
	line = 0
	for games in read_games(fn_in):
		game = parse_game(games)
#		print(game)
		if game is None:
			print('failed')
			continue
		else:
			print('success')
		x, x_parent, x_def, x_att, moves_left, y = game
		X.append(x)
		Xp.append(x_parent)
		Xd.append(x_def)
		Xa.append(x_att)
		Y.append(y)
		M.append(moves_left)
		line += 1
	print(lines)
	[d.resize(size=line, axis=0) for d in (X, Xp, Xd, Xa, Y, M)]
	print('finished')
	g.close()

def read_all_games_2(a):
	return read_all_games(*a)

def parse_dir():
	files = []
	d = './ChessData'
	for fn_in in os.listdir(d):
		if not fn_in.endswith('.pgn'):
			continue
		fn_in = os.path.join(d, fn_in)
		fn_out = fn_in.replace('.pgn', 's.hdf5')
		if not os.path.exists(fn_out):
			files.append((fn_in, fn_out))
	pool = multiprocessing.Pool()
	pool.map(read_all_games_2, files)


if __name__ == '__main__':
	parse_dir()
