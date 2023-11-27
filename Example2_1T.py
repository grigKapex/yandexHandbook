N = int(input('N_'))
M = int(input('M_'))
K1 = int(input('K1_'))
K2 = int(input('K2_'))
m1 = (N * M - K2 * N) / (K1 - K2)
m2 = N - m1
print(f'{int(m1)} {int(m2)}')