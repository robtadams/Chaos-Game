import random
import pygame

def chaosGame():
    pygame.display.init()
    
    windowWidth = 800
    windowHeight = 600
    window = pygame.display.set_mode((windowWidth, windowHeight))
    
    pygame.display.set_caption("Chaos Game")
    windowColor = [255, 255, 255]
    window.fill(windowColor)
    
    pygame.display.update()

    p1 = [random.randint(0,windowWidth), random.randint(0, windowHeight)]
    p2 = [random.randint(0,windowWidth), random.randint(0, windowHeight)]
    p3 = [random.randint(0,windowWidth), random.randint(0, windowHeight)]

    pygame.draw.circle(window, [255,0,0], p1, 5)
    pygame.draw.circle(window, [0,255,0], p2, 5)
    pygame.draw.circle(window, [0,0,255], p3, 5)

    pCurrent = [(p1[0] + p2[0] + p3[0]) // 3, (p1[1] + p2[1] + p3[1]) // 3]

    pygame.draw.circle(window, [0,0,0], pCurrent, 5)

    pygame.display.update()
    
    running = True

    while running:
        for i in range(0,5000):
            randomPoint = random.randint(1,3)
            
            match randomPoint:
                case 1:
                    pointColor = [255,0,0]
                    selectedPoint = p1

                case 2:
                    pointColor = [0,255,0]
                    selectedPoint = p2

                case 3:
                    pointColor = [0,0,255]
                    selectedPoint = p3

            tempPoint = [(pCurrent[0] + selectedPoint[0]) // 2, (pCurrent[1] + selectedPoint[1]) // 2]

            pygame.draw.circle(window, pointColor, tempPoint, 5)

            pCurrent = tempPoint

            pygame.display.update()
            
        window.fill(windowColor)

        p1 = [random.randint(0,windowWidth), random.randint(0, windowHeight)]
        p2 = [random.randint(0,windowWidth), random.randint(0, windowHeight)]
        p3 = [random.randint(0,windowWidth), random.randint(0, windowHeight)]
        pCurrent = [(p1[0] + p2[0] + p3[0]) // 3, (p1[1] + p2[1] + p3[1]) // 3]


                

def main():
    print("Hello, world!")
    print(random.randint(1,5))
    chaosGame()

main()
