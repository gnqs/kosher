import pygame
import sys

ILLEGAL = 0
GROUND = 1
TARGET = 2
FOOD = 3
PLAYER = 4

# 屏幕大小
size = width, height = 500, 500
# 颜色定义
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 128, 0)

TARGET = [0, 1, 2]



# 初始化Pygame和屏幕
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Kosher")

# 加载图片并调整大小
player = pygame.image.load("./data/player.jpg")
player_image = pygame.transform.scale(player, (50, 50))

box = pygame.image.load("./data/box.jpg")
box_image = pygame.transform.scale(box, (50, 50))

target = pygame.image.load("./data/target.jfif")
target_image = pygame.transform.scale(target, (50, 50))

ground = pygame.image.load("./data/ground.jfif")
ground_image = pygame.transform.scale(ground, (50, 50))

foods_id = [0,1,2]
# 食材图片 在data下 food1.jpg food2.jpg ....
foods_image = [ pygame.transform.scale(pygame.image.load("./data/food{}.jpg".format(i)), (50, 50)) for i in foods_id ]

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
                    screen.blit(box_image, (col * 50, row * 50))

class Player:
    def __init__(self, pos):
        self.pos = pos
    def draw(self):
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

class Box:
    def __init__(self, pos):
        self.pos = pos

class Food( Box ):
    def __init__(self, pos, food_id):
        super().__init__(pos)
        self.food_id = food_id    
    def draw(self):
        screen.blit(foods_image[self.food_id], (self.pos[1] * 50, self.pos[0] * 50))

class Game:
    def __init__(self, map, player, foods:list, target):
        self.map = map
        self.player = player
        self.foods = foods 
        self.target = target
        #TODO检查是否存在位置冲突，越界等情况
        
    def draw(self):
        self.map.draw()
        self.target.draw()
        self.player.draw()
        for food in self.foods:
            food.draw()
    def move_player(self, direction):
        x , y = self.player.pos
        if direction == "up":
            x -= 1
        elif direction == "down":
            x += 1
        elif direction == "left":
            y -= 1
        elif direction == "right":
            y += 1
        else:
            assert False, "Wrong direction!"
        
        pos_type = self.check_pos([x, y])
        print(pos_type , x, y )
        if pos_type == ILLEGAL:
            return False
        elif pos_type == GROUND or pos_type == TARGET:
            self.player.move(direction)
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
        return GROUND

    def check_win(self):
        if self.target.is_finish():
            return True
        else:
            return False

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

class Button( pygame.sprite.Sprite ):
    def __init__ (self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.bottomleft = screen.get_rect().bottomleft
    
    def draw(self):
        screen.blit(self.image, self.rect)

    def clicked(self, pos): 
        if self.rect.collidepoint(pos):
            return True
        else:   
            return False
            
# 创建地图


def init_game():
    map_data = [
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    ]
    map = Map(map_data)
    player = Player([0, 0])
    foods = [ Food([1, 1], 0), Food([2, 2], 1), Food([3, 3], 2) ]
    target = Target([4, 4], [0, 1, 2])
    game = Game(map, player, foods, target)
    return game

game = init_game()
button_image = pygame.image.load("./data/button.jpg")
button_image = pygame.transform.scale(button_image, (50, 50))
button = Button( button_image )
# 游戏循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            print("鼠标点击的位置：",pygame.mouse.get_pos())
            if button.clicked(pygame.mouse.get_pos()):
                print("button clicked")
                game = init_game()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.move_player("up")
            elif event.key == pygame.K_DOWN:
                game.move_player("down")
            elif event.key == pygame.K_LEFT:
                game.move_player("left")
            elif event.key == pygame.K_RIGHT:
                game.move_player("right")
    
    # 绘制地图
    screen.fill(black)
    game.draw()
    button.draw()
    pygame.display.update()
   
