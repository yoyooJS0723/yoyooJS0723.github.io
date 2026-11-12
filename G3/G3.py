import pygame
import keyboard
import move,show
from item import *
print('在這裡',player['pos'])
def entity_draw(n):
    return screen.blit(n["show"],(n['pos'][0],n['pos'][1]))
def giu_draw(n):
    return screen.blit(n["show"],(n['pos'][0],n['pos'][1]))
while True:
    if keyboard.is_pressed('ESC'):
        break
    #鍵盤
      #左
    left["turn"],left["show"],player["pos"][0] = move.leftf(keyboard.is_pressed('a') or keyboard.is_pressed('left'),left,player["pos"][0])
      #右
    right["turn"],right["show"],player["pos"][0] = move.rightf(keyboard.is_pressed('d') or keyboard.is_pressed('right'),right,player["pos"][0])
      #上
    up["turn"],up["show"],player["on_the_ground"] = move.upf(keyboard.is_pressed('w') or keyboard.is_pressed('up'),up,player["on_the_ground"])
    #玩家物理量
    up["turn"],player = move.physics(up["turn"],player)
    #玩家渲染
    player["show"] = show.playerf(left["turn"],right["turn"])
    #渲染
    screen.fill("aqua")
    pygame.draw.rect(screen,pygame.Color([122, 226, 80]),grass)
    for i in entity_list:
        entity_draw(i)
    for i in giu_list:
        giu_draw(i)
    pygame.display.flip()
    tick.tick(60)
pygame.quit()
