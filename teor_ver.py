from math import sqrt
#MIN_X = -1.7 #Нижняя граница
#FREQUENCY = [4, 6, 8, 10, 8, 2] #Список частот
#STEP = 0.7 #Шаг

#test_data
MIN_X = 2.9
FREQUENCY = [3, 5 ,14, 6, 2]
STEP = 1

N = sum(FREQUENCY)

class Interval:


    def __init__(self, lower_bound, freq):
        self.freq = freq
        self.lower_bound = lower_bound
        self.higher_bound = lower_bound+STEP
        self.mid_interv = lower_bound+(STEP/2)

    def __str__(self):
        return 'Нижняя граница:{:.2f} ' \
               'Верхняя граница: {:.2f} ' \
               'Частота: {} ' \
               'Середина интервала: {:.2f}'.format(self.lower_bound, self.higher_bound, self.freq, self.mid_interv)

class AvgX:
    '''Расчет среднего выборочного X(a)'''

    def __init__(self, ranges):
        self.ranges = ranges
        self.x = self.calc()

    def calc(self):
        result=0
        self.calc_string = 'N=1/{}'.format(N)
        for i in self.ranges:
            result+=i.mid_interv*i.freq
            self.calc_string+='*({:.2f}*{})'.format(i.mid_interv, i.freq)
        result*=1/N
        #print(avg_x.__doc__)
        self.calc_string+='='+str(result)
        return result

    def __str__(self):
        return self.__doc__ +'\n' + self.calc_string

class DespS(AvgX):
    '''Расчет среднеквадратического отклонения S^2'''

    def __init__(self, ranges, power=2):
        self.ranges = ranges
        self.s = self.calc(power)

    def calc(self, power):
        result = 0
        self.calc_string = 'S^2=1/{}'.format(N)
        X = AvgX(ranges).x
        for i in self.ranges:
            result+=((i.mid_interv-X)**2)*i.freq
            self.calc_string+='*(({:.2f}-{:.2f})^2*{})'.format(i.mid_interv, X, i.freq)
        result*=1/(N)
        self.calc_string += '='+str(result)
        self.calc_string += '\nS='+str(sqrt(result))
        result = sqrt(result)**power
        return result

class DespSCube(DespS):
    '''Расчет центрального момента третьего порядка u3'''


    def calc(self, power):
        result = 0
        self.calc_string = 'u3=1/{}'.format(N)
        X = AvgX(ranges).x
        for i in self.ranges:
            result+=((i.mid_interv-X)**3)*i.freq
            self.calc_string+='*(({:.2f}-{:.2f})^3*{})'.format(i.mid_interv, X, i.freq)
        result*=1/(N)
        self.calc_string += '='+str(result)
        return result

class DespSQuad(DespS):
    '''Расчет центрального момента четвертого порядка u4'''


    def calc(self, power):
        result = 0
        self.calc_string = 'u4=1/{}'.format(N)
        X = AvgX(ranges).x
        for i in self.ranges:
            result+=((i.mid_interv-X)**4)*i.freq
            self.calc_string+='*(({:.2f}-{:.2f})^4*{})'.format(i.mid_interv, X, i.freq)
        result*=1/(N)
        self.calc_string += '='+str(result)
        return result

class DespVibor(DespS):
    '''Расчет дисперсии выборки o по формуле (n/n-1)*O^2 ...'''

    def calc(self, power):
        result = 0
        self.calc_string = 'o^2=1/({}-1)'.format(N)
        X = AvgX(ranges).x
        for i in self.ranges:
            result+=((i.mid_interv-X)**2)*i.freq
            self.calc_string+='*(({:.2f}-{:.2f})^2*{})'.format(i.mid_interv, X, i.freq)
        result*=1/(N-1)
        self.calc_string += '='+str(result)
        result = sqrt(result)
        self.calc_string += '\no='+str(result)
        return result

class Async(DespS):
    '''Расчет параметров ассиметрии β по формуле As=u3/S^3'''


    def __init__(self, ranges):
        self.ranges = ranges
        self.As = self.calc()

    def calc(self):
        self.calc_string = 'As=u3/S^3'
        result = (DespSCube(ranges).s/(DespS(ranges, 3).s))
        self.calc_string += '='+str(result)
        return result

class Excess(DespS):
    '''Расчет эксцесса по формуле Ex=u4/S^4'''


    def __init__(self, ranges):
        self.ranges = ranges
        self.Ex = self.calc()

    def calc(self):
        self.calc_string = 'Ex=S^4/S^4'
        result = (DespSQuad(ranges).s/(DespS(ranges, 4).s))-3
        self.calc_string += '='+str(result)
        return result

class Pravilo3o:
    '''Правило 3o'''

    def __init__(self):
        self.calc()

    def calc(self):
        self.low_bound = AvgX(ranges).x-3*(DespVibor(ranges).s/sqrt(N))
        self.calc_string = '1){:.2f}-3({:.2f}/sqrt({}))={}'.format(AvgX(ranges).x, DespVibor(ranges).s, N, self.low_bound)
        self.higher_bound = AvgX(ranges).x+(DespVibor(ranges).s/sqrt(N))
        self.calc_string+='\n2){:.2f}+3({:.2f}/sqrt({}))={}'.format(AvgX(ranges).x, DespVibor(ranges).s, N, self.higher_bound)

    def __str__(self):
        return 'Строим по правилу 3 сигм доверительный интервал:\n{}\n{}<a<{} Это неравенство выполняется с вероятностью 0.9973'.format(self.calc_string,self.low_bound, self.higher_bound)

# генерируем список интервалов
ranges = []
lower_bound = MIN_X
for freq in FREQUENCY:
    interv = Interval(lower_bound, freq)
    lower_bound = interv.higher_bound
    ranges.append(interv)


def main():
    print('Часть А)')
    print(AvgX(ranges))
    print()
    print(DespS(ranges))
    print()
    print(DespVibor(ranges))
    print()
    print(DespSCube(ranges))
    print(Async(ranges))
    print()
    print(DespSQuad(ranges))
    print(Excess(ranges))
    print()
    print()
    print('Часть Б)')
    print()
    print(Pravilo3o())

if __name__ == '__main__':
    main()