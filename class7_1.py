from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random
import time

x,y,z = mc.player.getPos()


while True:
    rx = random.randrange(-10,10) + x
    rz = random.randrange(-10,10) + z
    ry = y + 20

    mc.spawnEntity(rx,ry,rz, 93)
    time.sleep(1)