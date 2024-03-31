import logging
import os
import time
import xmltodict
from compass.compass import Compass

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

save_path="/mnt/c/Users/Mark/Documents/My Games/Stationeers/saves"
save_name="2024-03-27 Moon Normal"
world_file=f"{save_path}/{save_name}/world.xml"
world_mtime=0

meta_file=f"{save_path}/{save_name}/world_meta.xml"
file=open(meta_file, "r")
meta_xml=file.read()
file.close()

# Find out what world we're on
d=xmltodict.parse(meta_xml)
world_name=d["WorldMetaData"]["WorldName"]
print(f"World is {world_name}.")
compass = Compass(world_name)

# Find out where we're going
target = [0, 0]
print(f"Destination is [{target[0]:.0f},{target[1]:.0f}].\n")

while True:
    world_stat = os.stat(world_file)
    if (world_stat.st_mtime > world_mtime):
        world_mtime = world_stat.st_mtime

        file=open(world_file, "r")
        world_xml=file.read()
        file.close()

        d=xmltodict.parse(world_xml)
        world_data=d["WorldData"]
        all_things=world_data["AllThings"]
        data=all_things["ThingSaveData"]
        brains=[t for t in data if t.get('PrefabName', None) == 'OrganBrain']

        for brain in brains:
            name=brain["CustomName"]
            name = name.replace("'s Brain's Brain", "")
            x = float(brain["WorldPosition"]["x"])
            y = float(brain["WorldPosition"]["y"])
            z = float(brain["WorldPosition"]["z"])
            position = [x, z]

            distance = compass.distance([x, z], target)
            bearing = compass.bearing(position, target)

            print(f"{name} is at [{x:.0f},{z:.0f}]. Destination is {distance:.0f}m away at {bearing:.0f}°")

        time.sleep(1)