import numpy as np
import math

# основная ф-ия
'''def function(x,y):
    return 3*x*x+4*y*y-2*x*y+x
# ф-ии для Дихотомии
def const(a, b, e):
    return (a+b+e)/2
# поиск нормы точки
def norma(a):
    return math.sqrt(a[0]*a[0]+a[1]*a[1])
# поиск градиента ф-ии при передаче ф-ии
def grad_func(a):
    mas=[]
    mas.append(6*a[0]-2*a[1]+1)
    mas.append(8*a[1] - 2*a[0])
    return mas
# ф-ия для поиска t
def x_koord(x, f, t):
    return 3*((x[0]+(t*f[0]))**2)+4*((x[1]+(t*f[1]))**2)-2*(x[0]+(t*f[0]))*(x[1]+(t*f[1]))+(x[0]+(t*f[0]))

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

def sven(a, b, Y, f):
    X = []
    x=-2
    t=1
    i=0
    X.append(x)
    f_1 = x_koord(Y, f, (X[i]-t))
    f_2 = x_koord(Y, f,X[i])
    f_3 = x_koord(Y, f,X[i]+t)
    if (f_1 >= f_2 and f_2 <= f_3):
        print("[" + str(X[i]-t) + ";" + str(X[i]+t)+ "]")
    elif (f_1 <= f_2 and f_2 >= f_3):
        print("задайте другой x0")
    else:
        if (f_1 >= f_2 >= f_3):
            d = t
            a = X[0]
            x_next=X[0]+t
            i = 1
        else:
            d = -t
            b = X[0]
            x_next = X[0] - t
            i = 1
        X.append(x_next)
        while(1>0):
            x_next = X[i] + pow(2,i) * d
            X.append(x_next)
            if (x_koord(Y, f,X[i+1])< x_koord(Y, f,X[i]) and d == t):
                a = X[i]
            elif(x_koord(Y, f,X[i+1])< x_koord(Y, f,X[i]) and d == t):
                b = X[i]
            else:
                if (d == t):
                    b = X[i+1]
                else:
                    a = X[i+1]
                break
            i += 1

E1 = 0.1
E2 = 0.15
M = 10
E = 0.2
l = 0.25
a = -5
b = 3
N = 4
k = 1
kol = -1
summa=0
i, t, tmp = 0,0, 0
X, D, T = [], [], []

#задание х0
s = '2;1.5'
X.append(list(map(float, (s.split(";")))))


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
    if (tmp == 0):
        d = f * (-1)
        tmp += 1
    else:
        f_pred = grad_func(X[i - 1])
        bet = (norma(f) * norma(f))/(norma(f_pred) * norma(f_pred))
        print("betta= " + str(bet))
        d = f * (-1) + np.dot(bet, d)
    print("d=")
    print(d)
    sven(a,b,X[i], d)
#Метод Дихотомии
    while (k > 0):
        y = const(a, b, -E)
        z = const(a, b, E)
        f_y = x_koord(X[i], d, y)
        f_z = x_koord(X[i], d, z)
        if (f_y < f_z):
            b = z
        else:
            a = y
        if (abs(b - a) < l):
            x = (a + b) / 2
            T.append(x)
            print("t = " + str(x), end=" ")
            break
        else:
            k += 1
            N = 2 * (k + 1)
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
print("Otvet = [-0.18, -0.045]")'''

import random
from math import sqrt
import numpy as np
import pandas as pd


class Neuron:
    def __init__(self, weights, samples=None):
        if samples is None:
            samples = []
        self.weights = weights
        self.samples = samples

# Загружаем данные из Excel файла
df = pd.read_excel('students_dataset.xlsx')

# Преобразуем DataFrame в массив словарей
dataset = df.to_dict('records')
dataset_copy = dataset

# Нормализуем данные
for sample in dataset:
    sample['x1'] = 1.0 if sample['x1'] == 'М' else 0.0
    sample['x2'] = 1.0 if sample['x2'] == 'Да' else 0.0
    sample['x3'] /= 100
    sample['x4'] /= 100
    sample['x5'] /= 100
    sample['x6'] /= 100
    sample['x7'] /= 100

# Нормализованные данные
print(pd.DataFrame(dataset))

# Создаём и инициализируем K нейронов.
# Каждый имеет M входов.
# Веса задаются случайным образом в диапазоне [0.5 - 1/sqrt(M); 0.5 + 1/sqrt(M)].
neurons = []
M = 7
K = 4
a = 0.5 - 1/sqrt(M)
b = 0.5 + 1/sqrt(M)

for i in range(K):
    weights = []
    for j in range(M):
        weights.append(random.uniform(a, b))
    weights = np.array(weights)
    neurons.append(Neuron(weights=weights))

# for neuron in neurons:
#     print(neuron.weights)

epochs = 6
lr = 0.30

# Обучение
for i in range(epochs):
    # Перемешиваем примеры
    random.shuffle(dataset_copy)

    for sample in dataset_copy:
        # Евклидовы расстояния от входного вектора до центров всех кластеров
        r = []
        x = np.array(list(sample.values())[:-1])
        for neuron in neurons:
            r.append(np.linalg.norm(x - neuron.weights))
        min_index = r.index(min(r))
        neurons[min_index].weights = neurons[min_index].weights + lr * (x - neurons[min_index].weights)
    lr -= 0.05

for sample in dataset_copy:
    r = []
    x = np.array(list(sample.values())[:-1])
    for neuron in neurons:
        r.append(np.linalg.norm(x - neuron.weights))
    min_index = r.index(min(r))
    neurons[min_index].samples.append(sample)

for i, neuron in enumerate(neurons):
    print(f'\nСluster {i + 1}')
    print('Weights: ')
    for a in neuron.weights:
        print(a, end=' | ')
    print('\nSamples: ')
    print(pd.DataFrame(neuron.samples))

# Парни без стипухи
# Девушки со стипухой
# Парни со стипухой
# Девушки без стипухи