import numpy as np
from scipy.integrate import solve_ivp

class SIR:
    def __init__(self, S0: float = 100,
                 I0: float = 1, R0: float = 0,
                 beta: float = 0.05, gamma: float = 0.05, 
                 t_length: float = 100):
        self.S0 = S0
        self.I0 = I0
        self.R0 = R0

        self.beta = beta
        self.gamma = gamma

        self.t_length = t_length

    def basic_sir(self, t, y):
        S,I,R = y

        dSdt = -self.beta*S*I
        dIdt = self.beta*S*I - self.gamma*I
        dRdt = self.gamma*I

        return np.array([dSdt, dIdt, dRdt])

    def solve_basic_sir(self):
        t_span = [0, self.t_length]
        y0 = np.array([ self.S0, self.I0, self.R0 ])
        t_eval = np.linspace( 0, self.t_length )

        soln = solve_ivp( fun=self.basic_sir, t_span=t_span, y0=y0, t_eval=t_eval )

        return soln