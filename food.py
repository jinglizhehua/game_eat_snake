import pygame
import random
from pygame.color import THECOLORS
from snake import Snake
from snake_block import SnakeBlock

class Food(SnakeBlock):
    def __init__(self, screen: pygame.Surface, background_color: tuple, img: str, snake: Snake,
                 screen_size=[800, 600], size=20):
        super(Food, self).__init__(screen, img, 0, 0, size)
        pygame.draw.rect(self.screen, background_color, [0, 0, self.size, self.size], 0)
        self.background_color = background_color
        self.screen_size = screen_size
        self.snake = snake
        self.refresh()

    def move_to(self, x: int, y: int, back_ground_color: tuple):
        self.screen.blit(self.img, [x * self.size, y * self.size])
        self.x = x
        self.y = y

    def refresh(self) -> bool:
        """ 返回False表示已经没有地方生成食物 """
        # 先检查蛇身有没有占满屏幕
        check = [[0 for _ in range(self.screen_size[0]//self.size)] for _ in range(self.screen_size[1]//self.size)]
        check[self.snake.head.y][self.snake.head.x] = 1
        for node in self.snake.body:
            check[node.y][node.x] = 1
        is_full = True
        for i in range(self.screen_size[1]//self.size):
            for j in range(self.screen_size[0]//self.size):
                if check[i][j] == 0:
                    is_full = False
        if is_full:
            return False

        # 生成食物
        x, y = None, None
        loop = True
        while loop:
            loop = False
            x = random.randint(0, self.screen_size[0]//self.size-1)
            y = random.randint(0, self.screen_size[1]//self.size-1)
            if x == self.snake.head.x and y == self.snake.head.y:
                loop = True
                continue
            for node in self.snake.body:
                if x == node.x and y == node.y:
                    loop = True
        self.move_to(x, y, self.background_color)
        return True

