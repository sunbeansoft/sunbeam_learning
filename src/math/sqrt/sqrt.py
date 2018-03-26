# encoding=utf-8

import math


class RootNum:
    def newton(self, n):

        result = 1.0
        eps = 0.00001
        tmp = result * result - n

        times = 0
        while math.fabs(tmp) > eps:
            result = 0.5 * (result + (n / result))
            tmp = result * result - n
            times += 1
            print result
        return result, times

    def bin(self, n):
        start = 0
        end = n / 2.0
        result = n / 2.0
        eps = 0.00001

        tmp = result * result - n

        times = 0

        if (tmp < eps):
            return result

        while math.fabs(tmp) > eps:
            times += 1
            if tmp > 0:
                end = result
                result = (start + result) / 2
            else:
                start = result
                result = (result + end) / 2
            tmp = result * result - n
            print result

        return result, times


if __name__ == '__main__':
    n = 5
    root_num = RootNum()
    result, times = root_num.bin(n)
    print("bin is: " + str(result) + "-" + str(times))

    result, times = root_num.newton(n)
    print("bin is: " + str(result) + "-" + str(times))
