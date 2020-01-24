from planet import *
import pygame
import math

pygame.init()

canvasWidth = 1920
canvasHeight = 1080

sunMass = 1000

#used to reset the screen after each update
background = pygame.image.load("assets/spaceBackground.jpg")

canvas = pygame.display.set_mode((canvasWidth,canvasHeight))
pygame.display.set_caption('Space')

endlessLoop = 1

planetList = []

planetList.append(planet("sun", 1000, 0, 0, 0, 0, canvasWidth/2, canvasHeight/2, pygame.image.load("assets/sun.png")))
planetList.append(planet("earth", sunMass*0.000003, 0.2, 1.5, 0, 0, 585, canvasHeight/2-50, pygame.image.load("assets/earth.png")))
planetList.append(planet("mars", sunMass*0.0000322, 0.3, 1.0, 0, 0, 550, canvasHeight/2-75, pygame.image.load("assets/mars.png"))) #had to increase the mass by a factor of 10, mass was too small and got yeeted offscreen
planetList.append(planet("neptune", sunMass*0.000513, 0.2, 1.2, 0, 0, 640, canvasHeight/2-25, pygame.image.load("assets/neptune.png"))) #idk why but neptune yeets itself off the screen
planetList.append(planet("jupiter", sunMass*0.0001, 0.05, 0.45, 0, 0, 150, canvasHeight/2-400, pygame.image.load("assets/jupiter.png")))
planetList.append(planet("saturn", sunMass*0.000029, 0.1, 0.6, 0, 0, 300, canvasHeight/2-300, pygame.image.load("assets/saturn.png")))
planetList.append(planet("venus", sunMass*0.00000245, 0.5, 2.0, 0, 0, 744, canvasHeight/2+50, pygame.image.load("assets/venus.png")))
planetList.append(planet("uranus", sunMass*0.0000044, 0.2, 0.8, 0, 0, 450, canvasHeight/2-175, pygame.image.load("assets/uranus.png")))
planetList.append(planet("mercury", sunMass*0.00000166, 0.6, 2.0, 0, 0, 856, canvasHeight/2+110, pygame.image.load("assets/mercury.png")))

def calculateForce(planetA):
	forceX = 0
	forceY = 0

	#calculating the force on planetA induced by every planet (except for the force exerted on itself)
	for j in range(len(planetList)):
	
		#dont calculate the planets force on itself
		if(planetA != planetList[j]):

			#distance formula
			planetA.distance = math.sqrt((planetA.x - planetList[j].x)**2 + (planetA.y - planetList[j].y)**2)

			#newtons law of gravational attraction.  Multiply by 10 to scale it down a little
			planetA.force = (6.67*planetA.mass*planetList[j].mass)/(planetA.distance**2 * 10)

			#calculating angle between the planets
			planetA.theta = math.atan2(planetList[j].y - planetA.y, planetList[j].x - planetA.x)

			#remember AP Physics, x = r cos(theta)
			forceX += math.cos(planetA.theta) * planetA.force
			forceY += math.sin(planetA.theta) * planetA.force

	#a=f/m
	planetA.accelerationX = forceX/(planetA.mass)
	planetA.accelerationY = forceY/(planetA.mass)

	planetA.velocityX += planetA.accelerationX
	planetA.velocityY += planetA.accelerationY


while endlessLoop:
	#reset the background
	canvas.blit(background, (0,0))

	#draw updated images
	for i in range(len(planetList)):
		canvas.blit(planetList[i].image, (planetList[i].x, planetList[i].y))

	#update planet attributes
	for i in range(len(planetList)):
		calculateForce(planetList[i])
		
		planetList[i].x += planetList[i].velocityX
		planetList[i].y += planetList[i].velocityY

	#"Commit" the changes
	pygame.display.update()

