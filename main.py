from snakeGame import snakeGame as snake

'''
@author Felix Schürmeyer
@version 0.0.1 

'''

color = (140,200,100)
ratio = 800
title = "Snake Game by Felix"
zoom  = ratio // 30 # Default Value 10
fps = 60

s = snake(ratio,ratio,title,color,zoom)

s.gameLoop(fps)