import numpy as np
from scipy.integrate import solve_ivp

class PredatorPrey:
    def __init__(self, alpha: float = 1.1,
                 beta: float = 0.4, gamma:float = 0.4,
                 delta:float = 0.1, x0: int = 10, y0: int = 10,
                 t_length: float = 100, n_steps: int = 10000):
        self.alpha = alpha      # Prey birth rate
        self.beta = beta        # Prey death rate
        self.gamma = gamma      # Predator death rate
        self.delta = delta      # Predator birth rate

        self.x0 = x0            # Population of prey
        self.y0 = y0            # Population of predator

        self.t_length = t_length
        self.n_steps = n_steps
    
    def basic_predator_prey(self, t, y):
        x,y = y

        dxdt = self.alpha*x - self.beta*x*y
        dydt = -self.gamma*y + self.delta*x*y

        return np.array([dxdt, dydt])
    
    def solve_basic_predator_prey(self):
        t_span = [0, self.t_length]
        y0 = np.array([self.x0, self.y0])
        t_eval = np.linspace( 0, self.t_length, int(self.n_steps) )

        soln = solve_ivp( fun=self.basic_predator_prey, t_span=t_span, y0=y0, t_eval=t_eval ) 

        return soln