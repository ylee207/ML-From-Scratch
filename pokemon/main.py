import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Pokemon:
    def __init__(self, name, type, hp, moves):
        self.name = name
        self.type = type
        self.hp = hp
        self.max_hp = hp
        self.moves = moves

    def attack(self, opponent, move):
        damage = move['damage']
        opponent.hp = max(0, opponent.hp - damage)
        print(f"{self.name} used {move['name']} and dealt {damage} damage to {opponent.name}!")

class Player:
    def __init__(self, name, pokemon):
        self.name = name
        self.pokemon = pokemon
        self.x = 0
        self.y = 0

def display_battle(player_pokemon, opponent_pokemon):
    clear_screen()
    print(f"{'=' * 40}")
    print(f"{player_pokemon.name:^20} VS {opponent_pokemon.name:^20}")
    print(f"{'=' * 40}")
    print(f"{player_pokemon.name:<20} {opponent_pokemon.name:>20}")
    print(f"HP: {player_pokemon.hp}/{player_pokemon.max_hp:<13} HP: {opponent_pokemon.hp}/{opponent_pokemon.max_hp:>13}")
    print(f"{'=' * 40}")

def get_move_choice(pokemon):
    while True:
        print("\nChoose a move:")
        for i, move in enumerate(pokemon.moves):
            print(f"{i+1}. {move['name']}")
        try:
            choice = int(input("Enter the number of your move: ")) - 1
            if 0 <= choice < len(pokemon.moves):
                return pokemon.moves[choice]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a number.")

def battle(player, opponent):
    print(f"A wild {opponent.name} appeared!")
    time.sleep(2)
    
    while player.pokemon.hp > 0 and opponent.hp > 0:
        display_battle(player.pokemon, opponent)
        
        player_move = get_move_choice(player.pokemon)
        player.pokemon.attack(opponent, player_move)
        time.sleep(1)
        
        if opponent.hp > 0:
            opponent_move = random.choice(opponent.moves)
            opponent.attack(player.pokemon, opponent_move)
            time.sleep(1)
    
    display_battle(player.pokemon, opponent)
    if player.pokemon.hp > 0:
        print(f"\nCongratulations! You defeated the wild {opponent.name}!")
    else:
        print(f"\nYour {player.pokemon.name} fainted. You lost the battle.")

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

def display_map(map, player):
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if x == player.x and y == player.y:
                print('P', end='')
            else:
                print(cell, end='')
        print()

def move_player(player, direction, map):
    dx, dy = {
        'w': (0, -1),
        's': (0, 1),
        'a': (-1, 0),
        'd': (1, 0)
    }.get(direction, (0, 0))

    new_x, new_y = player.x + dx, player.y + dy

    if 0 <= new_x < len(map[0]) and 0 <= new_y < len(map) and map[new_y][new_x] == ' ':
        player.x, player.y = new_x, new_y
        return True
    return False

def explore_area(player):
    clear_screen()
    print(f"{player.name} is exploring a new area...")
    time.sleep(1)
    
    map, player.x, player.y = generate_map(20, 10)
    
    while True:
        clear_screen()
        display_map(map, player)
        print("\nUse W/A/S/D to move, or Q to quit exploring.")
        
        action = input("Enter your move: ").lower()
        
        if action == 'q':
            break
        elif action in ['w', 'a', 's', 'd']:
            moved = move_player(player, action, map)
            if moved and random.random() < 0.1:  # 10% chance of encounter after each move
                return True  # Trigger a battle
        else:
            print("Invalid input. Use W/A/S/D to move or Q to quit.")
    
    return False  # No battle triggered

def main():
    player_name = input("Enter your name, trainer: ")
    pikachu = Pokemon("Pikachu", "Electric", 100, [
        {"name": "Thunderbolt", "damage": 40},
        {"name": "Quick Attack", "damage": 20},
        {"name": "Iron Tail", "damage": 30}
    ])
    player = Player(player_name, pikachu)

    while True:
        battle_triggered = explore_area(player)
        
        if battle_triggered:
            charmander = Pokemon("Charmander", "Fire", 90, [
                {"name": "Ember", "damage": 30},
                {"name": "Scratch", "damage": 20},
                {"name": "Flamethrower", "damage": 40}
            ])
            battle(player, charmander)
        
        choice = input("Do you want to explore another area? (y/n): ").lower()
        if choice != 'y':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()