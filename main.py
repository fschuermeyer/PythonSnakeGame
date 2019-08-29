from snakeGame import snakeGame as snake

'''
@author Felix Schürmeyer
@version 0.0.1 

'''

color = (140,200,100)
ratio = 900
title = "Snake Game by Felix"
zoom  = ratio // 30 # Default Value 10
fps = 30
apppleSpawnChance = 40

s = snake(ratio,ratio,title,color,zoom,apppleSpawnChance)

print(s.getRandomCords())

s.gameLoop(fps)