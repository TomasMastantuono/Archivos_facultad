#%% Problema 9
import numpy as np
k = 1.380649E-23 # J/K
h_planck = 6.63E-34 #J*s
h_b = h_planck/(2*np.pi)
c = 300_000_000 #m/s
def pot(T, A):
    alpha = np.pi**4 * k**4 / (15 * h_b * (h_planck * c)**2)
    return alpha * A * T**4

S_T = 5.10E14 #m
T_EB = 25_000
P_EB = pot(T_EB, S_T)/S_T

T_GR = 3000
P_GR = pot(T_GR, 1E15 * S_T)/(1E15 * S_T)

print(f'Enana blanca: {P_EB} J/A*s\nGigante Roja: {P_GR} J/A*s')
print(f'El cociente de frecuencias es: {T_GR/T_EB}')

#%% Problema 11
import numpy as np

k = 1.380649E-23 # J/K
h_planck = 6.63E-34 #J*s
h_b = h_planck/(2*np.pi)
alpha = 2.88

lambda_CA2 = 3.969E-7 #metros = 3969 A
T_CA2 = h_b*c/(alpha*k*lambda_CA2)
m_CA2 = 1.989E33 #g
D_lamnda = lambda_CA2 * np.sqrt(2*k*T_CA2 / (m_CA2 * c**2))
print(D_lamnda)

Dre_labda = 4E-10 #metros
cociente = Dre_labda/D_lamnda
print(cociente)