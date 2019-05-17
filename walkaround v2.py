#

import pygame
import pytmx
from pytmx.util_pygame import load_pygame

pygame.init()

#

scopeWid = 650
scopeLen = 450 # Set the initial position_on_map of the player to center of screen

game_window = pygame.display.set_mode((scopeWid,scopeLen)) # Create game window using size of Scope (camera)
pygame.display.set_caption("WIP walkaround")

#

walkLeft = [pygame.image.load('Sprites/walking_left1.png').convert_alpha(),pygame.image.load('Sprites/walking_left2.png').convert_alpha()]
walkRight = [pygame.image.load('Sprites/walking_right1.png').convert_alpha(),pygame.image.load('Sprites/walking_right2.png').convert_alpha()]
walkUp = [pygame.image.load('Sprites/walking_up1.png').convert_alpha(),pygame.image.load('Sprites/walking_up2.png').convert_alpha()]
walkDown = [pygame.image.load('Sprites/walking_down1.png').convert_alpha(),pygame.image.load('Sprites/walking_down2.png').convert_alpha()]
standLeft = pygame.image.load('Sprites/standing_left.png').convert_alpha()
standRight = pygame.image.load('Sprites/standing_right.png').convert_alpha()
standUp = pygame.image.load('Sprites/standing_up.png').convert_alpha()
standDown = pygame.image.load('Sprites/standing_down.png').convert_alpha()
currentPlayerImage = standDown
playerImageLen = standDown.get_rect().size[0]
playerImageHt = standDown.get_rect().size[1]

#

position_on_screen = (scopeWid / 2 - playerImageLen /2 +10, scopeLen / 2 - playerImageHt/2 + 22)

#

background_image = pygame.image.load('Maps/background_layer.png').convert_alpha()
foreground_image = pygame.image.load('Maps/foreground_layer.png').convert_alpha()

game_mapWid = background_image.get_rect().size[0] # Get the size of the base image.
game_mapLen = background_image.get_rect().size[1]

#

clock = pygame.time.Clock()

#

def main():
	global player, lkp
	run = True	# Enable while loop
	lkp = 4 	# Last key press state - default (down)

	# Create objects on screen
	player = playerObject(150,150,playerImageLen,playerImageHt)

	while run:
		# Set FPS
		clock.tick(20)

		# Check for quit
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		player.checkMovement() 	#Check for movement
		redrawGameWindow()		# Redraw window for next frame

	pygame.quit()

def redrawGameWindow():
    # Window redraw BG

    scopeRect = (player.x - scopeWid/2, player.y - scopeLen/2, scopeWid, scopeLen) # Map scope

    game_window.fill((9,18,23))
    game_window.blit(background_image, (0,0), scopeRect)

    # Window redraw player
    player.draw(game_window)

    # Update
    pygame.display.update()

#

class gameObject(object):
	def __init__(self,x,y,width,height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

class playerObject(object):
    # Init, setup whatever
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 8
        self.left = self.right = self.up = self.down = False
        self.walkCount = 0
        self.hitbox_x = position_on_screen[0]+5
        self.hitbox_y = position_on_screen[1]+10
        self.hitbox_wid = 15     
        self.hitbox_len = 45  #Allows hitbox for collision use later

    def checkMovement(self):								# Allows for control of the user character, changing directional variables for left right up down
        global lkp, keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > self.vel:		#Extra complication used to prevent character from escaping map grounds - Left wall
            self.x -= self.vel
            self.left = True
            self.right = False
            self.up = False
            self.down = False
            lkp = 1
        elif keys[pygame.K_RIGHT] and self.x < game_mapWid - self.width - self.vel:	# Right wall escape prevention
            self.x += self.vel
            self.left = False
            self.right = True
            self.up = False
            self.down = False
            lkp = 2

        if keys[pygame.K_UP] and self.y > self.vel: # Top wall escape prevention
            self.y -= self.vel
            self.left = False
            self.right = False
            self.up = True
            self.down = False
            lkp = 3
        elif keys[pygame.K_DOWN] and self.y < game_mapLen - self.height - self.vel:	#Lower boundary escape prev.
            self.y += self.vel
            self.left = False
            self.right = False
            self.up = False
            self.down = True
            lkp = 4

        if not any((keys[pygame.K_UP], keys[pygame.K_DOWN], keys[pygame.K_LEFT], keys[pygame.K_RIGHT])): #If there's nothing, do nothing. Do not update lkp (Last key press) - we need to remember that
            self.left = False	
            self.right = False
            self.up = False
            self.down = False

    def draw(self, window):
        global keys
        
        if self.walkCount + 1 >= 3:	# If walk count exceeds the amount of frames loaded in walkLeft/Right etc, reset to 0. 
            self.walkCount = 0

        if keys[pygame.K_h]:
        	pygame.draw.rect(game_window, (255,0,0), (self.hitbox_x,self.hitbox_y,self.hitbox_wid,self.hitbox_len),1)  # Red hitbox rect - uncomment for debug

        if self.right:										# Save current image for mask and blit
            currentPlayerImage = walkRight[self.walkCount]
            window.blit(currentPlayerImage,(position_on_screen))
            self.walkCount += 1
        elif self.left:
            currentPlayerImage = walkLeft[self.walkCount]
            window.blit(currentPlayerImage, (position_on_screen))
            self.walkCount += 1
        elif self.up:
            currentPlayerImage = walkUp[self.walkCount]
            window.blit(currentPlayerImage, (position_on_screen))
            self.walkCount += 1
        elif self.down:
            currentPlayerImage = walkDown[self.walkCount]
            window.blit(currentPlayerImage, (position_on_screen))
            self.walkCount += 1
        else:
            if lkp == 1:							# Remember last direction
                currentPlayerImage = standLeft
                window.blit(standLeft, (position_on_screen)) 
            elif lkp == 2:
                currentPlayerImage = standRight
                window.blit(standRight, (position_on_screen))
            elif lkp == 3:
                currentPlayerImage = standUp
                window.blit(standUp, (position_on_screen)) 
            elif lkp == 4:
                currentPlayerImage = standDown
                window.blit(standDown, (position_on_screen))
        
if __name__ == "__main__":
    main()