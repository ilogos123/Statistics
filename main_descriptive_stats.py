from collections import Counter
from playStats.descriptive_stats import frequency
if __name__ == '__main__':
    # 测试频率
    data = [2, 2, 2, 2, 1, 1, 1, 3, 3]
    print(frequency(data))
