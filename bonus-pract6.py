import pygame
import sys

from practice6_homework import Field

# Initialize pygame
pygame.init()

# Set up the window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("circles example")

circles = []
f1 = Field()
f1.field_size = 100  # Using setter method to update field_size
f1.circles_amount = 200  # Using setter method to update circles_amount


WHITE = (255, 255, 255)
BLUE = (0, 128, 255, 30)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional, for visualization)
    screen.fill((0,) * 3)
    f1.run()
    for circle in f1._circles:
        viewcoords = circle.coords[0] + f1.field_size, circle.coords[1] + f1.field_size
        pygame.draw.circle(screen, BLUE, viewcoords, circle.radius)
    f1.move()

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()