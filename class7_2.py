from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getPos()


for i in range(10):
    mc.setBlock(x+i,y,z+i, 46)