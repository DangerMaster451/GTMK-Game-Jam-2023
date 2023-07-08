import pygame
import random
import json

class Task():
    def __init__(self, weapon_type:str, material_names:list[str], material_icon_paths:list[str], completed_material_icon_paths:list[str],icon_scale:tuple[int,int]) -> None:
        self.weapon_type = weapon_type
        self.material_names = material_names
        self.material_icons = [pygame.transform.scale(pygame.image.load(icon_path), icon_scale) for icon_path in material_icon_paths]
        self.completed_material_icons = [pygame.transform.scale(pygame.image.load(icon_path), icon_scale) for icon_path in completed_material_icon_paths]

def new_task(items_file_path, icon_scale) -> Task:
    with open(items_file_path, "r") as file:
        items = json.load(file)
        random_item = items[random.randint(0, len(items)-1)]

        material_names = []
        for index in range(len(random_item["materials"])):
            material_names.append(random_item["materials"][index]["name"])

        material_icon_paths = []
        for index in range(len(random_item["materials"])):
            material_icon_paths.append(random_item["materials"][index]["icon_path"])

        completed_material_icon_paths = []
        for index in range(len(random_item["materials"])):
            completed_material_icon_paths.append(random_item["materials"][index]["completed_icon_path"])
        
        return Task(random_item["name"], material_names, material_icon_paths, completed_material_icon_paths, icon_scale)