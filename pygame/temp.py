import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Shoot Game")

x=230
y=460
width=30
height=30
vel=10
ox=10
oy=10

run = True
while run:
    pygame.time.delay(5)

    while ox < 500 - width - vel:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    z = y-30
                    while z > vel:
                        z -= 2
                        pygame.time.delay(10)
                        win.fill((0,0,0))
                        pygame.draw.rect(win, (255,0,0), (x,z,width,height))
                        pygame.draw.rect(win, (255,255,0), (x,y,width,height))
                        pygame.draw.rect(win, (255,255,0), (ox,oy,width,height))
                        pygame.display.update()
                        ox += vel
                        if (ox>=480):
                            ox = 10
                            win.fill((0,0,0))
                            pygame.draw.rect(win, (255,0,0), (x,z,width,height))
                            pygame.draw.rect(win, (255,255,0), (x,y,width,height))
                            pygame.draw.rect(win, (255,255,0), (ox,oy,width,height))
                            pygame.display.update()

        ox += vel
        pygame.time.delay(15)
        win.fill((0,0,0))
        pygame.draw.rect(win, (255,255,0), (ox,oy,width,height))
        pygame.draw.rect(win, (255,255,0), (x,y,width,height))
        pygame.display.update()

    ox=10

    win.fill((0,0,0))
    pygame.draw.rect(win, (255,255,0), (x,y,width,height))
    pygame.display.update()

pygame.quit()
