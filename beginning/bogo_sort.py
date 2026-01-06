import random
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

# Bogosort just randomly rearranges the list of values over and over,
# so the first thing it's going to need is a function to detect when
# the list is sorted. 
def is_sorted(values):
  for index in range(len(values) - 1):
    if values[index] > values[index + 1]:
      return False
  return True

def bogo_sort(values):
  while not is_sorted(values):
    random.shuffle(values)
  return values

print(bogo_sort(numbers))