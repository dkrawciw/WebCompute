import numpy as np

class SIR:
    def __init__(self, S0: float, I0: float, R0: float, beta: float, gamma: float, t_length: float):
        self.S0 = S0
        self.I0 = I0
        self.R0 = R0

        self.beta = beta
        self.gamma = gamma

        self.t_length = t_length

        def diffeq(t, y):
            S,I,R = y

            

def SIR_basic(t, y, beta=0, gamma=0):
    S,I,R = y

    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I

    return [ dSdt, dIdt, dRdt ]