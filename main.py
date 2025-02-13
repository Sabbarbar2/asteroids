
import pygame # type: ignore
from constants  import * 

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #fill(color, rect=None, special_flags=0) -> Rect
        screen.fill(color="black")
        #pygame.display.flip()
        pygame.display.flip()
        
    
    
if __name__ == "__main__":
    main()
    