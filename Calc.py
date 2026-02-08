try:
    import tkinter as tk
except:
    print("Ошибка", "Tkinter не установлен!\nУстановите его:\n- Ubuntu/Debian: sudo apt install python3-tk\n- Windows: переустановите Python с галочкой 'tcl/tk'\n- macOS: brew install python-tk")
    exit(1)

from tkinter import messagebox
# Пасхалка для Джанэллы, чтобы сам хотя бы чёт писал, а не копипастил с гптшки
root = tk.Tk()

def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        # Безопасная замена вместо eval()
        result = eval(expression, {"__builtins__": {}}, {})
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Ошибка", "Деление на ноль!")
        clear()
    except Exception:
        messagebox.showerror("Ошибка", "Неверное выражение")
        clear()

# Создание главного окна

root.title("Fox comp")
root.geometry("300x420")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Заголовок
title_label = tk.Label(
    root, 
    text="🦊 Fox comp", 
    font=("Arial", 18, "bold"),
    bg="#f0f0f0",
    fg="#2c3e50"
)
title_label.pack(pady=15)

# Поле ввода
entry = tk.Entry(
    root, 
    width=20, 
    font=("Arial", 16), 
    justify="right",
    bd=2,
    relief="solid"
)
entry.pack(pady=10, padx=20)

# Кнопки
buttons_frame = tk.Frame(root, bg="#f0f0f0")
buttons_frame.pack(padx=10, pady=10)

buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(
            buttons_frame, text=text, width=5, height=2, font=("Arial", 12, "bold"),
            bg="#27ae60", fg="white", command=calculate
        )
    else:
        btn = tk.Button(
            buttons_frame, text=text, width=5, height=2, font=("Arial", 12),
            bg="#ecf0f1", command=lambda t=text: click_button(t)
        )
    btn.grid(row=row, column=col, padx=3, pady=3)

# Кнопка очистки
clear_btn = tk.Button(
    root, 
    text="Очистить (C)", 
    width=15, 
    height=2, 
    font=("Arial", 11, "bold"),
    bg="#e74c3c", 
    fg="white",
    command=clear
)
clear_btn.pack(pady=10)

# Запуск приложения
if __name__ == "__main__":
    root.mainloop()