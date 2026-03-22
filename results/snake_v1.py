import curses

def draw_snake(snake_body):
    for position in snake_body:
        print(f"{' ' * 5}|", end="")
        for coord in position:
            print(f"|{coord} ", end="")
        print("|")

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    
    # Snake body initialization
    snake = [(curses.COLS // 2, curses.YP)]
    while True:
        key = stdscr.getch()
        
        if key == ord('q'):
            break
        
        for event in curses.EventCurses.keyboard():
            if event.type() == curses.KEY_DOWN and not (event.state() & curses.KEY_LEFT):
                snake[0] = (snake[0][0], curses.YP)
                
            elif event.type() == curses.KEY_UP and not (event.state() & curses.KEY_RIGHT):
                snake[0] = (snake[0][0], curses.COLS // 2)
                
            elif event.type() == curses.KEY_LEFT and not (event.state() & curses.KEY_DOWN):
                snake[0] = (curses.YP, curses.COLS // 2)
                
            elif event.type() == curses.KEY_RIGHT and not (event.state() & curses.KEY_UP):
                snake[0] = (curses.COLS // 2, curses.YP)
        
        draw_snake(snake)

if __name__ == "__main__":
    curses.wrapper(main)