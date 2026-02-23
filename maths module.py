import math


user_input = float(input("Enter a number: "))

square_root = math.sqrt(user_input)
natural_log = math.log(user_input)
sine_value = math.sin(user_input)


print(f"--- Results for {user_input} ---")
print(f"Square Root: {square_root}")
print(f"Natural Logarithm (ln): {natural_log}")
print(f"Sine (in radians): {sine_value}")