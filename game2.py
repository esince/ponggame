import sys
import pygame #as pg der isek pg olarak kısaltmış oluruz
import random
from pygame.locals import *



WHITE =  (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
YELLOW = (255,255,0)
width = 1000
height = 600

pygame.init()
screen = pygame.display.set_mode((width, height))


ball_pos = [400, 400]
ball_speed = [0.5,0.5]
ball_radius = 12

paddle_width =10
paddle_height =200
paddle_speed = 2

paddle_1_pos_x = 0
paddle_1_pos_y = 170

paddle_2_pos_x = width- paddle_width
paddle_2_pos_y = 170

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

#def roint(num)
#    int(round(a))
#    return roint(num)


	screen.fill(BLACK)

	
	pygame.draw.line(screen, WHITE , (width/2,0), (width/2, height), 5)

	pygame.draw.line(screen, WHITE , (paddle_width,0), (paddle_width, height), 1)

	pygame.draw.line(screen, WHITE , (width- paddle_width,0), (width- paddle_width, height), 1)

	pygame.draw.circle(screen, YELLOW, [int(round(ball_pos[0])), int(round(ball_pos[1]))], ball_radius, 0)
	
	pygame.draw.polygon(screen, WHITE, [[paddle_1_pos_x, paddle_1_pos_y], 
		                               [paddle_1_pos_x, paddle_1_pos_y + paddle_height],
		                               [paddle_1_pos_x + paddle_width,  paddle_1_pos_y + paddle_height],
		                               [paddle_1_pos_x + paddle_width,  paddle_1_pos_y]], 0)


	pygame.draw.polygon(screen, WHITE, [[paddle_2_pos_x, paddle_2_pos_y], 
		                               [paddle_2_pos_x, paddle_2_pos_y + paddle_height],
		                               [paddle_2_pos_x + paddle_width,  paddle_2_pos_y + paddle_height],
		                               [paddle_2_pos_x + paddle_width,  paddle_2_pos_y]], 0)

	keys = pygame.key.get_pressed()
	if keys [K_UP]:
		paddle_2_pos_y -= paddle_speed
	if keys [K_DOWN]:
		paddle_2_pos_y += paddle_speed

	keys = pygame.key.get_pressed()
	if keys [K_w]:
		paddle_1_pos_y -= paddle_speed
	if keys [K_s]:
		paddle_1_pos_y += paddle_speed

	ball_pos[0] += ball_speed[0]
	ball_pos[1] += ball_speed[1]

#x collision
	if ball_pos[0] + ball_radius > width - paddle_width and \
	  paddle_2_pos_y <= ball_pos[1] <= paddle_2_pos_y + paddle_height:
		ball_speed[0] = -ball_speed[0]

	elif ball_pos[0] + ball_radius > width - paddle_width:
		ball_pos = [width/2, height/2]
		ball_speed = [random.uniform(-2.0,2.0),random.uniform(-1.0,1.0)]

	if ball_pos[0] - ball_radius < paddle_width and \
	  paddle_1_pos_y <= ball_pos[1] <= paddle_1_pos_y + paddle_height:
		ball_speed[0] = -ball_speed[0]
		
	elif ball_pos[0] - ball_radius < paddle_width:
		ball_pos = [width/2, height/2]
		ball_speed = [random.uniform(-2.0,2.0),random.uniform(-1.0,1.0)]


#y collision
	if ball_pos[1] + ball_radius > height or ball_pos [1] - ball_radius < 0:
		ball_speed[1] = -ball_speed[1]

#paddle limit
	if paddle_1_pos_y < 0:
		paddle_1_pos_y = 0
	elif paddle_1_pos_y + paddle_height > height:
		paddle_1_pos_y = height - paddle_height

	if paddle_2_pos_y < 0:
		paddle_2_pos_y = 0
	elif paddle_2_pos_y + paddle_height > height:
		paddle_2_pos_y = height - paddle_height	



	pygame.display.flip()









