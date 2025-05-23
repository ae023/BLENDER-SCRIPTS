import bpy

bevel_depth = 1
bevel_resolution = 5

for obj in bpy.context.selected_objects:
    if obj.type == 'CURVE':
        curve_data = obj.data
        curve_data.bevel_depth = bevel_depth
        curve_data.bevel_resolution = bevel_resolution
        curve_data.fill_mode = 'FULL'
        curve_data.use_fill_caps = True
