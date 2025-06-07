from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc

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

            Sir_Input(label="Time Length (days)", id="sir_basic_tlength", default_value=100),

            dbc.Button("Simulate", id="sir_basic_btn"),

            html.Div(id="sir_basic_output"),
        ]),
    ])

# @callback(
#     Output("sir_basic_output", "fig"),
#     Input("sir_basic_btn", "n_clicks"),
#     [
#         State("sir_basic_S_IC", "value"),
#         State("sir_basic_I_IC", "value"),
#         State("sir_basic_R_IC", "value"),
#         State("sir_basic_beta", "value"),
#         State("sir_basic_gamma", "value"),
#         State("sir_basic_tlength", "value"),
#     ],
#     prevent_initial_call=True,
# )
# def simulate_basic_sir(sir_basic_btn, sir_basic_S_IC,
#                        sir_basic_I_IC, sir_basic_R_IC,
#                        sir_basic_beta, sir_basic_gamma,
#                        sir_basic_tlength):
#     # Setup diffeq
#     set_sir_basic_fun = lambda t, y: SIR_basic(t, y, beta=sir_basic_beta, gamma=sir_basic_gamma)
#     t_span = [0, sir_basic_tlength]
#     y0 = np.array([sir_basic_S_IC, sir_basic_I_IC, sir_basic_R_IC])

#     # Solve diffeq
#     soln = solve_ivp( fun=set_sir_basic_fun, t_span=t_span, y0=y0 )

#     df = pd.DataFrame(soln.y)
#     df['t'] = soln.t

#     print( df )

#     # Plot Solution
#     fig = None
    
#     return fig