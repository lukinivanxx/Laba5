import soundFunctions as sf
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
    p.append(sf.speed_of_sound(20, 2340, q[i])) #20 град. C , давление насыщенного пара при 20 град., ~
    f.write(str(q[i])+' '+str(p[i])+'\n')
k=(p[0]-p[5000])/(q[5000]-q[0]) #убеждаемся, что график приближённо линеен, и определяем модуль коэффициента наклона (функция имеет вид: a(x3)=p[0]-k*x3)