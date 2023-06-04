import pygame
import sys

# 定义常量 
# 地图信息
ILLEGAL = 0
GROUND = 1
TARGET = 2
FOOD = 3
PLAYER = 4
TP = 5

# 游戏状态信息
START_MENU = 10
GAME_PAGE = 11
HELP_MENU = 12
GAME_SELECT_MENU = 13

game_level = 1
state = START_MENU

# 屏幕大小
size = width, height = 500, 500
# 颜色定义
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 128, 0)

TARGET = [0, 1]


# 初始化Pygame和屏幕
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Kosher")

# 加载图片并调整大小
player_front = pygame.image.load("./data/player_front.png")
player_front = pygame.transform.scale(player_front, (50, 50))

player_back = pygame.image.load("./data/player_back.png")
player_back = pygame.transform.scale(player_back, (50, 50))

player_right = pygame.image.load("./data/player_right.png")
player_right = pygame.transform.scale(player_right, (50, 50))

player_left = pygame.image.load("./data/player_left.png")
player_left = pygame.transform.scale(player_left, (50, 50))

wall = pygame.image.load("./data/wall_cross.png")
wall_image = pygame.transform.scale(wall, (50, 50))

target = pygame.image.load("./data/pot.png")
target_image = pygame.transform.scale(target, (50, 50))

ground = pygame.image.load("./data/ground.png")
ground_image = pygame.transform.scale(ground, (50, 50))

tp = pygame.image.load("./data/tp.png")
tp_image = pygame.transform.scale(tp, (50, 50))


food_name_dic = {0:"鹰嘴豆", 1:"橄榄油", 2:"牛奶"}
foods_id = [0,1]
# 食材图片 在data下 food1.jpg food2.jpg ....
foods_image = [ pygame.transform.scale(pygame.image.load("./data/{}.png".format(food_name_dic[i])), (50, 50)) for i in foods_id ]

class GameState:
    def __init__(self, game, start_menu, help_menu, game_select_menu):
        self.game = game
        self.start_menu = start_menu
        self.help_menu = help_menu
        self.game_select_menu = game_select_menu

    def draw(self):
        if state == START_MENU:
            self.start_menu.draw()
        elif state == GAME_PAGE:
            self.game.draw()
        elif state == HELP_MENU:
            self.help_menu.draw()
        elif state == GAME_SELECT_MENU:
            self.game_select_menu.draw()
        else:
            assert False, "Wrong state!"
    
    def update(self, event):
        if state == START_MENU:
            self.start_menu.update(event)
        elif state == GAME_PAGE:
            self.game.update(event)
        elif state == HELP_MENU:
            self.help_menu.update(event)
        elif state == GAME_SELECT_MENU:
            self.game_select_menu.update(event)
        else:
            assert False, "Wrong state!"
    
    def change_game(self, game):
        self.game = game

def to_start_game():
    print("to_start_game")
    global state
    state = GAME_PAGE
    global game_level
    game_level = 1
    
def to_help_menu():
    print("to_help_menu")
    global state
    state = HELP_MENU

def exit_game():
    print("exit_game")
    pygame.quit()
    sys.exit()
    
def to_level_select_menu():
    print("to_level_select_menu")
    global state
    state = GAME_SELECT_MENU

def to_start_menu():
    print("to_start_menu")
    global state
    state = START_MENU

def to_start_level_1():
    print("to_start_level_1")
    global state
    state = GAME_PAGE
    global game_level
    game_level = 1
    update_game()

def to_start_level_2():
    print("to_start_level_2")
    global state
    state = GAME_PAGE
    global game_level
    game_level = 2
    update_game()

class StartMenu:
    def __init__(self):
        self.buttons = []
        
        self.start_button = Button( 200, 100, 100, 50, red, "Start", white, 25, to_start_game)
        self.buttons.append(self.start_button)
        
        self.help_button = Button( 200, 200, 100, 50, red, "Help", white, 25, to_help_menu )
        self.buttons.append(self.help_button)

        self.level_select_button = Button( 200, 300, 100, 50, red, "Level selection", white, 25, to_level_select_menu)
        self.buttons.append(self.level_select_button)
        
        self.exit_button = Button( 200, 400, 100, 50, red, "Exit", white, 25, exit_game )
        self.buttons.append(self.exit_button)

    def draw(self):
        for button in self.buttons:
            button.draw(screen)
    
    def update(self, event):
        for button in self.buttons:
            button.is_clicked(event)

class HelpMenu:
    def __init__(self):
        self.buttons = []
        self.help_text = "This is the help menu. Here you can find instructions and tips for playing the game."
        
        self.back_button = Button(150, 400, 100, 50, red, "Back", white, 25, to_start_menu)
        self.buttons.append(self.back_button)

    def draw(self):
        # 绘制帮助信息文本
        text_surface = pygame.font.Font(None, 20).render(self.help_text, True, white)
        screen.blit(text_surface, (100, 200))
        
        # 绘制按钮
        for button in self.buttons:
            button.draw(screen)
    
    def update(self, event):
        for button in self.buttons:
            button.is_clicked(event)

class GameSelectMenu:
    def __init__(self):
        self.buttons = []
        
        self.back_button = Button(150, 400, 100, 50, red, "Back", white, 25, to_start_menu)
        self.buttons.append(self.back_button)

        # 添加关卡选择按钮
        self.level1_button = Button(150, 200, 100, 50, red, "Level 1", white, 25, to_start_level_1)
        self.buttons.append(self.level1_button)

        self.level2_button = Button(150, 300, 100, 50, red, "Level 2", white, 25, to_start_level_2)
        self.buttons.append(self.level2_button)

    def draw(self):
        # 绘制按钮
        for button in self.buttons:
            button.draw(screen)
    
    def update(self, event):
        for button in self.buttons:
            button.is_clicked(event)

# 定义类，包括地图，角色，箱子和目标
class Map:
    def __init__(self, map_data):
        self.map_data = map_data   
        self.height = len(map_data)
        self.width = len(map_data[0])
    def draw(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.map_data[row][col] == GROUND:
                    screen.blit(ground_image, (col * 50, row * 50))
                elif self.map_data[row][col] == ILLEGAL:
                    screen.blit(wall_image, (col * 50, row * 50))

class Player:
    def __init__(self, pos):
        self.pos = pos
        self.state = "front"
    def draw(self):
        if self.state == "front":
            player_image = player_front
        elif self.state == "back":
            player_image = player_back
        elif self.state == "left":
            player_image = player_left
        elif self.state == "right":
            player_image = player_right
        screen.blit(player_image, (self.pos[1] * 50, self.pos[0] * 50))
   
    def move(self, direction):
        if direction == "up":
            self.pos[0] -= 1
        elif direction == "down":
            self.pos[0] += 1
        elif direction == "left":
            self.pos[1] -= 1
        elif direction == "right":
            self.pos[1] += 1
        else:
            assert False, "Wrong direction!"

class Food():
    def __init__(self, pos, food_id):
        self.pos = pos
        self.food_id = food_id    
    def draw(self):
        screen.blit(foods_image[self.food_id], (self.pos[1] * 50, self.pos[0] * 50))

class Game:
    def __init__(self, map, player, foods:list, target, tp):
        self.map = map
        self.player = player
        self.foods = foods 
        self.target = target
        self.tp = tp
        self.regame_button = Button(0, 450, 100, 50, red, "restart", white, 25, update_game)
        self.start_menu_button = Button(100, 450, 100, 50, red, "start menu", white, 25, to_start_menu)
        self.buttons = [self.regame_button, self.start_menu_button]
        #TODO检查是否存在位置冲突，越界等情况
        
    def draw(self):
        self.map.draw()
        self.target.draw()
        self.tp.draw()
        self.player.draw()
        for food in self.foods:
            food.draw()
        for button in self.buttons:
            button.draw(screen)

    def move_player(self, direction):
        x , y = self.player.pos
        if direction == "up":
            self.player.state = "back"
            x -= 1
        elif direction == "down":
            self.player.state = "front"
            x += 1
        elif direction == "left":
            self.player.state = "left"
            y -= 1
        elif direction == "right":
            self.player.state = "right"
            y += 1
        else:
            assert False, "Wrong direction!"
        
        pos_type = self.check_pos([x, y])
        print(pos_type , x, y )
        if pos_type == ILLEGAL:
            return False
        elif pos_type == GROUND or pos_type == TARGET:
            self.player.move(direction)
        elif pos_type == TP:
            print("------tp-----")
            self.player.pos = self.tp.teleport([x, y])
        elif pos_type == FOOD:
            food = None
            for _food in self.foods:
                if _food.pos == [x, y]:
                    food = _food
                
            new_x, new_y = x, y
            if direction == "up":
                new_x -= 1
            elif direction == "down":
                new_x += 1
            elif direction == "left":
                new_y -= 1
            elif direction == "right":
                new_y += 1
            else:
                assert False, "Wrong direction!"

            if self.check_pos([new_x, new_y]) == GROUND:
                self.player.move(direction)
                food.pos = [new_x, new_y]
            elif self.check_pos([new_x, new_y]) == TARGET:
                if self.target.check(food.food_id):
                    print("put in food: ", food.food_id)
                    self.player.move(direction)
                    self.foods.remove(food)
                    self.target.put_in_food(food.food_id)
        
        if self.check_win():
            self.draw()
            pygame.display.update()
            
            text = pygame.font.Font(None, 50).render("You win!", True, green)
            text_rect = text.get_rect(center=(width/2, height/2))
            screen.blit(text, text_rect)
            pygame.display.update()
            pygame.time.delay(2000)
            pygame.quit()
            sys.exit()
    
    def check_pos(self, pos) ->int:
        """
        检查位置是否合法
        返回值：
        ILLEGAL = 0
        GROUND = 1
        TARGET = 2
        FOOD = 3
        PLAYER = 4
        TP = 5
        """
        [x, y] = pos
        if x < 0 or x >= self.map.height or y < 0 or y >= self.map.width:
            return ILLEGAL
        if self.map.map_data[x][y] == ILLEGAL:
            return ILLEGAL

        if pos == self.target.pos:
            return TARGET
        for food in self.foods:
            if pos == food.pos:
                return FOOD
        if pos == self.player.pos:
            return PLAYER
        
        if self.tp.check(pos):
            return TP

        return GROUND

    def check_win(self):
        if self.target.is_finish():
            return True
        else:
            return False
    
    def update(self, event):
        if event.type==pygame.MOUSEBUTTONDOWN:
            print("鼠标点击的位置：",pygame.mouse.get_pos())
            for button in self.buttons:
                button.is_clicked(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.move_player("up")
            elif event.key == pygame.K_DOWN:
                self.move_player("down")
            elif event.key == pygame.K_LEFT:
                self.move_player("left")
            elif event.key == pygame.K_RIGHT:
                self.move_player("right")

#目标必须是食材按一定顺序推入才可以
class Target:
    def __init__(self, pos, food_ids:list):
        """
        pos: 目标位置 [x, y]
        food_ids: 目标食材id列表 [id1, id2, id3, ...]
        """
        self.pos = pos
        self.food_ids = food_ids
        self.food_num = 0
    
    def draw(self):
        screen.blit(target_image, (self.pos[1] * 50, self.pos[0] * 50))

    def check(self, food_id):
        """检查食材是否是目标顺序中的下一个"""
        if food_id == self.food_ids[self.food_num]:
            return True
        else:
            return False
    
    def put_in_food(self, food_id):
        """将食材推入目标，必须首先检查食材是否是目标顺序中的下一个check()"""
        if self.check(food_id):
            self.food_num += 1
        else:
            assert False, "Wrong food id put in!"
    
    def is_finish(self):
        """检查食材是否全部放入目标"""
        print("check_is_finish", self.food_num, len(self.food_ids))
        if self.food_num == len(self.food_ids):
            return True
        else:
            return False

class Teleportation ():
    def __init__(self, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2
    
    def draw(self):
        screen.blit(tp_image, (self.pos1[1] * 50, self.pos1[0] * 50))
        screen.blit(tp_image, (self.pos2[1] * 50, self.pos2[0] * 50))
    
    def check(self, pos):
        if pos == self.pos1 or pos == self.pos2:
            return True
        else:
            return False
    
    def teleport(self, pos):
        if pos == self.pos1:
            return self.pos2.copy()
        elif pos == self.pos2:
            return self.pos1.copy()
        else:
            assert False, "Wrong position to teleport!"
        
class Button:
    def __init__(self, x, y, width, height, color, text, text_color, font_size, click_handler):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(None, font_size)
        self.click_handler = click_handler  # 传递点击处理函数参数

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_render = self.font.render(self.text, True, self.text_color)
        text_rect = text_render.get_rect(center=self.rect.center)
        screen.blit(text_render, text_rect)

    def is_clicked(self, event, *args, **kwargs):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            if self.rect.collidepoint(event.pos):
                print("button clicked")
                self.click_handler(*args, **kwargs)  # 调用点击处理函数


# 创建地图

def init_game():
    global game
    if game_level == 1:

        map_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    ]
        map = Map(map_data)
        tp = Teleportation([0, 7], [6, 5])
        player = Player([0, 0])
        foods = [ Food([1, 1], 0), Food([2, 2], 1)]
        target = Target([4, 4], TARGET)
        
        game = Game(map, player, foods, target, tp)
    elif game_level == 2:
        map_data = [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    ]
        map = Map(map_data)
        tp = Teleportation([0, 7], [6, 5])
        player = Player([0, 0])
        foods = [ Food([1, 1], 0), Food([2, 2], 1)]
        target = Target([4, 4], TARGET)
        
        game = Game(map, player, foods, target, tp)
    else:
        assert False, "Wrong game level!"

def update_game():
    init_game()
    game_state.change_game(game)

init_game()

help_menu = HelpMenu()
game_select_menu = GameSelectMenu()
start_menu = StartMenu()
game_state = GameState(game, start_menu, help_menu, game_select_menu)

# 游戏循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        game_state.update(event)
    
    # 绘制地图
    screen.fill(black)
    game_state.draw()
    pygame.display.update()
   
