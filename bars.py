import pygame
import random
import easygui
# Beginning of global variables
is_running_run = False
is_running_blocks = False
is_running_end = False
window_surface = pygame.display.set_mode((500, 600))
playerswitch = 0
score = 0
hiscore = 0
medscore = 0
lowscore = 0


# End of global variables

# Beginning of the UI class
def UI():
    global hiscore, medscore, lowscore
    pygame.display.set_caption('Bars')
    startImg = pygame.transform.scale((pygame.image.load("resources/images/start.png")), (150, 100))
    window_surface.blit(startImg, (175, 150))
    is_running = True
    j = 0
    white = (255, 255, 255)
    blue = (0, 255, 255)
    font = pygame.font.Font('freesansbold.ttf', 20)
    window_surface.blit(font.render("Leaderboard", True, white), (187, 325))
    window_surface.blit(font.render("__------------------------------------__", True, blue), (97, 360))
    # Code to update leaderboard
    with open("resources/leaderboard/leaderboard.txt"):
        lines = [line.rstrip('\n') for line in open('resources/leaderboard/leaderboard.txt')]
    hiscore = int(lines[1])
    medscore = int(lines[3])
    lowscore = int(lines[5])
    k = 0
    le = 1
    count = 1
    while k < 6:
        white = (255, 255, 255)
        font = pygame.font.Font('freesansbold.ttf', 20)
        if count == 1:
            if le == 1:
                window_surface.blit(font.render(lines[k], True, white), (150, 400))
            if le == -1:
                window_surface.blit(font.render(lines[k], True, white), (325, 400))
                count = 2
        elif count == 2:
            if le == 1:
                window_surface.blit(font.render(lines[k], True, white), (150, 450))
            if le == -1:
                window_surface.blit(font.render(lines[k], True, white), (325, 450))
                count += 1
        elif count == 3:
            if le == 1:
                window_surface.blit(font.render(lines[k], True, white), (150, 500))
            if le == -1:
                window_surface.blit(font.render(lines[k], True, white), (325, 500))
                count += 1
        pygame.display.update()
        k += 1
        le *= -1
    # End of leaderboard code

    global is_running_run
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    window_surface.fill(pygame.Color("black"))
                    j = 1
                    is_running_run = True
                    is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_running = False
                    pygame.quit()
                    exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 175 < x < 325 and 150 < y < 250 and j == 0:
                    window_surface.fill(pygame.Color("black"))
                    j = 1
                    is_running_run = True
                    is_running = False
        pygame.display.update()


# End of environment class
# Beginning of randomize class to decide which block should be missing
def Random():
    # initial random blocks
    a = random.randint(0, 3)
    b = random.randint(0, 3)
    while b == a:
        b = random.randint(0, 3)
    c = random.randint(0, 3)
    while c == a or c == b:
        c = random.randint(0, 3)
    d = random.randint(0, 3)
    while d == a or d == b or d == c:
        d = random.randint(0, 3)
    return a, b, c, d


# End of randomize class
def Run():
    # Loads Images
    global score
    global is_running_run
    global playerswitch
    global is_running_end
    block = pygame.transform.scale((pygame.image.load("resources/images/red.jpg")), (125, 30))
    block1 = pygame.transform.scale((pygame.image.load("resources/images/blue.jpg")), (125, 30))
    block2 = pygame.transform.scale((pygame.image.load("resources/images/gold.jpg")), (125, 30))
    block3 = pygame.transform.scale((pygame.image.load("resources/images/green.jpg")), (125, 30))
    player = pygame.transform.scale((pygame.image.load("resources/images/white.jpg")), (25, 25))
    a, b, c, d = Random()
    # Creating the motion and variables for game
    x = 0  # for block
    y = 0  # for player
    count = 0  # for incrementing
    count2 = 0  # for incrementing the blocks longer
    playerswitch = 0  # to switch player direction
    saver = playerswitch  # saves the player value
    score = 0
    # sets which block is missing
    if a == 0:
        start = 0
        end = 125
    elif b == 0:
        start = 125
        end = 250
    elif c == 0:
        start = 250
        end = 375
    else:
        start = 375
        end = 500
    while is_running_run:
        if a != 0:
            window_surface.blit(block, (0, x))
        if b != 0:
            window_surface.blit(block1, (125, x))
        if c != 0:
            window_surface.blit(block2, (250, x))
        if d != 0:
            window_surface.blit(block3, (375, x))
        window_surface.blit(player, (y, 550))
        # Slows down blocks movement
        count += 0.25
        if count.is_integer():
            if playerswitch == 0:
                y += 1
            if playerswitch == 1:
                y -= 1
            count2 += 0.5
            if count2.is_integer():
                x += 1
        else:
            pygame.display.flip()
            window_surface.fill(0)
        if x == 700:
            x = 0
            a, b, c, d = Random()
            if a == 0:
                start = 0
                end = 125
            elif b == 0:
                start = 125
                end = 250
            elif c == 0:
                start = 250
                end = 375
            else:
                start = 375
                end = 500
            score += 1
        if y == 475:
            playerswitch = 1
            saver = playerswitch
        if y == 0:
            playerswitch = 0
            saver = playerswitch
        # Tests if player hit block
        if 520 < x < 575 and (start > y or y + 25 > end):
            is_running_run = False
            is_running_end = True
            End()
        global is_running_blocks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running_blocks = False
                pygame.quit()
                exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playerswitch = 3
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    playerswitch = saver
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_running_blocks = False
                    pygame.quit()
                    exit(0)


# Beginning of End class
def End():
    global is_running_end
    global is_running_run
    global window_surface
    global score
    global hiscore, medscore, lowscore
    global happened
    i = 0
    happened = 1
    x = 1
    j = 0
    # Code to update leaderboard

    # End of leaderboard code
    oooImg = pygame.transform.scale((pygame.image.load("resources/images/wtf.png")), (250, 300))
    window_surface.blit(oooImg, (125, 25))
    pygame.display.update()
    while is_running_end:
        if x == 250000:
            white = (255, 255, 255)
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render('Your Score:', True, white)
            window_surface.blit(text, (100, 365))
            pygame.display.update()
        if x == 500000:
            white = (255, 255, 255)
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render(str(score), True, white)
            window_surface.blit(text, (350, 365))
            pygame.display.update()
        if x == 750000:
            retryImg = pygame.transform.scale((pygame.image.load("resources/images/retry.png")), (50, 50))
            window_surface.blit(retryImg, (225, 435))
            pygame.display.update()
            j = 1
            i = 2
        x += 1
        if score > lowscore and i == 2:
            myvar = easygui.enterbox(
                "Congrats you made it to the prestigous leaderboard! Please enter your name below (must be less than "
                "10 characters).")
            try:
                if len(myvar) <= 10:
                    pass
            except TypeError:
                myvar = "Ghost"
            if len(myvar) <= 10:
                with open('resources/leaderboard/leaderboard.txt'):
                    lines = [line.rstrip('\n') for line in open('resources/leaderboard/leaderboard.txt')]
                if lowscore < score <= medscore:
                    open('resources/leaderboard/leaderboard.txt', "w").close()
                    file = open("resources/leaderboard/leaderboard.txt", "w")
                    file.write(lines[0] + "\n")
                    file.write(lines[1] + "\n")
                    file.write(lines[2] + "\n")
                    file.write(lines[3] + "\n")
                    file.write(myvar + "\n")
                    file.write(str(score) + "\n")
                    file.close()
                elif medscore < score <= hiscore:
                    open('resources/leaderboard/leaderboard.txt', "w").close()
                    file = open("resources/leaderboard/leaderboard.txt", "w")
                    file.write(lines[0] + "\n")
                    file.write(lines[1] + "\n")
                    file.write(myvar + "\n")
                    file.write(str(score) + "\n")
                    file.write(lines[2] + "\n")
                    file.write(lines[3] + "\n")
                    file.close()
                else:
                    open('resources/leaderboard/leaderboard.txt', "w").close()
                    file = open("resources/leaderboard/leaderboard.txt", "w")
                    file.write(myvar + "\n")
                    file.write(str(score) + "\n")
                    file.write(lines[0] + "\n")
                    file.write(lines[1] + "\n")
                    file.write(lines[2] + "\n")
                    file.write(lines[3] + "\n")
                    file.close()
            i += 1
        i = 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    window_surface.fill(pygame.Color("black"))
                    is_running_run = True
                    is_running_end = False
                    UI()
                    Run()
                    pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 225 < x < 275 and 435 < y < 485 and j == 1:
                    window_surface.fill(pygame.Color("black"))
                    is_running_run = True
                    is_running_end = False
                    UI()
                    Run()
                    pygame.display.update()


# End of End class

# Beginning of the main statements
pygame.init()
UI()
Run()
End()
# End of the main statements
