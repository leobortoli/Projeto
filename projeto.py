from random import randint
import numpy as np
DANOS= np.array([[[1, 2, 3, 4],[5, 6, 7, 8]],[[9, 10, 11, 12],[13, 14, 15, 16]]])
print(DANOS[:, 1, :])
print(DANOS.ndim)