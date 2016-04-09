from math import sqrt
MIN_X = -1.7 #Нижняя граница
FREQUENCY = [4, 6, 8, 10, 8, 2] #Список частот
STEP = 0.7 #Шаг
VER_95 = 2.0452 #Посмотреть значения коэфиц Стьюдента по таблице
VER_99 = 2.7564 #Посмотреть значения коэфиц Стьюдента по таблице

#test_data
#MIN_X = 2.9
#FREQUENCY = [3, 5 ,14, 6, 2]
#STEP = 1

#MIN_X = -5.0
#FREQUENCY = [4,6,10,8,5,3]
#STEP = 1.4


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

class GeneralClass:

    def __init__(self, ranges):
        self.ranges = ranges
        self.res = self.calc()
        self.annotation = self.__doc__

    def calc(self):
        raise NotImplemented

    def __str__(self):
        return self.annotation +'\n' + self.calc_string

class AvgX(GeneralClass):
    '''Расчет среднего выборочного X(ȧ)'''

    def __init__(self, ranges):
        self.ranges = ranges
        self.res = self.calc()
        self.annotation = 'Расчет математического ожидания X(ȧ)'

    def calc(self):
        result=0
        self.calc_string = 'X=1/{}'.format(N)
        for i in self.ranges:
            result+=i.mid_interv*i.freq
            self.calc_string+='*({:.2f}*{})'.format(i.mid_interv, i.freq)
        result*=1/N
        #print(avg_x.__doc__)
        self.calc_string+='='+str(result)
        return result

class DespS(GeneralClass):
    '''Расчет среднеквадратичного S'''

    def __init__(self, ranges, power=2):
        self.ranges = ranges
        self.res = self.calc(power)
        self.annotation = 'Расчет среднеквадратичного отклониения S и дисперсии S^2'.format(power)

    def calc(self, power):
        result = 0
        self.calc_string = 'S^2=1/{}'.format(N)
        X = AvgX(ranges).res
        for i in self.ranges:
            result+=((i.mid_interv-X)**2)*i.freq
            self.calc_string+='*(({:.2f}-{:.2f})^2*{})'.format(i.mid_interv, X, i.freq)
        result*=1/(N)
        self.calc_string += '='+str(result)
        self.calc_string += '\nS='+str(sqrt(result))
        result = sqrt(result)**power
        return result

class DespSCube(GeneralClass):
    '''Расчет центрального момента третьего порядка u3'''


    def calc(self):
        result = 0
        self.calc_string = 'u3=1/{}'.format(N)
        X = AvgX(ranges).res
        for i in self.ranges:
            result+=((i.mid_interv-X)**3)*i.freq
            self.calc_string+='*(({:.2f}-{:.2f})^3*{})'.format(i.mid_interv, X, i.freq)
        result*=1/(N)
        self.calc_string += '='+str(result)
        return result

class DespSQuad(GeneralClass):
    '''Расчет центрального момента четвертого порядка u4'''


    def calc(self):
        result = 0
        self.calc_string = 'u4=1/{}'.format(N)
        X = AvgX(ranges).res
        for i in self.ranges:
            result+=((i.mid_interv-X)**4)*i.freq
            self.calc_string+='*(({:.2f}-{:.2f})^4*{})'.format(i.mid_interv, X, i.freq)
        result*=1/(N)
        self.calc_string += '='+str(result)
        return result

class DespVibor(GeneralClass):
    '''Расчет стандартного отклонения по формуле O = sqrt(n/n-1)*S^2 ...'''

    def calc(self):
        result = 0
        self.calc_string = 'o^2=1/({}-1)'.format(N)
        X = AvgX(ranges).res
        for i in self.ranges:
            result+=((i.mid_interv-X)**2)*i.freq
            self.calc_string+='*(({:.2f}-{:.2f})^2*{})'.format(i.mid_interv, X, i.freq)
        result*=1/(N-1)
        self.calc_string += '='+str(result)
        result = sqrt(result)
        self.calc_string += '\no='+str(result)
        return result

class Async(GeneralClass):
    '''Расчет параметров ассиметрии β по формуле As=u3/S^3'''


    def __init__(self, ranges):
        self.ranges = ranges
        self.res = self.calc()
        self.annotation = 'Расчет параметров ассиметрии β по формуле As=u3/S^3'

    def calc(self):
        self.calc_string = 'As=u3/S^3'
        result = (DespSCube(ranges).res/(DespS(ranges, 3).res))
        self.calc_string += '='+str(result)
        return result

class Excess(GeneralClass):
    '''Расчет эксцесса по формуле Ex=u4/S^4'''


    def __init__(self, ranges):
        self.ranges = ranges
        self.res = self.calc()
        self.annotation = 'Расчет эксцесса по формуле Ex=u4/S^4'

    def calc(self):
        self.calc_string = 'Ex=S^4/S^4'
        result = (DespSQuad(ranges).res/(DespS(ranges, 4).res))-3
        self.calc_string += '='+str(result)
        return result

class Pravilo3o:
    '''Правило 3o'''

    def __init__(self):
        self.calc()

    def calc(self):
        self.low_bound = AvgX(ranges).res-3*(DespVibor(ranges).res/sqrt(N))
        self.calc_string = '1){:.2f}-3({:.2f}/sqrt({}))={}'.format(AvgX(ranges).res, DespVibor(ranges).res, N, self.low_bound)
        self.higher_bound = AvgX(ranges).res+(DespVibor(ranges).res/sqrt(N))
        self.calc_string+='\n2){:.2f}+3({:.2f}/sqrt({}))={}'.format(AvgX(ranges).res, DespVibor(ranges).res, N, self.higher_bound)

    def __str__(self):
        return 'Строим по правилу 3 сигм доверительный интервал:\n{}\n{}<a<{} Это неравенство выполняется с вероятностью 0.9973'.format(self.calc_string,self.low_bound, self.higher_bound)


class DoverInterv(GeneralClass):

    def __init__(self, ver, coff):
        self.calc(ver, coff)
        self.annotation = 'Ищем доверительный интервал для вероятности {}'.format(ver)

    def calc(self, ver, coff):
        self.calc_string = 'X-t*(o/sqrt(N))<a<X+t*(o/sqrt(N))\n'
        self.calc_string += '{0}-{1}*({2}/sqrt({3}))<a<{0}+{1}*({2}/sqrt({3}))\n'.format(AvgX(ranges).res, coff, DespVibor(ranges).res, N)
        self.low_bound = AvgX(ranges).res-coff*(DespVibor(ranges).res/sqrt(N))
        self.higher_bound = AvgX(ranges).res+coff*(DespVibor(ranges).res/sqrt(N))
        self.calc_string += '{}<a<{}'.format(self.low_bound, self.higher_bound)


# генерируем список интервалов
ranges = []
lower_bound = MIN_X
for freq in FREQUENCY:
    interv = Interval(lower_bound, freq)
    lower_bound = interv.higher_bound
    ranges.append(interv)


def main():
    print('Часть А)')
    print(AvgX(ranges)) # Находим Х
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
    print(DoverInterv('99', VER_99))
    print(DoverInterv('95', VER_95))


if __name__ == '__main__':
    main()
    assert AvgX(ranges).res == 5.366666666666667 #X
    assert DespVibor(ranges).res == 1.0333518722845685
    assert Excess(ranges).res == -0.17582710439017246
    assert Async(ranges).res == -0.12403119735284537
