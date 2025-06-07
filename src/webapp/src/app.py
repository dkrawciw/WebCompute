from dash import Dash
import dash_bootstrap_components as dbc
from index import index

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

app.layout = index()

app.run()