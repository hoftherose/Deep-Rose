Deep-Rose is a school project which tries to improve on the project of deep-pink (information below)
The project didn't succed, for now I was only able to implement a simple chess board to visualize results but have yet to make my own trained model to test against the two.

The different types of players are: Human, deep-pink, sunfish, and outside model (where I would test the models I made).

deep-pink
=========
* [deep-pink](https://github.com/erikbern/deep-pink): `git clone https://github.com/erikbern/deep-pink; most of the code is also included in this prject`
(http://erikbern.com/2014/11/29/deep-learning-for-chess/)

Dependencies
============

* [Theano](https://github.com/Theano/Theano): `git clone https://github.com/Theano/Theano; cd Theano; python setup.py install`
* [Sunfish](https://github.com/thomasahle/sunfish): `git clone https://github.com/thomasahle/sunfish`. You need to add it to PYTHONPATH to be able to play
* [python-chess](https://pypi.python.org/pypi/python-chess) `pip install python-chess`
* [scikit-learn](http://scikit-learn.org/stable/install.html) (only needed for training)
* [h5py](http://www.h5py.org/): can be installed using `apt-get install python-hdf5` or `pip install hdf5` (only needed for training)
