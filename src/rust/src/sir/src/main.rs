use ndarray::Array1;
use ndarray::Array2;

fn main() {
    solve_sir( &[100.0, 1.0, 0.0], 0.5, 0.5, 10.0, 10000 );
}

fn sir(_t: f64, y: &[f64; 3], beta: f64, gamma: f64) -> [f64; 3]{
    let S = y[0];
    let I = y[1];
    let R = y[2];

    let dSdt = -beta*S*I;
    let dIdt = beta*S*I - gamma*I;
    let dRdt = gamma * I;

    [ dSdt, dIdt, dRdt ]
}

fn solve_sir(y0: &[f64; 3], beta: f64, gamma: f64, t_stop: f64, n_steps: usize) {
    let t_len: usize = n_steps + 1;
    let h = t_stop / (t_len as f64);
    let t = (0..t_len) / t_stop;

    let t: Vec<f64> = vec![0.0]
    let mut y: Vec<[f64; 3]> = vec![[0.0; 3]; t_len];

    y[0..3][0] = *y0;

    for i in (1..t_len) {
        k1 = h * sir()
        y[0..3][i] = [  ]
    }
}