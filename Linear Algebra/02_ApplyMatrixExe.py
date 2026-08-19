import numpy as np

u = np.array([[2, 5, -3]]).T
u2 = np.array([[0], [-4], [6]])

B = np.array([[2, 0, -1], [-2, 3, 1], [0, 4, -1]])

print(u)
print(f'u.shape: {u.shape}')

print(f'u2.shape: {u2.shape}')
print(u2)

print(f'B.shape: {B.shape}')
I = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

print(f'I.shape: {I.shape}')
print(I)

Iu = I.dot(u)
print(f'Iu.shape: {Iu.shape}')
print(Iu)

print(f'B.shape: {B.shape}')
print(B)

U = np.concatenate((u, u2), axis=1)
print(f'U.shape: {U.shape}')
print(U)

BU = B.dot(U)
print(f'BU.shape: {BU.shape}')
print(BU)
