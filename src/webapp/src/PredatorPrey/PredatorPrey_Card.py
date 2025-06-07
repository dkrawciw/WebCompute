from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from .PredatorPrey import PredatorPrey
import plotly.express as px
import pandas as pd

example_pred_prey = PredatorPrey()

def pred_prey_input(label: str, id: str,
                    placeholder:str = "",
                    default_value: float = 0):
    return html.Div([
        html.Span(label, className="input-group-text"),
        dbc.Input(
            id=id,
            placeholder=placeholder,
            type="number",
            className="form-control",
            value=default_value
        ),
    ], className="input-group mb-3")

def PredatorPrey_Card() -> html:
    return html.Div([
        html.H2("Predator-Prey (Lotka–Volterra) Simulation"),
        html.Div([
            pred_prey_input(label="Initial Population of Prey", id="pred_prey_x0", default_value=example_pred_prey.x0),
            pred_prey_input(label="Initial Population of Predators", id="pred_prey_y0", default_value=example_pred_prey.y0),

            pred_prey_input(label="Prey Birth Rate", id="pred_prey_alpha", default_value=example_pred_prey.alpha),
            pred_prey_input(label="Prey Death Rate", id="pred_prey_beta", default_value=example_pred_prey.beta),
            pred_prey_input(label="Predator Birth Rate", id="pred_prey_delta", default_value=example_pred_prey.delta),
            pred_prey_input(label="Predator Death Rate", id="pred_prey_gamma", default_value=example_pred_prey.gamma),

            pred_prey_input(label="End Time (days)", id="pred_prey_t_length", default_value=example_pred_prey.t_length),
            pred_prey_input(label="Number of Steps (int)", id="pred_prey_n_steps", default_value=example_pred_prey.n_steps),

            dbc.Button("Simulate", id="pred_prey_btn"),
        ]),
        html.Div([], id="pred_prey_output"),
    ])

@callback(
    Output("pred_prey_output", "children"),
    Input("pred_prey_btn", "n_clicks"),
    [
        State("pred_prey_x0", "value"),
        State("pred_prey_y0", "value"),
        State("pred_prey_alpha", "value"),
        State("pred_prey_beta", "value"),
        State("pred_prey_gamma", "value"),
        State("pred_prey_delta", "value"),
        State("pred_prey_t_length", "value"),
        State("pred_prey_n_steps", "value"),
    ],
)
def simulate_pred_prey(pred_prey_btn, x0, y0,
                       alpha, beta, gamma, delta,
                       t_length, n_steps):
    new_pred_prey = PredatorPrey()
    new_pred_prey.x0 = x0
    new_pred_prey.y0 = y0

    new_pred_prey.alpha = alpha
    new_pred_prey.beta = beta
    new_pred_prey.beta = beta
    new_pred_prey.gamma = gamma
    new_pred_prey.delta = delta

    new_pred_prey.t_length = t_length
    new_pred_prey.n_steps = n_steps

    soln = new_pred_prey.solve_basic_predator_prey()

    df = pd.DataFrame( soln.y.T )
    df['t'] = soln.t.T
    df.columns = ["Rabbits","Foxes","t"]

    hist_fig = px.histogram( df, x='t', y=['Rabbits',"Foxes"], barmode="stack", nbins=df.shape[0], histfunc="avg" )

    line_fig = px.line(df, x="t", y=["Rabbits", "Foxes"])

    return [
        dcc.Graph(figure=hist_fig),
        dcc.Graph(figure=line_fig),
    ]