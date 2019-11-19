import pygame, time

pygame.init()

window = pygame.display.set_mode((600, 300))
myfont = pygame.font.SysFont('comic sans', 60)
label =  myfont.render("meow", 1, (255,51,255))
window.blit(label, (100,100))
pygame.display.update()
time.sleep(3)
pygame.quit()
