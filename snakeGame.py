import pygame
import time
import random

class snakeGame:

    def __init__(self,w,h,title,dc,zoom,diff):
        pygame.init()
        self.zoom = zoom
        self.title = title
        self.w = w
        self.h = h
        self.defaultColor = dc
        self.diff = diff
        self.apples = list()

        self.start = (self.w / 2,self.h / 2)

        self.lead_x = self.start[0]
        self.lead_y = self.start[1]

        startValues = (w,h)

        self.screen = pygame.display.set_mode(startValues)

        pygame.display.flip()
        pygame.display.set_caption(title)

        self.changeScreenColor(dc)
        self.createSquare(self.zoom,"red")


    def gameLoop(self,fps):
        self.apples = list()
        self.appleScore = 0
        self.lead_x = self.start[0]
        self.lead_y = self.start[1]
        self.snakeList = []
        self.snakeList.append((self.lead_x,self.lead_y))

        over = False
        r = True
        clock = pygame.time.Clock()
        x = 0
        y = 0
        l = False

        while r:
            while l: 
                self.screen.fill(self.defaultColor)
                self.createTextCenter("Game Over",(self.getColor("white"),self.getColor("black")),"RobotoSlab-Regular.ttf",self.zoom * 4,(self.w // 2, self.h // 2))
                self.createTextCenter("Score: " + str(self.appleScore),(self.getColor("white"),self.getColor("Black")),"RobotoSlab-Regular.ttf",self.zoom,(self.start[0],self.start[1] + 75))
                self.createTextCenter("Press C for Next Game or Q for Exit",(self.getColor("white"),self.getColor("black")),"RobotoSlab-Regular.ttf",self.zoom,(self.start[0],self.start[1] + 150))
              
                if over:
                    self.createTextCenter("Snake Over the Field",(self.getColor("white"),self.getColor("black")),"RobotoSlab-Regular.ttf",int(self.zoom * 0.8),(self.w // 2, self.h // 5))
             
                

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            (l,r) = False
                        
                        if event.key == pygame.K_c:
                            self.gameLoop(fps)

                pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    y = self.snakeMoveWrapper(event.key,pygame.K_UP,pygame.K_DOWN)
                    x = self.snakeMoveWrapper(event.key,pygame.K_LEFT,pygame.K_RIGHT)
                elif  event.type == pygame.KEYUP:
                    x = self.snakeStopWrapper(event.key,pygame.K_LEFT,pygame.K_RIGHT)
                    y = self.snakeStopWrapper(event.key,pygame.K_UP,pygame.K_DOWN)
                elif event.type == pygame.QUIT:
                    r = False
                    l = False

    
            if x == None:
                x = 0
            
            if y == None: 
                y = 0

            if l == False:
                self.lead_x += x
                self.lead_y += y

            
            if self.gameOver():
                l = True


  
            else:
                self.screen.fill(self.defaultColor)
                self.createApple()
                self.checkForApples()
                

                if not self.snakeList[::-1][0] ==(self.lead_x,self.lead_y):
                    self.snakeList.append((self.lead_x,self.lead_y))


                if self.buildSnake("black",(self.lead_x,self.lead_y)):
                    l = True
                    over = True

                self.createTextCenter("Score: " + str(self.appleScore),(self.getColor("white"),self.defaultColor),"RobotoSlab-Regular.ttf",self.zoom,(self.start[0],self.start[1] // 4))
                

                self.createSquare(self.zoom,"red")


            clock.tick(fps)
            pygame.display.update()
                

        

        pygame.quit()
        quit()

    def checkForApples(self):
        for aIndex,apple in enumerate(self.apples):
            if apple[0] > self.lead_x - self.zoom - 2 and apple[0] < self.lead_x + self.zoom - 2 and apple[1] > self.lead_y - self.zoom - 2 and apple[1] < self.lead_y + self.zoom - 2:
                self.apples.remove(apple)
                self.appleScore += 1

    def gameOver(self):
        if self.lead_x < 0 or self.lead_x > self.w or self.lead_y < 0 or self.lead_y > self.w:
            return True

    def borders(self):
        self.lead_y = self.border(self.lead_y)
        self.lead_x = self.border(self.lead_x)
    
    def border(self,x):
        if x < 0:
            x = 0
        elif x >= 600:
            x = 600 - self.zoom

        return x

    def snakeStopWrapper(self,key,KF,KS):
        if key == KF or key == KS:
            return 0

    def snakeMoveWrapper(self,key,KF,KS):
        n = 0

        if key == KF:
            n = - self.zoom
        
        if key == KS:
            n = self.zoom

        return n

        
    def changeScreenColor(self,color):
        c = self.getColor(color)
        
        self.screen.fill(c) 

    def createSquare(self,x,color):
        c = self.getColor(color)
        pygame.draw.rect(self.screen,c,[self.lead_x,self.lead_y,x,x])

    def buildSnake(self,color,cords):
        c = self.getColor(color)
        s = 0
        x = False

        for x in range(0,self.appleScore + 1):
            pygame.draw.rect(self.screen,c,[self.snakeList[::-1][x][0],self.snakeList[::-1][x][1],self.zoom,self.zoom])

        if self.appleScore > 1:
            x = True
            newList = list()

            for x in range(0,self.appleScore + 1):
                newList.append(self.snakeList[::-1][x + 1])

            for pos in newList:
                if pos[0] == cords[0] and pos[1] == cords[1]:
                        print(newList)
                        print(cords)

                        return True


        return False
            

    def getColor(self,color):
        maps = {
            "black": (0,0,0),
            "white": (255,255,255),
            "red": (255,0,0),
            "apple": (235,44,162),
            "default": color
        }

        if type(color) is tuple:
            c = maps.get("default")
        elif type(color) is str:
            c = maps.get(color)

        return c

    def createTextCenter(self,title,color,f,size,pos):
        font = pygame.font.Font(f,size)
        text = font.render(title,True,color[0])
        textRect = text.get_rect()
        textRect.center = pos

        self.screen.blit(text,textRect)

    def getRandomCords(self):
        span = 40
        return (random.randrange(span,self.w - span),random.randrange(span,self.h - span))
    
    def getRandomColor(self):
        return (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))

    def createApple(self):

        c = self.getRandomColor()

        if random.randrange(0,self.diff) == 5 and len(self.apples) < 5:
            cords = self.getRandomCords()
            self.apples.append(cords)
        
        for x in self.apples:
            if self.appleScore > 5 and self.appleScore < 10:
                pygame.draw.ellipse(self.screen,c,(self.addToGrid(x[0]),self.addToGrid(x[1]),self.zoom,self.zoom))
            else:
                pygame.draw.ellipse(self.screen,self.getColor("apple"),(self.addToGrid(x[0]),self.addToGrid(x[1]),self.zoom,self.zoom))


    def addToGrid(self,x):
        return round(x/self.zoom)*self.zoom
