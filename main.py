import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# Equação diferencial (forma adimensional)
# ==========================================
def f(t, v, St, Re):
    return (1 - v - (3/8)*Re*v**2) / St


# ==========================================
# Método Runge-Kutta 4ª ordem
# ==========================================
def rk4(f, v0, t0, tf, h, St, Re):
    n = int((tf - t0)/h)

    t = np.zeros(n+1)
    v = np.zeros(n+1)

    t[0] = t0
    v[0] = v0

    for i in range(n):
        k1 = f(t[i], v[i], St, Re)
        k2 = f(t[i] + h/2, v[i] + h*k1/2, St, Re)
        k3 = f(t[i] + h/2, v[i] + h*k2/2, St, Re)
        k4 = f(t[i] + h, v[i] + h*k3, St, Re)

        v[i+1] = v[i] + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
        t[i+1] = t[i] + h

    return t, v


# ==========================================
# Parâmetros
# ==========================================
St = 1.0
v0 = 0.0
t0 = 0.0
tf = 10.0


# ==========================================
# 1. VALIDAÇÃO (Re → 0)
# ==========================================
h = 0.1
Re = 0.0

t, v = rk4(f, v0, t0, tf, h, St, Re)

# solução analítica
v_exata = 1 - np.exp(-t/St)

plt.figure()
plt.plot(t, v, label='Numérico (RK4)')
plt.plot(t, v_exata, '--', label='Analítico')
plt.title('Validação (Re → 0)')
plt.xlabel('t*')
plt.ylabel('v*')
plt.legend()
plt.grid()
plt.savefig('validacao.png')


# ==========================================
# 2. REFINAMENTO TEMPORAL
# ==========================================
hs = [0.5, 0.1, 0.01]

plt.figure()

for h in hs:
    t, v = rk4(f, v0, t0, tf, h, St, 0.0)
    plt.plot(t, v, label=f'h={h}')

plt.title('Refinamento Temporal')
plt.xlabel('t*')
plt.ylabel('v*')
plt.legend()
plt.grid()
plt.savefig('refinamento.png')


# ==========================================
# 3. EFEITO DO REYNOLDS
# ==========================================
Res_list = [0.0, 0.5, 1.0, 2.0]

plt.figure()

for Re in Res_list:
    t, v = rk4(f, v0, t0, tf, 0.1, St, Re)
    plt.plot(t, v, label=f'Re={Re}')

plt.title('Efeito do Número de Reynolds')
plt.xlabel('t*')
plt.ylabel('v*')
plt.legend()
plt.grid()
plt.savefig('reynolds.png')

plt.show()
