import pygame
pygame.mixer.pre_init(48000,-16, 2, 1024)
pygame.init()

windowWid = 650
windowLen = 450
window = pygame.display.set_mode((windowWid,windowLen))
pygame.display.set_caption("WIP walkaround")

clock = pygame.time.Clock()

walkRight = [pygame.image.load('Sprites/R1.png'),pygame.image.load('Sprites/R2.png'),pygame.image.load('Sprites/R3.png'),pygame.image.load('Sprites/R4.png')]
walkLeft = [pygame.image.load('Sprites/L1.png'),pygame.image.load('Sprites/L2.png'),pygame.image.load('Sprites/L3.png'),pygame.image.load('Sprites/L4.png')]
walkUp = [pygame.image.load('Sprites/U1.png'),pygame.image.load('Sprites/U2.png'),pygame.image.load('Sprites/U3.png'),pygame.image.load('Sprites/U4.png')]
walkDown = [pygame.image.load('Sprites/D1.png'),pygame.image.load('Sprites/D2.png'),pygame.image.load('Sprites/D3.png'),pygame.image.load('Sprites/D4.png')]
char = pygame.image.load('Sprites/CHAR.png')
bg1 = pygame.image.load('Background Art/BG1.png')

# SOUND

pygame.mixer.music.load('Music/bgm_void.wav')
pygame.mixer.music.play()


# PLAYER object

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10

        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0

        self.hitbox = (self.x, self.y, 30,60)               #hitbox

    def draw(self, window):
        
        if self.walkCount + 1 >= 5:
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
            window.blit(char, (self.x, self.y))

        self.hitbox = (self.x, self.y, 30,60)               # hitbox
        pygame.draw.rect(window, (255,0,0), self.hitbox,2)  # hitbox
            

def redrawGameWindow():
    global walkCount
    
    # Window redraw BG
    window.blit(bg1, (0,0))

    # Window redraw playerA
    playerA.draw(window)

    # Update
    pygame.display.update()

playerA = player(325,225,30,60)
run = True
while run:
    # FPS
    clock.tick(12)

    # BGM loop

    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play(-1,7)   ##FIX THIS
    
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
    elif keys[pygame.K_RIGHT] and playerA.x < windowWid - playerA.width - playerA.vel:
        playerA.x += playerA.vel
        playerA.left = False
        playerA.right = True
        playerA.up = False
        playerA.down = False
    elif keys[pygame.K_UP] and playerA.y > playerA.vel:
        playerA.y -= playerA.vel
        playerA.left = False
        playerA.right = False
        playerA.up = True
        playerA.down = False
    elif keys[pygame.K_DOWN] and playerA.y < windowLen - playerA.height - playerA.vel:
        playerA.y += playerA.vel
        playerA.left = False
        playerA.right = False
        playerA.up = False
        playerA.down = True
    else:
        playerA.left = False
        playerA.right = False
        playerA.up = False
        playerA.down = False
        playerA.walkCount = 0

    # CALL FUNCTION AT END #
    redrawGameWindow()

pygame.quit()
