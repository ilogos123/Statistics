from collections import Counter


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
