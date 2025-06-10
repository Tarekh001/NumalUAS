import numpy as np

def my_nth_root(x, N, tol, y): #x sebage parameter bisa juga y, N, tol
    if abs(y**N - x) <= tol:
        return y
    else:
        y = y - (y**N - x) / (N * y**(N - 1))
        return my_nth_root(x, N, tol, y)

#TEST CASE 1 
estimate = my_nth_root(2, 2, 1e-6, 2) #x ama y = 2 karena sama dan parameternya ada 4
print("estimate1 =", estimate)
print("sqrt(2) =", np.sqrt(2))

# #TEST CASE 2
# estimate = my_nth_root(3, 2, 1e-6, 3)
# print("estimate2 =", estimate)
# print("sqrt(3) =", np.sqrt(3))
    

# f = lambda x: x**2 - 2
# f_prime = lambda x: 2*x
# newton_rapshon = 1.4 - (f(1.4))/(f_prime(1.4))

# print("Newton Rapshon =", newton_rapshon)
# print("sqrt(2) = ", np.sqrt(2))

# def my_newton(f,df,x0,tol):
#     if abs(f(x0)) < tol:
#         return x0
#     else:
#         return my_newton(f,df,x0 - f(x0)/df(x0),tol)
# estimate = my_newton(f,f_prime,1.5,1e-6)
# print("estimate =", estimate)

