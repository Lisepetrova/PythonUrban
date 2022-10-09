from Task2 import list_index

def get_mean_green_index(list_index) -> float:
    mean_index = 0
    mean_index = sum(list_index)/len(list_index)
    
    return round(mean_index,2)

print(get_mean_green_index(list_index)) 
