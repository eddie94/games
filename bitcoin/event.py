from source import *
from object import *
from time import sleep
import random

me = make_char()
left = me.set_design('img/character_design/Afios_standard_left.jpg')
right = me.set_design('img/character_design/Afios_standard_right.jpg')
front = me.set_design('img/character_design/Afios_standard_forward.jpg')
back = me.set_design('img/character_design/Afios_standard_back.jpg')
images = [front,back,left,right]

screen = pygame.display.set_mode((400,400))

def room(mychar):

    global images

    room_floor = object()
    room_floor_design = room_floor.set_design('img/map_design/Room_floor.jpg')
    room_floor_size = room_floor.set_size(0,0,400,400)

    btc_carpet = object()
    btc_carpet_design = btc_carpet.set_design('img/map_design/Red_carpet2.jpg')
    btc_carpet_size = btc_carpet.set_size(0,150,50,100)

    ither_carpet = object()
    ither_carpet_design = ither_carpet.set_design('img/map_design/Red_carpet2.jpg')
    ither_carpet_size = ither_carpet.set_size(350,150,50,100)

    ripple_carpet = object()
    ripple_carpet_design = ripple_carpet.set_design('img/map_design/Red_carpet.gif')
    ripple_carpet_size = ripple_carpet.set_size(150,0,100,50)

    exchange_carpet = object()
    exchange_carpet_design = exchange_carpet.set_design('img/map_design/Red_carpet.gif')
    exchange_carpet_size = exchange_carpet.set_size(150,350,100,50)

    object_list = []

    done = False

    #mychar.rect.center = room_floor.rect.center

    while not done:
        quit()

        mychar.move(object_list,room_floor_size)

        screen.blit(room_floor_design,room_floor.rect)
        screen.blit(btc_carpet_design,btc_carpet.rect)
        screen.blit(ither_carpet_design,ither_carpet.rect)
        screen.blit(ripple_carpet_design,ripple_carpet.rect)
        screen.blit(exchange_carpet_design,exchange_carpet.rect)
        screen.blit(images[mychar.image_index],mychar.rect)
        pygame.display.flip()

        if mychar.rect.top == ripple_carpet.rect.top and mychar.rect.left > ripple_carpet.rect.left:
            mychar.locus = [0,2,0]
            done = True
        if mychar.rect.left == btc_carpet.rect.left and mychar.rect.top > btc_carpet.rect.top:
            mychar.locus = [0,1,0]
            done = True
        if mychar.rect.right == ither_carpet.rect.right and mychar.rect.top > ither_carpet.rect.top:
            mychar.locus = [0,3,0]
            done = True
        if mychar.rect.bottom == exchange_carpet.rect.bottom and mychar.rect.left > btc_carpet.rect.left:
            mychar.locus = [0,4,0]
            done = True

def btc_room(mychar):

    global images

    ripple_floor = object()
    ripple_floor_design = ripple_floor.set_design('img/map_design/ripple_floor.jpg')
    ripple_floor_size = ripple_floor.set_size(0, 0, 400, 400)

    exit_carpet = object()
    exit_carpet_design = exit_carpet.set_design('img/map_design/Red_carpet2.jpg')
    exit_carpet_size = exit_carpet.set_size(350, 150, 50, 100)

    ripple = object()
    ripple_design = ripple.set_design('img/map_design/btc.jpg')
    ripple_size = ripple.set_size(0, 0, 201, 400)

    logo = object()
    logo_design = logo.set_design('img/map_design/btc_logo.jpg')
    logo_size = logo.set_size(0, 0, 50, 50)

    done = False
    object_list = [ripple]

    while not done:

        quit()

        mychar.move(object_list, ripple_floor_size)

        screen.blit(ripple_floor_design, ripple_floor.rect)
        screen.blit(exit_carpet_design, exit_carpet.rect)
        screen.blit(ripple_design, ripple.rect)
        screen.blit(logo_design, logo.rect)
        screen.blit(images[mychar.image_index], mychar.rect)

        pygame.display.flip()

        if mychar.rect.left == ripple.rect.right:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_SPACE]:
                mychar.bitcoin += 0.01
                nogada_effect(mychar)

        if mychar.rect.right == exit_carpet.rect.right and mychar.rect.top > exit_carpet.rect.top:
            mychar.locus = [1, 0, 0]
            done = True

def ither_room(mychar):
    global images

    ripple_floor = object()
    ripple_floor_design = ripple_floor.set_design('img/map_design/ripple_floor.jpg')
    ripple_floor_size = ripple_floor.set_size(0, 0, 400, 400)

    exit_carpet = object()
    exit_carpet_design = exit_carpet.set_design('img/map_design/Red_carpet2.jpg')
    exit_carpet_size = exit_carpet.set_size(0, 150, 50, 100)

    ripple = object()
    ripple_design = ripple.set_design('img/map_design/btc.jpg')
    ripple_size = ripple.set_size(199, 0, 200, 400)

    logo = object()
    logo_design = logo.set_design('img/map_design/ether_logo.png')
    logo_size = logo.set_size(350, 0, 50, 50)

    done = False
    object_list = [ripple]

    while not done:

        quit()

        mychar.move(object_list, ripple_floor_size)

        screen.blit(ripple_floor_design, ripple_floor.rect)
        screen.blit(exit_carpet_design, exit_carpet.rect)
        screen.blit(ripple_design, ripple.rect)
        screen.blit(logo_design, logo.rect)
        screen.blit(images[mychar.image_index], mychar.rect)

        pygame.display.flip()

        if mychar.rect.right == ripple.rect.left:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_SPACE]:
                mychar.itherium += 0.1
                nogada_effect(mychar)

        if mychar.rect.left == exit_carpet.rect.left and mychar.rect.top > exit_carpet.rect.top:
            mychar.locus = [3, 0, 0]
            done = True

def exchange_room(mychar):

    global images

    ex_floor = object()
    ex_floor_design = ex_floor.set_design('img/map_design/ripple_floor.jpg')
    ex_floor_size = ex_floor.set_size(0,0,400,400)

    ex_desk = object()
    ex_desk_design = ex_desk.set_design('img/map_design/ex_desk.jpg')
    ex_desk_size = ex_desk.set_size(0,198,400,200)

    exit_carpet = object()
    exit_carpet_design = exit_carpet.set_design('img/map_design/Red_carpet.gif')
    exit_carpet_size = exit_carpet.set_size(150, 00, 50, 100)

    done = False
    object_list = [ex_desk]

    while not done:

        quit()
        mychar.move(object_list,ex_floor_size)

        screen.blit(ex_floor_design, ex_floor.rect)
        screen.blit(ex_desk_design,ex_desk.rect)
        screen.blit(exit_carpet_design,exit_carpet.rect)
        screen.blit(images[mychar.image_index],mychar.rect)

        pygame.display.flip()
        pressed = pygame.key.get_pressed()

        if mychar.rect.bottom == ex_desk.rect.top:
            if pressed[pygame.K_SPACE]:
                sleep(0.2)
                exchange(mychar)

        if mychar.rect.top == exit_carpet.rect.top and mychar.rect.left > exit_carpet.rect.left:
            mychar.locus = [4,0,0]
            done = True

def exchange(mychar):

    menu_surface = pygame.Surface((300,300))

    menu1 = font.render('BITCOIN',False,(0,0,0))
    menu2 = font.render('ETHERIUM',False,(0,0,0))
    menu3 = font.render('RIPPLE',False,(0,0,0))
    menu4 = font.render('QUIT',False,(0,0,0))

    done = False
    select_axis=[0,0]

    while not done:
        quit()

        menu_surface.fill(white)
        pressed = pygame.key.get_pressed()

        screen.blit(menu_surface,(50,50))
        screen.blit(menu1,(50,250))
        screen.blit(menu2,(50,300))
        screen.blit(menu3,(200,250))
        screen.blit(menu4,(250,300))

        if pressed[pygame.K_UP] and select_axis[0] == 1:
            select_axis[0] = 0
        if pressed[pygame.K_DOWN] and select_axis[0] == 0:
            select_axis[0] = 1
        if pressed[pygame.K_LEFT] and select_axis[1] == 1:
            select_axis[1] = 0
        if pressed[pygame.K_RIGHT] and select_axis[1] == 0:
            select_axis[1] = 1

        if select_axis == [0,0]:
            pygame.draw.line(screen,(0,0,0),[50,300],[180,300],5)
        elif select_axis == [0,1]:
            pygame.draw.line(screen,(0,0,0),[200,300],[320,300],5)
        elif select_axis == [1,0]:
            pygame.draw.line(screen,(0,0,0),[50,340],[230,340],5)
        elif select_axis ==[1,1]:
            pygame.draw.line(screen, (0, 0, 0), [250,340], [320,340], 5)

        if pressed[pygame.K_SPACE]:

            if select_axis == [0, 0]:
                sleep(0.2)
                btc_menu(mychar)
            elif select_axis == [0, 1]:
                sleep(0.2)
                ripple_menu(mychar)
            elif select_axis == [1, 0]:
                sleep(0.2)
                ether_menu(mychar)
            elif select_axis == [1, 1]:
                done = True
                sleep(0.2)

        pygame.display.flip()

def btc_menu(mychar):

    cost = random.randint(1,260000)
    fail = random.random()
    select_axis = [0, 0]

    #bitcoin_surface = font.render("my bitcoin : %.2f" % (mychar.bitcoin), False, (0, 0, 0))
    #money_surface = font.render("my cash : %s" % (mychar.money), False, (0, 0, 0))
    cost_surface = font.render('current cost : %s' %(cost),False,(0,0,0))
    menu_surface = pygame.Surface((300, 300))
    menu1 = font.render('BUY', False, (0, 0, 0))
    menu2 = font.render('SELL', False, (0, 0, 0))
    menu3 = font.render('RETURN', False, (0, 0, 0))

    done = False

    while not done:
        bitcoin_surface = font.render("my bitcoin : %.2f" % (mychar.bitcoin), False, (0, 0, 0))
        money_surface = font.render("my cash : %d" % (mychar.money), False, (0, 0, 0))

        quit()
        menu_surface.fill(white)
        pressed = pygame.key.get_pressed()

        screen.blit(menu_surface, (50, 50))
        screen.blit(menu1, (50, 250))
        screen.blit(menu2, (50, 300))
        screen.blit(menu3, (200, 250))
        screen.blit(cost_surface, (50,50))
        screen.blit(money_surface,(50,80))
        screen.blit(bitcoin_surface,(50,110))

        if pressed[pygame.K_UP]:
            select_axis[0] = 0
        if pressed[pygame.K_DOWN]:
            select_axis[0] = 1
        if pressed[pygame.K_LEFT] and select_axis[1] == 1:
            select_axis[1] = 0
        if pressed[pygame.K_RIGHT] and select_axis[1] == 0:
            select_axis[1] = 1

        if select_axis == [0,0]:
            pygame.draw.line(screen,(0,0,0),[50,300],[180,300],5)
        elif select_axis == [0,1]:
            pygame.draw.line(screen,(0,0,0),[200,300],[320,300],5)
        elif select_axis[0] == 1:
            pygame.draw.line(screen,(0,0,0),[50,340],[230,340],5)

        if pressed[pygame.K_SPACE]:
            sleep(0.2)
            if select_axis == [0, 0]:#buy
                if mychar.money > cost:
                    mychar.bitcoin += mychar.money/cost
                    mychar.money = 0
                else:
                    error_font = pygame.font.SysFont('Arial',30)
                    error = error_font.render('NOT ENOUGH MONEY',False,(0,0,0))
                    screen.blit(error,(50,150))
                    pygame.display.flip()
                    sleep(1)
            elif select_axis == [0, 1]:#return
                sleep(0.2)
                done = True
            elif select_axis[0] == 1:#sell
                if fail > 0.7:
                    mychar.money += mychar.bitcoin * cost
                    mychar.bitcoin = 0
                else:
                    error_font = pygame.font.SysFont('Arial', 30)
                    error = error_font.render('REGULATED T.T', False, (0, 0, 0))
                    screen.blit(error, (50, 150))
                    pygame.display.flip()
                    sleep(1)

        pygame.display.flip()

def ether_menu(mychar):
    cost = random.randint(1, 50000)
    fail = random.random()
    select_axis = [0, 0]

    cost_surface = font.render('current cost : %s' % (cost), False, (0, 0, 0))
    menu_surface = pygame.Surface((300, 300))
    menu1 = font.render('BUY', False, (0, 0, 0))
    menu2 = font.render('SELL', False, (0, 0, 0))
    menu3 = font.render('RETURN', False, (0, 0, 0))

    done = False

    while not done:
        ether_surface = font.render("my ether : %.1f" % (mychar.itherium), False, (0, 0, 0))
        money_surface = font.render("my cash : %d" % (mychar.money), False, (0, 0, 0))

        quit()
        menu_surface.fill(white)
        pressed = pygame.key.get_pressed()

        screen.blit(menu_surface, (50, 50))
        screen.blit(menu1, (50, 250))
        screen.blit(menu2, (50, 300))
        screen.blit(menu3, (200, 250))
        screen.blit(cost_surface, (50, 50))
        screen.blit(money_surface, (50, 80))
        screen.blit(ether_surface, (50, 110))

        if pressed[pygame.K_UP]:
            select_axis[0] = 0
        if pressed[pygame.K_DOWN]:
            select_axis[0] = 1
        if pressed[pygame.K_LEFT] and select_axis[1] == 1:
            select_axis[1] = 0
        if pressed[pygame.K_RIGHT] and select_axis[1] == 0:
            select_axis[1] = 1

        if select_axis == [0, 0]:
            pygame.draw.line(screen, (0, 0, 0), [50, 300], [180, 300], 5)
        elif select_axis == [0, 1]:
            pygame.draw.line(screen, (0, 0, 0), [200, 300], [320, 300], 5)
        elif select_axis[0] == 1:
            pygame.draw.line(screen, (0, 0, 0), [50, 340], [230, 340], 5)

        if pressed[pygame.K_SPACE]:
            sleep(0.2)
            if select_axis == [0, 0]:  # buy
                if mychar.money > cost:
                    mychar.itherium += mychar.money / cost
                    mychar.money = 0
                else:
                    error_font = pygame.font.SysFont('Arial', 30)
                    error = error_font.render('NOT ENOUGH MONEY', False, (0, 0, 0))
                    screen.blit(error, (50, 150))
                    pygame.display.flip()
                    sleep(1)
            elif select_axis == [0, 1]:  # return
                sleep(0.2)
                done = True
            elif select_axis[0] == 1:  # sell
                if fail > 0.5:
                    mychar.money += mychar.itherium * cost
                    mychar.itherium = 0
                else:
                    error_font = pygame.font.SysFont('Arial', 30)
                    error = error_font.render('REGULATED T.T', False, (0, 0, 0))
                    screen.blit(error, (50, 150))
                    pygame.display.flip()
                    sleep(1)

        pygame.display.flip()

def ripple_menu(mychar):
    cost = random.randint(1, 5)
    select_axis = [0, 0]

    cost_surface = font.render('current cost : %s' % (cost), False, (0, 0, 0))
    menu_surface = pygame.Surface((300, 300))
    menu1 = font.render('BUY', False, (0, 0, 0))
    menu2 = font.render('SELL', False, (0, 0, 0))
    menu3 = font.render('RETURN', False, (0, 0, 0))

    done = False

    while not done:
        ripple_surface = font.render("my ripple : %d" % (mychar.ripple), False, (0, 0, 0))
        money_surface = font.render("my cash : %d" % (mychar.money), False, (0, 0, 0))

        quit()
        menu_surface.fill(white)
        pressed = pygame.key.get_pressed()

        screen.blit(menu_surface, (50, 50))
        screen.blit(menu1, (50, 250))
        screen.blit(menu2, (50, 300))
        screen.blit(menu3, (200, 250))
        screen.blit(cost_surface, (50, 50))
        screen.blit(money_surface, (50, 80))
        screen.blit(ripple_surface, (50, 110))

        if pressed[pygame.K_UP]:
            select_axis[0] = 0
        if pressed[pygame.K_DOWN]:
            select_axis[0] = 1
        if pressed[pygame.K_LEFT] and select_axis[1] == 1:
            select_axis[1] = 0
        if pressed[pygame.K_RIGHT] and select_axis[1] == 0:
            select_axis[1] = 1

        if select_axis == [0, 0]:
            pygame.draw.line(screen, (0, 0, 0), [50, 300], [180, 300], 5)
        elif select_axis == [0, 1]:
            pygame.draw.line(screen, (0, 0, 0), [200, 300], [320, 300], 5)
        elif select_axis[0] == 1:
            pygame.draw.line(screen, (0, 0, 0), [50, 340], [230, 340], 5)

        if pressed[pygame.K_SPACE]:
            sleep(0.2)
            if select_axis == [0, 0]:  # buy
                if mychar.money > cost:
                    mychar.ripple += mychar.money / cost
                    mychar.money = 0
                else:
                    error_font = pygame.font.SysFont('Arial', 30)
                    error = error_font.render('NOT ENOUGH MONEY', False, (0, 0, 0))
                    screen.blit(error, (50, 150))
                    pygame.display.flip()
                    sleep(1)
            elif select_axis == [0, 1]:  # return
                sleep(0.2)
                done = True
            elif select_axis[0] == 1:  # sell
                mychar.money += mychar.ripple * cost
                mychar.ripple = 0

        pygame.display.flip()

def ripple_room(mychar):

    global images

    ripple_floor = object()
    ripple_floor_design = ripple_floor.set_design('img/map_design/ripple_floor.jpg')
    ripple_floor_size = ripple_floor.set_size(0,0,400,400)

    exit_carpet = object()
    exit_carpet_design = exit_carpet.set_design('img/map_design/Red_carpet.gif')
    exit_carpet_size = exit_carpet.set_size(150,350,100,50)

    ripple = object()
    ripple_design = ripple.set_design('img/map_design/ripple.jpg')
    ripple_size = ripple.set_size(0,0,400,200)

    logo = object()
    logo_design = logo.set_design('img/map_design/ripple_logo.jpg')
    logo_size = logo.set_size(0,0,50,50)

    done = False
    object_list = [ripple]

    while not done:

        quit()

        mychar.move(object_list,ripple_floor_size)

        screen.blit(ripple_floor_design,ripple_floor.rect)
        screen.blit(exit_carpet_design,exit_carpet.rect)
        screen.blit(ripple_design,ripple.rect)
        screen.blit(logo_design,logo.rect)
        screen.blit(images[mychar.image_index],mychar.rect)

        pygame.display.flip()

        if mychar.rect.top == ripple.rect.bottom:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_SPACE]:
                mychar.ripple += 1
                nogada_effect(mychar)

        if mychar.rect.bottom == exit_carpet.rect.bottom and mychar.rect.left > exit_carpet.rect.left:
            mychar.locus = [2,0,0]
            done = True

def nogada_effect(char):
    nogada_stone = object()
    nogada_stone_design = nogada_stone.set_design("img/map_design/stone.jpg")
    stone_surface = pygame.Surface([30,30])
    stone_rect1 = stone_surface.get_rect(center = char.rect.center)
    stone_rect2 = stone_surface.get_rect(center = char.rect.center)
    stone_rect3 = stone_surface.get_rect(center = char.rect.center)
    stone_rect4 = stone_surface.get_rect(center = char.rect.center)

    for i in range(50):
        stone_rect1 = stone_rect1.move([0,-2])
        stone_rect2 = stone_rect2.move([0,2])
        stone_rect3 = stone_rect3.move([2,0])
        stone_rect4 = stone_rect4.move([-2,0])
        screen.blit(nogada_stone_design, stone_rect1)
        screen.blit(nogada_stone_design, stone_rect2)
        screen.blit(nogada_stone_design, stone_rect3)
        screen.blit(nogada_stone_design, stone_rect4)
        pygame.display.flip()

def move_rooms(mychar):

    previous_map_id = mychar.locus[0]
    next_map_id = mychar.locus[1]
    print(mychar.locus)
    if mychar.locus[2] == 1:
        mychar.locus[2] = 0
        mychar.rect.center = [200,200]
        room(mychar)

    if previous_map_id == 0 and next_map_id == 2:
        mychar.rect.bottom = 390
        mychar.rect.left = 185
        ripple_room(mychar)
    elif previous_map_id == 2 and next_map_id == 0:
        mychar.rect.top = 10
        mychar.rect.left = 185
        room(mychar)
    elif previous_map_id == 0 and next_map_id == 1:
        mychar.rect.right = 390
        mychar.rect.top = 185
        btc_room(mychar)
    elif previous_map_id == 1 and next_map_id == 0:
        mychar.rect.left = 10
        mychar.rect.top = 185
        room(mychar)
    elif previous_map_id == 0 and next_map_id == 3:
        mychar.rect.left = 10
        mychar.rect.top = 185
        ither_room(mychar)
    elif previous_map_id == 3 and next_map_id == 0:
        mychar.rect.right = 390
        mychar.rect.top = 185
        room(mychar)
    elif previous_map_id == 0 and next_map_id == 4:
        mychar.rect.top = 10
        mychar.rect.left = 185
        exchange_room(mychar)
    elif previous_map_id == 4 and next_map_id == 0:
        mychar.rect.bottom = 390
        mychar.rect.left = 185
        room(mychar)