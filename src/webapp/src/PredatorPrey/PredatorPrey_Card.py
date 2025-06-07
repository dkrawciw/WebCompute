from dash import html, dcc
import dash_bootstrap_components as dbc

def PredatorPrey_Card() -> html:
    return html.Div([
        html.H2("Predator-Prey (Lotka–Volterra) Simulation")
    ])