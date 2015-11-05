import numpy as np
from matplotlib.pylab import plot,show
import time

def trapezoidal_eff(f,a,x,n):
	h = (x-a)/float(n)
	I = 0.5*(f(a)+f(x))
	X = np.linspace(a,x,n+1)
	I += np.sum(f(X[1:-1]))
	I *= h
	return I

def trapezoidal(f,a,x,n):
	h = (x-a)/float(n)
	I = 0.5*f(a)
	for i in range(1,n):
		I += f(a + i*h)
	I += 0.5*f(x)
	I *= h
	return I


class Integral:
	def __init__(self,f,a,n=100):
		self.f, self.a, self.n = f, a, n
	
	def __call__(self,x):
		f, a, n = self.f, self.a, self.n
		if isinstance(x,np.ndarray):
			m = len(x)
			I = np.zeros(m)			
			I[0] = trapezoidal(f,a,x[0],n)
			for i in range(m-1):
				I[i+1] = I[i] + trapezoidal(f,x[i],x[i+1],n)
			return I
		else:
			return trapezoidal(f,a,x,n)

f = lambda x: np.exp(x)
def time_saved():
	n = 2000
	I = Integral(f,0,n)
	x = np.linspace(0,2*np.pi,10)
	t1 = time.time()
	for xi in x:
		result = I(xi)
	t2 = time.time()
	result2 = I(x)
	t3 = time.time()
	print 'Integral, t=%g' %(t2-t1)
	print 'Integral_eff, t=%g' %(t3-t2)

time_saved()

def error():
	E = lambda x: np.exp(x) - 1

	for n in [10,20,40,80,160]:
		I = Integral(f,0,n)
		x = np.linspace(0,2*np.pi,201)
		t1 = time.time()
		F = I(x)
		print 'time elapsed: %g' %(time.time()-t1)
		print 'n = %d, error=%g' %(n,abs(F[-1]-E(x[-1])))

	plot(x,F,x,E(x))
	show()

