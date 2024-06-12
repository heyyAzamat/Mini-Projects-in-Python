import tkinter as tk
from math import sqrt, pow, sin, cos, tan, radians, pi

def perform_operation():
    operation = operation_var.get()
    x = entry_x.get().replace('π', f'*{pi}')
    y = entry_y.get().replace('π', f'*{pi}')
    
    try:
        if operation in ('+', '-', '*', '/', '^'):
            x = eval(x) if x else 0
            y = eval(y) if y else 0
            if operation == '+':
                result = x + y
            elif operation == '-':
                result = x - y
            elif operation == '*':
                result = x * y
            elif operation == '/':
                if y != 0:
                    result = x / y
                else:
                    result = "Ошибка: Деление на ноль!"
            elif operation == '^':
                result = pow(x, y)
        elif operation == 'sqrt':
            x = eval(x)
            result = sqrt(x)
        elif operation == 'sin':
            x = eval(x)
            result = sin(radians(x))
        elif operation == 'cos':
            x = eval(x)
            result = cos(radians(x))
        elif operation == 'tan':
            x = eval(x)
            result = tan(radians(x))
        elif operation == 'cot':
            x = eval(x)
            result = 1/tan(radians(x))
        elif operation == '%':
            x = eval(x)
            y = eval(y) if y else 0
            result = x * y / 100
        label_result.config(text="Результат: " + str(result))
    except Exception as e:
        label_result.config(text=f"Ошибка: {e}")

root = tk.Tk()
root.title("Инженерный калькулятор")

operation_var = tk.StringVar()

label_x = tk.Label(root, text="Введите первое число (можно использовать π):")
label_x.pack()

entry_x = tk.Entry(root)
entry_x.pack()

label_y = tk.Label(root, text="Введите второе число (если необходимо, можно использовать π):")
label_y.pack()

entry_y = tk.Entry(root)
entry_y.pack()

label_operation = tk.Label(root, text="Выберите операцию:")
label_operation.pack()

operations = ['+', '-', '*', '/', '√', '^', 'sin', 'cos', 'tan', 'cot', '%']
for op in operations:
    radio = tk.Radiobutton(root, text=op, variable=operation_var, value=op if op != '√' else 'sqrt')
    radio.pack()

button_calc = tk.Button(root, text="Вычислить", command=perform_operation)
button_calc.pack()

label_result = tk.Label(root, text="Результат: ")
label_result.pack()

root.mainloop()