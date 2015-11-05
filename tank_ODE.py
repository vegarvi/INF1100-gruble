from matplotlib.pylab import *

class Tank:
	def __init__(self,r,R,g=9.81):
		self.r = r
		self.R = R
		self.g = g
	
	def dh(self,h,t):
		r, R, g = self.r, self.R, self.g
		if h>0:
			return -(float(r)/R)**2*sqrt(2*g*h)
		else:
			return 0

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


	def h_exact(self,t):
		h0,g,r,R = self.h0, self.g, self.r, self.R
		tmax = 2*sqrt(h0)/((r/R)**2*sqrt(2*g))
		return (t <= tmax)*0.25*(2*sqrt(h0) - (r/R)**2*sqrt(2*g)*t)**2

dt = 0.1
T = 200
N = int(T/dt)
t = linspace(0,T,N)

r = 0.01
R = 0.2
h0 = 1

T = Tank(r,R)
T.set_h0(h0)
h = T(t)
plot(t,h,t,T.h_exact(t))
show()

