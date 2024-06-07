import pygame
import sys
import time  # Note this!
import random  # Note this!


class Raindrop:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5,15)


    def move(self):
        self.y = self.y + self.speed

    def off_screen(self):
        if self.y > 800:
            return True
        else:
            return False

    def draw(self):
        pygame.draw.line(self.screen, (0,0,150), (self.x, self.y), (self.x, self.y+5), 2)


class Hero:
    def __init__(self, screen, x, y, with_umbrella_filename, without_umbrella_filename):
        self.screen = screen
        self.x = x
        self.y = y
        self.image_umbrella = pygame.image.load(with_umbrella_filename)
        self.image_no_umbrella = pygame.image.load(without_umbrella_filename)
        self.last_hit_time = 0
    def draw(self):
        current_image = self.image_umbrella
        if time.time() > self.last_hit_time + 1:
            current_image = self.image_no_umbrella
        self.screen.blit(current_image, (self.x, self.y))

    def hit_by(self, raindrop):
        hero_hit_box = pygame.Rect(self.x, self.y, 170, 192)
        return hero_hit_box.collidepoint(raindrop.x, raindrop.y)

class Cloud:
    def __init__(self, screen, x, y, image_filename):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_filename)
        self.raindrops = []

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        drop = Raindrop(self.screen, random.randint(self.x, self.x + 300), (self.y + 100))
        self.raindrops.append(drop)


def main():

    pygame.init()
    screen = pygame.display.set_mode((1000,600))
    pygame.display.set_caption("Rainy Day")

    clock = pygame.time.Clock()

    mike = Hero(screen, 200,400, "Mike_umbrella.png", "Mike.png")

    alyssa = Hero(screen, 700,400, "Alyssa_umbrella.png", "Alyssa.png")

    cloud = Cloud(screen, 300, 50, 'cloud.png')

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_d]:
            cloud.x = cloud.x + 5
        if pressed_keys[pygame.K_a]:
            cloud.x = cloud.x - 5

        screen.fill((255,255,255))

        cloud.draw()

        cloud.rain()

        for raindrop in cloud.raindrops:

            raindrop.move()
            raindrop.draw()

            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)

            if alyssa.hit_by(raindrop):
                alyssa.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)

            if raindrop.off_screen():
                cloud.raindrops.remove(raindrop)

        mike.draw()
        alyssa.draw()
        pygame.display.update()

main()