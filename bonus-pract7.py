import pygame
import sys
import time

from practice7_homework import Field, CircleForest

# Initialize pygame
pygame.init()

# Set up the window
screen_width, screen_height = 1000, 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Circles Example")

f1 = Field()
# f1.field_size = 800  # Increase the field size
# f1.circles_amount = 20 # Number of circles

WHITE = (255, 255, 255)
BLUE = (0, 128, 255)
GREEN = (0, 255, 1)
RED = (255, 0, 0)
OUTLINE_COLOR = (255, 255, 255)  # Color for the circle outline


# Scale the coordinates of circles to fit the entire window
def scale_coords(coords, field_size, screen_width, screen_height):
    x, y = coords
    scale_x = (x + field_size) / (2 * field_size) * screen_width
    scale_y = (y + field_size) / (2 * field_size) * screen_height
    return int(scale_x), int(scale_y)


# Draw a circle with an outline on a transparent surface
def draw_circle_with_outline(surface, color, outline_color, center, radius, outline_width=2, alpha=128):
    temp_surface = pygame.Surface((radius * 2 + outline_width * 2, radius * 2 + outline_width * 2), pygame.SRCALPHA)
    temp_surface = temp_surface.convert_alpha()
    temp_center = (radius + outline_width, radius + outline_width)

    # Draw the outline
    pygame.draw.circle(temp_surface, outline_color + (alpha,), temp_center, radius + outline_width)
    # Draw the circle
    pygame.draw.circle(temp_surface, color + (alpha,), temp_center, radius)

    # Blit the transparent surface onto the main surface
    surface.blit(temp_surface, (center[0] - temp_center[0], center[1] - temp_center[1]))


# Recursive function to draw lines between parent and children
def draw_connections(surface, parent, parent_coords, field_size, screen_width, screen_height):
    for child in parent.children:
        child_coords = scale_coords(child._coords, field_size, screen_width, screen_height)
        pygame.draw.line(surface, RED, parent_coords, child_coords)
        draw_connections(surface, child, child_coords, field_size, screen_width, screen_height)


# Main loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# Fill the screen with a color (optional, for visualization)
screen.fill((0,) * 3)

forest = CircleForest(f1._circles)

# Build the forest (all k-d trees)
forest.build_forest()

# Draw all circles in the field with an outline
for circle in f1._circles:
    viewcoords = scale_coords(circle._coords, f1.field_size, screen_width, screen_height)
    draw_circle_with_outline(screen, BLUE, OUTLINE_COLOR, viewcoords, circle._radius)

# Draw connections and circles in the forest with an outline
for circle, tree in forest.get_trees().items():
    viewcoords = scale_coords(circle._coords, f1.field_size, screen_width, screen_height)
    draw_circle_with_outline(screen, GREEN, OUTLINE_COLOR, viewcoords, circle._radius)
    draw_connections(screen, circle, viewcoords, f1.field_size, screen_width, screen_height)
    pygame.display.flip()
    time.sleep(2)

# # Update the display
# pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()