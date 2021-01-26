from tkinter import *
from tkinter import messagebox


class Calculator:
    def __init__(self):
        calc_layout = Tk()
        calc_layout.configure(background='#D9D9D9')
        calc_layout.title("Calculator")
        calc_layout.resizable(False, False)
        btn = {}
        input_values = Entry(calc_layout, width=14, font="Arial 20", state="disabled")
        input_values.grid(row=0, columnspan=3, pady=10, padx=10)

        for i in range(0, 10):
            btn[f'{i}'] = Button(calc_layout, text=f"{i}", width=10, height=4, bd=1)

        btn['+'] = Button(calc_layout, text="+", width=10, height=4, bd=1)
        btn['+']['command'] = lambda: sum_values()
        btn['+'].grid(row=1, column=3, pady=3, padx=3)

        btn['-'] = Button(calc_layout, text="-", width=10, height=4, bd=1)
        btn['-']['command'] = lambda: sub_values()
        btn['-'].grid(row=2, column=3, pady=3, padx=3)

        btn['*'] = Button(calc_layout, text="*", width=10, height=4, bd=1)
        btn['*']['command'] = lambda: mult_values()
        btn['*'].grid(row=3, column=3, pady=3, padx=3)

        btn['/'] = Button(calc_layout, text="/", width=10, height=4, bd=1)
        btn['/']['command'] = lambda: div_values()
        btn['/'].grid(row=4, column=3, pady=3, padx=3)

        btn['.'] = Button(calc_layout, text=".", width=10, height=4, bd=1)
        btn['.']['command'] = lambda: make_float()
        btn['.'].grid(row=4, column=1, pady=3, padx=3)

        btn['='] = Button(calc_layout, text="=", width=10, height=4, bd=1)
        btn['='].grid(row=4, column=2, pady=3, padx=3)

        btn['C'] = Button(calc_layout, text="C", width=10, height=4, bd=1)
        btn['C']['command'] = lambda: clear_input()
        btn['C'].grid(row=0, column=3, pady=3, padx=3)

        btn['0']['command'] = lambda: display_value(0)
        btn['1']['command'] = lambda: display_value(1)
        btn['2']['command'] = lambda: display_value(2)
        btn['3']['command'] = lambda: display_value(3)
        btn['4']['command'] = lambda: display_value(4)
        btn['5']['command'] = lambda: display_value(5)
        btn['6']['command'] = lambda: display_value(6)
        btn['7']['command'] = lambda: display_value(7)
        btn['8']['command'] = lambda: display_value(8)
        btn['9']['command'] = lambda: display_value(9)

        i = 1
        for row in range(1, 4):
            for column in range(0, 3):
                btn[f'{i}'].grid(row=row, column=column, pady=3, padx=3)
                i += 1
                if i == 10:
                    btn['0'].grid(row=4, column=0, pady=3, padx=3)

        def display_value(btn_index):
            if len(input_values.get()) > 13:
                messagebox.showwarning(title='Warning', message="Too many arguments")
            else:
                input_values['state'] = "normal"
                input_values.insert(len(input_values.get()), btn_index)
                input_values['state'] = "disabled"

        def sum_values():
            num = float(input_values.get())
            input_values['state'] = 'normal'
            input_values.delete(0, END)
            input_values['state'] = 'disabled'
            btn['=']['command'] = lambda: equals_sum()

            def equals_sum():
                res = num + float(input_values.get())
                input_values['state'] = 'normal'
                input_values.delete(0, END)
                input_values.insert(0, res)
                input_values['state'] = 'disabled'

        def sub_values():
            num = float(input_values.get())
            input_values['state'] = 'normal'
            input_values.delete(0, END)
            input_values['state'] = 'disabled'
            btn['=']['command'] = lambda: equals_sub()

            def equals_sub():
                res = num - float(input_values.get())
                input_values['state'] = 'normal'
                input_values.delete(0, END)
                input_values.insert(0, res)
                input_values['state'] = 'disabled'

        def mult_values():
            num = float(input_values.get())
            input_values['state'] = 'normal'
            input_values.delete(0, END)
            input_values['state'] = 'disabled'
            btn['=']['command'] = lambda: equals_mult()

            def equals_mult():
                res = num * float(input_values.get())
                input_values['state'] = 'normal'
                input_values.delete(0, END)
                input_values.insert(0, res)
                input_values['state'] = 'disabled'

        def div_values():
            num = float(input_values.get())
            input_values['state'] = 'normal'
            input_values.delete(0, END)
            input_values['state'] = 'disabled'
            btn['=']['command'] = lambda: equals_div()

            def equals_div():
                res = num / float(input_values.get())
                input_values['state'] = 'normal'
                input_values.delete(0, END)
                input_values.insert(0, res)
                input_values['state'] = 'disabled'

        def make_float():
            if len(input_values.get()) > 13:
                messagebox.showwarning(title='Warning', message="Too many arguments")
            else:
                input_values['state'] = "normal"
                input_values.insert(len(input_values.get()), '.')
                input_values['state'] = "disabled"

        def clear_input():
            input_values['state'] = 'normal'
            input_values.delete(0, END)
            input_values['state'] = 'disabled'

        calc_layout.mainloop()


calc = Calculator()
