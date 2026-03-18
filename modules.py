import os
import math

# 1
print("Current working directory:", os.getcwd())

# 2
num = int(input("Enter an integer: "))
log_value = math.log2(num)
print(f"Log base 2 of {num} is: {log_value}")

# 3
print("Floor:", math.floor(log_value))
print("Ceiling:", math.ceil(log_value))