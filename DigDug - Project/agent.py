# Autores:
#  Tiago Pereira    Nmec:98360
#  Rafael Pinto     Nmec:103379

import math
from consts import Direction

class Agent():
    
    def __init__(self):
        self.map = []
        self.digdug = []
        self.enemies = []
        self.rocks = []
        self.last_move = ' '
        self.avoiding_rock = False
        self.go_back = []
        self.go_back_steps = 0
        self.opposite_moves = {'w': 's', 's': 'w', 'a': 'd', 'd': 'a'}
    
    # Update the data with current state
    def update_data(self, state):
        if state.get('map') != self.map and state.get('map') != None:
            self.map = state.get('map')
            self.last_move = ' '
            self.avoiding_rock = False
            self.go_back_steps = 0
            self.go_back = []
        else:
            self.digdug = state.get('digdug')
            self.enemies = state.get('enemies')
            self.rocks = state.get('rocks')

    # Get an action to perform
    def get_action(self, state):

        self.update_data(state)
        if self.enemies == None or self.enemies == []:
            return ' '
        
        # Go back N steps
        if self.go_back_steps > 0 and self.go_back != []:
            self.go_back_steps = self.go_back_steps - 1
            return self.go_back.pop()
        
        self.go_back_steps = 0

        closest_enemy = self.get_closest_enemy()
        orientation = self.get_path_orientation(self.enemies[closest_enemy[0]].get('pos'))
        move = self.get_move(closest_enemy[0], orientation)

        # Avoid rocks and prevent digdug from getting stuck in a loop that occurs when enemy and rock are in the same axis
        if self.check_rock_in_front(move) or (self.avoiding_rock and self.check_repeating_moves(move)):
            return self.handle_rock(move, closest_enemy)

        self.avoiding_rock = False

        # Wait for enemy to stop traversing
        if self.enemies[closest_enemy[0]].get('traverse') == True:
            return ' '
        
        # If digdug is facing enemy and enemy
        if self.check_facing_enemy(self.enemies[closest_enemy[0]]):
            # If digdug has cover, wait to attack enemy from behind
            if self.check_wall_in_front():
                return ' '
            # Else if there is danger of getting killed by fire, then go back
            if self.check_fire_danger(move, closest_enemy):
                return self.handle_fire()
        
        # If is safe to attack, then attack
        if self.check_safe_attack(move, closest_enemy):
            return 'A'
        
        self.update_move_variables(move)
        return move
    
    # Avoid rocks
    def handle_rock(self, move, closest):
        self.avoiding_rock = True

        if move in ['w', 's']:
            move = 'd' if self.digdug[0] < self.enemies[closest[0]]['pos'][0] else 'a'
        else:
            move = 's' if self.digdug[1] < self.enemies[closest[0]]['pos'][1] else 'w'
                
        self.update_move_variables(move)
        return move
    
    # Update last_move, go_back_list and map
    def update_move_variables(self, move):
        self.last_move = move
        self.go_back.append(self.opposite_moves[move])
        self.update_map(move)

    # Go back to avoid fire
    def handle_fire(self):
        if self.go_back != []:
            self.go_back_steps = 3
            return self.go_back[-1]
        return ' '
    
    # Get the closest enemy and its distance
    def get_closest_enemy(self):
        distancies = {}
        for index,enemy in enumerate(self.enemies):
            distance = calc_distance(self.digdug[0], self.digdug[1], enemy.get('pos')[0], enemy.get('pos')[1])
            distancies[index] = distance
        return min(distancies, key=distancies.get), distancies.get(min(distancies, key=distancies.get))

    # Get the move to get closer to the enemy
    def get_move(self, enemy, orientation):
        if orientation == 'vertical':
            if self.digdug[0] == self.enemies[enemy].get('pos')[0]:
                if self.digdug[1] < self.enemies[enemy].get('pos')[1]:
                    return 's'
                return 'w'
            else:
                if self.digdug[0] < self.enemies[enemy].get('pos')[0]:
                    return 'd'
                return 'a'
        else:
            if self.digdug[1] == self.enemies[enemy].get('pos')[1]:
                if self.digdug[0] < self.enemies[enemy].get('pos')[0]:
                    return 'd'
                return 'a'
            else:
                if self.digdug[1] < self.enemies[enemy].get('pos')[1]:
                    return 's'
                return 'w'
    
    # Check if it is safe to attack
    def check_safe_attack(self, move, closest_enemy):
        # If enemy is close and digdug is facing the enemy and there is no wall in front, then attack
        if closest_enemy[1] <= 3 and move == self.last_move and not self.check_wall_in_front():
            return True
        return False

    # Check if there is danger of getting killed by fire 
    def check_fire_danger(self, move, closest_enemy):
        if self.check_fire_in_front(move):
            return True
        return False
        
    # If digdug goes into fire in the next move, then True
    def check_fire_in_front(self, move):
        locations = self.get_fire_locations()
        if locations == []:
            return False
        next_pos = get_next_position(self.digdug, move)
        for fire in locations:
            for pos in fire:
                if pos == next_pos:
                    return True
        return False

    # Check if digdug is repeating moves
    def check_repeating_moves(self, move):
        if move == self.opposite_moves[self.last_move]:
            return True
        return False
    
    # True, if there is a wall in front of digdug
    def check_wall_in_front(self):
        if self.digdug[0]-1 >= 0 and self.digdug[0]+1 < len(self.map) and self.digdug[1]-1 >= 0 and self.digdug[1]+1 < len(self.map[0]):
            if self.last_move == 'a':
                if self.map[self.digdug[0]-1][self.digdug[1]] == 1:
                    return True
            elif self.last_move == 'd':
                if self.map[self.digdug[0]+1][self.digdug[1]] == 1:
                    return True
            elif self.last_move == 'w':
                if self.map[self.digdug[0]][self.digdug[1]-1] == 1:
                    return True
            elif self.last_move == 's':
                if self.map[self.digdug[0]][self.digdug[1]+1] == 1:
                    return True
        return False
    
    # True, if digdug is face to face with enemy
    def check_facing_enemy(self, enemy):
        if self.last_move == 'a ' and enemy.get('dir') == Direction.EAST:
            return True
        if self.last_move == 'd' and enemy.get('dir') == Direction.WEST:
            return True
        if self.last_move == 'w' and enemy.get('dir') == Direction.SOUTH:
            return True
        if self.last_move == 's' and enemy.get('dir') == Direction.NORTH:
            return True
        return False

    # True, if there is a rock in front of digdug
    def check_rock_in_front(self, move):
        next_pos = get_next_position(self.digdug, move)
        for rock in self.rocks:
            if rock.get('pos') == next_pos:
                return True
        return False

    # Get the locations of the fire   
    def get_fire_locations(self):
        fire_locations = []
        for enemy in self.enemies:
            if enemy.get('fire') != None:
                fire_locations.append(enemy.get('fire'))
        return fire_locations

    # Get the orientation of the tunnel where the enemy is
    def get_path_orientation(self,enemy_pos):
        for i, col in enumerate(self.map):
            for j in range(len(col)):
                if i == enemy_pos[0] and j == enemy_pos[1]:
                    up = None
                    down = None
                    left = None
                    right = None
                    if i-1 >= 0:
                        right = self.map[i-1][j]
                    if i+1 < len(self.map):
                        left = self.map[i+1][j]
                    if j-1 >= 0:
                        up = self.map[i][j-1]
                    if j+1 < len(self.map[i]):
                        down = self.map[i][j+1]
                    if (up == 0 or down == 0) and (left == 1 or right == 1):
                        return 'vertical'
                    if (left == 0 or right == 0) and (up == 1 or down == 1):
                        return 'horizontal'
        return ' '
    
    # Updates the map
    def update_map(self, move):
        next_pos = get_next_position(self.digdug, move)
        if self.map[next_pos[0]][next_pos[1]] == 1:
            self.map[next_pos[0]][next_pos[1]] = 0

# Get the next position when performing a certain move
def get_next_position(pos, move):
    if isinstance(move, Direction):
        if move == Direction.EAST:
            return [pos[0]+1, pos[1]]
        if move == Direction.WEST:
            return [pos[0]-1, pos[1]]
        if move == Direction.NORTH:
            return [pos[0], pos[1]-1]
        if move == Direction.SOUTH:
            return [pos[0], pos[1]+1]
    if move == 'a':
        return [pos[0]-1, pos[1]]
    elif move == 'd':
        return [pos[0]+1, pos[1]]
    elif move == 'w':
        return [pos[0], pos[1]-1]
    elif move == 's':
        return [pos[0], pos[1]+1]
    return pos

# Calculate the distance between two points
def calc_distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
            