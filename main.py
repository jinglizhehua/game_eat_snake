# coding=utf-8
import pygame
from pygame.color import THECOLORS
from snake import Snake
from snake_block import SnakeBlock
from food import Food

def main():
    game_run_flag = True
    background_color = THECOLORS['white']
    size = 150
    screen_size = [800, 600]
    speed = 1

    pygame.init()
    screen = pygame.display.set_mode(screen_size)    # type: pygame.Surface
    screen.fill(background_color)
    snake = Snake(screen, background_color, size=size)
    food = Food(screen, background_color, '方块蛋糕.png', snake, screen_size, size)
    pygame.display.flip()

    font = pygame.font.Font('simsun.ttc', 30)

    cnt = 0
    while game_run_flag:
        pygame.time.delay(10)
        cnt += 1

        # loop
        if cnt >= 40 + 1 - speed:
            cnt = 0
            pygame.draw.rect(screen, background_color, [650, 0, 150, 30], 0)
            screen.blit(font.render('速度：' + str(speed), False, THECOLORS['black']), [650, 0])
            is_eat, is_end = snake.go(food)
            if is_eat:
                if food.refresh() is False:     # 蛇占满屏幕
                    game_run_flag = False
                    pygame.quit()
                    continue
            if is_end:
                game_run_flag = False
                pygame.quit()
                continue
            pygame.display.flip()

        # input and exit
        for event in pygame.event.get():    # type: pygame.event
            if event.type == pygame.QUIT:
                game_run_flag = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.set_direction('up')
                if event.key == pygame.K_DOWN:
                    snake.set_direction('down')
                if event.key == pygame.K_LEFT:
                    snake.set_direction('left')
                if event.key == pygame.K_RIGHT:
                    snake.set_direction('right')
                if event.key == pygame.K_l:
                    snake.append_a_body()
                if event.key == pygame.K_LEFTBRACKET:   # [
                    if speed > 1:
                        speed -= 1
                if event.key == pygame.K_RIGHTBRACKET:  # ]
                    if speed < 40:
                        speed += 1


if __name__ == '__main__':
    main()
