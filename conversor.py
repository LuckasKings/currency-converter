import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
from currency_converter import CurrencyConverter
from currency_symbols import CurrencySymbols


# Setting up color codes
purple = '#856ff8'
white = '#f5f2f5'

# Initializing the main application window
app = tk.Tk()
app.geometry("600x300")
app.title('Conversor de Moedas - Match')
app['background'] = purple

# Initializing currency converter and symbols
c_symbol = CurrencySymbols
c_converter = CurrencyConverter()

# Result label placement and initialization
result = tk.Label(app, text="", font="Lato 25 bold", bg=purple, fg=white)
result.place(x=200, y=290)

# Function for currency conversion
def converter():
    try:
        amount = float(amount_entry.get())
        if amount <= 0:
            messagebox.showerror("Erro", "Por favor, insira um número maior que zero.")
        else:
            currency_origin = combobox_currency_origin.get()
            currency_destiny = combobox_currency_destiny.get()
            data = round(c_converter.convert(amount, currency_origin, currency_destiny), 2)
            result.config(text=c_symbol.get_symbol(currency_destiny) + ' ' + str(data))
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número maior que zero.")
        
# Function to clear all input data
def clean_data():
    amount_entry.delete(0, 'end')
    combobox_currency_origin.set('')
    combobox_currency_destiny.set('')
    result.config(text='')

# Labels for the application
app_title = tk.Label(app, text="Conversor de Moedas", font="Lato 20 bold", bg=purple, fg=white)
app_title.place(x=170, y=30)
amount_label = tk.Label(app, text="Insira o valor aqui: ", font="Lato 18 bold", bg=purple, fg=white)
amount_label.place(x=40, y=80)

# Currency code list and sorting
CurrencyCode_list = ['USD', 'JPY', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'PLN', 'RON', 'SEK', 'CHF', 'ISK',
                     'NOK', 'TRY', 'AUD', 'BRL', 'CAD', 'CNY', 'HKD', 'IDR', 'ILS', 'INR', 'KRW', 'MXN', 'MYR',
                     'NZD', 'PHP', 'SGD', 'THB', 'ZAR']
CurrencyCode_list.sort()

# Comboboxes and entry placement
combobox_currency_origin = ttk.Combobox(app, values=CurrencyCode_list)
combobox_currency_destiny = ttk.Combobox(app, values=CurrencyCode_list)
combobox_currency_origin.place(x=350, y=140)
combobox_currency_destiny.place(x=445, y=190)

amount_entry = tk.Entry(app)
amount_entry.place(x=260, y=90)

# Labels for currency selection
currency_origin_label = tk.Label(app, text="Insira o código da moeda: ", font="Lato 18 bold", bg=purple, fg=white)
currency_origin_label.place(x=40, y=130)
currency_destiny_label = tk.Label(app, text="Insira o código da moeda destino: ", font="Lato 18 bold", bg=purple, fg=white)
currency_destiny_label.place(x=40, y=180)

# Buttons for conversion and data clearing
converter_button = tk.Button(app, text="Converter", command=converter)
converter_button.place(x=200, y=240)
button_clean_all = tk.Button(app, text="Limpar Tudo", command=clean_data)
button_clean_all.place(x=300, y=240)

# Running the application
app.mainloop()
