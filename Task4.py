from Task1 import GreenZoneIndex
from Task2 import list_index

def filter_min_green_index (list_index, min_value: float = 0.1):
  zones_counter = 0
  for item in list_index:
        if item > min_value:
            zones_counter += 1
  return zones_counter
  print(zones_counter)
