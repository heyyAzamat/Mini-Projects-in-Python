from tkinter import colorchooser

def mix_colors():
    color1 = colorchooser.askcolor()[0]
    color2 = colorchooser.askcolor()[0]
    mixed_color = '#%02x%02x%02x' % (
        (color1[0] + color2[0]) // 2,
        (color1[1] + color2[1]) // 2,
        (color1[2] + color2[2]) // 2
    )
    canvas.config(bg=mixed_color)
    
root = tk.Tk()
root.title("Генератор смешанных цветов")
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()
mix_button = tk.Button(root, text="Смешать цвета", command=mix_colors)
mix_button.pack()

root.mainloop()