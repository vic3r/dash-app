import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
server = app.server
app.layout = html.Div(
    html.H1(children=['Dash App']),
    dcc.Graph(
        id='first chart',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [9, 6, 2, 1, 5], 'type': 'line', 'name': 'Boats'},
                {'x': [1, 2, 3, 4, 5], 'y': [8, 7, 2, 7, 3], 'type': 'bar', 'name': 'Cars'},
            ],
            'layout': {
                'title': 'Movies chart'
            }
        }
    )
)

if __name__ == '__main__':
    app.run_server(debug=True)
