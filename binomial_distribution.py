from scipy.stats import nbinom
import numpy as np
from matplotlib import pyplot as plt

r = 3
p = 0.25
m = 2

X1 = nbinom(r,p)
X2 = nbinom(r*m,p*m)

i = range(0,int(np.round(2*r/p,0)))
p_X1_i = X1.pmf([xx for xx in i])
p_X2_i = X2.pmf([xx for xx in i])

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.plot(i, p_X2_i, 'v', label="$X2 sim NB({{{0}}},{{{1}}})$".format(r*m,p*m))
plt.plot(i, p_X1_i, 'v', label="$X1 sim NB({{{0}}},{{{1}}})$".format(p,r))
plt.xlabel("i",fontsize=14)
plt.ylabel("P(X=i)",fontsize=14)
plt.legend()
plt.show

mean_X1, var_X1 = nbinom.stats(r,p,loc=r)
mean_X2, var_X2 = nbinom.stats(r*m,p*m,loc=m*r)
print(f'E(X1_1)={mean_X1}, Var(X1_1)={var_X1}')
print(f'E(X2_1)={mean_X2}, Var(X2_1)={var_X2}')

v1 = 8
v2 = 20
f_X1_v1 = X1.cdf(v1)
f_X2_v1 = X2.cdf(v1)
f_X1_v2 = X1.cdf(v2)
f_X2_v2 = X2.cdf(v2)
print(f'F_X1({v1})={f_X1_v1}, F_X2({v1})={f_X2_v1}')
print(f'F_X1({v2})={f_X1_v2}, F_X2({v2})={f_X2_v2}')
plt.subplot(1,2,2)
plt.plot(i, X1.cdf(i), 'o', label="$F_{X1}(i)$")
plt.plot(i, X2.cdf(i), 'o', label="$F_{X2}(i)$")
plt.xlabel("i",fontsize=14)
plt.ylabel("F_X(i)",fontsize=14)
plt.legend()
plt.show()  

