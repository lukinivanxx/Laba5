from matplotlib import pyplot as plt
import os
# --- Инициализация нужных нам переменных --- #

dat_dir = os.getcwd()
os.chdir("..")
dat_dir = os.getcwd()
dat_dir += '\\data\\1-clear.txt'

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
plt.show()
