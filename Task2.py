from Task1 import GreenZoneIndex

list_territories = [
    {
        "territory_name": "Пушкин",
        "territory_area": 28676,
        "green_zones": [302, 487, 420, 325, 471, 363, 404]
    },
    {
        "territory_name": "Павловск",
        "territory_area": 21025,
        "green_zones": [360, 375, 223, 258, 345, 296, 303]
    },
    {
        "territory_name": "Петергоф",
        "territory_area": 44274,
        "green_zones": [364, 447, 438, 223, 336, 431, 442]
    },
]
list_index = []
for city_dict in list_territories:
  territory_name = city_dict.get("territory_name")
  territory_area = city_dict.get("territory_area")
  green_zones = city_dict.get("green_zones")
  value = GreenZoneIndex(territory_name, territory_area,green_zones)
  list_index.append(value.green_index)
  print(f"Индекс озеленения территории {value.territory_name} равен {value.green_index}%")
print(list_index)
