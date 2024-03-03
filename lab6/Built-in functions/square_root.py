import time
import math

def square_root_after_milliseconds(number, millisec):
    sec = millisec / 1000
    result = math.sqrt(number)
    
    print(f"Square root of {number} after {millisec} milliseconds is {result}")

number = 25100
milliseconds = 2123
square_root_after_milliseconds(number, milliseconds)