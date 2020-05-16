from collections import Counter
from math import sqrt


def frequency(data):
    """频率"""
    counter = Counter(data)
    ret = []
    for point in counter.most_common():
        ret.append((point[0], point[1] / len(data)))
    return ret


def mode(data):
    """寻找众数"""
    counter = Counter(data)
    counter_data = counter.most_common()

    if counter_data[0][1] == 1:
        return None, None

    ret = []
    count = counter_data[0][1]
    for point in counter_data:
        if point[1] == count:
            ret.append(point[0])
        else:
            break
    return ret, count


def median(data):
    """中位数"""
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 1:
        return sorted_data[n // 2]

    return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2


def mean(data):
    """均值"""
    return sum(data) / len(data)


def rng(data):
    """极差"""
    return max(data) - min(data)


def quartile(data):
    """四分位数"""
    n = len(data)
    q1, q2, q3 = None, None, None

    if n >= 4:
        sorted_data = sorted(data)
        q2 = median(data)

        if n % 2 == 1:
            q1 = median(sorted_data[:n // 2])
            q3 = median(sorted_data[n // 2 + 1:])
        else:
            q1 = median(sorted_data[:n // 2 - 1])
            q3 = median(sorted_data[n // 2:])

    return q1, q2, q3


def variance(data):
    """方差"""
    n = len(data)
    if n <= 1:
        return None

    mean_value = mean(data)

    # 如果拿到的数据是
    #   全部样本，方差除以n
    #   部分样本，方差除以n-1
    return sum((e - mean_value) ** 2 for e in data) / (n - 1)


def std(data):
    """标准差"""
    return sqrt(variance(data))
