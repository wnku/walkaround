import pygame
pygame.mixer.pre_init(48000,-16, 2, 1024)
pygame.init()

game_windowWid = 650
game_windowLen = 450
game_window = pygame.display.set_mode((game_windowWid,game_windowLen))
pygame.display.set_caption("WIP walkaround")

clock = pygame.time.Clock()

walkLeft = [pygame.image.load('Sprites/walking_left1.png'),pygame.image.load('Sprites/walking_left2.png')]
walkRight = [pygame.image.load('Sprites/walking_right1.png'),pygame.image.load('Sprites/walking_right2.png')]
walkUp = [pygame.image.load('Sprites/walking_up1.png'),pygame.image.load('Sprites/walking_up2.png')]
walkDown = [pygame.image.load('Sprites/walking_down1.png'),pygame.image.load('Sprites/walking_down2.png')]

standLeft = pygame.image.load('Sprites/standing_left.png')
standRight = pygame.image.load('Sprites/standing_right.png')
standUp = pygame.image.load('Sprites/standing_up.png')
standDown = pygame.image.load('Sprites/standing_down.png')


bg1 = pygame.image.load('Background Art/BG1.png')

# SOUND

pygame.mixer.music.load('Music/bgm_void.ogg')
pygame.mixer.music.play()

# PLAYER object

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 8

        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0

        self.hitbox = (self.x, self.y, 25,55)               #hitbox

    def draw(self, window):
        
        if self.walkCount + 1 >= 3:
            self.walkCount = 0

        if self.right:
            window.blit(walkRight[self.walkCount],(self.x,self.y))
            self.walkCount += 1
        elif self.left:
            window.blit(walkLeft[self.walkCount], (self.x,self.y))
            self.walkCount += 1
        elif self.up:
            window.blit(walkUp[self.walkCount], (self.x,self.y))
            self.walkCount += 1
        elif self.down:
            window.blit(walkDown[self.walkCount], (self.x,self.y))
            self.walkCount += 1
        else:
            if lastKeyPressed == 1:
                window.blit(standLeft, (self.x,self.y)) 
            elif lastKeyPressed == 2:
               window.blit(standRight, (self.x,self.y)) 
            elif lastKeyPressed == 3:
                window.blit(standUp, (self.x,self.y)) 
            elif lastKeyPressed == 4:
                window.blit(standDown, (self.x,self.y)) 

        self.hitbox = (self.x, self.y, 25,55)               # hitbox
        # pygame.draw.rect(window, (255,0,0), self.hitbox,2)  # hitbox
            
class collisionObject(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

def redrawGameWindow():
    global walkCount
    
    # Window redraw BG
    game_window.blit(bg1, (0,0))

    # Window redraw playerA
    playerA.draw(game_window)

    # Update
    pygame.display.update()

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
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and playerA.x > playerA.vel:
        playerA.x -= playerA.vel
        playerA.left = True
        playerA.right = False
        playerA.up = False
        playerA.down = False
        lastKeyPressed = 1
    elif keys[pygame.K_RIGHT] and playerA.x < game_windowWid - playerA.width - playerA.vel:
        playerA.x += playerA.vel
        playerA.left = False
        playerA.right = True
        playerA.up = False
        playerA.down = False
        lastKeyPressed = 2

    if keys[pygame.K_UP] and playerA.y > playerA.vel:
        playerA.y -= playerA.vel
        playerA.left = False
        playerA.right = False
        playerA.up = True
        playerA.down = False
        lastKeyPressed = 3
    elif keys[pygame.K_DOWN] and playerA.y < game_windowLen - playerA.height - playerA.vel:
        playerA.y += playerA.vel
        playerA.left = False
        playerA.right = False
        playerA.up = False
        playerA.down = True
        lastKeyPressed = 4

    if not any((keys[pygame.K_UP], keys[pygame.K_DOWN], keys[pygame.K_LEFT], keys[pygame.K_RIGHT])):
        playerA.left = False
        playerA.right = False
        playerA.up = False
        playerA.down = False
        playerA.walkCount = 0

    # CALL FUNCTION AT END #
    redrawGameWindow()

pygame.quit()
