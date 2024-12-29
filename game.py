import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Objects!")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

basket_width = 100
basket_height = 20
basket = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50, basket_width, basket_height)

object_width = 30
object_height = 30
objects = []
object_speed = 5

score = 0
lives = 5

def add_object():
    x = random.randint(0, SCREEN_WIDTH - object_width)
    y = -object_height
    obj = pygame.Rect(x, y, object_width, object_height)
    objects.append(obj)

def draw():
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, basket)

    for obj in objects:
        pygame.draw.rect(screen, RED, obj)

    score_text = font.render(f"Score: {score}", True, BLACK)
    lives_text = font.render(f"Lives: {lives}", True, BLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 50))

    pygame.display.flip()

def main():
    global score, lives
    add_object()  # Add the first object

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket.left > 0:
            basket.move_ip(-10, 0)
        if keys[pygame.K_RIGHT] and basket.right < SCREEN_WIDTH:
            basket.move_ip(10, 0)

        # Move objects
        for obj in objects[:]:
            obj.move_ip(0, object_speed)

            # Check for collision with basket
            if obj.colliderect(basket):
                objects.remove(obj)
                score += 1

            # Check if object goes off screen
            elif obj.top > SCREEN_HEIGHT:
                objects.remove(obj)
                lives -= 1

                # Game over condition
                if lives <= 0:
                    running = False

        # Add new objects periodically
        if random.randint(1, 30) == 1:
            add_object()

        # Draw everything
        draw()

        # Control the frame rate
        clock.tick(30)

    # Game Over
    game_over_text = font.render("Game Over!", True, RED)
    screen.fill(WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)

# Run the game
if __name__ == "__main__":
    main()
