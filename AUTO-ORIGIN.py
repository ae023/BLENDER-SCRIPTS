import bpy

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
ORIGIN SETTING OPTIONS
#01. 'ORIGIN_GEOMETRY'          = CENTRE OF GEOMETRY
#02. 'ORIGIN_CENTER_OF_MASS'    = CENTRE OF MASS (GEOMETRY)
#03. 'ORIGIN_CENTER_OF_MASS'    = CENTRE OF MASS (BOUNDS)
#04. 'ORIGIN_CURSOR             = MOVE ORIGIN TO 3D CURSOR
#05. 'ORIGIN_CENTER_OF_VOLUME'  = VOLUMETRIC CENTRE

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

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
