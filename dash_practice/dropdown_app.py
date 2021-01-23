import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div([
    html.H3('cheklist'),
    dcc.Checklist(id='checklist-id',
                  options=[
                      {'label': 'New York City', 'value': 'NYC'},
                      {'label': 'Montréal', 'value': 'MTL'},
                      {'label': 'San Francisco', 'value': 'SF'}
                  ],
                  value=['NYC', 'MTL'],
                  style={'background': 'green'},
                  labelStyle={'display': 'outline' },
                  ),

                 html.Div(id='show-data-id')
])

@app.callback(
    Output('show-data-id', 'children'),
    Input('checklist-id', 'value'))
def display_value(value):
    print(value)
    return 'You have selected "{}"'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
