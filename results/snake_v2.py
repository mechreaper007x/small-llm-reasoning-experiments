import curses

def draw_snake(snake, walls):
    stdscr.addch(0, 0, curses.color_pair(1))
    for i in range(len(snake) - 1):
        stdscr.addch(i * 2 + 1, 0, curses.ACS_LEFT)
        stdscr.addch(i * 2 + 1, 1, "Snake: ")
        stdscr.addch(i * 2 + 2, 0, curses.ACS_RIGHT)
    for i in range(len(snake)):
        if snake[i] != (curses.YP, curses.COLS // 2):
            stdscr.addch(i * 2 + 1, 0, "Snake: ")
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    walls = [
        (curses.YP, curses.COLS // 2),
        (curses.YP, curses.COLS // 4),
        (curses.YP, curses.COLS // 8),
        (curses.YP, curses.COLS // 16),
        (curses.YP, curses.COLS // 32),
    ]
    
    snake = [(0, curses.YP)]
    direction = "UP"
    food = None
    score = 0

    while True:
        stdscr.clear()
        draw_snake(snake, walls)
        stdscr.refresh()

        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == curses.KEY_DOWN and direction != "UP":
            direction = "DOWN"
        elif key == curses.KEY_UP and direction != "LEFT":
            direction = "UP"
        elif key == curses.KEY_LEFT and direction != "RIGHT":
            direction = "LEFT"
        elif key == curses.KEY_RIGHT and direction != "DOWN":
            direction = "RIGHT"

        if food is not None:
            snake[0] = (food)
            score += 1
            food = None

        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i - 1][0], snake[i - 1][1])

        if direction == "DOWN":
            snake[0] = (snake[0][0], curses.COLS // 2)
        elif direction == "UP":
            snake[0] = (snake[0][0], curses.YP)
        elif direction == "LEFT":
            snake[0] = (curses.YP, curses.COLS // 2)
        elif direction == "RIGHT":
            snake[0] = (curses.YP, curses.COLS // 2)

    draw_snake(snake, walls)
    stdscr.addch(0, 0, "Game Over")

if __name__ == "__main__":
    curses.wrapper(main)