import scipy.io
mat = scipy.io.loadmat('config1.mat')

data = {}
for d in mat:
    data[str(d)] = mat[str(d)]

print(data)
