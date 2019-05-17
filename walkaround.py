import pygame
pygame.mixer.pre_init(48000,-16, 2, 1024)
pygame.init()

world_Wid = 1000
world_Len = 1000

game_windowWid = 650
game_windowLen = 450
game_window = pygame.display.set_mode((game_windowWid,game_windowLen))
pygame.display.set_caption("WIP walkaround")

clock = pygame.time.Clock()

# sprite loading

walkLeft = [pygame.image.load('Sprites/walking_left1.png'),pygame.image.load('Sprites/walking_left2.png')]
walkRight = [pygame.image.load('Sprites/walking_right1.png'),pygame.image.load('Sprites/walking_right2.png')]
walkUp = [pygame.image.load('Sprites/walking_up1.png'),pygame.image.load('Sprites/walking_up2.png')]
walkDown = [pygame.image.load('Sprites/walking_down1.png'),pygame.image.load('Sprites/walking_down2.png')]
standLeft = pygame.image.load('Sprites/standing_left.png')
standRight = pygame.image.load('Sprites/standing_right.png')
standUp = pygame.image.load('Sprites/standing_up.png')
standDown = pygame.image.load('Sprites/standing_down.png')
currentPlayerImage = standDown

#

bg1 = pygame.image.load('Maps/BG1.png')

# SOUND

pygame.mixer.music.load('Music/bgm_void.ogg')                 # commented out for debug
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)

# Main loop

def main():
    global playerA, lastKeyPressed

    playerA = player(325,225,25,55)
    run = True
    lastKeyPressed = 4

    while run:
        # FPS
        clock.tick(20)

        # BGM loop

        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1,7)                       ##FIX THIS  - Music does not loop right
        
        # Check for quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        # MOVE playerA object ANY DIRECTION #

        playerA.checkMovement()

        # CALL FUNCTION AT END #
        redrawGameWindow()

    pygame.quit()

def redrawGameWindow():
    # Window redraw BG
    game_window.blit(bg1, (0,0))

    # Window redraw playerA
    playerA.draw(game_window)

    # Update
    pygame.display.update()

# ALL THINGS UNRELATED TO THE MAIN LOOP UNDER THIS LINE - - - - - - - - - - - - - - - - - 

# PLAYER object

class player(object):
    # Init, setup whatever
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 8
        self.left = self.right = self.up = self.down = False
        self.walkCount = 0

        self.hitbox = (self.x, self.y, 25,55)               #Allows hitbox for collision use later

    def checkMovement(self):
        global lastKeyPressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > self.vel:
            self.x -= playerA.vel
            self.left = True
            self.right = False
            self.up = False
            self.down = False
            lastKeyPressed = 1
        elif keys[pygame.K_RIGHT] and self.x < game_windowWid - self.width - self.vel:
            self.x += self.vel
            self.left = False
            self.right = True
            self.up = False
            self.down = False
            lastKeyPressed = 2

        if keys[pygame.K_UP] and self.y > self.vel:
            self.y -= self.vel
            self.left = False
            self.right = False
            self.up = True
            self.down = False
            lastKeyPressed = 3
        elif keys[pygame.K_DOWN] and self.y < game_windowLen - self.height - self.vel:
            self.y += self.vel
            self.left = False
            self.right = False
            self.up = False
            self.down = True
            lastKeyPressed = 4

        if not any((keys[pygame.K_UP], keys[pygame.K_DOWN], keys[pygame.K_LEFT], keys[pygame.K_RIGHT])):
            self.left = False
            self.right = False
            self.up = False
            self.down = False

    def draw(self, window):
        
        if self.walkCount + 1 >= 3:
            self.walkCount = 0

        if self.right:
            currentPlayerImage = walkRight[self.walkCount]
            window.blit(currentPlayerImage,(self.x,self.y))
            self.walkCount += 1
        elif self.left:
            currentPlayerImage = walkLeft[self.walkCount]
            window.blit(currentPlayerImage, (self.x,self.y))
            self.walkCount += 1
        elif self.up:
            currentPlayerImage = walkUp[self.walkCount]
            window.blit(currentPlayerImage, (self.x,self.y))
            self.walkCount += 1
        elif self.down:
            currentPlayerImage = walkDown[self.walkCount]
            window.blit(currentPlayerImage, (self.x,self.y))
            self.walkCount += 1
        else:
            if lastKeyPressed == 1:
                currentPlayerImage = standLeft
                window.blit(standLeft, (self.x,self.y)) 
            elif lastKeyPressed == 2:
                currentPlayerImage = standRight
                window.blit(standRight, (self.x,self.y))
            elif lastKeyPressed == 3:
                currentPlayerImage = standUp
                window.blit(standUp, (self.x,self.y)) 
            elif lastKeyPressed == 4:
                currentPlayerImage = standDown
                window.blit(standDown, (self.x,self.y)) 

        self.hitbox = (self.x, self.y, 25,55)               # hitbox
        # pygame.draw.rect(window, (255,0,0), self.hitbox,2)  # Red hitbox rect - uncomment for debug
            
class collisionObject(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height        

# Call main loop

if __name__ == "__main__":
    main()