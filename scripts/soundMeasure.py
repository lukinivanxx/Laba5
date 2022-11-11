import soundFunctions as sf
from numpy import around as ar
import os
dat_dir=os.getcwd()
os.chdir("..")
dat_dir=os.getcwd()
dat_dir+='\\data\\dat.txt'
f=open(dat_dir, 'w') #Открываем файл dat.txt, находящийся в директории data для записи
q=[]
p=[]
for i in range (0, 5001): # строим 2 массива на 5 тыс значений, вычисляющий для каждой концентрации углекислого газа (0-5%) скорость звука
    q.append(i/1000)
    p.append(sf.speed_of_sound(24, 2990, q[i])) #24 град. C , давление насыщенного пара при 24 град., ~ (нигде не было написано: сколько градусов и какая влажность была)
    f.write(str(q[i])+' '+str(p[i])+'\n')
k=(p[0]-p[5000])/(q[5000]-q[0]) #убеждаемся, что график приближённо линеен, и определяем модуль коэффициента наклона (функция имеет вид: a(x3)=p[0]-k*x3)
f.close()
# --- Поиск экспериментально полученных значений скорости звука --- #
collected = {}
clear_air = sf.experimental_v('\\data\\1-clear.txt')
no = sf.experimental_v('\\data\\1-no.txt')
collected[clear_air] = 0; collected[no] = 0;
# --- Поиск соответствующих коэффициентов для экспериментально полученных значений скорости звука в файле dat.txt --- #
f = open(dat_dir, 'r')
while True:
    s = f.readline()
    if s != '':
        coefficient, speed_of_sound = map(float, s.split())
        if sf.rounding(speed_of_sound) == str(clear_air): # 346.577 - скорость звука в "чистом" воздухе
            collected[clear_air] = coefficient
        elif sf.rounding(speed_of_sound) == str(no): # 344.515 - скорость звука после выдоха человека
            collected[no] = coefficient
    else:
        break
f.close()
f = open(dat_dir, 'a')
##f.write('\n' + 'clear ' + str(collected['clear']) + '\n' + 'no ' + str(collected['no']))
f.write(f'\n{str(clear_air)} {collected[clear_air]}\n{str(no)} {collected[no]}')
f.close()


