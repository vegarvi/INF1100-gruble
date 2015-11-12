from matplotlib.pylab import *
from numpy import random
import time

class Random_walk:
	def __init__(self, start, finish, N=9, M=9, sleep=0.2):
		self.start = start
		self.finish = finish
		self.N = N
		self.M = M
		self.sleep = sleep
		self.image = np.zeros(N*M).reshape((N,M))

		self.idx = list(start)

		self.image[start[0],start[1]] = 1
		self.image[finish[0],finish[1]] = 2

	def move(self):
		var = random.choice((1,0))  # x=0,y=1
		di = random.choice((-1,1))  # direction of movement
		
		if self.idx[var] == 0 and di == -1:
			self.move()
		elif (var == 0 and self.idx[0] == self.N-1 and di == 1):
			self.move()
		elif (var == 1 and self.idx[1] == self.M-1 and di == 1):
			self.move()

		else:
			print self.idx
			self.image[self.idx[0],self.idx[1]] = 0
			self.idx[var] = self.idx[var] + di
			self.image[self.idx[0],self.idx[1]] = 1
		
	
	def walk(self, maxtime=100):
		t1 = time.time()
		ion()
		mat = imshow(self.image)
		draw()
		time.sleep(3*self.sleep)
		while self.idx != self.finish and time.time()-t1 < maxtime:
			self.move()
			mat.set_data(self.image)
			draw()
			time.sleep(self.sleep)
		
		for i in range(10):
			self.image[self.finish[0],self.finish[1]] *= -1
			mat.set_data(self.image)
			draw()
			time.sleep(0.2)

N = 5
M = 15
start = [3,10]
finish = [3,6]
R = Random_walk(start,finish,N,M,sleep=0.)
R.walk()

