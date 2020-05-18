import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, State, Input
from producer.kafka_producer import produce_data
from consumer.kafka_consumer import films

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    html.H1(children=["Enter Movie Title"]),
    dcc.Input(id="film-name", type="text", placeholder=""),
    html.Button(id="submit-button", type="submit", children="Submit"),
    html.Div(id="output_div"),
    html.Div(id="output_div_consumer")
])

@app.callback(Output("output_div", "children"),
                [Input("submit-button", "n_clicks"), Input("film-name", "value")])
def update_output(clicks, input_value):
    if clicks is not None:
        print(clicks, input_value)
        if input_value != "":
             produce_data(input_value)
             print(input_value)
    if len(films) > 0:
        return [html.Img(
                src = app.get_asset_url(film),
                style = {
                    'height': '40%',
                    'width': '40%',
                    'float': 'left',
                    'position': 'relative',
                    'padding-top': 0,
                    'padding-right': 0
                }
            ) for film in films]
    else:
        return None

if __name__ == '__main__':
    app.run_server(debug=True)
