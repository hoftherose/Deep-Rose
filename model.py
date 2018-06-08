import keras
#12 boards (pieces) + 2 Def maps = 14*64 = 
from keras.models import Sequential
from keras.layers import Dense
import sys
import dill
from sklearn.cross_validation import train_test_split
import os
import h5py
sys.path.insert(0,'../')
import parse_game
import numpy
# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
dill.dumps(Sequential)
# load pima indians dataset

def load_data(dir='./ChessData'):
	for fn in os.listdir(dir):
		if not fn.endswith('.hdf5'):
			continue

		fn = os.path.join(dir, fn)
		try:
			yield h5py.File(fn, 'r')
		except:
			print 'could not read', fn

def get_data(series=['x', 'xp', 'xd', 'xa']):
	data = [[] for s in series]
	for f in load_data():
		try:
			for i, s in enumerate(series):
				data[i].append(f[s].value)
		except:
			print 'failed reading from', f
			raise
	def stack(vectors):
		if len(vectors[0].shape) > 1:
			return numpy.vstack(vectors)
		else:
			return numpy.hstack(vectors)
	data = [stack(d) for d in data]

#	test_size = 10000.0 / len(data[0])
	test_size = 0.25
	print 'Splitting', len(data[0]), 'entries into train/test set'
	data = train_test_split(*data, test_size=test_size)

	print data[0].shape[0], 'train set', data[1].shape[0], 'test set'
	return data

dataset = get_data()
odataset = get_data(['y'])
Xtrain = [numpy.concatenate([dataset[x][i].flatten() for x in range(0,8,2)]) for i in range(len(dataset[0]))]
Xtest = [numpy.concatenate([dataset[x][i].flatten() for x in range(1,8,2)]) for i in range(len(dataset[1]))]

# split into input (X) and output (Y) variables
X = numpy.array([numpy.concatenate([i.flatten() for i in x]) for x in Xtrain])
Y = numpy.array(odataset[0])
# create model
model = Sequential()
model.add(Dense(200, input_dim=1664, init='uniform', activation='relu'))
model.add(Dense(200, init='uniform', activation='relu'))
#model.add(Dense(400, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X, Y, epochs=100, batch_size=1000,  verbose=2)
# calculate predictions
predictions = model.predict(X)
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
print(predictions)
