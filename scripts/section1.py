#!/usr/bin/env python3
# add import and helper functions here
import numpy as np

if __name__ == "__main__":
    # code goes here
    print("hello Jingyun")
    np.random.seed(42)
    A = np.random.normal(size=(4, 4))
    B = np.random.normal(size=(4, 2))
    print(A @ B)
    
    np.random.seed(42)
    x = np.random.normal(size=(4, 10))
    
    L2 = ((x.reshape(4, 1, 10) - x.reshape(1, 4, 10))**2).sum(axis=-1)
    
    print(L2)