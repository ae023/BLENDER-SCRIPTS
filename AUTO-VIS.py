import bpy

# GET SELECTED MESH OBJECTS
selected_objects = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']
selected_objects.sort(key=lambda obj: obj.name)

# SET FRAMERANGE TO MATCH NUMBER OF MESH OBJECTS
bpy.context.scene.frame_start = 1
bpy.context.scene.frame_end = len(selected_objects)

# LOOP THROUGH EACH MESH OBJECT AND KEYFRAME VISIBILITY
for i, obj in enumerate(selected_objects):
    frame = i + 1
    for o in selected_objects:
        o.hide_render = True
        o.hide_viewport = True
        o.keyframe_insert(data_path="hide_render", frame=frame)
        o.keyframe_insert(data_path="hide_viewport", frame=frame)

    obj.hide_render = False
    obj.hide_viewport = False
    obj.keyframe_insert(data_path="hide_render", frame=frame)
    obj.keyframe_insert(data_path="hide_viewport", frame=frame)
