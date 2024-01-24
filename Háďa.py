import tkinter as tk
win = tk.Tk()
canvas = tk.Canvas(win, width=400, height=400)
canvas.pack()
direction = 'Up'
snake = [(10, 10)]
trail = []
speed = 100

def move_snake():
    global snake, trail
    head_x, head_y = snake[0]
    if direction == 'Up': snake = [(head_x, head_y - 1)] + snake[:-1]
    elif direction == 'Down': snake = [(head_x, head_y + 1)] + snake[:-1]
    elif direction == 'Left': snake = [(head_x - 1, head_y)] + snake[:-1]
    elif direction == 'Right': snake = [(head_x + 1, head_y)] + snake[:-1]
    if snake[0] in snake[1:] or snake[0] in trail:
        print("Game over")
        return
    trail.append(snake[-1])
    canvas.delete('all')
    for x, y in snake: canvas.create_rectangle(x*20, y*20, x*20 + 20, y*20 + 20, fill='black')
    for x, y in trail: canvas.create_rectangle(x*20, y*20, x*20 + 20, y*20 + 20, fill='black')
    win.after(speed, move_snake)
def change_direction(new_direction):
    global direction
    direction = new_direction

win.bind('<Up>', lambda _: change_direction('Up'))
win.bind('<Down>', lambda _: change_direction('Down'))
win.bind('<Left>', lambda _: change_direction('Left'))
win.bind('<Right>', lambda _: change_direction('Right'))

move_snake()
win.mainloop()