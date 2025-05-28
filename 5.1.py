import pygame

# Инициализация Pygame
pygame.init()

# Размер окна
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("House Drawing")

# Цвета
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BROWN = (139, 69, 19)

# Установка частоты обновления
clock = pygame.time.Clock()

# Основной цикл программы
running = True
while running:
    screen.fill(WHITE)

    # Рисование дома (координаты центра окна)
    house_rect = pygame.Rect(150, 150, 100, 80)  # Основа дома
    pygame.draw.rect(screen, BLUE, house_rect)

    # Рисование крыши
    roof_points = [(150, 150), (250, 150), (200, 100)]
    pygame.draw.polygon(screen, RED, roof_points)

    # Рисование двери
    door_rect = pygame.Rect(190, 190, 20, 40)
    pygame.draw.rect(screen, BROWN, door_rect)

    # Обновление экрана
    pygame.display.update()
    clock.tick(60)

    # Обработка выхода
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
