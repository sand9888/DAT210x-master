import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
import numpy as np

x = np.arange(9)

print(x)
x= np.split(x, 3)
print(x)