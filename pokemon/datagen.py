import random
import numpy as np
import os

def generate_map(width, height):
    map = [[' ' for _ in range(width)] for _ in range(height)]
    
    center_x, center_y = width // 2, height // 2
    map[center_y][center_x] = '#'
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    for _ in range(width * height // 4):
        x, y = random.randint(0, width-1), random.randint(0, height-1)
        
        while map[y][x] == ' ':
            dx, dy = random.choice(directions)
            new_x, new_y = x + dx, y + dy
            
            if 0 <= new_x < width and 0 <= new_y < height:
                if map[new_y][new_x] == '#':
                    map[y][x] = '#'
                    break
                else:
                    x, y = new_x, new_y
    
    # Find a clear spot for the player
    while True:
        x, y = random.randint(0, width-1), random.randint(0, height-1)
        if map[y][x] == ' ':
            return map, x, y

def save_map(map, filename):
    with open(filename, 'w') as f:
        for row in map:
            f.write(''.join(row) + '\n')

# Generate and save 1000 maps
dataset_dir = 'map_dataset'
os.makedirs(dataset_dir, exist_ok=True)

for i in range(1000):
    map, _, _ = generate_map(20, 20)
    save_map(map, os.path.join(dataset_dir, f'map_{i}.txt'))
