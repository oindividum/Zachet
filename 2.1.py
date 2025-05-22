import pygame

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sprite Collision")
clock = pygame.time.Clock()

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))  # Синий цвет
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 100, 100

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

# Класс препятствия
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 60), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (30, 30), 30)  # Красный круг
        self.rect = self.image.get_rect(center=(400, 300))

# Создание объектов
player = Player()
obstacle = Obstacle()

# Группы спрайтов
all_sprites = pygame.sprite.Group(player, obstacle)

collision_detected = False  # Флаг для отслеживания столкновения

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получение нажатых клавиш
    keys = pygame.key.get_pressed()
    player.update(keys)

    # Проверка коллизии (сообщение только при первом столкновении)
    if pygame.sprite.collide_rect(player, obstacle):
        if not collision_detected:
            print("Collision detected!")
            collision_detected = True
    else:
        collision_detected = False  # Если игрок ушёл, сбрасываем флаг

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
