import pygame
import time
class snakeGame:

    def __init__(self,w,h,title,dc,zoom):
        pygame.init()
        self.zoom = zoom
        self.title = title
        self.w = w
        self.h = h
        self.defaultColor = dc

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

        self.lead_x = self.start[0]
        self.lead_y = self.start[1]

        r = True
        clock = pygame.time.Clock()
        x = 0
        y = 0
        l = False

        while r:

            while l: 
                self.screen.fill(self.getColor("black"))
                self.createTextCenter("Game Over",(self.getColor("white"),self.getColor("black")),"RobotoSlab-Regular.ttf",self.zoom * 4,(self.w // 2, self.h // 2))
                self.createTextCenter("Press C for Next Game or Q for Exit",(self.getColor("white"),self.getColor("black")),"RobotoSlab-Regular.ttf",self.zoom,(self.start[0],self.start[1] + 100))
                pygame.display.update()

                for event in pygame.event.get():
                    pass

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    y = self.snakeMoveWrapper(event.key,pygame.K_UP,pygame.K_DOWN)
                    x = self.snakeMoveWrapper(event.key,pygame.K_LEFT,pygame.K_RIGHT)
                elif  event.type == pygame.KEYUP:
                    x = self.snakeStopWrapper(event.key,pygame.K_LEFT,pygame.K_RIGHT)
                    y = self.snakeStopWrapper(event.key,pygame.K_UP,pygame.K_DOWN)
                elif event.type == pygame.QUIT:
                    r = False

    
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
                self.createSquare(self.zoom,"red")


            clock.tick(fps)

        

        pygame.quit()
        quit()

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
        pygame.display.update()

    def createSquare(self,x,color):
        c = self.getColor(color)
        pygame.draw.rect(self.screen,c,[self.lead_x,self.lead_y,x,x])
        pygame.display.update()


    def getColor(self,color):
        maps = {
            "black": (0,0,0),
            "white": (255,255,255),
            "red": (255,0,0),
            "default": color
        }

        if type(color) is tuple:
            c = maps.get("default")
        elif type(color) is str:
            c = maps.get(color)

        return c

    def createTextCenter(self,title,color,f,size,pos):
        font = pygame.font.Font(f,size)
        text = font.render(title,True,color[0],color[1])
        textRect = text.get_rect()
        textRect.center = pos

        self.screen.blit(text,textRect)
    