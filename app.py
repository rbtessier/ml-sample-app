import dash
from dash import html

app = dash.Dash(__name__)

server = app.server  # Expose the server variable for deployments.

app.layout = html.Div('Hello, world!')

if __name__ == '__main__':
    app.run_server(debug=True)
