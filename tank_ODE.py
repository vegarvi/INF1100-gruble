from matplotlib.pylab import *

class Tank:
	def __init__(self,r,R,g=9.81):
		self.r = r
		self.R = R
		self.g = g
	
	def dh(self,h,t):
		r, R, g = self.r, self.R, self.g
		return -(float(r)/R)**2*sqrt(2*g*h)

	def set_h0(self,h0):
		self.h0 = h0
	
	def __call__(self,t):
		n = len(t)
		h = zeros(n)
		h[0] = self.h0
		for i in range(n-1):
			dt = t[i+1]-t[i]
			h[i+1] = h[i] + dt*self.dh(h[i],t[i])
		return h
			

dt = 0.1
T = 100
N = int(T/dt)
t = linspace(0,T,N)

r = 0.01
R = 0.2
h0 = 1

T = Tank(r,R)
T.set_h0(h0)
h = T(t)
plot(t,h)
show()

