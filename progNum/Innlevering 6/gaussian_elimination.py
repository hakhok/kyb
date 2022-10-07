import numpy as np

def add(A, i1, i2, num):
    """Add"""
    A[i2] += num*A[i1]

def swap(A, i1, i2):
    """Swap"""
    i1_old = np.array(A[i1])
    A[i1] = A[i2]
    A[i2] = i1_old

def get_max_row(A, i, j):
    """Get max row"""
    max_number = 0
    max_row_index = 0
    for row_index in range(len(A) - i):
        if A[row_index+j][j] > max_number:
            max_number = abs(A[row_index+j][j])
            max_row_index = row_index+j
    return max_row_index

def row_ops(A, i, j):
    """Row ops"""
    if not A[i][j]:
        return None
    for row_index in range(len(A) - i-1):
        gain = A[row_index+1+i][j]/A[i][j]
        for n in range(len(A[row_index+1])):
            A[row_index+1+i][n] = A[row_index+1+i][n] - A[i][n]*gain

def gauss(A):
    """Gauss elimination"""
    for i in range(len(A)-1):
        max_row = get_max_row(A, i, i)
        swap(A, i, max_row)
        row_ops(A, i, i)

def back_subs(A):
    """Back substitution"""
    ans = []
    rows = len(A)-1
    columns = len(A[0])-1

    for i, _ in enumerate(A):
        b_i = A[rows-i][columns]
        a_i = 0
        for j in range(i):
            a_i += A[rows-i][rows-j]*ans[j]
        value = A[rows-i][rows-i]
        ans.append(round((b_i-a_i)/value, 2))
    ans.reverse()
    return ans

A = np.array([[1.,1.,1.,3.], [1.,2.,3.,0.], [1.,3.,4.,-2.]])
A = np.array([[4.,6.,5.,3.], [6.,8.,5.,3.], [2.,4.,7.,5.]])
gauss(A)
x = back_subs(A)
print(x)
