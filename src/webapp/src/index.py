from dash import html
from SIR import SIR_Card
from PredatorPrey import PredatorPrey_Card

def index() -> html:
    return html.Div([
        html.H1('Web Compute'),
        SIR_Card(),
        PredatorPrey_Card(),
    ])