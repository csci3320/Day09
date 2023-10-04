'''
Covert integer i (base 10) into either base 8 or 16, based on the value of the second argument
Return the string representation of the resulting number.
'''

import math

def base_convert(i, base):
  if i < 0:
    return "I can't do negative numbers yet."
  value = i
  to_return = ""
  while value > 0:
    #print(" - looping on: " + str(value))
    m = value % base
    to_return = str(m) + to_return
    value = math.floor(value/base)
  print(to_return)
  return to_return

base_convert(1, 8)
base_convert(1, 16)

base_convert(8, 8)
base_convert(16, 16)

base_convert(10, 8)
base_convert(18, 16)

base_convert(16, 8)
base_convert(32, 16)

base_convert(100, 8)
base_convert(100, 16)


