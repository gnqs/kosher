# -*- coding: utf-8 -*-
import pygame
import sys

# 定义常量 
# 地图信息
WALL_CROSS = -1
WALL_H = -2
WALL_W = -3
WALL_L_D = -4
WALL_L_U = -5
WALL_R_D = -6
WALL_R_U = -7

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
GAME_WIN_MENU = 14

game_level = 1
unlock_level = 1
state = START_MENU

# 屏幕大小
size = width, height = 500, 600
# 颜色定义
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 128, 0)
dark_blue = (0, 0, 128)

BUTTON_COLOR = dark_blue

font_path = "./data/font.ttf"
# 初始化Pygame和屏幕
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Kosher")

# 加载图片并调整大小
button_image = pygame.image.load("./data/button.png")
button_image = pygame.transform.scale(button_image, (100, 50))

button_unlock_image = pygame.image.load("./data/button_unlock.png")
button_unlock_image = pygame.transform.scale(button_unlock_image, (100, 50))

player_front = pygame.image.load("./data/player_front.png")
player_front = pygame.transform.scale(player_front, (50, 50))

player_back = pygame.image.load("./data/player_back.png")
player_back = pygame.transform.scale(player_back, (50, 50))

player_right = pygame.image.load("./data/player_right.png")
player_right = pygame.transform.scale(player_right, (50, 50))

player_left = pygame.image.load("./data/player_left.png")
player_left = pygame.transform.scale(player_left, (50, 50))

wall_cross = pygame.image.load("./data/wall_cross.png")
wall_cross = pygame.transform.scale(wall_cross, (50, 50))

wall_h = pygame.image.load("./data/wall_h.png")
wall_h = pygame.transform.scale(wall_h, (50, 50))

wall_w = pygame.image.load("./data/wall_w.png")
wall_w = pygame.transform.scale(wall_w, (50, 50))

wall_l_d = pygame.image.load("./data/wall_l_d.png")
wall_l_d = pygame.transform.scale(wall_l_d, (50, 50))

wall_l_u = pygame.image.load("./data/wall_l_u.png")
wall_l_u = pygame.transform.scale(wall_l_u, (50, 50))

wall_r_d = pygame.image.load("./data/wall_r_d.png")
wall_r_d = pygame.transform.scale(wall_r_d, (50, 50))

wall_r_u = pygame.image.load("./data/wall_r_u.png")
wall_r_u = pygame.transform.scale(wall_r_u, (50, 50))

target = pygame.image.load("./data/pot.png")
target_image = pygame.transform.scale(target, (50, 50))

ground = pygame.image.load("./data/ground.png")
ground_image = pygame.transform.scale(ground, (50, 50))

tp = pygame.image.load("./data/tp.png")
tp_image = pygame.transform.scale(tp, (50, 50))

arrow = pygame.image.load("./data/arrow.png")
arrow_image = pygame.transform.scale(arrow, (50, 50))

question_mark = pygame.image.load("./data/q_mark.png")
question_mark_image = pygame.transform.scale(question_mark, (50, 50))

foo1 = pygame.image.load("./data/鹰嘴豆泥.jpg")
foo1 = pygame.transform.scale(foo1, (300, 250 ))

foo2 = pygame.image.load("./data/薯饼.jpg")
foo2 = pygame.transform.scale(foo2, (300, 250 ))

foo3 = pygame.image.load("./data/辫子面包.jpg")
foo3 = pygame.transform.scale(foo3, (300, 250 ))

foo4 = pygame.image.load("./data/无酵饼丸子汤.jpg")
foo4 = pygame.transform.scale(foo4, (300, 250 ))

food_name_dic = {0:"蜂蜜", 1:"橄榄油", 2:"胡萝卜", 3:"鸡蛋", 4:"鸡肉", 5:"面粉", 6:"芹菜", 7:"土豆", 8:"无酵饼", 9:"鹰嘴豆"}
foods_id = [i for i in range(10)]
# 食材图片 在data下 food1.jpg food2.jpg ....
foods_image = [ pygame.transform.scale(pygame.image.load("./data/{}.png".format(food_name_dic[i])), (50, 50)) for i in foods_id ]
target1 = [9,1]  #鹰嘴豆+橄榄油=鹰嘴豆泥
target2 = [5,7]  #面粉+土豆=土豆饼 
target3 = [5,3,0]  #面粉+鸡蛋+蜂蜜=辫子面包
target4 = [4,2,6,8]  #鸡肉+胡萝卜+芹菜+无酵饼=无酵饼丸子汤 

class GameState:
    def __init__(self, game, start_menu, help_menu, game_select_menu, game_win_menu):
        self.game = game
        self.start_menu = start_menu
        self.help_menu = help_menu
        self.game_select_menu = game_select_menu
        self.game_win_menu = game_win_menu

    def draw(self):
        if state == START_MENU:
            self.start_menu.draw()
        elif state == GAME_PAGE:
            self.game.draw()
        elif state == HELP_MENU:
            self.help_menu.draw()
        elif state == GAME_SELECT_MENU:
            self.game_select_menu.draw()
        elif state == GAME_WIN_MENU:
            self.game_win_menu.draw()
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
        elif state == GAME_WIN_MENU:
            self.game_win_menu.update(event)
        else:
            assert False, "Wrong state!"
    
    def change_game(self, game):
        self.game = game

def to_start_game():
    global state
    state = GAME_PAGE
    global game_level
    game_level = 1
    
def to_help_menu():
    global state
    state = HELP_MENU

def exit_game():
    pygame.quit()
    sys.exit()
    
def to_level_select_menu():
    global state
    state = GAME_SELECT_MENU
    global game_level
    game_level = 1

def to_start_menu():
    global state
    state = START_MENU
    global game_level
    game_level = 1
    update_game()

def to_start_level_1():
    global state
    state = GAME_PAGE
    global game_level
    game_level = 1
    update_game()

def to_start_level_2():
    if(unlock_level < 2):
        return
    else:
        global state
        state = GAME_PAGE
        global game_level
        game_level = 2
        update_game()

def to_start_level_3():
    if(unlock_level < 3):
        return
    else:
        global state
        state = GAME_PAGE
        global game_level
        game_level = 3
        update_game()

def to_start_level_4():
    if(unlock_level < 4):
        return
    else:
        global state
        state = GAME_PAGE
        global game_level
        game_level = 4
        update_game()

def to_next_level():
    global state
    state = GAME_PAGE
    global game_level
    if game_level < 4:
        game_level += 1
    update_game()

class StartMenu:
    def __init__(self):
        self.buttons = []
        
        self.start_button = Button( 200, 100, 100, 50, red, "开始游戏", BUTTON_COLOR, 25, to_start_game, button_image)
        self.buttons.append(self.start_button)
        
        self.help_button = Button( 200, 200, 100, 50, red, "帮助", BUTTON_COLOR, 25, to_help_menu, button_image)
        self.buttons.append(self.help_button)

        self.level_select_button = Button( 200, 300, 100, 50, red, "选择关卡", BUTTON_COLOR, 25, to_level_select_menu, button_image)
        self.buttons.append(self.level_select_button)
        
        self.exit_button = Button( 200, 400, 100, 50, red, "退出游戏", BUTTON_COLOR, 25, exit_game, button_image)
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
        self.help_text = "请按提示信息按顺序将食物放入锅中\n做成美味的食物吧!!!\n注意:\n1.一定要注意放入食材顺序\n2.传送阵只能传送自己哦\n3.也可以经过锅哦"
        
        self.back_button = Button(150, 400, 100, 50, red, "返回", BUTTON_COLOR, 25, to_start_menu, button_image)
        self.buttons.append(self.back_button)

    def draw(self):
        # 绘制帮助信息文本
        lines = self.help_text.split("\n")
        for i, line in enumerate(lines):
            text_surface = pygame.font.Font(font_path, 20).render(line, True, white)
            screen.blit(text_surface, (100, 200 + i * 30))
        
        # 绘制按钮
        for button in self.buttons:
            button.draw(screen)
    
    def update(self, event):
        for button in self.buttons:
            button.is_clicked(event)

class GameSelectMenu:
    def __init__(self):
        self.buttons = []

        # 添加关卡选择按钮
        self.level1_button = Button(150, 200, 100, 50, red, "Level 1", BUTTON_COLOR, 25, to_start_level_1, button_image)
        self.buttons.append(self.level1_button)

        self.level2_button = Button(150, 300, 100, 50, red, "Level 2", BUTTON_COLOR, 25, to_start_level_2, button_unlock_image)
        self.buttons.append(self.level2_button)

        self.level3_button = Button(250, 200, 100, 50, red, "Level 3", BUTTON_COLOR, 25, to_start_level_3, button_unlock_image)
        self.buttons.append(self.level3_button)

        self.level4_button = Button(250, 300, 100, 50, red, "Level 4", BUTTON_COLOR, 25, to_start_level_4, button_unlock_image)
        self.buttons.append(self.level4_button)

        self.back_button = Button(150, 400, 100, 50, red, "返回", BUTTON_COLOR, 25, to_start_menu, button_image)
        self.buttons.append(self.back_button)

    def draw(self):
        # 绘制按钮
        for index, button in enumerate(self.buttons):
            if index < unlock_level or index > 3:
                button.image = button_image
                button.draw(screen)
            else:
                button.image = button_unlock_image
                button.draw(screen)
    
    def update(self, event):
        for  button in self.buttons:
            button.is_clicked(event)

class GameWinMenu:
    def __init__(self):
        self.buttons = []
        self.win_title = "You win!"
        self.image = None
        self.info = None

        self.back_button = Button(125, 550, 100, 50, red, "返回", BUTTON_COLOR, 25, to_start_menu, button_image)
        self.buttons.append(self.back_button)

        self.next_button = Button(275, 550, 100, 50, red, "下一关", BUTTON_COLOR, 25, to_next_level, button_image)
        self.buttons.append(self.next_button)
    
    def draw(self):
        # 绘制帮助信息文本
        global game_level
        if game_level == 1:
            self.win_title = "制作成功:鹰嘴豆泥！！！"
            self.image = foo1
            self.info = "<鹰嘴豆泥=鹰嘴豆+橄榄油>\n鹰嘴豆泥是以色列日常膳食的常见部分。它由遵循Kashrut的成分制成。\n19世纪末和20世纪初从欧洲抵达的犹太移民采用了大部分巴勒斯坦当地\n美食,包括鹰嘴豆泥,尽管传统上它是生活在阿拉伯语地区的Mizrahi犹\n太人美食的一部分。来自这些国家的许多Mizrahi犹太移民带来了他们自\n己独特的变种虽然有时被批评为犹太人对巴勒斯坦和阿拉伯文化的挪用,\n鹰嘴豆泥已被采纳为以色列的非官方“国菜”,反映了它在整个以色列\n人口中的巨大受欢迎程度和重要性\n"

        elif game_level == 2:
            self.win_title = "制作成功:薯饼!!!"
            self.image = foo2
            self.info = "<薯饼=面粉+土豆>\n庆祝光明节的传统食物多数是油炸的,象征着圣殿使用的烛台上的油,主\n要包括炸薯饼和甜甜圈。犹太人也喜欢在炸薯饼上面点缀各式美味,从甜品到\n香薄荷,从普通到特别的风味：自制苹果酱、奶油奶酪和烟熏三文鱼、以色列沙拉,\n甚至熏牛肉和芥末等等。"
            
        elif game_level == 3:
            self.win_title = "制作成功:辫子面包！！！"
            self.image = foo3
            self.info = "<辫子面包=面粉+鸡蛋+蜂蜜>\n在犹太历中,一周的开始是周日,从周五傍晚日落时开始的安息日一直延续\n到周六日落后一小时。安息日是犹太教每周一天的休息日。在希伯来圣经中创 \n世纪篇章里讲述上帝在创造世界后,在第七天休息。在这段时间内,按照犹\n太教的规定,不能使用明火、不能远行、不能从事劳动。周五晚上安息日开\n始前,遵守犹太宗教传统的家庭会在家点上蜡烛,并徒步去犹太会堂参加安\n息日的祈祷仪式。仪式结束后,每个家庭会进行一场安息日晚餐,在晚餐中\n要品尝两样食品:红葡萄酒和辫子面包。"

        elif game_level == 4:
            self.win_title = "制作成功:无酵饼丸子汤！！！"
            self.image = foo4
            self.info = "<无酵饼丸子汤=鸡肉+胡萝卜+芹菜+无酵饼>\n按照风俗,逾越节的前两天是要在欢宴中度过的,而家宴上最重要的食物,\n便是无酵饼了。当法老最终释放犹太人之后,他们迅速逃离了家,自然也\n没有时间像平时一样等面包发酵。没发酵的面包被撕成小块扔进篮子带走,\n炽热阳光将它们烤熟,最后成了一张张的饼干。也因此,犹太人认定发\n酵的食物是不洁的,在神圣的逾越节其间,只有无酵饼才是最适宜的食物。\n不知什么时代开始,有人发现无酵饼打碎了磨成粉之后,味道居然和生\n面粉差很大,之前烘焙的过程给了它一种独特的焦香。此去多年后年,有\n人发现,无酵饼捏成丸子后,做汤居然超级好喝。于是乎,这种无酵饼丸\n子汤正式登堂入室,成为一道经典西餐"
           
        
        text_title = pygame.font.Font(font_path, 20).render(self.win_title, True, white)
        
        scroll_offset = 0
        scroll_speed = 20
        font_size = 12
        text_area = pygame.Surface((400, 300))
        lines = self.info.split("\n")
        line_height = font_size + 3
        font = pygame.font.Font(font_path, font_size)
        for i, line in enumerate(lines):
            text_surface = font.render(line, True, white)
            text_area.blit(text_surface, (10, i * line_height + 5 - scroll_offset))
        
        screen.blit(text_title, (100, 15))
        screen.blit(self.image, (100, 50))
        screen.blit(text_area, (50, 350))
        
        
        # 绘制按钮
        if game_level < 4:
            self.next_button.draw(screen)
        self.back_button.draw(screen)
        
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
                elif self.map_data[row][col] == WALL_CROSS:
                    screen.blit(wall_cross, (col * 50, row * 50))
                elif self.map_data[row][col] == WALL_H:
                    screen.blit(wall_h, (col * 50, row * 50))
                elif self.map_data[row][col] == WALL_W:
                    screen.blit(wall_w, (col * 50, row * 50))
                elif self.map_data[row][col] == WALL_L_D:
                    screen.blit(wall_l_d, (col * 50, row * 50))
                elif self.map_data[row][col] == WALL_L_U:
                    screen.blit(wall_l_u, (col * 50, row * 50))
                elif self.map_data[row][col] == WALL_R_D:
                    screen.blit(wall_r_d, (col * 50, row * 50))
                elif self.map_data[row][col] == WALL_R_U:
                    screen.blit(wall_r_u, (col * 50, row * 50))

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
        self.regame_button = Button(0, 550, 100, 50, red, "重新开始", BUTTON_COLOR, 25, update_game, button_image)
        self.start_menu_button = Button(100, 550, 100, 50, red, "返回", BUTTON_COLOR, 25, to_start_menu, button_image)
        self.buttons = [self.regame_button, self.start_menu_button]
        #TODO检查是否存在位置冲突，越界等情况
        
    def draw(self):
        self.map.draw()
        self.target.draw()
        if self.tp:
            self.tp.draw()
        self.player.draw()
        for food in self.foods:
            food.draw()
        for button in self.buttons:
            button.draw(screen)
        for index,food_id in  enumerate(self.target.food_ids):
            screen.blit(foods_image[food_id], (200+index*50, 550))
        for i in range(len(self.target.food_ids),6):
            screen.blit(ground_image, (200+i*50, 550))
        screen.blit(arrow_image, (200+len(self.target.food_ids)*50, 550))
        screen.blit(question_mark_image, (250+len(self.target.food_ids)*50, 550))

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
        if pos_type == ILLEGAL :
            return False
        elif pos_type == GROUND or pos_type == TARGET:
            self.player.move(direction)
        elif pos_type == TP:
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

            if self.check_pos([new_x, new_y]) == GROUND :
                self.player.move(direction)
                food.pos = [new_x, new_y]
            elif self.check_pos([new_x, new_y]) == TARGET:
                if self.target.check(food.food_id):
                    self.player.move(direction)
                    self.foods.remove(food)
                    self.target.put_in_food(food.food_id)
        
        if self.check_win():
            self.draw()
            # pygame.display.update()   
            text = pygame.font.Font(font_path, 50).render("You win!", True, green)
            text_rect = text.get_rect(center=(width/2, height/2))
            screen.blit(text, text_rect)
            pygame.display.update()
            pygame.time.delay(1000)
            global game_level
            global unlock_level
            if(unlock_level < game_level + 1):
                unlock_level = game_level + 1
            global state
            state = GAME_WIN_MENU
    
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
        if self.map.map_data[x][y] <= ILLEGAL:
            return ILLEGAL

        if pos == self.target.pos:
            return TARGET
        for food in self.foods:
            if pos == food.pos:
                return FOOD
        if pos == self.player.pos:
            return PLAYER
        
        if self.tp and self.tp.check(pos):
            return TP

        return GROUND

    def check_win(self):
        if self.target.is_finish():
            return True
        else:
            return False
    
    def update(self, event):
        if event.type==pygame.MOUSEBUTTONDOWN:
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
    def __init__(self, x, y, width, height, color, text, text_color, font_size, click_handler, image=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(font_path, font_size)
        self.click_handler = click_handler  # 传递点击处理函数参数
        self.image = image
        if self.image:
            self.image = pygame.transform.scale(self.image, (width, height))
        self.image_rect = self.image.get_rect(center=self.rect.center) if self.image else None

    def draw(self, screen):
        if self.image:
            self.image_rect = self.image.get_rect(center=self.rect.center)
            screen.blit(self.image, self.image_rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

        text_render = self.font.render(self.text, True, self.text_color)
        text_rect = text_render.get_rect(center=self.rect.center)
        screen.blit(text_render, text_rect)

    def is_clicked(self, event, *args, **kwargs):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
            if self.rect.collidepoint(event.pos):
                self.click_handler(*args, **kwargs)  # 调用点击处理函数

# 创建地图



def init_game():
    global game
    if game_level == 1:

        map_data = [
    [-5, -3, -3,-3, -3, -3, -3, -3, -3, -7],
    [-2, 1, 1, 1, 1, 1, 1, 1, 1, -2],
    [-2, 1, 1, 1, 1, 1, 1, 1, 1, -2],
    [-2, 1, 1, -5, -3, -3, -3, -3, -3, -1],
    [-2, 1, 1, -2, 1, 1, 1, 1, 1, -2],
    [-2, 1, 1, 1, 1, 1, 1, 1, 1, -2],
    [-1, -3, -3, -3, 1, 1, -2, 1, 1, -2],
    [-2, 1, 1, 1, 1, 1, -2, 1, 1, -2],
    [-2, 1, 1, 1, 1, 1, -2, 1, 1, -2],
    [-4, -3 ,-3, -3, -3, -3, -1, -3, -3, -6],
    [1, 1, 1, 1 ,1, 1, 1, 1, 1, 1],
    ]
        map = Map(map_data)
        player = Player([1, 8])
        foods = [ Food([2, 4], target1[0]), Food([7, 5], target1[1])]
        target = Target([8, 8], target1)
        
        game = Game(map, player, foods, target, None)
    elif game_level == 2:
        map_data = [
    [1, 1, -5 ,-3, -3, -3, -3, -7, 1, 1],
    [1, 1, -2, 1, 1, 1, 1, -2, 1, 1],
    [-5, -3, -6, 1, 1, 1, 1, -4, -3, -7],
    [-2, 1, 1, 1, -2, 1, 1, 1, 1, -2],
    [-2, 1, 1, 1, -2, 1, -2, 1, 1, -2],
    [-2, 1, 1, 1, 1, 1, -2, 1, 1, -2],
    [-4, -3, -7, 1, 1, 1, -4, -1, -3, -6],
    [1, 1, -2, 1, 1, 1, 1, -2, 1, 1],
    [1, 1, -4, -3, -3, -3, -3, -6, 1, 1],
    [1, 1 ,1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1 ,1, 1, 1, 1, 1, 1],
    ]
        map = Map(map_data)
        player = Player([5, 8])
        foods = [ Food([2, 5], target2[0]), Food([3, 7], target2[1])]
        target = Target([3, 3], target2)
        
        game = Game(map, player, foods, target, None)
    elif game_level == 3:
        map_data = [
    [-5, -3, -3 ,-3, -3, -3, -3, -3, -3, -7],
    [-2, 1, 1, 1 ,1, 1, 1, 1, 1, -2],
    [-1, -3, -7, 1 ,1, 1, 1, -2, 1, -2],
    [-2, 1, -4, -3 ,-3, -7, 1, -2, 1, -2],
    [-2, 1, 1, 1 ,1, -2, 1, -4, -3, -1],
    [-1, -3, -3, -3 ,1, 1, 1, 1, 1, -2],
    [-2, 1, 1, 1 ,1, -3, -3, -3, 1, -2],
    [-2, 1, 1, 1 ,1, 1, 1, 1, 1, -2],
    [-2, 1, 1, 1 ,-2, 1, 1, 1, 1, -2],
    [-4, -3, -3 ,-3, -1, -3, -3, -3, -3, -6],
    [1, 1, 1, 1 ,1, 1, 1, 1, 1, 1],
    ]
        map = Map(map_data)
        tp = Teleportation([3, 1], [3, 8])
        player = Player([1, 1])
        foods = [ Food([4, 2], target3[0]), Food([2, 4], target3[1]), Food([7, 6], target3[2])]
        target = Target([4, 4], target3)

        game = Game(map, player, foods, target, tp)
 
# WALL_CROSS = -1
# WALL_H = -2
# WALL_W = -3
# WALL_L_D = -4
# WALL_L_U = -5
# WALL_R_D = -6
# WALL_R_U = -7
    elif game_level == 4:
        map_data = [
    [-5, -3, -3 ,-3, -1, -3, -3, -3, -3, -7],
    [-2, 1, 1, 1 ,-2, 1, 1, 1, 1, -2],
    [-2, 1, 1, 1 ,-2, 1, -2, 1, 1, -2],
    [-2, 1, 1, 1, -2, 1, -2, 1, 1, -2],
    [-1, -3, 1, -3 ,-6, 1, -2, 1, 1, -2],
    [-2, 1, 1, 1 ,1, 1, -2, 1, 1, -2],
    [-2, 1, 1, -2 ,1, 1, -2, 1, 1, -2],
    [-2, 1, 1, -2 ,1, 1, 1, 1, 1, -2],
    [-2, 1, 1, -2 ,1, 1, 1, 1, 1, -2],
    [-4, -3, -3 ,-3, -3, -3, -3, -3, -3, -6],
    [1, 1, 1, 1 ,1, 1, 1, 1, 1, 1]
    ]
        map = Map(map_data)
        tp = Teleportation([1, 2], [7, 8])
        player = Player([8, 8])
        foods = [ Food([6, 4], target4[0]), Food([5, 3], target4[1]), Food([2, 2], target4[2]), Food([3, 7], target4[3])]
        target = Target([5, 2], target4)
        
        game = Game(map, player, foods, target, tp)
    else:
        assert False, "Wrong game level!"

def update_game():
    init_game()
    game_state.change_game(game)

init_game()

game_win_menu = GameWinMenu()
help_menu = HelpMenu()
game_select_menu = GameSelectMenu()
start_menu = StartMenu()
game_state = GameState(game, start_menu, help_menu, game_select_menu, game_win_menu)

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
   
