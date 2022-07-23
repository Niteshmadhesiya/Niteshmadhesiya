import matplotlib.pyplot as plt
import numpy as np

#create data of complex numbers
data=np.array([1+2j,2-4j,-2j,-4,4+1j,3+8j,-2-6j,5j])

#extract real part using numpy array

x=data.real
#extract imaginary part using numpy array
y=data.imag

#plot the complex numbers
plt.plot(x,y)
plt.ylabel('Imaginary')
plt.xlabel('Real')
plt.show()
