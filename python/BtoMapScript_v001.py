import bpy
import os
from datetime import datetime
try:
    filePath = bpy.data.filepath
    projectFolder = filePath.rsplit("\\blend\\",1)[0]
    mapsFolder = projectFolder+"\\maps"
    if(os.path.isdir(mapsFolder) == False):
        print("Maps folder not found.")
        os.mkdir(projectFolder+"/maps")
        print("Maps folder created.")
except:
    pass
#Types list
types = ["custom","base","spawnpoint","photon"]
#Objects lists
names_spawnpoint = ["playerC","playerM","titan"]
names_base = ["aot_supply"]
names_photon = ["CannonWall","CannonGround"]
names_custom_nature = ["leaf0","leaf1","leaf2","field1",
"field2","tree0","tree1","tree2",
"tree3","tree4","tree5","tree6",
"tree7","log1","log2","trunk1",
"boulder1","boulder2","boulder3","boulder4",
"boulder5","cave1","cave2"]
names_custom_buildings = ["tower1","tower2","tower3","tower4",
"tower5","house1","house2","house3",
"house4","house5","house6","house7",
"house8","house9","house10","house11",
"house12","house13","house14","pillar1",
"pillar2","village1","village2","windmill1",
"arch1","canal1","castle1","church1",
"cannon1","statue1","statue2","wagon1",
"elevator1","bridge1","dummy1","spike1",
"wall1","wall2","wall3","wall4"]
#Merge all lists
names = []
names.extend(names_spawnpoint)
names.extend(names_base)
names.extend(names_photon)
names.extend(names_custom_nature)
names.extend(names_custom_buildings)
#Declare map script string
map_script = ""
#script = "map,disablebounds;\n"
for obj in bpy.data.collections["level"].all_objects:
    #Get objects transforms
    locationX = obj.location[0]
    locationY = obj.location[1]
    locationZ = obj.location[2]
    scaleX = obj.scale[0]
    scaleY = obj.scale[1]
    scaleZ = obj.scale[2]
    rotation_quaternionW = obj.rotation_quaternion[0]
    rotation_quaternionX = obj.rotation_quaternion[1]
    rotation_quaternionY = obj.rotation_quaternion[2]
    rotation_quaternionZ = obj.rotation_quaternion[3]
    #Get objects names
    try:
        type = obj.name.split("_",1)[0]
        name = obj.name.split("_",1)[1].rsplit(".")[0]
    except:
        continue
    #Check type
    if type in types:
        #Check name
        if name in names:
            #Convert Blender transforms to AottgRC transforms
            posX = format(locationX, ".4f")
            posY = format(locationZ, ".4f")
            posZ = format(locationY, ".4f")
            length = format(scaleX, ".4f")
            width = format(scaleZ, ".4f")
            height = format(scaleY, ".4f")
            rotateW = format(rotation_quaternionW, ".4f")
            rotateX = format(rotation_quaternionX, ".4f")
            rotateY = format(-rotation_quaternionY, ".4f")
            rotateZ = format(rotation_quaternionZ, ".4f")
            if type == "custom" or type == "base" or type == "photon":
                map_script += type+","+name+",default,"+length+","+width+","+height+",0,1,1,1,1.0,1.0,"+posX+","+posY+","+posZ+","+rotateW+","+rotateY+","+rotateZ+","+rotateX+";\n"
                continue
            elif type == "spawnpoint":
                map_script += "spawnpoint,"+name+","+posX+","+posY+","+posZ+","+rotateW+","+rotateY+","+rotateZ+","+rotateX+";\n"
                continue
        else:
            continue
#Print map script in console
print(map_script)
#Save script to maps folder
now = datetime.now()
now = now.strftime("%Y_%m_%d_%Hh%Mm%S")
try:
    f = open(mapsFolder+"\\"+now+".txt","w")
    f.write(map_script)
    f.close()
except:
    print("Couldn't save file.")
    pass