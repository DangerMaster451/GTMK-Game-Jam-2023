import pygame
import random
import json
from Classes.grid import Grid
from Classes.npc import NPC


class Task:
    def __init__(
        self,
        weapon_type: str,
        weapon_icon:pygame.surface.Surface,
        material_names: list[str],
        material_icon_paths: list[str],
        completed_material_icon_paths: list[str],
        icon_scale: tuple[int, int],
        npc: NPC
    ) -> None:
        self.weapon_type = weapon_type
        self.weapon_icon = weapon_icon
        self.material_names = material_names
        self.material_icons = [
            pygame.transform.scale(pygame.image.load(icon_path), icon_scale)
            for icon_path in material_icon_paths
        ]
        self.completed_material_icons = [
            pygame.transform.scale(pygame.image.load(icon_path), icon_scale)
            for icon_path in completed_material_icon_paths
        ]
        self.npc = npc

    def check_if_task_completed(self, grid: Grid) -> bool:
        for index in range(len(self.material_names)):
            if self.material_names[index] in grid.get_anvil_inventories()[0]:
                pass
            else:
                return False  # If this is never called, the function will return true
        return True

def new_task(npc, items_file_path, icon_scale) -> Task:
    with open(items_file_path, "r") as file:
        items = json.load(file)
        random_item = items[random.randint(0, len(items) - 1)]

        weapon_icon = pygame.image.load(random_item["weapon_icon_path"])

        material_names = []
        for index in range(len(random_item["materials"])):
            material_names.append(random_item["materials"][index]["name"])

        material_icon_paths = []
        for index in range(len(random_item["materials"])):
            material_icon_paths.append(random_item["materials"][index]["icon_path"])

        completed_material_icon_paths = []
        for index in range(len(random_item["materials"])):
            completed_material_icon_paths.append(
                random_item["materials"][index]["completed_icon_path"]
            )

        return Task(
            random_item["name"],
            weapon_icon,
            material_names,
            material_icon_paths,
            completed_material_icon_paths,
            icon_scale,
            npc
        )
