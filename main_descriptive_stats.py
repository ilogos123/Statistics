from collections import Counter
from playStats.descriptive_stats import frequency
from playStats.descriptive_stats import mode
from playStats.descriptive_stats import median

if __name__ == '__main__':
    data = [2, 2, 2, 1, 1, 1, 3, 3]

    # 测试频率
    print(frequency(data))

    # 测试众数
    print(mode(data))

    # 测试中位数
    print(median(data))


