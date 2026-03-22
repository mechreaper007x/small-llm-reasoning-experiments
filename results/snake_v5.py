import curses

def draw_snake():
    stdscr.addch(0, 0, "SNAKE")
    for i in range(len(snake)):
        y = (i // width) * height + 1
        x = (i % width) * height + 1
        stdscr.addch(y, x, curses.ACS.WALL)

def eat_food():
    food_x = random.randint(0, width - 2)
    food_y = random.randint(0, height - 2)
    snake[0] = (food_x, food_y)

def grow_snake():
    if len(snake) > 1:
        head = snake[0]
        y, x = head
        while True:
            y += 1
            y %= height
            if (y, x) in snake:
                break
            else:
                snake.append((y, x))
                break

def move_snake():
    for i in range(len(snake) - 1):
        y, x = snake[i]
        y, x = (y + dx, x + dy)
        if not (0 <= y < height and 0 <= x < width):
            grow_snake()
            return
    head = snake[-1]
    y, x = head
    while True:
        y += 1
        y %= height
        if (y, x) in snake:
            break
        else:
            snake.append((y, x))
            break

def keypress(key):
    global dx, dy, snake, food
    if key == curses.KEY_DOWN and not (0 <= y < height - 1 and 0 <= x < width - 2):
        y += 1
        y %= height
        if (y, x) in snake:
            return
        else:
            dx = 1
            dy = 0
    elif key == curses.KEY_UP and not (0 <= y > 0 and 0 <= x < width - 2):
        y -= 1
        y %= height
        if (y, x) in snake:
            return
        else:
            dx = -1
            dy = 0
    elif key == curses.KEY_LEFT and not (0 <= x > 0 and 0 <= y < width - 2):
        x -= 1
        x %= width
        if (x, y) in snake:
            return
        else:
            dx = 0
            dy = -1
    elif key == curses.KEY_RIGHT and not (0 <= x > 0 and 0 <= y < width - 2):
        x += 1
        x %= width
        if (x, y) in snake:
            return
        else:
            dx = 0
            dy = 1

def main():
    height, width = stdscr.getmaxyx()
    curses.curs_set(0)
    
    # Initialize the snake and food positions
    snake = [(height // 2 - 1, width // 2)]
    food = (width // 2, height // 2)
    grow_snake()

    while True:
        key = stdscr.getch()
        if key == curses.KEY_DOWN and not (0 <= y < height - 1 and 0 <= x < width - 2):
            y += 1
            y %= height
            if (y, x) in snake:
                return
            else:
                dx = 1
                dy = 0
        elif key == curses.KEY_UP and not (0 <= y > 0 and 0 <= x < width - 2):
            y -= 1
            y %= height
            if (y, x) in snake:
                return
            else:
                dx = -1
                dy = 0
        elif key == curses.KEY_LEFT and not (0 <= x > 0 and 0 <= y < width - 2):
            x -= 1
            x %= width
            if (x, y) in snake:
                return
            else:
                dx = 0
                dy = -1
        elif key == curses.KEY_RIGHT and not (0 <= x > 0 and 0 <= y < width - 2):
            x += 1
            x %= width
            if (x, y) in snake:
                return
            else:
                dx = 0
                dy = 1

        move_snake()
        grow_snake()

if __name__ == "__main__":
    curses.wrapper(main)