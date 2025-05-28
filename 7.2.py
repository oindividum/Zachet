import pygame
import math

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Colorful Shapes")
clock = pygame.time.Clock()

# Определение цветов
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)


# Функция для создания точек звезды
def get_star_points(center_x, center_y, outer_radius, inner_radius, points=5):
    star_points = []
    for i in range(points * 2):
        angle = i * math.pi / points - math.pi / 2  # Начало сверху
        radius = outer_radius if i % 2 == 0 else inner_radius
        x = center_x + math.cos(angle) * radius
        y = center_y + math.sin(angle) * radius
        star_points.append((x, y))
    return star_points


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    screen.fill(WHITE)

    # Рисование круга (красный, центр в (100, 100))
    pygame.draw.circle(screen, RED, (100, 100), 30)

    # Рисование прямоугольника (синий, верхний левый угол в (250, 80))
    pygame.draw.rect(screen, BLUE, (250, 80, 60, 40))

    # Рисование звезды (жёлтая, центр в (100, 300))
    star_points = get_star_points(100, 300, 30, 15)
    pygame.draw.polygon(screen, YELLOW, star_points)

    # Рисование треугольника (зелёный, вершины указаны)
    triangle_points = [(250, 280), (300, 360), (200, 360)]
    pygame.draw.polygon(screen, GREEN, triangle_points)

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)

# Завершение Pygame
pygame.quit()