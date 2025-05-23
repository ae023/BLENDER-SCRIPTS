import bpy

# ORIGIN SETTING OPTIONS
# 'ORIGIN_GEOMETRY'          - CENTRE OF GEOMETRY
# 'ORIGIN_CENTER_OF_MASS'    - CENTRE OF MASS (GEOMETRY)
# 'ORIGIN_CENTER_OF_MASS'    - CENTRE OF MASS (BOUNDS)
# 'ORIGIN_CURSOR'            - MOVE ORIGIN TO 3D CURSOR.
# 'ORIGIN_CENTER_OF_VOLUME'  - VOLUMETRIC CENTRE.

origin_mode = 'ORIGIN_GEOMETRY'
# origin_mode = 'ORIGIN_CENTER_OF_MASS'  # USE WITH BOUNDS
# origin_mode = 'ORIGIN_CURSOR'
# origin_mode = 'ORIGIN_CENTER_OF_VOLUME'

center_option = 'MEDIAN'
# center_option = 'BOUNDS'

# SET ORIGIN FOR ALL SELECTED OBJECTS
for obj in bpy.context.selected_objects:
    if obj.type in {'MESH', 'CURVE', 'SURFACE'}:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.origin_set(type=origin_mode, center=center_option)
