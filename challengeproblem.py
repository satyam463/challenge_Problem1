import numpy as np
import matplotlib.pyplot as plt
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

a=6
b=3
A=np.array([a+b,a-b])
print(A)
B=np.array([a-b,a+b])
print(B)
P=(1/(a+b))*(np.column_stack((B,A))@np.array([a,b]).T)
print(P)
Q=(1/(a-b))*(np.column_stack((B,A))@np.array([a,-b]).T)
print(Q)
x_AB = line_gen(A,B)
x_AP=line_gen(A,P)
x_PB=line_gen(P,B)
x_QB=line_gen(Q,B)
#x_QA = line_gen(Q,A)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_AP[0,:],x_AP[1,:],label='$AP$')
plt.plot(x_PB[0,:],x_PB[1,:],label='$PB$')
plt.plot(x_QB[0,:],x_QB[1,:],label='$PB$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 - 0.01), A[1] * (1 - 0.1) , 'A')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 - 0.01), P[1] * (1 - 0.1) , 'P')
plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0] * (1 - 0.01), Q[1] * (1 - 0.1) , 'Q')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.1), B[1] * (1) , 'B')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.show()
