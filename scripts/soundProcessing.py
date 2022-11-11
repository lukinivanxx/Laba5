import matplotlib.pyplot as plt
import matplotlib.ticker as tic
import matplotlib.artist as art
import os
dat_dir=os.getcwd()
os.chdir("..")
dat_dir=os.getcwd()
dat_dir+='\\data\\dat.txt'
f=open(dat_dir) #Открываем файл dat.txt, находящийся в директории data для чтения
q=[]
p=[]
s=''
while True: #считываем значения концентраций и скоростей звука в массивы
    s = f.readline()
    if s == '\n':
        break
    s = list(map(float, s.split()))
    qs=s[0] # qs=s[:s.find(' ')]
    ps=s[1] # то же самое, только s.find + 1:
    q.append(float(qs))
    p.append(float(ps))
# --- Считывание точек для графика (пункт 5) --- #
collected = {}
for i in range(2):
    s = f.readline().split()
    collected[float(s[0])] = float(s[1])
# --- Собственно построение --- #
fig, ax = plt.subplots()
ax.scatter(collected.values(), collected.keys(), marker='D', edgecolors='black', s=30, label='Скорости при различных концентрациях C02', color='yellow', zorder=4)
ax.plot(q, p, linestyle='-', linewidth = 1.5,  color= 'forestgreen', label='Аналитическая зависимость', zorder=3) #строим график
ax.legend(loc=0) #добавляем легенду
ax.set_ylabel('Скорость звука, м/с') #подписываем оси
ax.set_xlabel('Концентрация CO2, %')
ax.set_title('Зависимость скорости звука\nот концентрации углекислого газа', loc='center', pad=10) #подписываем график
ax.set_xlim([-0.1, 5.1]) #устанавливаем пределы концентраций и скоростей звука для графика
ax.set_ylim([341.6, 347.3])
ax.yaxis.set_minor_locator(tic.MultipleLocator(0.2)) #делаем сетку
ax.xaxis.set_minor_locator(tic.MultipleLocator(0.2))
ax.yaxis.set_major_locator(tic.MultipleLocator(1))
ax.xaxis.set_major_locator(tic.MultipleLocator(1))
ax.grid(axis= 'both', which = 'minor', linestyle='--', linewidth=0.5, color='lightgrey', zorder=0)
ax.grid(axis= 'both', which = 'major', linestyle='-', linewidth=1, color='lightgrey', zorder=0)
plt.show() #показ графика
dat_dir=os.getcwd() #сохранение графика в директорию plots
dat_dir+='\\plots\\plot.svg'
fig.savefig(dat_dir)


# --- Возможно нужный код для визуализации сдвига и сжатия графиков --- #
'''
# --- Инициализация нужных нам переменных --- #

dat_dir = os.getcwd()
os.chdir("..")
dat_dir = os.getcwd()
dat_dir += '\\data\\1-clear.txt' # Аналогично для no.

f = open(dat_dir)

ch1_mas = []
ch2_mas = []
n_mas = []

ch1_max = -10 ** 20
ch2_max = -10 ** 20
ch1_max_i = 0
ch2_max_i = 0

v = 0
s = 1.158
delta_t = 0
# --- Считывание файла, сдвиг к 0 --- #
for i in range(10): f.readline()
for i in range(4096):
    n, ch1, ch2 = map(int, f.readline().split())
    ch1_mas.append(ch1 - 79); ch2_mas.append(ch2 - 135); n_mas.append(n * ((0.2 * 10 ** (-3)) / 160))
# --- Поиск вершины первого подъёма, "сжатие" графиков --- #
ch1_max = max(ch1_mas); ch2_max = max(ch2_mas)
ch1_max_i = ch1_mas.index(ch1_max); ch2_max_i = ch2_mas.index(ch2_max)
ch1_mas = [i / ch1_max for i in ch1_mas]; ch2_mas = [j / ch2_max for j in ch2_mas]
# --- Поиск скорости --- #
delta_t = (ch2_max_i - ch1_max_i) * ((0.2 * 10 ** (-3)) / 160)
v = s / delta_t
print(round(v, 3))
# --- Построение графиков без сдвига и со сдвигом --- #
plt.plot(n_mas, ch1_mas, 'bo', label="CH1", markersize=1)
plt.plot(n_mas, ch2_mas, 'ro', label="CH2", markersize=1) # Без сдвига

plt.legend()
plt.xlabel("t")
plt.ylabel("A")
plt.grid()
plt.savefig('graph_without_shift_clear.svg')
plt.show()
plt.plot([n_mas[i] for i in range(ch1_max_i, len(n_mas))], [ch1_mas[i] for i in range(ch1_max_i, len(n_mas))], 'bo', label="CH1", markersize=1)
plt.plot([n_mas[i] - delta_t for i in range(ch2_max_i, len(n_mas))], [ch2_mas[i] for i in range(ch2_max_i, len(ch2_mas))], 'ro', label="CH2", markersize=1) # Со сдвигом
plt.legend()
plt.xlabel("t")
plt.ylabel("A")
plt.grid()
plt.savefig('graph_with_shift_clear.svg')
plt.show()'''
