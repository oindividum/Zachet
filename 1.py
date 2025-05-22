import pygame

pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)  # Белый фон
CIRCLE_COLOR = (255, 0, 0)  # Красный круг
CIRCLE_RADIUS = 50
CIRCLE_SPEED = 5

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Circle")

# Переменные для движения круга
x = WIDTH // 2
y = HEIGHT // 2
speed_x = CIRCLE_SPEED

# Установка FPS
clock = pygame.time.Clock()

# Основной игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление позиции круга
    x += speed_x

    # Проверка границ и изменение направления
    if x - CIRCLE_RADIUS <= 0 or x + CIRCLE_RADIUS >= WIDTH:
        speed_x = -speed_x

    # Отрисовка
    screen.fill(BG_COLOR)
    pygame.draw.circle(screen, CIRCLE_COLOR, (x, y), CIRCLE_RADIUS)

    # Обновление экрана
    pygame.display.flip()

    # Ограничение FPS
    clock.tick(60)

# Завершение работы Pygame
pygame.quit()
