import pygame

TILES_RES = 8
TILES_SCALE = 5
TILES_DIM = TILES_RES * TILES_SCALE

panocha_texture = pygame.image.load("data/gfx/panocha.png")
panocha_texture = pygame.transform.scale(panocha_texture, (TILES_DIM, TILES_DIM))

# Tiles Rect list
tiles = [
			pygame.Rect((40+TILES_DIM*0, 120), (TILES_DIM, TILES_DIM)),
			pygame.Rect((40+TILES_DIM*1, 120), (TILES_DIM, TILES_DIM)),
			pygame.Rect((40+TILES_DIM*2, 120), (TILES_DIM, TILES_DIM)),
			pygame.Rect((40+TILES_DIM*3, 120), (TILES_DIM, TILES_DIM)),
			pygame.Rect((40+TILES_DIM*4, 160), (TILES_DIM, TILES_DIM)),
			
			pygame.Rect((300+TILES_DIM*0, 220), (TILES_DIM, TILES_DIM)),
			pygame.Rect((300+TILES_DIM*1, 220), (TILES_DIM, TILES_DIM)),
			pygame.Rect((300+TILES_DIM*2, 220), (TILES_DIM, TILES_DIM)),
			pygame.Rect((300+TILES_DIM*3, 180), (TILES_DIM, TILES_DIM)),
			pygame.Rect((300+TILES_DIM*4, 180), (TILES_DIM, TILES_DIM)),
		]

def tiles_debug(color):
	for tile in tiles:
		pygame.draw.rect(window, color, tile)

def tiles_render(window):
	for tile in tiles:
		window.blit(panocha_texture, tile.topleft)
