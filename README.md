# AoTTG-RC-Blender-Map-Editor
A Blender map editor for AoTTG RC

For now :
- There is a .blend file (made with Blender 2.9) in the blend directory containing props from AoTTG RC Map Editor.
- These props are textured with the images from textures directory, and are more or less at the right position / scale / rotation.
- To create a map, you'll have to copy objects from "ressource" collection to "level" collection.
- There's a python script in the Scripting workspace, it converts "level" collection content to an AoTTRC map script.
- The map script is then printed in Blender console and saved in "maps" directory.
