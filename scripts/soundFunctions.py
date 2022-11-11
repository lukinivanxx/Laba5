from numpy import around as ar
import os


def speed_of_sound (t, p, x3): # 1-воздух, 2-пар, 3-CO2 (x3-молярная концентрация CO2 (в %))
    pa=101325 #атм. давление
    R=8.314 #газ. постоянная
    ui=[28.97*(10**(-3)), 18.01*(10**(-3)), 44.01*(10**(-3))] #молярная масса (кг) для 3-х газов
    Cpi=[1.0036, 1.863, 0.838] #Cp 3-х газов
    Cvi=[0.7166, 1.403, 0.649] #Cv 3-х газов
    v=p/(pa+p) #молярка пара при общей с воздухом молярки = 1
    va=1-v #молярка воздуха
    dx=100-x3 #молярная концентрация пара и воздуха
    x1=dx*va #молярная концентрация воздуха и пара по отдельности
    x2=dx*v
    yi=[x1/100, x2/100, x3/100] #перевод концентрации из %
    u=0
    for i in range(0, 3): #подсчёт сумарной молярной массы
        u+=ui[i]*yi[i]
    g1=0
    g2=0
    for i in range(0, 3): #подсчёт показателя адиабаты
        g1+=Cpi[i]*ui[i]*yi[i]
        g2+=Cvi[i]*ui[i]*yi[i]
    g=g1/g2
    T=273.15+t #перевод в Кельвины
    a=((g*R*T)/u)**(1/2) #подстановка значений в формулу скорости звука
    return a


def rounding(n): # округление
    s = [int(i) for i in str(n) if i != '.']
    collected = []
    while len(s) > 6:
        if s[-1] >= 5:
            s[-2] += 1
        s.pop(-1)
    s = [str(i) for i in s]
    return ''.join(s[:3]) + '.' + ''.join(s[3:])

def experimental_v(location): # поиск нужной нам скорости
    dat_dir=os.getcwd()
    initial = dat_dir
    os.chdir("..")
    dat_dir=os.getcwd()
    dat_dir+='\\sound' +location

    f = open(dat_dir)

    ch1_mas = []; ch2_mas = []; n_mas = []

    ch1_max = -10 ** 20; ch2_max = -10 ** 20
    ch1_max_i = 0; ch2_max_i = 0

    v = 0; s = 1.158; delta_t = 0
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
    os.chdir(initial)
    return(round(v, 3))
