import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 600, 400
BG_COLOR = (255, 255, 255)
PLAYER_COLOR = (0, 0, 255)  # Синий круг
RECT_COLOR = (255, 0, 0)  # Красные квадраты
PLAYER_RADIUS = 20
RECT_SIZE = 30
PLAYER_SPEED = 3
GRAVITY = 2  # Скорость падения объектов
SPAWN_INTERVAL = 1000  # Квадраты появляются каждую 1 секунду
MAX_OBJECTS = 20  # Увеличено количество объектов

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Objects Game")
clock = pygame.time.Clock()

# Шрифт для счётчика
font = pygame.font.Font(None, 36)

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_RADIUS * 2, PLAYER_RADIUS * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, PLAYER_COLOR, (PLAYER_RADIUS, PLAYER_RADIUS), PLAYER_RADIUS)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

        self.rect.clamp_ip(screen.get_rect())

# Класс падающего объекта
class FallingObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((RECT_SIZE, RECT_SIZE))
        self.image.fill(RECT_COLOR)
        self.rect = self.image.get_rect(center=(random.randint(RECT_SIZE // 2, WIDTH - RECT_SIZE // 2), 0))

    def update(self):
        self.rect.y += GRAVITY
        if self.rect.top >= HEIGHT:
            self.kill()

# Создание игрока и группы спрайтов
player = Player()
all_sprites = pygame.sprite.Group(player)
falling_objects = pygame.sprite.Group()

# Таймер появления объектов
pygame.time.set_timer(pygame.USEREVENT, SPAWN_INTERVAL)

# Счётчик столкновений
collision_count = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT:
            if len(falling_objects) < MAX_OBJECTS:
                new_object = FallingObject()
                all_sprites.add(new_object)
                falling_objects.add(new_object)

    # Получение нажатых клавиш
    keys = pygame.key.get_pressed()
    player.update(keys)

    # Обновление объектов
    falling_objects.update()

    # Проверка столкновений
    if pygame.sprite.spritecollide(player, falling_objects, True):
        collision_count += 1

    # Отрисовка
    screen.fill(BG_COLOR)
    all_sprites.draw(screen)

    # Отображение счётчика столкновений
    score_text = font.render(f"Collisions: {collision_count}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
