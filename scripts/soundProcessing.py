import matplotlib.pyplot as plt
import matplotlib.ticker as tic
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
    s=f.readline()
    if s=='':
        break
    qs=s[:s.find(' ')]
    ps=s[s.find(' ')+1:]
    q.append(float(qs))
    p.append(float(ps))
f.close()
fig, ax = plt.subplots()
ax.plot(q, p, linestyle='-', linewidth = 1.5,  color= 'forestgreen', label='аналитическая зависимость') #строим график
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
ax.grid(axis= 'both', which = 'minor', linestyle='--', linewidth=0.5, color='lightgrey')
ax.grid(axis= 'both', which = 'major', linestyle='-', linewidth=1, color='lightgrey')
plt.show() #показ графика
dat_dir=os.getcwd() #сохранение графика в директорию plots
dat_dir+='\\plots\\plot.svg'
fig.savefig(dat_dir)
