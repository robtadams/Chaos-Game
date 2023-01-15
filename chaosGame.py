import random
import pygame

def chaosGame():

    # Initialize Pygame
    pygame.display.init()

    # Initialize the Clock
    clock = pygame.time.Clock()

    # Set the dimensions of the window
    windowWidth = 800
    windowHeight = 600
    window = pygame.display.set_mode((windowWidth, windowHeight))

    # Set the window captain and window color
    pygame.display.set_caption("Chaos Game")
    windowColor = [0, 0, 0]
    window.fill(windowColor)

    # Update the window
    pygame.display.update()
    
    # Initialize the three coordinate points of the triangle
    p1 = [random.randint(0,windowWidth), random.randint(0, windowHeight)]
    p2 = [random.randint(0,windowWidth), random.randint(0, windowHeight)]
    p3 = [random.randint(0,windowWidth), random.randint(0, windowHeight)]

    # Draw the points of the triangle
    pygame.draw.circle(window, [255,0,0], p1, 5)
    pygame.draw.circle(window, [0,255,0], p2, 5)
    pygame.draw.circle(window, [0,0,255], p3, 5)

    # Set the center point coordinate of the triangle
    pCurrent = [(p1[0] + p2[0] + p3[0]) // 3, (p1[1] + p2[1] + p3[1]) // 3]

    # Draw the center point of the triangle
    pygame.draw.circle(window, [0,0,0], pCurrent, 5)
    
    # Update the window
    pygame.display.update()
    
    running = True

    # While running...
    while running:

        # ... run for 5000 iterations ...
        for i in range(0,2500):

            # ... Get an event ...
            for event in pygame.event.get():

                # ... if the event is a key press ...
                if event.type == pygame.KEYDOWN:

                    # ... and that key press is escape ...
                    if event.key == pygame.K_ESCAPE:

                        # ... quit the game
                        pygame.quit()

                    # ... and that key press is space ...
                    if event.key == pygame.K_SPACE:

                        # ... pause the game
                        paused = True

                        # While paused ...
                        while paused:

                            # ... get an event ...
                            for event in pygame.event.get():

                                # ... if the event is a key press ...
                                if event.type == pygame.KEYDOWN:

                                    # ... and that key press is space ...
                                    if event.key == pygame.K_SPACE:

                                        # ... unpause the game
                                        paused = False

                                    # ... and that key press is escape ...
                                    if event.key == pygame.K_ESCAPE:

                                        # ... quit the game
                                        paused = False
                                        pygame.quit()

            # ... pick a random point        
            randomPoint = random.randint(1,3)

            match randomPoint:

                # If you picked the first point...
                case 1:

                    # Set the selected point to p1 and set the color to Red
                    pointColor = [255,0,0]
                    selectedPoint = p1

                # If you picked the second point...
                case 2:

                    # Set the selected point to p2 and set the color to Green
                    pointColor = [0,255,0]
                    selectedPoint = p2

                # If you picked the third point ...
                case 3:

                    # Set the selected point to p3 and set the color to Blue
                    pointColor = [0,0,255]
                    selectedPoint = p3

            # Find the median between your current point's position and the position of the point you picked
            tempPoint = [(pCurrent[0] + selectedPoint[0]) // 2, (pCurrent[1] + selectedPoint[1]) // 2]

            # Draw that point with the color you picked
            pygame.draw.circle(window, pointColor, tempPoint, 5)

            # Set your current point to the new point
            pCurrent = tempPoint

            # Update the window
            pygame.display.update()
            print(clock.tick())

        # Generate new coordinate points for the triangle
        p1 = [random.randint(0,windowWidth), random.randint(0, windowHeight)]
        p2 = [random.randint(0,windowWidth), random.randint(0, windowHeight)]
        p3 = [random.randint(0,windowWidth), random.randint(0, windowHeight)]
        pCurrent = [(p1[0] + p2[0] + p3[0]) // 3, (p1[1] + p2[1] + p3[1]) // 3]

if __name__ == "__main__":
    chaosGame()
