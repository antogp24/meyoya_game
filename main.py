import pygame, sys
from pygame.locals import *
from player import *
from tiles import *


# Init Functions
# ---------------------------------- #
pygame.init() # for everything else
pygame.mixer.init() # for music

# FPS setup
# ---------------------------------- #
FPS = 60
clock = pygame.time.Clock()

# Display
# ---------------------------------- #
window_size = [640, 480]

window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Nigger Game")

# Custom Class Instances
# ---------------------------------- #
monda = Player(5, 4)
monda.scale_textures()

# Loading Sounds
# ---------------------------------- #
pygame.mixer.music.load("data/audio/cunumi.mp3")
pygame.mixer.music.play(-1) # Has -1 as a parameter to loop the song

# C style main function
def main():
	while True:
		window.fill( (255, 255, 255) ) # White Background
		# Logic
		# ---------------------------------- #
		monda.movement(tiles)
		# ---------------------------------- #
		# Draw
		# ---------------------------------- #
		monda.render(window)
		tiles_render(window)
		# ---------------------------------- #
		# Input
		# ---------------------------------- #
		for event in pygame.event.get():
			if event.type == QUIT or (
			event.type == KEYDOWN and
			event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			# Custom Input Functions
			monda.input_check(event, K_LEFT, K_RIGHT, K_UP, K_DOWN)
			monda.input_check(event, K_a, K_d, K_w, K_s)
		# ---------------------------------- #
		pygame.display.update()
		clock.tick(FPS)

main()
