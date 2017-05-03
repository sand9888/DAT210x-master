import math
import sys
sys.float_info.max
# 365! / 365**n * (365-n)!
birth_two = math.factorial(365)//365**42*math.factorial(365-42)
print(birth_two)