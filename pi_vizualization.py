import math
import pygame

def side_size(R, n): # gets the side size of a regular polygon
    return 2 * R * math.sin(math.pi / n)

def Area(R, n): # gets the area of a regular polygon
    return (n / 2) * (R ** 2) * math.sin(2 * math.pi / n)

def get_angle(n): # gets the angle of a regular polygon
    return 2 * math.pi / n

def get_pi(n, Area): # gets the value of pi
    return Area(R, n) / (R ** 2)

def get_vetices(cx, cy, R, n): # gets the vertices of a regular polygon
    vertices = []
    for i in range(n):
        angle = get_angle(n) * i 
        x = cx + R * math.cos(angle)
        y = cy + R * math.sin(angle)
        vertices.append((x, y))
    return vertices

# Main variables
R = 400 # Radius
n = 3 # Inital number of sides

# Pygame setup
x, y = 1920, 1080

pygame.init()
size = (x, y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Get Pi")

cx = x/2
cy = y/2


running = True
auto_increment = False

while running:
    angle = get_angle(n) 
    area = Area(R, n)
    side = side_size(R, n)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                n -= 1
            elif event.key == pygame.K_RIGHT:
                n += 1
            elif event.key == pygame.K_SPACE:
                auto_increment = not auto_increment


    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Draw the circle
    pygame.draw.circle(screen, (0, 0, 0), (cx, cy), R, 1)

    # Draw the polygon
    vertices = get_vetices(cx, cy, R, n)
    pygame.draw.polygon(screen, (0, 0, 0), vertices, 1)


    # text
    font = pygame.font.Font(None, 36)
    text = font.render(f"n: {n}, Pi: {get_pi(n, Area)}", True, (0, 0, 0))
    text_rect = text.get_rect(center=(cx, y - 50))
    screen.blit(text, text_rect)

    pygame.display.flip()
    pygame.time.Clock().tick(60)
    
    if auto_increment:
        n += 1
        pygame.time.delay(200)

    

pygame.quit()