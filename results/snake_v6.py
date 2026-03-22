import curses

def draw_snake(snake):
    for y, x in snake:
        stdscr.addch(y, x, 'O')

def grow_snake(snake):
    while food in snake:
        continue
    
    new_head = (snake[-1][0] + dx, snake[-1][1] + dy)
    
    if not 0 <= new_head[0] < len(snake) and not 0 <= new_head[1] < len(snake[0]):
        stdscr.clear()
        draw_snake(snake)
        return
    
    snake.append(new_head)

def eat_food(food):
    global dx, dy
    dx, dy = random.randint(0, width - 2), random.randint(0, height - 2)
    new_head = (snake[-1][0] + dx, snake[-1][1] + dy)
    
    if not 0 <= new_head[0] < len(snake) and not 0 <= new_head[1] < len(snake[0]):
        stdscr.clear()
        draw_snake(snake)
        return
    
    snake.append(new_head)

def move_snake(snake):
    global dx, dy
    if not (snake[-1][0] + dx, snake[-1][1] + dy) == food:
        new_head = (snake[-1][0] + dx, snake[-1][1] + dy)
        
        if not 0 <= new_head[0] < len(snake) and not 0 <= new_head[1] < len(snake[0]):
            stdscr.clear()
            draw_snake(snake)
            return
    
    snake.pop()

def main():
    curses.curs_set(0)
    
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.napms(100)  # Sleep for 100 milliseconds to avoid flickering
    stdscr.timeout(100)
    
    snake = [(height // 2 - 1, width // 2)]
    food = (random.randint(0, width - 2), random.randint(0, height - 2))
    
    while True:
        move_snake(snake)
        
        if stdscr.getch() == ord('q'):
            break
        
        eat_food(food)
        
        grow_snake(snake)
        
        draw_snake(snake)

if __name__ == "__main__":
    main()