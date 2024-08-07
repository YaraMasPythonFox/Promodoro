import tkinter as tk


def draw_shapes(canvas):
    # Малювання прямокутника
    canvas.create_rectangle(50, 50, 200, 150, fill='blue', outline='black')

    # Малювання кола (овальної форми)
    canvas.create_oval(250, 50, 350, 150, fill='red', outline='black')

    # Малювання лінії
    canvas.create_line(50, 200, 350, 200, fill='green', width=3)

    # Додавання тексту
    canvas.create_text(200, 250, text='Hello, Tkinter Canvas!', font=('Arial', 20), fill='purple')


# Створення головного вікна
root = tk.Tk()
root.title('Tkinter Canvas Example')

# Створення Canvas
canvas = tk.Canvas(root, width=400, height=300, bg='white')
canvas.pack()

# Виклик функції для малювання фігур
draw_shapes(canvas)

# Запуск головного циклу
root.mainloop()