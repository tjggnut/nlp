import numpy as np

array1 = np.ones((2,3))
print(array1)

vector = np.array([1,2,3,4])
print(type(vector))
print(vector)

matrix = np.array([[1,'Tim'],[2,'Tom'],[3,'Helon'],[4,'HeShen']])
print(matrix)
print(type(matrix))
print(matrix.dtype)

ott = np.arange(10).reshape((2,5))
print(ott)
print(ott.shape)
print(ott.dtype)


d = np.genfromtxt("data.csv",delimiter=",")
print(d)
print(d[0][2])
print(d[0,2])

mm = np.arange(0,30,5)
print(mm)
mmm = mm % 10 == 0
print(mmm)

print(mm[mmm])

mm[mm==0] = 10
print(mm)

print(mm.sum())

print(mm.astype(np.str))

tredim = np.array([[[1,2,3,4],[2,3,4,5]],[[6,7,8,9],[1,4,6,8]]])
print(tredim)
print("axis = 0")
print(tredim.sum(0))

print("axis = 1")
print(tredim.sum(1))

print("axis = 2")
print(tredim.sum(2))