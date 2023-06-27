import pygame

pygame.init()

# Create a game window
window_width = 550
window_height = 450
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Player Movement Example")

# Set up the speed of the player
player_speed = 5

clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.is_running = False
        self.is_jumping = False
        self.is_facing_left = False
        self.animation_index = 0
        self.idle = [pygame.image.load(r'idle/idle1.png'),
                     pygame.image.load(r'idle/idle2.png'),
                     pygame.image.load(r'idle/idle3.png'),
                     pygame.image.load(r'idle/idle4.png'),
                     pygame.image.load(r'idle/idle5.png')]
        self.run = [pygame.image.load(r'run/run1.png'),
                    pygame.image.load(r'run/run2.png'),
                    pygame.image.load(r'run/run3.png'),
                    pygame.image.load(r'run/run4.png'),
                    pygame.image.load(r'run/run5.png'),
                    pygame.image.load(r'run/run6.png'),
                    pygame.image.load(r'run/run7.png'),
                    pygame.image.load(r'run/run8.png')]
        self.jump = [pygame.image.load(r'jump/jump1.png'),
                     pygame.image.load(r'jump/jump2.png'),
                     pygame.image.load(r'jump/jump3.png'),
                     pygame.image.load(r'jump/jump4.png'),
                     pygame.image.load(r'jump/jump5.png'),
                     pygame.image.load(r'jump/jump6.png'),
                     pygame.image.load(r'jump/jump7.png'),
                     pygame.image.load(r'jump/jump8.png')]
        self.idle_left = []
        self.run_left = []
        self.jump_left = []

        for image in self.idle:
            self.idle_left.append(pygame.transform.flip(image, True, False))
        for image in self.run:
            self.run_left.append(pygame.transform.flip(image, True, False))
        for image in self.jump:
            self.jump_left.append(pygame.transform.flip(image, True, False))

    def animate(self, animation_list):
        self.animation_index += 1
        if self.animation_index >= len(animation_list) * 6:
            self.animation_index = 0
        return animation_list[self.animation_index // 6]

    def draw(self, camera_x):
        if self.is_running:
            if self.is_facing_left:
                animated_image = self.animate(self.run_left)
            else:
                animated_image = self.animate(self.run)
        elif self.is_jumping:
            if self.is_facing_left:
                animated_image = self.animate(self.jump_left)
            else:
                animated_image = self.animate(self.jump)
        else:
            if self.is_facing_left:
                animated_image = self.animate(self.idle_left)
            else:
                animated_image = self.animate(self.idle)
        player_rect = animated_image.get_rect()
        player_rect.x = self.x - camera_x
        player_rect.y = self.y
        window.blit(animated_image, (player_rect.x, player_rect.y))

        return player_rect

    def update_position(self, keys):
        self.is_running = False
        self.is_jumping = False

        if keys[pygame.K_LEFT]:
            self.x -= player_speed
            self.is_running = True
            self.is_facing_left = True
        if keys[pygame.K_RIGHT]:
            self.x += player_speed
            self.is_running = True
            self.is_facing_left = False
        if keys[pygame.K_SPACE]:
            self.is_jumping = True
            self.y -= player_speed
        if not self.is_running and not self.is_jumping:
            self.y += player_speed


floor = pygame.image.load(r'floor_wood_1.png')
floor_rect = floor.get_rect()
floor_rect.x = 32
floor_rect.y = 320

Map = pygame.image.load(r'layer_1.png')

player_width = 50
player_height = 50
player = Player(window_width // 2 - player_width // 2, window_height // 2 - player_height // 2, player_width, player_height)

camera_x = 0

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Update player position based on key input
    player.update_position(keys)

    # Adjust camera position based on player movement
    if player.x - camera_x > window_width * 0.6:
        camera_x = player.x - window_width * 0.6
    elif player.x - camera_x < window_width * 0.4:
        camera_x = player.x - window_width * 0.4

    # Check collision between player and floor
    if player.draw(camera_x).colliderect(floor_rect):
        player.y = floor_rect.y - player_height

    # Clear the screen
    window.blit(Map, (0, 0))

    # Draw the floor
    window.blit(floor, floor_rect)

    # Draw the player on the screen
    player.draw(camera_x)

    # Update the window display
    pygame.display.update()

pygame.quit()
