import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 600
pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Renk Çarkı")
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.rect.centery -= 5
        else:
            self.rect.centery += 5
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT


class Wheel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((200, 200))
        self.image.fill((255, 255, 255))
        pygame.draw.circle(self.image, (255, 0, 0), (100, 100), 100)
        pygame.draw.circle(self.image, (0, 255, 0), (100, 100), 50)
        pygame.draw.circle(self.image, (0, 0, 255), (100, 100), 25)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5
        self.direction = random.choice([-1, 1])

    def update(self):
        self.rect.centery += self.speed * self.direction
        if self.rect.top <= 0:
            self.direction = 1
        if self.rect.bottom >= HEIGHT:
            self.direction = -1
player = Player()
wheel = Wheel()
all_sprites = pygame.sprite.Group(player, wheel)

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    if pygame.sprite.collide_rect(player, wheel):
        print("Oyun Bitti!")

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
