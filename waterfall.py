import pygame
import pandas as pd
import random

# Load the dataset
file_path = "genders.csv"  # Ensure the file is in the same directory
data = pd.read_csv(file_path)

# Aggregate male and female counts
gender_counts = data.groupby("gender")["count"].sum()
male_count = gender_counts.get("male", 0)
female_count = gender_counts.get("female", 0)

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)  # Black background
WHITE = (255, 255, 255)  # Snow color
LINE_COLOR = (200, 200, 200)  # Divider line
TEXT_COLOR = (255, 255, 255)  # Label text color
FONT_SIZE = 36
BASE_SNOW_COUNT = 100

# Determine snowfall and peak sizes
if male_count > female_count:
    snowfall_side = "left"
    peak_color_left = (0, 255, 0)  # Green for more males
    peak_color_right = (255, 0, 0)  # Red for fewer females
    snowflakes = [(random.randint(0, WIDTH // 2 - 10), random.randint(0, HEIGHT)) for _ in range(BASE_SNOW_COUNT)]
    peak_height_left = 200  # Bigger peak for more males
    peak_height_right = 50   # Smaller peak for fewer females
elif female_count > male_count:
    snowfall_side = "right"
    peak_color_right = (0, 255, 0)  # Green for more females
    peak_color_left = (255, 0, 0)  # Red for fewer males
    snowflakes = [(random.randint(WIDTH // 2 + 10, WIDTH), random.randint(0, HEIGHT)) for _ in range(BASE_SNOW_COUNT)]
    peak_height_right = 200  # Bigger peak for more females
    peak_height_left = 50   # Smaller peak for fewer males
else:
    snowfall_side = "both"
    peak_color_left = peak_color_right = (0, 255, 0)  # Green peaks for equal count
    snowflakes = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(BASE_SNOW_COUNT)]
    peak_height_left = peak_height_right = 150  # Equal peaks

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gender-Based Snowfall with Peaks")

# Load font
font = pygame.font.Font(None, FONT_SIZE)

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    # Fill the background (black)
    screen.fill(BACKGROUND_COLOR)

    # Draw the divider line
    pygame.draw.line(screen, LINE_COLOR, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 3)

    # Draw labels
    male_text = font.render(f"Male ({male_count})", True, TEXT_COLOR)
    female_text = font.render(f"Female ({female_count})", True, TEXT_COLOR)
    screen.blit(male_text, (WIDTH // 4 - male_text.get_width() // 2, 20))
    screen.blit(female_text, (3 * WIDTH // 4 - female_text.get_width() // 2, 20))

    # Draw Peaks with color-coded sizes
    # Left side peak (Male)
    left_peak = [(WIDTH // 4, HEIGHT - peak_height_left),  # Peak top
                 (WIDTH // 4 - 80, HEIGHT),  # Bottom left
                 (WIDTH // 4 + 80, HEIGHT)]  # Bottom right
    pygame.draw.polygon(screen, peak_color_left, left_peak)

    # Right side peak (Female)
    right_peak = [(3 * WIDTH // 4, HEIGHT - peak_height_right),  # Peak top
                  (3 * WIDTH // 4 - 80, HEIGHT),  # Bottom left
                  (3 * WIDTH // 4 + 80, HEIGHT)]  # Bottom right
    pygame.draw.polygon(screen, peak_color_right, right_peak)

    # Draw snowflakes only on the dominant side
    for x, y in snowflakes:
        pygame.draw.circle(screen, WHITE, (x, y), 3)

    # Update snowflake positions
    snowflakes = [(x, (y + 2) % HEIGHT) for x, y in snowflakes]

    # Update display
    pygame.display.flip()
    clock.tick(30)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
