import bpy
import math

grid_width = 10
spacing = 20 

selected_objects = bpy.context.selected_objects

for idx, obj in enumerate(selected_objects):
    row = idx // grid_width
    col = idx % grid_width
    obj.location.x = col * spacing
    obj.location.y = 0
    obj.location.z = -row * spacing
