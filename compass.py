import click
import logging
import os
import time
import xmltodict

from stationeers.compass import Compass
from stationeers.save import Save

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

@click.command()
@click.option('--path', envvar='STATIONEERS_PATH', help='Path to the Stationeers save files')
@click.option('--save', envvar='STATIONEERS_SAVE', help="The name of the save")
def run(path, save):
    s = Save(f"{path}/{save}")
    s.load()

    world_mtime=0

    # Find out what world we're on
    print(f"World is {s.world}.")
    compass = Compass(s.world)

    # Find out where we're going
    target = [0, 0]
    print(f"Destination is [{target[0]:.0f},{target[1]:.0f}].\n")

    while True:
        world_stat = os.stat(s.world_file)
        if (world_stat.st_mtime > world_mtime):
            world_mtime = world_stat.st_mtime

            for brain in s.get_brains():
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
            
        
if __name__ == '__main__':
    run()

