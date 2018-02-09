from source import *
from object import *

def title():

    title_font = pg.font.SysFont('Arial',50)

    done = False
    title_text = 'avoid the box'
    easy = 'EASY'
    normal = 'NORMAL'

    title_text_surface = title_font.render(title_text,False,(0,0,0))

    easy_surface = font.render(easy,False,(0,0,0))
    normal_surface = font.render(normal,False,(0,0,0))

    menu_select_bar_surface = pg.Surface((150,50))
    menu_select_bar_rect = menu_select_bar_surface.get_rect()
    menu_select_bar_rect.top = 295
    menu_select_bar_rect.left = 225
    menu_num = 0
    while not done:

        quit()
        screen.fill(white)

        screen.blit(title_text_surface,(175,100))
        screen.blit(easy_surface,(250,300))
        screen.blit(normal_surface,(250,400))

        pressed = pg.key.get_pressed()

        if pressed[pg.K_UP] and menu_num == 1:
            menu_num = 0
            menu_select_bar_rect.top -= 100
        if pressed[pg.K_DOWN] and menu_num ==0:
            menu_num = 1
            menu_select_bar_rect.top += 100
        if pressed[pg.K_SPACE]:
            return menu_num

        pg.draw.rect(screen,(0,0,0),menu_select_bar_rect,2)

        pg.display.flip()

def game_play(index):

    if index == 0:

        done = False
        pressed = pg.key.get_pressed()

        with open('high_score_easy.txt','r') as f:
            line=f.readline()

        name = line.split(',')[0]
        score = line.split(',')[1]
        current_score = 0

        me = rect()
        me.rect.center = (300, 300)

        enemy_list = []

        for i in range(4):
            enemy = obstacle()
            check_speed(enemy.speed)
            enemy.rect.center = (randint(10, 590), randint(10, 590))
            enemy_list.append(enemy)

        while not done:

            quit()

            screen.fill(white)

            score_surface = font.render('score:%s' % (current_score), False, (0, 0, 0))
            pg.draw.rect(screen, blue, me.rect)
            for i in range(4):
                pg.draw.rect(screen, blue, enemy_list[i].rect)
            screen.blit(score_surface, (0, 0))
            me.move()

            for i in range(4):
                enemy_list[i].move()
            for i in range(4):
                done = me.rect.colliderect(enemy_list[i].rect)

            pg.display.flip()
            current_score += 1
        if current_score > int(score):
            name = input_box()
            score = current_score

            with open('high_score_easy.txt', 'w') as f:
                f.write('%s,%s' % (name, score))


    elif index == 1:

        done = False
        pressed = pg.key.get_pressed()

        with open('high_score_hard.txt', 'r') as f:
            line = f.readline()

        name = line.split(',')[0]
        score = line.split(',')[1]
        current_score = 0

        me = rect()
        me.rect.center = (300, 300)

        enemy_list = []

        for i in range(10):
            enemy = obstacle()
            check_speed(enemy.speed)
            enemy.rect.center = (randint(10, 590), randint(10, 590))
            enemy_list.append(enemy)

        while not done:

            quit()

            screen.fill(white)

            score_surface = font.render('score:%s' % (current_score), False, (0, 0, 0))
            pg.draw.rect(screen, blue, me.rect)
            for i in range(10):
                pg.draw.rect(screen, blue, enemy_list[i].rect)
            screen.blit(score_surface, (0, 0))
            me.move()

            for i in range(10):
                enemy_list[i].move()
            for i in range(10):
                done = me.rect.colliderect(enemy_list[i].rect)

            pg.display.flip()
            current_score += 1

        if current_score > int(score):
            name = input_box()
            score = current_score

            with open('high_score_hard.txt', 'w') as f:
                f.write('%s,%s' % (name, score))

index = title()
print(index)
game_play(index)