import pygame
import sif

white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()

W = 1200
H = 600

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("IFS")
sc.fill(white)

surf_e = pygame.Surface((400, 400))
surf_e.fill(black)
# pygame.draw.rect(surf_e, white, surf_e.get_rect(), 6)
scale = 1 / 3
C = [(scale, 0, 0, scale, 0, 0),
     (scale, 0, 0, scale, scale, 0),
     (scale, 0, 0, scale, 2 * scale, 0),
     (scale, 0, 0, scale, 0, scale),
     (scale, 0, 0, scale, 0, 2 * scale),
     (scale, 0, 0, scale, scale, 2 * scale),
     (scale, 0, 0, scale, 2 * scale, scale),
     (scale, 0, 0, scale, 2 * scale, 2 * scale)
     ]

system = sif.SIF(C)
surf_res = system.create_attractor(surf_e, 0)
surf_res = pygame.transform.flip(surf_res, False, True)

FPS = 30
clock = pygame.time.Clock()

n_iter = 1
step = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    step += 1
    if step > 30 and n_iter < 6:
        step = 0
        surf_res = system.create_attractor(surf_e, n_iter)
        surf_res = pygame.transform.flip(surf_res, False, True)
        n_iter += 1

    sc.blit(surf_res, (400, 100))
    pygame.display.update()
    clock.tick(FPS)
