import curses

def draw_snake(snake):
    for x, y in snake:
        stdscr.addch(y, x)

def eat_food(snake):
    return (curses.YP, curses.COLS // 2)

def main(stdscr):
    curses.curs_set(0)
    
    # Initialize the screen
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    stdscr.addstr("Snake Game\n")
    stdscr.clear()

    snake = [(curses.YP, curses.COLS // 2)]
    while True:
        key = stdscr.getch()
        
        if key == ord('q'):
            break
        
        # Move the snake
        if key == curses.KEY_DOWN:
            snake[0] = (snake[0][0], curses.YP)
        elif key == curses.KEY_UP:
            snake[0] = (snake[0][0], curses.COLS // 2)
        elif key == curses.KEY_LEFT:
            snake[0] = (curses.COLS // 2, curses.YP)
        elif key == curses.KEY_RIGHT:
            snake[0] = (curses.COLS // 2, curses.COLS // 2)

        # Check for collision with walls or itself
        if curses.isatty(stdscr) and curses.ASCIITEXT:
            stdscr.clear()
            draw_snake(snake)
            return

        # Draw the snake body
        draw_snake(snake)

        # Eat food (if possible)
        if eat_food(snake):
            snake[0] = eat_food(snake)

    # Clean up after drawing
    curses.napms(100)  # Adjust the delay as needed

if __name__ == "__main__":
    curses.wrapper(main)