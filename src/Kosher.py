import pygame
import sys

GROUND = 1
TARGET = 2
BOX = 3
PLAYER = 4

# 初始化Pygame和屏幕
pygame.init()
size = width, height = 500, 500

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Kosher")
# 颜色定义
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 128, 0)

# 加载图片并调整大小
player = pygame.image.load("./data/player.jpg")
player = pygame.transform.scale(player, (50, 50))

box = pygame.image.load("./data/box.jpg")
box = pygame.transform.scale(box, (50, 50))

target = pygame.image.load("./data/target.jfif")
target = pygame.transform.scale(target, (50, 50))

ground = pygame.image.load("./data/ground.jfif")
ground = pygame.transform.scale(ground, (50, 50))

# 定义类，包括地图，角色，箱子和目标
class Map:
    def __init__(self, width, height, map_data):
        self.width = width
        self.height = height
        self.map_data = map_data   # 1:地面 2:目标 3:箱子 4:角色
        self.player_pos = self.find_player()
        self.box_pos = self.find_boxes()

    # 在地图上绘制不同的元素
    def draw(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.map_data[row][col] == GROUND:
                    screen.blit(ground, (col * 50, row * 50))
                elif self.map_data[row][col] == TARGET:
                    screen.blit(target, (col * 50, row * 50))
                elif self.map_data[row][col] == BOX:
                    screen.blit(box, (col * 50, row * 50))
                elif self.map_data[row][col] == PLAYER:
                    screen.blit(player, (col * 50, row * 50))

    # 找到角色位置
    def find_player(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.map_data[row][col] == PLAYER:
                    return (row, col)

    # 找到箱子位置
    def find_boxes(self):
        boxes = []
        for row in range(self.height):
            for col in range(self.width):
                if self.map_data[row][col] == BOX :
                    boxes.append((row, col))
        return boxes

    # 移动角色并检查是否胜利
    def move_player(self, direction):
        x, y = self.player_pos
        if direction == "up":
            x -= 1
            if x < 0:
                return False
        elif direction == "down":
            x += 1
            if x >= self.height:
                return False
        elif direction == "left":
            y -= 1
            if y < 0:
                return False
        elif direction == "right":
            y += 1
            if y >= self.width:
                return False
        else:
            return False
        #判断将要移动位置是否合法
        if self.map_data[x][y] == GROUND:
            self.map_data[self.player_pos[0]][self.player_pos[1]] = GROUND
            self.map_data[x][y] = PLAYER
            self.player_pos = (x, y)
            return True
        if self.map_data[x][y] == TARGET:
            self.map_data[self.player_pos[0]][self.player_pos[1]] = GROUND
            self.map_data[x][y] = PLAYER
            self.player_pos = (x, y)
            if self.check_win():
                self.win()
            return True
        if self.map_data[x][y] == BOX:
            new_x, new_y = x, y
            if direction == "up":
                new_x -= 1
                if new_x < 0:
                    return False
            elif direction == "down":
                new_x += 1
                if new_x >= self.height:
                    return False
            elif direction == "left":
                new_y -= 1
                if new_y < 0:
                    return False
            elif direction == "right":
                new_y += 1
                if new_y >= self.width:
                    return False
            else:
                return False
            if self.map_data[new_x][new_y] == GROUND :
                self.map_data[self.player_pos[0]][self.player_pos[1]] = GROUND
                self.map_data[x][y] = PLAYER
                self.player_pos = (x, y)
                self.map_data[new_x][new_y] = BOX
                for i, box_pos in enumerate(self.box_pos):
                    if box_pos == (x, y):
                        self.box_pos[i] = (new_x, new_y)
                        break
                return True
        return False

    # 检查是否胜利
    def check_win(self):
        for box_pos in self.box_pos:
            if self.map_data[box_pos[0]][box_pos[1]] != 2:
                return False
        return True

    # 胜利提示
    def win(self):
        font = pygame.font.Font(None, 50)
        text = font.render("You win!", True, green)
        text_rect = text.get_rect(center=(width/2, height/2))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

class Player:
    def __init__(self, pos):
        self.pos = pos

class Box:
    def __init__(self, pos):
        self.pos = pos

class Food( Box ):
    def __init__(self, pos):
        super().__init__(pos)

class Game:
    def __init__(self, map, player, box, food):
        self.map = map
        self.player = player
        self.box = box
        self.food = food

# 创建地图
map_data = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 1, 3, 1, 1, 1, 1],
    [1, 1, 1, 1, 3, 1, 1, 1],
    [1, 1, 4, 3, 2, 3, 1, 1],
    [1, 1, 1, 1, 3, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]
map = Map(8, 6, map_data)

# 游戏循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                map.move_player("up")
            elif event.key == pygame.K_DOWN:
                map.move_player("down")
            elif event.key == pygame.K_LEFT:
                map.move_player("left")
            elif event.key == pygame.K_RIGHT:
                map.move_player("right")
    
    # 绘制地图
    screen.fill(black)
    map.draw()
    pygame.display.update()
