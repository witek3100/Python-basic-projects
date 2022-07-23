import pygame
import random
import time

lo=random.randint(0,19)
# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((400, 400))

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            class kwadrat:
                def __init__(self, xowe, ykowe):
                    self.xowe=xowe
                    self.ykowe=ykowe
                    self.dotyk=0
                    self.image=pygame.image.load("pelny.png")
            with open("nazwy.txt", "r") as nazwy:
                names = nazwy.readlines()
            pion=0
            poziom=0
            for y in range(len(names)):
                names[y] = names[y].replace(" ", " ")
                names[y] = names[y].replace("\n", "_")
            names = dict(zip(names, [None]*len(names)))
            print(names)
            for i in names:
                names[i] = pygame.image.load("pusty.png")
                pion+=1
                if pion <= 19:
                    screen.blit(names[i], (pion*20, poziom*20))
                else:
                    pion=0
                    poziom+=1
                    screen.blit(names[i], (pion * 20, poziom*20))
            jd = pygame.image.load("pusty.png")
            screen.blit(jd, (0, 0))
            pygame.display.flip()
            with open("nazwy.txt", "r") as nazwy:
                imiona = nazwy.readlines()
                for y in range(len(imiona)):
                    imiona[y] = imiona[y].replace(" ", " ")
                    imiona[y] = imiona[y].replace("\n", "_")
            imiona = dict(zip(names, [None] * len(names)))
            for x in imiona:
                imiona[x] = kwadrat(lo, 0)
                screen.blit(imiona[x].image, (imiona[x].xowe, imiona[x].ykowe))
                pygame.display.flip()
                time.sleep(10)

            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()