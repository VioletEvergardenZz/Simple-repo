import numpy as np
import matplotlib.pyplot as plt
n1=plt.imread('C:\WorkSpace\VSC\Simple-repo\pexels-photo-20898612.jpeg')
# print(type(n1),n1)
plt.imshow(n1)

n2 =np.array([0.299,0.587,0.114])
x= np.dot(n1,n2)
plt.imshow(x,cmap='gray')
plt.show()