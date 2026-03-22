import curses

def main(stdscr):
    curses.curs_set(0)  # Hide cursor

    # Initialize screen dimensions
    stdscr.nodelay(True)
    stdscr.timeout(100)

    # Snake initial position
    snake = [(curses.YP, curses.COLS // 2)]

    while True:
        key = stdscr.getch()  # Get user input
        if key == ord('q'):  # Quit game
            break

        # Handle key presses and update snake body
        if key == curses.KEY_DOWN:  # Move down
            snake[0] = (snake[0][0], curses.YP)
        elif key == curses.KEY_UP:  # Move up
            snake[0] = (snake[0][0], curses.COLS // 2)
        elif key == curses.KEY_LEFT:  # Move left
            snake[0] = (curses.YP, curses.COLS // 2)
        elif key == curses.KEY_RIGHT:  # Move right
            snake[0] = (snake[0][0], curses.COLS // 2)

        # Draw the snake on screen
        for i in range(len(snake) - 1):
            stdscr.addch(snake[i][0], curses.YP, curses.ACS.WALL)
            stdscr.addch(snake[i + 1][0], curses.YP, curses.ACS.WALL)

        # Draw food on screen
        for i in range(len(snake) - 1):
            if (snake[0] == (curses.COLS // 2, curses.COLS // 2)) or \
               ((snake[0][0] + curses.YP) % curses.COLS == curses.COLS // 2) or \
               ((snake[0][0] - curses.YP) % curses.COLS == curses.COLS // 2):
                stdscr.addch(snake[0][0], curses.ACS.WALL, curses.ACS.SNAKE)

        # Draw snake body
        for i in range(len(snake)):
            if (snake[i][0] + curses.YP) % curses.COLS == curses.COLS // 2:
                stdscr.addch(curses.COLS // 2, curses.ACS.WALL, curses.ACS.SNAKE)
            else:
                stdscr.addch(snake[i][0], curses.ACS.WALL)

        # Refresh screen
        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)