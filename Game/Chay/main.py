import pygame
fps=pygame.time.Clock()
def setup():
	pygame.init()
	screen = pygame.display.set_mode((300,400))
	title = pygame.display.set_caption('Litle Boy')
	icon = pygame.image.load(r'icon.jpg')
def mainloop():
	setup()
	fps.tick(60)
	run=True
	while run:
		for event in 
mainloop()