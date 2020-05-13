from window_interface import *

def main():
    width = 525
    rows = 20

    pygame.font.init()
    _font_name = pygame.font.match_font('Times New Roman')
    _font_module = pygame.font.Font(_font_name, 24)

    win = pygame.display.set_mode((width, width))

    s = snake((255, 0, 0), (10, 10))
    snack = cube(randomSnack(rows, s), color = (0, 255, 0))
    flag = True

    clock = pygame.time.Clock()
    
    while flag:
        pygame.time.delay(40)
        clock.tick(8)
        s.move()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color=(0, 255, 0))

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x + 1:])):
                print('Score: ', len(s.body))
                message_box('You Lose!', 'Play again...')
                s.reset((10, 10))
                break

            
        redrawWindow(win, s, snack, _font_module)

if __name__ == '__main__':
    main()