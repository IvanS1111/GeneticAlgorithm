import pygame
import random
import numpy as np

if __name__ == '__main__':
    pass


def createNeuroNet(vision_radius, middle_layer, left_interval, right_interval, value):
    neuroNet = []
    random.seed(a=value);
    for u in range(3):
        arr = []
        for t in range(4):
            random.seed(random.randint(0, 1000))
            buff_matrix = np.zeros((vision_radius * 2 + 1, vision_radius * 2 + 1))
            for i in range(vision_radius * 2 + 1):
                for j in range(vision_radius * 2 + 1):
                    buff_matrix[i][j] = random.uniform(left_interval, right_interval)
            arr.append(buff_matrix)
        neuroNet.append(arr)
    return neuroNet





def evaluateVector(vision_matrix, neuro_net, input_layer, midle_layer):
    w = 0
    d = 0
    s = 0
    a = 0
    for i in range(len(vision_matrix)):
        for j in range(len(vision_matrix)):
           if i * 2 + 1 == len(vision_matrix) and j * 2 + 1 == len(vision_matrix):
               continue
           if vision_matrix[i][j] == -1:
               w += neuro_net[0][0][i][j]
               d += neuro_net[0][1][i][j]
               s += neuro_net[0][2][i][j]
               a += neuro_net[0][3][i][j]
           elif vision_matrix[i][j] == 1:
               w += neuro_net[1][0][i][j]
               d += neuro_net[1][1][i][j]
               s += neuro_net[1][2][i][j]
               a += neuro_net[1][3][i][j]
           elif vision_matrix[i][j] == 2:
               w += neuro_net[2][0][i][j]
               d += neuro_net[2][1][i][j]
               s += neuro_net[2][2][i][j]
               a += neuro_net[2][3][i][j]

    if w > d and w > s and w > a:
        return "UP"
    elif d > w and d > s and d > a:
        return "RIGHT"
    elif s > d and s > w and s > a:
        return "DOWN"
    elif a > d and a > s and a > w:
        return "LEFT"
    else: return random.choice(["UP", "DOWN", "RIGHT", "LEFT"])


def createVisionMatrix(matrix, x, y, vision_radius):
    vision_matrix = np.zeros((vision_radius * 2 + 1, vision_radius * 2 + 1))
    i1 = 0
    j1 = 0
    for i in range(int(x - vision_radius), int(x + vision_radius)):
        for j in range(int(y - vision_radius), int(y + vision_radius)):
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix):
                vision_matrix[i1][j1] = -1
                j1 += 1
            else:
                vision_matrix[i1][j1] = matrix[i][j]
                j1 += 1
        i1 += 1
        j1 = 0
    return vision_matrix


def mutationNeuroNet(neuroNet, left_interval, right_interval, value, vision_radius):
    random.seed(value)
    mut_case = random.randint(0, 100)
    if mut_case >= 44 and mut_case <= 63:
        neuroNet[random.randint(0, 2)][random.randint(0, 3)][random.randint(0, vision_radius * 2)][random.randint(0, vision_radius * 2)] = random.randrange(left_interval, right_interval)
    if mut_case >= 27 and mut_case <= 31:
       neuroNet[random.randint(0, 2)][random.randint(0, 3)][random.randint(0, vision_radius * 2)][random.randint(0, vision_radius * 2)] = random.randrange(left_interval, right_interval)
       neuroNet[random.randint(0, 2)][random.randint(0, 3)][random.randint(0, vision_radius * 2)][random.randint(0, vision_radius * 2)] = random.randrange(left_interval, right_interval)
    if mut_case == 87:
       neuroNet[random.randint(0, 2)][random.randint(0, 3)][random.randint(0, vision_radius * 2)][random.randint(0, vision_radius * 2)] = random.randrange(left_interval, right_interval)
       neuroNet[random.randint(0, 2)][random.randint(0, 3)][random.randint(0, vision_radius * 2)][random.randint(0, vision_radius * 2)] = random.randrange(left_interval, right_interval)
       neuroNet[random.randint(0, 2)][random.randint(0, 3)][random.randint(0, vision_radius * 2)][random.randint(0, vision_radius * 2)] = random.randrange(left_interval, right_interval)
    return neuroNet


def randomBot(size, amount):
    array = []
    for i in range(amount):
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        for j in array:
            while j[0] == x and j[1] == y:
                x = random.randint(0, size - 1)
                y = random.randint(0, size - 1)
        array.append([x, y])
    return array


def randomFood(size, amount):
    array = []
    for i in range(amount):
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
        for j in array:
            while j[0] == x and j[1] == y:
                x = random.randint(0, size - 1)
                y = random.randint(0, size - 1)
        array.append([x, y])
    return array


random.seed(a=3);
# empty_cell - 0
# bot - 1
# food - 2
# wall - (-1)
WND_SIZE = 1000
BODY_SIZE = 25
START_KOL_BOTS = 1
KOL_FOODS = 70
VISION_RADIUS = 1
LIVE_DURATION = 100
INPUT_LAYER = (VISION_RADIUS * 2 + 1) ** 2
MIDLE_LAYER = 4
MATRIX_SIZE = int(WND_SIZE / BODY_SIZE)
TIME_FOOD = 80
FPS = 20

pygame.init()
screen = pygame.display.set_mode((WND_SIZE, WND_SIZE))
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
matrix = np.zeros((MATRIX_SIZE, MATRIX_SIZE))
bots = randomBot(MATRIX_SIZE, START_KOL_BOTS)
for i in range(len(bots)):
    pygame.draw.rect(screen, (0, 153, 0), (BODY_SIZE * bots[i][0], BODY_SIZE *  bots[i][1], BODY_SIZE, BODY_SIZE))
foods = randomFood(MATRIX_SIZE, KOL_FOODS)
for i in range(len(foods)):
    pygame.draw.rect(screen, (204, 0, 0), (BODY_SIZE * foods[i][0], BODY_SIZE *  foods[i][1], BODY_SIZE, BODY_SIZE))
pygame.display.flip()
clock.tick(FPS)
lives = []
for i in range(START_KOL_BOTS):
    lives.append(LIVE_DURATION)
neuroNets = []
for i in range(START_KOL_BOTS):
    neuroNets.append(createNeuroNet(VISION_RADIUS, MIDLE_LAYER, -1.0, 1.0, i))
    clock.tick(100)
print(neuroNets)
for i in bots:
    matrix[i[0]][i[1]] = 1
for i in foods:
    matrix[i[0]][i[1]] = 2
generations = [0 for i in range(len(bots))]
time_foods = []

while True:
    screen.fill((0, 0, 0))
    for i in range(len(time_foods)):
        time_foods[i] -= 1
    buff_time_foods = []
    for i in range(len(time_foods)):
        if time_foods[i] <= 0:
            x_f = random.randint(0, MATRIX_SIZE - 1)
            y_f = random.randint(0, MATRIX_SIZE - 1)
            while matrix[x_f][y_f] != 0:
                x_f = random.randint(0, MATRIX_SIZE - 1)
                y_f = random.randint(0, MATRIX_SIZE - 1)
            matrix[x_f][y_f] = 2
            foods.append([x_f, y_f])
        else:
            buff_time_foods.append(time_foods[i])
    time_foods = buff_time_foods
    buff_time_foods = []

    buff = len(bots)
    for i in range(buff):
        if lives[i] == 0:
            continue

        vison_matrix = createVisionMatrix(matrix, bots[i][0], bots[i][1], VISION_RADIUS)
        direction = evaluateVector(vison_matrix, neuroNets[i], INPUT_LAYER, MIDLE_LAYER)

        if direction == "UP":
            x = bots[i][0]
            y = bots[i][1] + 1
            if x >= 0 and x < MATRIX_SIZE and y >= 0 and y < MATRIX_SIZE:
                if matrix[x][y] != 1:
                    if matrix[x][y] == 0:
                        matrix[x][y] = 1
                        matrix[bots[i][0]][bots[i][1]] = 0
                        bots[i][1] += 1
                    elif matrix[x][y] == 2:
                        lives[i] = LIVE_DURATION
                        matrix[x][y] = 1
                        bots.append([x, y])
                        generations.append(generations[i] + 1)
                        lives.append(LIVE_DURATION)
                        neuroNets.append(mutationNeuroNet(neuroNets[i], -1, 1, i, VISION_RADIUS))
                        time_foods.append(TIME_FOOD)

        if direction == "LEFT":
            x = bots[i][0] - 1
            y = bots[i][1]
            if x >= 0 and x < MATRIX_SIZE and y >= 0 and y < MATRIX_SIZE:
                if matrix[x][y] != 1:
                    if matrix[x][y] == 0:
                        matrix[x][y] = 1
                        matrix[bots[i][0]][bots[i][1]] = 0
                        bots[i][0] -= 1
                    elif matrix[x][y] == 2:
                        lives[i] = LIVE_DURATION
                        matrix[x][y] = 1
                        bots.append([x, y])
                        generations.append(generations[i] + 1)
                        lives.append(LIVE_DURATION)
                        neuroNets.append(mutationNeuroNet(neuroNets[i], -1, 1, i, VISION_RADIUS))
                        time_foods.append(TIME_FOOD)

        if direction == "DOWN":
            x = bots[i][0]
            y = bots[i][1] - 1
            if x >= 0 and x < MATRIX_SIZE and y >= 0 and y < MATRIX_SIZE:
                if matrix[x][y] != 1:
                    if matrix[x][y] == 0:
                        matrix[x][y] = 1
                        matrix[bots[i][0]][bots[i][1]] = 0
                        bots[i][1] -= 1
                    elif matrix[x][y] == 2:
                        lives[i] = LIVE_DURATION
                        matrix[x][y] = 1
                        bots.append([x, y])
                        generations.append(generations[i] + 1)
                        lives.append(LIVE_DURATION)
                        neuroNets.append(mutationNeuroNet(neuroNets[i], -1, 1, i, VISION_RADIUS))
                        time_foods.append(TIME_FOOD)

        if direction == "RIGHT":
            x = bots[i][0] + 1
            y = bots[i][1]
            if x >= 0 and x < MATRIX_SIZE and y >= 0 and y < MATRIX_SIZE:
                if matrix[x][y] != 1:
                    if matrix[x][y] == 0:
                        matrix[x][y] = 1
                        matrix[bots[i][0]][bots[i][1]] = 0
                        bots[i][0] += 1
                    elif matrix[x][y] == 2:
                        lives[i] = LIVE_DURATION
                        matrix[x][y] = 1
                        bots.append([x, y])
                        generations.append(generations[i] + 1)
                        lives.append(LIVE_DURATION)
                        neuroNets.append(mutationNeuroNet(neuroNets[i], -1, 1, i, VISION_RADIUS))
                        time_foods.append(TIME_FOOD)
        lives[i] -= 1

    buff_bots = []
    buff_lives = []
    buff_neuroNets = []
    buff_generation = []
    for i in range(len(lives)):
        if lives[i] == 0:
            matrix[bots[i][0]][bots[i][1]] = 0
        else:
            buff_bots.append(bots[i])
            buff_lives.append(lives[i])
            buff_neuroNets.append(neuroNets[i])
            buff_generation.append(generations[i])
    bots = []
    lives = []
    neuroNets = []
    generations = []
    bots = buff_bots
    lives = buff_lives
    neuroNets = buff_neuroNets
    generations = buff_generation
    buff_foods = []
    for i in range(len(foods)):
        if matrix[foods[i][0]][foods[i][1]] != 1:
            buff_foods.append(foods[i])
    foods = []
    foods = buff_foods

    for i in range(len(foods)):
        pygame.draw.rect(screen, (204, 0, 0),
                         (BODY_SIZE * foods[i][0], BODY_SIZE * foods[i][1], BODY_SIZE, BODY_SIZE))
    for i in range(len(bots)):
        pygame.draw.rect(screen, (0, 153, 0),
                         (BODY_SIZE * bots[i][0], BODY_SIZE * bots[i][1], BODY_SIZE, BODY_SIZE))
    pygame.display.flip()
    clock.tick(FPS)

    key = pygame.key.get_pressed()
    index = 0
    max_value = -1

    if key[pygame.K_g]:
        print(max(generations))

    if key[pygame.K_n]:
        FPS = 20

    if key[pygame.K_f]:
        FPS = 1000

    if key[pygame.K_s]:
        FPS = 5

    if key[pygame.K_i]:
        TIME_FOOD /= 2

    if key[pygame.K_a]:
        TIME_FOOD *= 2
    if key[pygame.K_l]:
        KOL_FOODS = KOL_FOODS * 0.1

    pygame.event.pump()