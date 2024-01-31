import numpy as np
import time
import matplotlib.pyplot as plt

def block_matrix_mult(A, B, block_size):
    n = A.shape[0]
    C = np.zeros((n,n))
    for i in range(0,n,block_size):
        for j in range(0,n,block_size):
            for k in range(0,n,block_size):
                C[i:i+block_size,j:j+block_size] += A[i:i+block_size,k:k+block_size].dot(B[k:k+block_size,j:j+block_size])
    return C

matrix_sizes = [128, 512, 1024]
block_sizes = [16, 32, 64, 128]
results = {}

for n in matrix_sizes:
    results[n] = []
    A = np.random.rand(n,n)
    B = np.random.rand(n,n)
    for b in block_sizes:
        start_time = time.time()
        C = block_matrix_mult(A,B,b)
        end_time = time.time()
        results[n].append(end_time - start_time)

for n in matrix_sizes:
    plt.plot(block_sizes, results[n], label=f"Matrix size: {n}")
plt.legend()
plt.xlabel("Block size")
plt.ylabel("Time (s)")
plt.show()