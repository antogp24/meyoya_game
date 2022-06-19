import pygame

def check(rect, tiles):
	hit_list = []
	for tile in tiles:
		if rect.colliderect(tile):
			hit_list.append(tile)
	return hit_list

def move(rect, tiles, scalar):
	# Dictionary to keep track of the
	# sides the rect collided with
	collision_types = {
		'left' : False,
		'right' : False,
		'top' : False,
		'bottom' : False
	}

	# Move on the x axis
	rect.x += scalar[0]
	# Check collisions on the x axis
	collisions = check(rect, tiles)
	# Handle the collisions on the x axis
	for tile in collisions:
		if scalar[0] < 0:
			rect.left = tile.right
			collision_types['left'] = True
		elif scalar[0] > 0:
			rect.right = tile.left
			collision_types['right'] = True

	# Move on the y axis
	rect.y += scalar[1]
	# Check collisions on the y axis
	collisions = check(rect, tiles)
	# Handle the collisions on the y axis
	for tile in collisions:
		if scalar[1] > 0:
			rect.bottom = tile.top
			collision_types['bottom'] = True
		elif scalar[1] < 0:
			collision_types['top'] = True
			rect.top = tile.bottom
	
	return rect, collision_types
