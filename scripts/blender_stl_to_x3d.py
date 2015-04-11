import bpy
import os.path
import sys

for i in range(1, len(sys.argv)):
    if sys.argv[i] == '--':
        break

for file in sys.argv[i+1:]:
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()

    bpy.ops.import_mesh.stl(filepath=file)
    outfile = os.path.splitext(file)[0]+'.x3d'
    bpy.ops.export_scene.x3d(filepath=outfile)
