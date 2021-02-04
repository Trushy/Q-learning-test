import pygame
import maze as mazeMaker

def main():
    try:
        maze = init()
    except Exception as err:
        print("ERROR :", err.args)
        return
    loop(maze)

def init():
    pygame.init()
    pygame.display.set_mode((800, 800))
    maze = mazeMaker.createMaze()
    return maze

def loop(maze):
    launched = True

    print(maze)
    while launched:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                launched = False

if __name__ == "__main__":
    main()