import math
from itertools import combinations
from random import sample
import numpy as np
from scipy import stats
import pandas as pd

class WEAT:
    def __init__(self, word2vec, X, Y, A, B, steps=-1, effect_size_n=-1):
        self.word2vec = word2vec
        if len(X) != len(Y):
            #print('Warning: len(X) ==', len(X), '!= len(Y) ==', len(Y), ' only considering first', min(len(X), len(Y)), 'elements.')
            pass
        self.X = X[:len(Y)]
        self.Y = Y[:len(X)]
        self.A = A
        self.B = B
        self.steps = steps
        self.effect_size_n = effect_size_n
        self.a = np.mean([word2vec[a] / np.linalg.norm(word2vec[a]) for a in A], axis=0)
        self.b = np.mean([word2vec[b] / np.linalg.norm(word2vec[b]) for b in B], axis=0)
        self.s = {}
        for w in self.X + self.Y:
            wn = word2vec[w] / np.linalg.norm(word2vec[w])
            self.s[w] = np.dot(wn, self.a - self.b)
        self.p_val = self.p()
        self.effect_size_val = self.effect_size()

    def get_p(self):
        return self.p_val

    def get_effect_size(self):
        return self.get_effect_size

    def get_stats(self):
        return self.p_val, self.effect_size_val

    def statistic(self, X, Y):
        return np.sum([self.s[x] for x in X]) - np.sum([self.s[y] for y in Y])

    def p(self):
        base_statistic = self.statistic(self.X, self.Y)
        total = 0
        larger = 1
        if self.steps == -1:
            iterator = combinations(self.X + self.Y, len(self.X + self.Y) // 2)
        else:
            iterator = [sample(self.X + self.Y, len(self.X + self.Y) // 2) for _ in range(self.steps)]
        for Xi in iterator:
            Yi = [y for y in self.X + self.Y if not y in Xi]
            total += 1
            if self.statistic(Xi, Yi) > base_statistic:
                larger += 1
        return larger / total

    def effect_size(self):
        if self.effect_size_n > len(self.word2vec.keys()) or self.effect_size_n == -1:
            std_words = list(self.word2vec.keys())
        else:
            std_words = sample(self.word2vec.keys(), self.effect_size_n)
        std_wns = np.array([self.word2vec[w] for w in std_words])
        std_wns = std_wns / np.linalg.norm(std_wns, axis=1, keepdims=True)
        std_ss = np.matmul(std_wns, self.a) - np.matmul(std_wns, self.b)
        return (np.mean([self.s[x] for x in self.X]) - np.mean([self.s[y] for y in self.Y])) / np.std(std_ss)

class WEATvec:
    def __init__(self, word2vec, X, Y, A, B, steps=-1, effect_size_n=-1):
        self.word2vec = word2vec
        if len(X) != len(Y):
            #print('Warning: len(X) ==', len(X), '!= len(Y) ==', len(Y), ' only considering first', min(len(X), len(Y)), 'elements.')
            pass
        self.X = X[:len(Y)]
        self.Y = Y[:len(X)]
        self.A = A
        self.B = B
        self.steps = steps
        self.effect_size_n = effect_size_n
        self.a = np.mean([word2vec[a] for a in A], axis=0)
        self.b = np.mean([word2vec[b] for b in B], axis=0)
        self.s = {}
        for w in self.X + self.Y:
            self.s[w] = np.dot(self.word2vec[w], self.a - self.b)
        self.p_val = self.p()
        self.effect_size_val = self.effect_size()

    def get_p(self):
        return self.p_val

    def get_effect_size(self):
        return self.get_effect_size

    def get_stats(self):
        return self.p_val, self.effect_size_val

    def statistic(self, X, Y):
        return np.sum([self.s[x] for x in X]) - np.sum([self.s[y] for y in Y])

    def p(self):
        base_statistic = self.statistic(self.X, self.Y)
        total = 0
        larger = 1
        if self.steps == -1 or self.steps >= math.factorial(2 * len(self.X)) / (math.factorial(len(self.X)) ** 2):
            iterator = combinations(self.X + self.Y, len(self.X))
        else:
            iterator = [sample(self.X + self.Y, len(self.X + self.Y) // 2) for _ in range(self.steps)]
        for Xi in iterator:
            Yi = [y for y in self.X + self.Y if not y in Xi]
            total += 1
            if self.statistic(Xi, Yi) > base_statistic:
                larger += 1
        return larger / total

    def effect_size(self):
        if self.effect_size_n > len(self.word2vec.keys()) or self.effect_size_n == -1:
            std_words = list(self.word2vec.keys())
        else:
            std_words = sample(self.word2vec.keys(), self.effect_size_n)
        std_wns = np.array([self.word2vec[w] for w in std_words])
        std_ss = np.matmul(std_wns, self.a) - np.matmul(std_wns, self.b)
        return (np.mean([self.s[x] for x in self.X]) - np.mean([self.s[y] for y in self.Y])) / np.std(std_ss)

def weat_analysis(combined_word2vecs, quadruples, all_sets, steps=-1, effect_size_n=-1):
    if type(quadruples) == tuple:
        quadruples = [quadruples]
    print('This might take some time')
    res = []
    total = len(quadruples) * sum([len(combined_word2vecs[key]) for key in combined_word2vecs])
    counter = 0
    for names in quadruples:
        sets = [all_sets[name] for name in names]
        for wiki in combined_word2vecs:
            ps = []
            ds = []
            ps2 = []
            ds2 = []
            for word2vec in combined_word2vecs[wiki]:
                p, d = WEAT(word2vec, sets[0], sets[1], sets[2], sets[3], steps, effect_size_n=effect_size_n).get_stats()
                ps.append(p)
                ds.append(d)
                p, d = WEATvec(word2vec, sets[0], sets[1], sets[2], sets[3], steps, effect_size_n=effect_size_n).get_stats()
                ps2.append(p)
                ds2.append(d)
                counter += 1
                if counter % 25 == 0:
                    print('Finished', counter, 'of', total)
            res.append((names, wiki, ps, stats.combine_pvalues(ps, 'fisher')[1], ds, np.mean(ds), np.std(ds), ps2, stats.combine_pvalues(ps2, 'fisher')[1], ds2, np.mean(ds2), np.std(ds2)))
    print('Done!')
    return pd.DataFrame(res, columns=['names', 'wiki', 'p', 'fishers_p', 'd', 'mean_d', 'std_d', 'p2', 'fishers_p2', 'd2', 'mean_d2', 'std_d2'])