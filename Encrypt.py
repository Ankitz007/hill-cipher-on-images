# Importing the required libraries
import imageio
import numpy as np

# Reading the image that is to be encrypted
img = imageio.imread('1.jpg')

# Saving the image dimensions
l = img.shape[0]
w = img.shape[1]

# Making the image to have square dimensions by padding zeroes
n = max(l,w)
if n%2:
    n = n + 1
img2 = np.zeros((n,n,3))
img2[:l,:w,:] += img

# Generating Encryption Key
# The generation of the key is based on the following research paper:
# Acharya, Bibhudendra & Panigrahy, Saroj Kumar & Patra, Sarat & Panda, Ganapati. (2009). "Image Encryption Using Advanced Hill Cipher Algorithm". International Journal of Recent Trends in Engineering. Vol 1. 
# To have a look on the algorithm, please read the paper.
Mod = 256
k = 23

a22 = np.random.randint(256, size = (int(n/2),int(n/2))) # Arbitrary matrix
I = np.identity(int(n/2)) # Identity matrix of size n/2
a11 = np.mod(-a22,Mod) # (a11 = -a22)

a12 = np.mod((k * np.mod(I - a11,Mod)),Mod) # (a12 = k * (I - a11))
k = np.mod(np.power(k,127),Mod)
a21 = np.mod((I + a11),Mod)
a21 = np.mod(a21 * k, Mod)

# Generating the matrix from a11, a12, a21 and a22
A1 = np.concatenate((a11,a12), axis = 1)
A2 = np.concatenate((a21,a22), axis = 1)
A = np.concatenate((A1,A2), axis = 0)

# Making sure that A is an involutory matrix, A*A = I
Test = np.mod(np.matmul(np.mod(A,Mod),np.mod(A,Mod)),Mod)

# Saving key as an image
key = np.zeros((n + 1, n))
key[:n, :n] += A

# Adding the dimension of the original image within the key
# Elements of the matrix should be below 256
# (This info will be useful while decryption)
key[-1][0] = int(l / Mod)
key[-1][1] = l % Mod
key[-1][2] = int(w / Mod)
key[-1][3] = w % Mod
# Saving the key
imageio.imwrite("Key.png", key.astype('uint8'))

# Encryption
# Each channel of the image is being encrypted separately
Enc1 = (np.matmul(A % Mod,img2[:,:,0] % Mod)) % Mod
Enc2 = (np.matmul(A % Mod,img2[:,:,1] % Mod)) % Mod
Enc3 = (np.matmul(A % Mod,img2[:,:,2] % Mod)) % Mod

# Resizing the channels
Enc1 = np.resize(Enc1,(Enc1.shape[0],Enc1.shape[1],1))
Enc2 = np.resize(Enc2,(Enc2.shape[0],Enc2.shape[1],1))
Enc3 = np.resize(Enc3,(Enc3.shape[0],Enc3.shape[1],1))

#Enc = A * image
Enc = np.concatenate((Enc1,Enc2,Enc3), axis = 2)

# Saving the encrypted image
imageio.imwrite('Encrypted.png',Enc.astype('uint8'))

# Confirmation
print("Encryption was successfull..")