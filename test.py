import numpy as np

a = np.arange(10)
print(a)

b = np.array([9,2121,2123,'123'])
print(b)
print(b.dtype)

c = np.arange(20).reshape((4,5))
print(c)
print(c.shape)

d = c[:,3]
print(d)
print(d.shape)

