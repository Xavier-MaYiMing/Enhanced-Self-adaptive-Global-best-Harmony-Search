#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/9 9:50
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : ESGHS.py
# @Statement : Enhanced Self-adaptive Global-best Harmony Search
# @Reference : Kaiping Luo, Jie Ma, Qiuhong Zhao. Enhanced self-adaptive global-best harmony search without any extra statistic and external archive. Information Sciences, 2019. 482: 228-247.
import random
import math
import matplotlib.pyplot as plt


def obj(x):
    """
    The objective function of pressure vessel design
    :param x:
    :return:
    """
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    g1 = -x1 + 0.0193 * x3
    g2 = -x2 + 0.00954 * x3
    g3 = -math.pi * x3 ** 2 - 4 * math.pi * x3 ** 3 / 3 + 1296000
    g4 = x4 - 240
    if g1 <= 0 and g2 <= 0 and g3 <= 0 and g4 <= 0:
        return 0.6224 * x1 * x3 * x4 + 1.7781 * x2 * x3 ** 2 + 3.1661 * x1 ** 2 * x4 + 19.84 * x1 ** 2 * x3
    else:
        return 1e10


def main(hms, ni, lb, ub):
    """
    The main function of the ESGHS
    :param hms: harmony memory size
    :param ni: number of improvisations (iterations)
    :param lb: the lower bound (list)
    :param ub: the upper bound (list)
    :return:
    """
    # Step 1. Initialization
    pos = []  # the set of harmonies
    score = []  # the score of harmonies
    dim = len(lb)  # dimension
    for i in range(hms):
        temp_pos = [random.uniform(lb[j], ub[j]) for j in range(dim)]
        pos.append(temp_pos)
        score.append(obj(temp_pos))
    iter_best = []
    gbest = min(score)  # the score of the best-so-far harmony
    gbest_pos = pos[score.index(gbest)].copy()  # the best-so-far harmony
    con_iter = 0

    # Step 2. The main loop
    for t in range(ni):
        # Step 2.1. Set HMCR and PAR
        hmcr = (dim + random.normalvariate(0, 1)) / (dim + 1)  # harmony memory consideration rate
        par = 1 - t / ni  # pitch adjustment rate
        delta = 1 - (t / ni) ** 2  # the standard deviation used in the randomization selection
        new_pos = []

        # Step 2.2. Create a new harmony
        for i in range(dim):
            if random.random() < hmcr:
                ind1 = random.randint(0, hms - 1)
                new_pos.append(pos[ind1][i])
                if random.random() < par:  # pitch adjustment operation
                    ind2 = random.randint(0, hms - 1)
                    if pos[ind1][i] != pos[ind2][i]:
                        bw = abs(pos[ind1][i] - pos[ind2][i])  # bandwidth
                    else:
                        bw = (ub[i] - lb[i]) * math.exp(-(ub[i] - lb[i]) * (t + 1) / ni)
                    new_pos[i] += bw * random.uniform(-1, 1)
            else:  # randomization selection (Gaussian mutation)
                new_pos.append(random.normalvariate(gbest_pos[i], delta))
            if not lb[i] <= new_pos[i] <= ub[i]:  # boundary check
                new_pos[i] = random.uniform(lb[i], ub[i])

        # Step 2.3. Update harmony memory
        new_score = obj(new_pos)
        if new_score < max(score):
            ind = score.index(max(score))
            score.pop(ind)
            pos.pop(ind)
            score.append(new_score)
            pos.append(new_pos)
            if new_score < gbest:  # update global best
                gbest = new_score
                gbest_pos = new_pos.copy()
                con_iter = t + 1
        iter_best.append(gbest)

    # Step 3. Sort the results
    x = [i for i in range(ni)]
    plt.figure()
    plt.plot(x, iter_best, linewidth=2, color='blue')
    plt.xlabel('Iteration number')
    plt.ylabel('Global optimal value')
    plt.title('Convergence curve')
    plt.show()
    return {'best score': gbest, 'best solution': gbest_pos, 'convergence iteration': con_iter}


if __name__ == '__main__':
    # Parameter settings
    hms = 10
    lb = [0, 0, 10, 10]
    ub = [99, 99, 200, 200]
    ni = 10000 * len(lb)
    print(main(hms, ni, lb, ub))
