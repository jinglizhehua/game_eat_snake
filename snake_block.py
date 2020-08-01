import pygame
from pygame.color import THECOLORS

class SnakeBlock:
    def __init__(self, screen: pygame.Surface, img: str, x: int, y: int, size=20):
        self.screen = screen
        self.size = size      # 蛇身的大小，单位是像素
        self.img = pygame.transform.scale(pygame.image.load(img), (size, size))   # type: pygame.Surface
        self.x = x  # x, y都表示该方块左上角坐标
        self.y = y

        self.screen.blit(self.img, [self.x * self.size, self.y * self.size])

    def set_position(self, x: int, y: int):
        self.x = x
        self.y = y

    def move_to(self, x: int, y: int, back_ground_color: tuple):
        pygame.draw.rect(self.screen, back_ground_color, [self.x * self.size, self.y * self.size, self.size, self.size], 0)
        self.screen.blit(self.img, [x * self.size, y * self.size])
        self.x = x
        self.y = y

class SnakeHead(SnakeBlock):
    def __init__(self, screen: pygame.Surface, img: str, x: int, y: int, size=20):
        super(SnakeHead, self).__init__(screen, img, x, y, size)

    def display(self):
        self.screen.blit(self.img, [self.x * self.size, self.y * self.size])
