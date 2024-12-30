import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Initialize pygame
    pygame.init()

    # Set up display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(None, 36)

    # Initialize the clock
    clock = pygame.time.Clock()
    dt = 0

    # Create variables
    score = 0
    lives = 3

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add Player to groups
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Add Asteroid to groups
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    # Add Shot to groups
    Shot.containers = (shots, updatable, drawable)

    # Create an AsteroidField object
    asteroid_field = AsteroidField()

    def respawn_player():
        player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        player.rotation = 0
        player.velocity = pygame.Vector2(0, 0)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Calculate delta time
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds

        # Update all updatable objects
        for obj in updatable:
            obj.update(dt)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                lives -= 1
                if lives <= 0:
                    print("Game over!")
                    return
                else:
                    respawn_player()

        # Check for collisions between shots and asteroids
        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.split()
                    score += 100  # Increase score by 100 for each destroyed asteroid

        # Fill the screen with black color
        screen.fill((0, 0, 0))

        # Draw all drawable objects
        for obj in drawable:
            obj.draw(screen)

        # Display the score and lives
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 40))

        # Refresh the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()
