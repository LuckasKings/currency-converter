import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
from currency_converter import CurrencyConverter
from currency_symbols import CurrencySymbols

# Starting the Dash application
app = dash.Dash(__name__)

# Defining colors
colors = {
    'background': '#856ff8',  # Background color for the app
    'text': '#000000'  # Text color for the app
}

# Initializing the currency converter and symbols
c_symbol = CurrencySymbols  # Initializing CurrencySymbols
c_converter = CurrencyConverter()  # Initializing CurrencyConverter

# Currency code list and sorting
CurrencyCode_list = ['USD', 'JPY', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'PLN', 'RON', 'SEK', 'CHF', 'ISK',
                     'NOK', 'TRY', 'AUD', 'BRL', 'CAD', 'CNY', 'HKD', 'IDR', 'ILS', 'INR', 'KRW', 'MXN', 'MYR',
                     'NZD', 'PHP', 'SGD', 'THB', 'ZAR']
CurrencyCode_list.sort()  # Sorting the currency codes

# Layout of the web app
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='Conversor de Moedas', style={'textAlign': 'center', 'color': colors['text'], 'font-family': 'Lato'}),
    # Title and styling

    html.Label('Insira o valor aqui:', style={'color': colors['text'], 'font-size': '20px', 'font-family': 'Lato'}),
    # Input label for the amount

    dcc.Input(id='amount-entry', type='text', value='', style={'color': colors['text'], 'font-size': '20px', 'font-family': 'Lato'}),
    # Input field for the amount

    html.Hr(),  # Horizontal line for separation

    html.Label('Insira o código da moeda:', style={'color': colors['text'], 'font-size': '20px', 'font-family': 'Lato'}),
    # Input label for the original currency

    dcc.Dropdown(
        id='currency-origin',
        options=[{'label': currency, 'value': currency} for currency in CurrencyCode_list],
        value='',
        style={'color': colors['text'], 'font-size': '20px', 'font-family': 'Lato'}
    ),
    # Dropdown for selecting the original currency

    html.Label('Insira o código da moeda destino:', style={'color': colors['text'], 'font-size': '20px', 'font-family': 'Lato'}),
    # Input label for the destination currency

    dcc.Dropdown(
        id='currency-destiny',
        options=[{'label': currency, 'value': currency} for currency in CurrencyCode_list],
        value='',
        style={'color': colors['text'], 'font-size': '20px', 'font-family': 'Lato'}
    ),
    # Dropdown for selecting the destination currency

    html.Button('Convert', id='converter-button', n_clicks=0, style={'color': colors['text']}),
    # Convert button

    html.Div(id='result', style={'color': colors['text'], 'font-size': '20px', 'font-family': 'Lato'})
    # Result display area
])

# App callback initialization e definition

@app.callback(
    Output('result', 'children'),
    Input('converter-button', 'n_clicks'),
    State('amount-entry', 'value'),
    State('currency-origin', 'value'),
    State('currency-destiny', 'value')
)


# Function for currency conversion

def update_output(n_clicks_convert, amount, currency_origin, currency_destiny):
    if n_clicks_convert:
        try:
            amount = float(amount)
            if amount <= 0:
                return "Por favor, insira um número maior que zero."
            else:
                data = round(c_converter.convert(amount, currency_origin, currency_destiny), 2)
                return f"{c_symbol.get_symbol(currency_destiny)} {data}"
        except ValueError:
            return "Por favor, insira um número maior que zero."
    else:
        return ''

# Running the application
if __name__ == '__main__':
    app.run_server(debug=True)