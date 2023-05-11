#!/usr/bin/python3
if __name__ == "__main__":
# Assign values to a and b
a = 10
b = 5

# Import specific functions from calculator_1.py
from calculator_1 import add, subtract, multiply, divide

# Perform mathematical operations
sum_result = add(a, b)
diff_result = subtract(a, b)
prod_result = multiply(a, b)
div_result = divide(a, b)

# Print the results
print("Sum: {}".format(sum_result))
print("Difference: {}".format(diff_result))
print("Product: {}".format(prod_result))
print("Division: {}".format(div_result))
