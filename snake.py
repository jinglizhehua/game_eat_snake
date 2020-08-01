import pygame
from pygame.color import THECOLORS
from snake_block import SnakeBlock
from snake_block import SnakeHead

Directions = {'up': [0, -1], 'down': [0, 1], 'left': [-1, 0], 'right': [1, 0]}

class Snake:
    def __init__(self, screen: pygame.Surface, background_color: tuple,
                 length: int = 3, direction: str = 'right', x=None, y=None, size: int = 20,
                 screen_size=[800, 600]):
        self.screen = screen
        self.background_color = background_color
        self.length = length-1
        self.direction = direction
        if (x is None) or (y is None):
            self.x = screen_size[0]//2//size
            self.y = screen_size[1]//2//size
        else:
            self.x = x
            self.y = y
        self.size = size
        self.screen_size = screen_size

        self.head = SnakeHead(screen, '方块+.png', self.x, self.y, size)
        self.body = []
        self.input_enable = True

        for i in range(1, length+1):
            next_index = Directions[self.direction]
            self.body.append(SnakeBlock(screen, '方块-.png',
                                        self.x - next_index[0] * i, self.y - next_index[1] * i,
                                        size))

    def set_direction(self, direction: str):
        if self.input_enable:
            if self.direction == 'up' and direction == 'down':
                return
            if self.direction == 'down' and direction == 'up':
                return
            if self.direction == 'right' and direction == 'left':
                return
            if self.direction == 'left' and direction == 'right':
                return
            self.input_enable = False
            self.direction = direction

    def check_end(self):
        if self.head.x < 0 or self.head.x >= (self.screen_size[0]//self.size) or \
                self.head.y < 0 or self.head.y >= (self.screen_size[1]//self.size):
            return True
        for node in self.body:
            if self.head.x == node.x and self.head.y == node.y:
                return True
        return False

    def go(self, food: SnakeBlock):
        """ 第一个返回值为True表示吃到了实物，第二个返回值为True表示游戏结束 """
        self.input_enable = True

        x, y = self.head.x, self.head.y
        index = Directions[self.direction]
        self.head.move_to(self.head.x + index[0], self.head.y + index[1], self.background_color)

        # for node in self.body:
        #     temp_x, temp_y = x, y
        #     x, y = node.x, node.y
        #     node.move_to(temp_x, temp_y, self.background_color)
        node = self.body.pop()
        temp_x, temp_y = x, y
        x, y = node.x, node.y                   # 存储尾节点坐标，以便吃到食物后增加身体
        node.move_to(temp_x, temp_y, self.background_color)
        self.body.insert(0, node)

        # 头部显示刷新，以免尾部移动覆盖头部
        self.head.display()

        is_eat = False
        if self.head.x == food.x and self.head.y == food.y:
            self.body.append(SnakeBlock(self.screen, '方块-.png', x, y, self.size))
            is_eat = True
        return is_eat, self.check_end()

    def append_a_body(self):
        self.body.append(SnakeBlock(self.screen, '方块-.png', 0, 0, self.size))
