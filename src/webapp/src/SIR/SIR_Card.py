from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from .SIR import SIR

import pandas as pd
import plotly.express as px

def Sir_Input(label: str, id: str, placeholder:str = "", default_value: float = 0):
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

def SIR_Card() -> html:
    return html.Div([
        html.H2("Basic Susceptible-Infected-Recovered (SIR) Simulation"),
        html.Div([
            Sir_Input(label="Susceptible Initial Condition", id="sir_basic_S_IC", default_value=100),
            Sir_Input(label="Infected Initial Condition", id="sir_basic_I_IC", default_value=1),
            Sir_Input(label="Recovered Initial Condition", id="sir_basic_R_IC", default_value=0),

            Sir_Input(label="Beta", id="sir_basic_beta", default_value=0.1),
            Sir_Input(label="Gamma", id="sir_basic_gamma", default_value=0.1),

            Sir_Input(label="End Time (days)", id="sir_basic_tlength", default_value=100),
            Sir_Input(label="Number of Time Steps (int)", id="sir_basic_n_steps", default_value=10000),

            dbc.Button("Simulate", id="sir_basic_btn"),
        ]),
        html.Div([], id="sir_basic_output"),
    ])

@callback(
    Output("sir_basic_output", "children"),
    Input("sir_basic_btn", "n_clicks"),
    [
        State("sir_basic_S_IC", "value"),
        State("sir_basic_I_IC", "value"),
        State("sir_basic_R_IC", "value"),
        State("sir_basic_beta", "value"),
        State("sir_basic_gamma", "value"),
        State("sir_basic_tlength", "value"),
        State("sir_basic_n_steps", "value"),
    ],
    prevent_initial_call=True,
)
def simulate_basic_sir(sir_basic_btn, sir_basic_S_IC,
                       sir_basic_I_IC, sir_basic_R_IC,
                       sir_basic_beta, sir_basic_gamma,
                       sir_basic_tlength, sir_basic_n_steps):
    new_sir = SIR()
    new_sir.beta = sir_basic_beta
    new_sir.gamma = sir_basic_gamma
    new_sir.t_length = sir_basic_tlength
    new_sir.n_steps = sir_basic_n_steps

    new_sir.S0 = sir_basic_S_IC
    new_sir.I0 = sir_basic_I_IC
    new_sir.R0 = sir_basic_R_IC

    soln = new_sir.solve_basic_sir()

    df = pd.DataFrame( soln.y.T )
    df['t'] = soln.t.T
    df.columns = ["S","I","R","t"]

    hist_plot = px.histogram(df, x="t", y=["S", "I", "R"],
                             barmode="stack", histfunc="avg",
                             nbins=df.shape[0])
    
    line_plot = px.line(df, x="t", y=["S","I","R"])

    return [
        dcc.Graph(figure=hist_plot),
        dcc.Graph(figure=line_plot),
    ]