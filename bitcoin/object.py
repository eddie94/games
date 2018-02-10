from source import *

char_size = [31,48]


up = [0, -2]
down = [0, 2]
right = [2, 0]
left = [-2, 0]
stay = [0,0]

class make_char():

    def __init__(self):

        self.money = 100000
        self.bitcoin = 1
        self.itherium = 1
        self.ripple = 1
        self.speed = 2
        self.size = [31,48]
        self.image_index = 0
        self.locus = [0,0,1]
        self.surface = pygame.Surface(char_size)
        self.rect = self.surface.get_rect(center=(640,360))

    def set_design(self,file_name):

        char = pygame.image.load(file_name)

        return char

    def char_rect(self,image):
        return image.get_rect()

    def check_collision(self,obstacle):

        if self.rect.colliderect(obstacle):

            move_up = self.rect.move(up)
            move_down = self.rect.move(down)
            move_left = self.rect.move(left)
            move_right = self.rect.move(right)

            check_top = move_up.top < obstacle.bottom
            check_bot= move_down.bottom > obstacle.top
            check_left=move_left.left < obstacle.right
            check_right=move_right.right > obstacle.left

            if check_top and not(check_bot and check_left and check_right):
                self.rect = self.rect.move(stay)
            elif check_bot and not(check_right and check_left and check_top):
                self.rect = self.rect.move(stay)

    def move(self,object_list,size):

        pressed = pygame.key.get_pressed()

        money_surface = font.render("my cash : %s" % (self.money), False, (0, 0, 0))
        bitcoin_surface = font.render("bitcoin : %.2f" % (self.bitcoin), False, (0, 0, 0))
        itherium_surface = font.render("itherium : %.1s" % (self.itherium), False, (0, 0, 0))
        ripple_surface = font.render("ripple : %s" % (self.ripple), False, (0, 0, 0))
        info_surface = pygame.Surface((300,300))

        if pressed[pygame.K_UP]:
            self.image_index = 1
            next_move = self.rect.move(up)
            if self.rect.top > size[1]:
                ok=[]
                for ob in object_list:
                    if next_move.colliderect(ob):
                        ok.append(1)
                    else:
                        ok.append(0)
                if sum(ok)==0:
                    if next_move.top < size[1]:
                        self.rect.top = size[1]
                    else:
                        self.rect = self.rect.move(up)
        if pressed[pygame.K_DOWN]:
            self.image_index = 0
            next_move = self.rect.move(down)
            if self.rect.bottom < size[3]:
                ok=[]
                for ob in object_list:
                    if next_move.colliderect(ob):
                        ok.append(1)
                    else:
                        ok.append(0)
                if sum(ok)==0:
                    if next_move.bottom > size[3]:
                        self.rect.bottom = size[3]
                    else:
                        self.rect = self.rect.move(down)
        if pressed[pygame.K_LEFT]:
            self.image_index = 2
            next_move = self.rect.move(left)
            if self.rect.left > size[0]:
                ok=[]
                for ob in object_list:
                    if next_move.colliderect(ob):
                        ok.append(1)
                    else:
                        ok.append(0)
                if sum(ok)==0:
                    if next_move.left < size[0]:
                        self.rect.left = size[0]
                    else:
                        self.rect = self.rect.move(left)
        if pressed[pygame.K_RIGHT]:
            self.image_index = 3
            next_move = self.rect.move(right)
            if self.rect.right < size[2]:
                ok=[]
                for ob in object_list:
                    if next_move.colliderect(ob):
                        ok.append(1)
                    else:
                        ok.append(0)
                if sum(ok)==0:
                    if next_move.right > size[2]:
                        self.rect.right = size[2]
                    else:
                        self.rect = self.rect.move(right)
        if pressed[pygame.K_i]:
            end = False
            while not end:
                for ev in pygame.event.get(pygame.KEYDOWN):
                    if ev.key == pygame.K_ESCAPE:
                        end = True
                info_surface.fill(white)
                screen.blit(info_surface,(40,60))
                screen.blit(money_surface, (40,90))
                screen.blit(bitcoin_surface, (40,140))
                screen.blit(itherium_surface, (40,190))
                screen.blit(ripple_surface, (40, 240))
                pygame.display.flip()


class object():

    def __init__(self):
        self.width = 0
        self.height = 0
        self.surface = pygame.Surface([self.width, self.height])
        self.rect = self.surface.get_rect()

    def set_design(self,name):

        design = pygame.image.load(name)
        return design

    def set_size(self,width, height,x_length,y_length):

        '''
        :param width: 왼쪽 변의 위치
        :param height: 위쪽 변의 위치
        :param x_length: 오른쪽으로의 길이
        :param y_length: 위쪽으로의 길이
        '''

        self.surface = pygame.Surface([x_length, y_length])
        self.rect = self.surface.get_rect(top=height,left=width, bottom=height+y_length, right = width+x_length)
        return [width,height,width+x_length, height+y_length]