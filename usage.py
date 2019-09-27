import dash_leaflet
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(dash_leaflet.DashLeaflet(markers=[{"title": "Hello", "geom": [[1, 1], [1, 2]], "cluster": True}]))


if __name__ == '__main__':
    app.run_server(debug=True)
