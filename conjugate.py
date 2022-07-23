#B. Displaying the conjugate of Two numbers.
#source code

#importing numpy
import numpy as np

c1=complex(input("enter first no"))
con=np.conj(c1)
print("conjugate of number is ", con)

in_complex2=5-8j
out_complex2=np.conj(in_complex2)
print("Output conjugated complex number of 5-8j: ",out_complex2)
