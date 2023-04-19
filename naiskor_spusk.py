import math
def function(x,y):
    return 2*x*x+4*y*y-2*x*y+x

def const(a, b, e):
    return (a+b+e)/2

def norma(a):
    return math.sqrt(a[0]*a[0]+a[1]*a[1])

def grad_func(a):
    mas=[]
    mas.append(6*a[0]-2*a[1]+1)
    mas.append(8*a[1] - 2*a[0])
    return mas

def x_koord(x, f, t):
    return 3*((x[0]-(t*f[0]))**2)+4*((x[1]-(t*f[1]))**2)-2*(x[0]-(t*f[0]))*(x[1]-(t*f[1]))+(x[0]-(t*f[0]))

def xt_koord(x,f,t,x_new):
    x_new.append(x[0]-(t*f[0]))
    x_new.append(x[1]-(t*f[1]))
    return x_new

def norm_razn(x_1,x_0):
    a=[]
    a.append(x_1[0]-x_0[0])
    a.append(x_1[1]-x_0[1])
    return norma(a)

def fun_razn(X_1,X_0):
    a1 = function(X_1[0], X_1[1])
    a =function(X_0[0], X_0[1])
    return abs(a1-a)

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
i=0
X = []
t = []
#задание х0
s = '2;1.5'
X.append(list(map(float, (s.split(";")))))
while (summa !=2):
    kol += 1
    f = grad_func(X[i])
    print("k=" + str(kol) + " f=" + str(f), end=" ")
    if (norma(f) < E1):
        print("Min" + str(X[i]))
        break
    if (kol >= M):
        print("Min" + str(X[i]))
        break
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
            t.append(x)
            print("t = " + str(x), end=" ")
            break
        else:
            k += 1
            N = 2*(k+1)
    x_new = []
    x_new = xt_koord(X[i], f, t[i], x_new)
    print("x_next= " + str(x_new), end=" ")
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
if (summa==2):
    print("Min= " + str(X[-1]))
print("Otvet = [-0.18, -0.045]")
import math


def function(x, y):
    return 2 * x * x + 4 * y * y - 2 * x * y + x


def const(a, b, e):
    return (a + b + e) / 2


def norma(a):
    return math.sqrt(a[0] * a[0] + a[1] * a[1])


def grad_func(a):
    mas = []
    mas.append(6 * a[0] - 2 * a[1] + 1)
    mas.append(8 * a[1] - 2 * a[0])
    return mas


def x_koord(x, f, t):
    return 3 * ((x[0] - (t * f[0])) ** 2) + 4 * ((x[1] - (t * f[1])) ** 2) - 2 * (x[0] - (t * f[0])) * (
                x[1] - (t * f[1])) + (x[0] - (t * f[0]))


def xt_koord(x, f, t, x_new):
    x_new.append(x[0] - (t * f[0]))
    x_new.append(x[1] - (t * f[1]))
    return x_new


def norm_razn(x_1, x_0):
    a = []
    a.append(x_1[0] - x_0[0])
    a.append(x_1[1] - x_0[1])
    return norma(a)


def fun_razn(X_1, X_0):
    a1 = function(X_1[0], X_1[1])
    a = function(X_0[0], X_0[1])
    return abs(a1 - a)


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
summa = 0
i = 0
X = []
t = []
# задание х0
s = '2;1.5'
X.append(list(map(float, (s.split(";")))))
while (summa != 2):
    kol += 1
    f = grad_func(X[i])
    print("k=" + str(kol) + " f=" + str(f), end=" ")
    if (norma(f) < E1):
        print("Min" + str(X[i]))
        break
    if (kol >= M):
        print("Min" + str(X[i]))
        break
    while (k > 0):
        # print("k=" + str(k) + ", N=" + str(N), end=" ")
        y = const(a, b, -E)
        z = const(a, b, E)
        f_y = x_koord(X[i], f, y)
        f_z = x_koord(X[i], f, z)
        # print("f(y)="+str(f_y) + ", f(z)=" + str(f_z), end=" ")
        if (f_y < f_z):
            b = z
        else:
            a = y
        # print("L=["+str(a)+"," + str(b)+"]", "|L|=" + str(abs(b-a)), end=" ")
        if (abs(b - a) < l):
            x = (a + b) / 2
            t.append(x)
            print("t = " + str(x), end=" ")
            break
        else:
            k += 1
            N = 2 * (k + 1)
    x_new = []
    x_new = xt_koord(X[i], f, t[i], x_new)
    print("x_next= " + str(x_new), end=" ")
    X.append(x_new)
    on = norm_razn(X[i + 1], X[i])
    tw = fun_razn(X[i + 1], X[i])
    if (on < E2 and tw < E2):
        print(str(on) + "<" + str(E2), end=" ")
        print(str(tw) + "<" + str(E2), end=" ")
        summa += 1
    else:
        summa = 0
    print()
    i += 1
if (summa == 2):
    print("Min= " + str(X[-1]))
print("Otvet = [-0.18, -0.045]")

