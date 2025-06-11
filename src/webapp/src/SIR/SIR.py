import numpy as np
from scipy.integrate import solve_ivp

class SIR:
    def __init__(self, S0: float = 100,
                 I0: float = 1, R0: float = 0,
                 beta: float = 0.05, gamma: float = 0.05, 
                 t_length: float = 100, n_steps: int = 10000):
        self.S0 = S0
        self.I0 = I0
        self.R0 = R0

        self.beta = beta
        self.gamma = gamma

        self.t_length = t_length
        self.n_steps = n_steps

    def basic_sir(self, t, y):
        S,I,R = y

        if np.linalg.norm(S) < 5e-1:
            S = 0
        if np.linalg.norm(I) < 5e-1:
            I = 0
        if np.linalg.norm(R) < 5e-1:
            R = 0

        dSdt = -self.beta*S*I
        dIdt = self.beta*S*I - self.gamma*I
        dRdt = self.gamma*I

        return np.array([dSdt, dIdt, dRdt])

    def solve_basic_sir(self):
        y0 = np.array([ self.S0, self.I0, self.R0 ])
        t = np.linspace( 0, self.t_length, self.n_steps + 1 )

        y = np.zeros((3,self.n_steps + 1))
        y[:,0] = np.array([ self.S0, self.I0, self.R0 ])
        
        h = self.t_length / (self.n_steps + 1)

        for i in range(1,len(t)):
            t0 = t[i-1]
            y0 = y[:,i-1]

            K1 = h * self.basic_sir(t0,y0)
            K2 = h * self.basic_sir(t0 + h/2,y0 + K1/2)
            K3 = h * self.basic_sir(t0 + h/2,y0 + K2/2)
            K4 = h * self.basic_sir(t0 + h,y0 + K3)

            y[:,i] = y0 + K1/6 + K2/3 + K3/3 + K4/6

        return [t, y]