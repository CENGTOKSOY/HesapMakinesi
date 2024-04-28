import tkinter as tk

# İfadeyi güncellemek için bir fonksiyon oluştur
def press(num):
    current = expression.get()
    expression.set(current + str(num))

# Sonucu hesaplamak için bir fonksiyon oluştur
def equalpress():
    try:
        total = str(eval(expression.get()))
        expression.set(total)
    except:
        expression.set("Hata")
        entry.update()

# Alanı temizlemek için bir fonksiyon oluştur
def clear():
    expression.set("")

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Hesap Makinesi")

# StringVar() değişken sınıfını kullan
expression = tk.StringVar()

# İfadeyi göstermek için bir giriş alanı oluştur
entry = tk.Entry(root, textvariable=expression)
entry.grid(columnspan=4, ipadx=70)

# Hesap makinesi için düğmeleri oluştur
button1 = tk.Button(root, text=' 1 ', command=lambda: press(1), height=1, width=7)
button1.grid(row=2, column=0)

button2 = tk.Button(root, text=' 2 ', command=lambda: press(2), height=1, width=7)
button2.grid(row=2, column=1)

button3 = tk.Button(root, text=' 3 ', command=lambda: press(3), height=1, width=7)
button3.grid(row=2, column=2)

button4 = tk.Button(root, text=' 4 ', command=lambda: press(4), height=1, width=7)
button4.grid(row=3, column=0)

button5 = tk.Button(root, text=' 5 ', command=lambda: press(5), height=1, width=7)
button5.grid(row=3, column=1)

button6 = tk.Button(root, text=' 6 ', command=lambda: press(6), height=1, width=7)
button6.grid(row=3, column=2)

button7 = tk.Button(root, text=' 7 ', command=lambda: press(7), height=1, width=7)
button7.grid(row=4, column=0)

button8 = tk.Button(root, text=' 8 ', command=lambda: press(8), height=1, width=7)
button8.grid(row=4, column=1)

button9 = tk.Button(root, text=' 9 ', command=lambda: press(9), height=1, width=7)
button9.grid(row=4, column=2)

button0 = tk.Button(root, text=' 0 ', command=lambda: press(0), height=1, width=7)
button0.grid(row=5, columnspan=1)

plus = tk.Button(root, text=' + ', command=lambda: press("+"), height=1, width=7)
plus.grid(row=2, column=3)

minus = tk.Button(root, text=' - ', command=lambda: press("-"), height=1, width=7)
minus.grid(row=3, column=3)

multiply = tk.Button(root, text=' * ', command=lambda: press("*"), height=1, width=7)
multiply.grid(row=4, column=3)

divide = tk.Button(root, text=' / ', command=lambda: press("/"), height=1, width=7)
divide.grid(row=5, column=3)

equal = tk.Button(root, text=' = ', command=equalpress, height=1, width=7)
equal.grid(row=5, column=2)

clear = tk.Button(root, text='Temizle', command=clear, height=1, width=7)
clear.grid(row=1, column=0)

Decimal = tk.Button(root, text='.', command=lambda: press('.'), height=1, width=7)
Decimal.grid(row=5, column=1)

# GUI'yi başlat
root.mainloop()
