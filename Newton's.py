from math import exp
from random import seed
from random import random
import random
from sympy import *
import numpy as np
import math

# основная ф-ия
def function(x,y):
    return 2*x*x+4*y*y-2*x*y+x
# ф-ии для Дихотомии
def const(a, b, e):
    return (a+b+e)/2

def norma(a):
    return math.sqrt(a[0]*a[0]+a[1]*a[1])
# поиск градиента ф-ии при передаче ф-ии
def grad_func(a):
    mas=[]
    mas.append(6*a[0]-2*a[1]+1)
    mas.append(8*a[1] - 2*a[0])
    return mas

def x_koord(x, f, t):
    return 3*((x[0]-(t*f[0]))**2)+4*((x[1]-(t*f[1]))**2)-2*(x[0]-(t*f[0]))*(x[1]-(t*f[1]))+(x[0]-(t*f[0]))

# шаг 10. Подстановка т для поиска след х
def xt_koord(x,d,t,):
    xk= (np.add(x,np.dot(t,d)))
    return xk

# норма разности 2-х точек
def norm_razn(x_1,x_0):
    a=[]
    a.append(x_1[0]-x_0[0])
    a.append(x_1[1]-x_0[1])
    return norma(a)

# модуль разности двух ф-ий
def fun_razn(X_1,X_0):
    a1 = function(X_1[0], X_1[1])
    a =function(X_0[0], X_0[1])
    return abs(a1-a)

# поиск производной и формирование матрицы
def find_H():
    x = Symbol('x')
    y = Symbol('y')
    z1 = 6 * x - 2*y+1
    z2 = 8*y - 2*x
    H, h1, h2 = [], [], []

    x_one = z1.diff(x)
    xy_one = z1.diff(y)
    h1.append(float(x_one))
    h1.append(float(xy_one))
    y_one = z2.diff(y)
    h2.append(float(xy_one))
    h2.append(float(y_one))
    H.append(h1)
    H.append(h2)
    H = np.array(H)
    print(H)
    return H

E1 = 0.1
E2 = 0.15
M = 10
E = 0.2
l = 0.25
a = -3
b = 3
N = 4
k = 1
kol = -1
summa=0
i, t = 0,0
X, D, T = [],[],[]

#задание х0
s = '2;1.5'
X.append(list(map(float, (s.split(";")))))
H = find_H()
while (summa!=2):
    kol += 1
    f = grad_func(X[i]) #Поиск градиента
    f = np.array(f).T
    print("k=" + str(kol) + " f=" + str(f))
    if (norma(f) < E1):
        summa+=1
        print("Min" + str(X[i]))
        break
    if (kol >= M):
        print("Min" + str(X[i]))
        break
    H = np.linalg.inv(H) #Поиск обратной матрицы
    print("H`-1=")
    print(H)
    if (H[0][0]>0 and (H[0][0]*H[1][1]-H[0][1]*H[1][0])>0):#Проверка главных миноров
        d = np.dot(H, f)*(-1)
        t = 1
    else:
        d = f * (-1)
    print("d = ")
    print(d)
    if (t==1):
        T.append(t)
    else:
        while(k > 0):
            #print("k=" + str(k) + ", N=" + str(N), end=" ")
            y = const(a, b, -E)
            z = const(a, b, E)
            f_y = x_koord(X[i],f,y)
            f_z = x_koord(X[i],f,z)
            #print("f(y)="+str(f_y) + ", f(z)=" + str(f_z), end=" ")
            if (f_y < f_z):
                b = z
            else:
                a = y
            #print("L=["+str(a)+"," + str(b)+"]", "|L|=" + str(abs(b-a)), end=" ")
            if (abs(b-a) <l):
                x = (a+b)/2
                T.append(x)
                print("t = " + str(x), end=" ")
                break
            else:
                k += 1
                N = 2*(k+1)
    x_new = []
    x_new = xt_koord(X[i], d, T[i])
    print("x_next= ")
    print(x_new)
    X.append(x_new)

    on=norm_razn(X[i+1], X[i])
    tw=fun_razn(X[i+1], X[i])
    if ( on< E2 and tw < E2):
        print(str(on)+"<"+str(E2), end=" ")
        print(str(tw) + "<" + str(E2), end=" ")
        summa += 1
    else:
        summa = 0
    print()
    i += 1
print()
if (summa==2):
    print("Min= " + str(X[-1]))
print("Otvet = [-0.18, -0.045]")


