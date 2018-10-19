from world import World
from pygame.locals import *
import pygame
from sys import exit
import math
import time
from argparse import ArgumentParser
import os, sys

SCREEN_LENGTH = 800
SCREEN_WIDTH = 1000

def main(args):
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_LENGTH), 0, 32)
    world = World(SCREEN_LENGTH,SCREEN_WIDTH,asymmetry=args.asymmetry)
    world.set_ball_list(args.blue, args.red)
    clock = pygame.time.Clock()
    # Game loop:
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        time_passed_seconds = clock.tick()/ 1000.0
        world.update(time_passed_seconds)
        world.render(screen)
        pygame.display.update()

if __name__ == "__main__":

    parser = ArgumentParser(
        usage='%(prog)s [options]',
        description=__doc__, 
        prog=os.path.basename(sys.argv[0])
        )
    parser.add_argument('--red', type=int, default=10,
                        help='number of red balls')
    parser.add_argument('--blue', type=int, default=10,
                        help='number of blue balls')
    parser.add_argument('--asymmetry', type=float, default=0,
                        help='asymmetric interaction fraction between 0 and 1')
    
    args = parser.parse_args()
    main(args)
                    
