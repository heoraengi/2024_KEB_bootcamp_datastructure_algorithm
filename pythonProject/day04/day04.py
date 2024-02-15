import tkinter as tk

def fibo_momoization(number) -> int :
    '''
    fibonacci function by recursion with monoization
    :param number: integer number
    :return: integer number
    '''
    global memo
    if memo[number] is not None :
        return memo[number]
    if number < 2 :
        result = number
    else :
        result = fibo_momoization(number-1) + fibo_momoization(number-2)
        memo[number] = result
    return result

# memo = [0 if i==0 else 1 if i==1 else None for i in range(100)]
memo = [0,1] + [None] * (100-1)

def process_fibonacci():
    number = int(en_input_number.get())
    lbl_display_fibonacci_result.config(text=f'{number}! = {fibo_momoization(number)}')

if __name__ == "__main__" :
    w = tk.Tk() # create window object
    w.title("Fibonacci")
    w.geometry("250x100")

    # create widget
    lbl_display_fibonacci_result = tk.Label(w, text='Fibonacci by memoization')
    en_input_number = tk.Entry(w)
    btn_click = tk.Button(w, text='Click', command=process_fibonacci)

    # layout
    lbl_display_fibonacci_result.pack()
    en_input_number.pack(fill='x')
    btn_click.pack(fill='x')

    en_input_number.focus()
    w.mainloop()

# n = int(input('Input number : ')) # input box
# print(f'fibonacci({n}) : {fibo_momoization(n)}') # label
