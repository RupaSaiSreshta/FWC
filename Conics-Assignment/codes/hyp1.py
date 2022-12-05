import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys    #for path to external scripts
sys.path.insert(0,'/home/sreshta/Rupa/circles/CoordGeo')   #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

#Defining hyperbola equation
def hyperb_gen(y):
	x = np.sqrt(2)+np.sqrt(4+2*((y+np.sqrt(2))**2))
	return x

#Input parameters
e1=np.array([1,0]).reshape(2,1)
m=e1
u=np.array(([-np.sqrt(2),-2*np.sqrt(2)])).reshape(2,1)
V1 = np.array(([1,0],[0,-2])).reshape(2,2)
V2 = np.linalg.inv(V1)
p1 = np.array(([-1,0],[0,1])).reshape(2,2)
f = -6
n=np.matrix('0;1').reshape(2,1)

#l-eigen_values & P-eigen_vector		
l,P = np.linalg.eigh(V1)

#center of hyperbola
C=-(V2@u)
O=np.array(([1.4142,-1.4142])).reshape(2,1)
c=-np.sqrt(2)
f0=-4

l1 = l[0]	#lambda_1
l2 = l[1]	#lambda_2

#eccentricity
e = np.sqrt(1-(l1/l2))	

#Finding the focus
f1=e*np.sqrt(f0/(l2*(1-e**2)))
f2=f1*e1
d=np.array([1.414,-1.414]).reshape(2,1)
F=f2+d
print(F)


#Finding the vertex
kk2=m.T@V1@m
kk1=m.T@(V1@O+u)
kk=(kk1**2-(O.T@V1@O+2*u.T@O+f)*(kk2))
kk=np.sqrt(kk[0])
k1=(-kk1+kk)/kk2
k2=(-kk1-kk)/kk2
a=O+k1*m
b=p1@a
n1=F-a
m1=omat@n1
print(m1)

#Finding latus rectum
kk4=m1.T@V1@m1
kk3=m1.T@(V1@F+u)
kk5=(kk3**2-(F.T@V1@F+2*u.T@F+f)*(kk4))
kk5=np.sqrt(kk5[0])
k3=(-kk3+kk5)/kk4
k4=(-kk3-kk5)/kk4
a1=F+k3*m1
a2=F+k4*m1
print(a1,a2)

#Plotting the Latus rectum
x_AB = line_dir_pt(m1,F,-5,5)
plt.plot(x_AB[0,:],x_AB[1,:],linestyle='dotted')

#Generating the hyperbola
y = np.linspace(-4.7,2,100)
x = hyperb_gen(y)
plt.axhline(y=0,color='black')
plt.axvline(x=0,color='black')
plt.plot(x,y,label='Hyperbola')
plt.plot(-x,y)


#Generating all lines
xAB = line_gen(a,F)
xCD = line_gen(a,a1)
xCF = line_gen(F,a1)

#Plotting all lines
plt.plot(xAB[0,:],xAB[1,:])
plt.plot(xCD[0,:],xCD[1,:])
plt.plot(xCF[0,:],xCF[1,:])


#Labeling the coordinates
tri_coords = np.vstack((F.T,a.T,b.T,a1.T,a2.T)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['F','v1','v2', 'l1' , 'l2']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(-5,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x-axis$')
plt.ylabel('$y-axis$')
plt.legend(loc='upper left')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('/home/sreshta/Rupa/circles/conic.pdf')
#subprocess.run(shlex.split("termux-open '/sdcard/FWC/Matrices/Conic/conicp.pdf'"))
#else
plt.show()

