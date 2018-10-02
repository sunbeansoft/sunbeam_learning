# encoding=utf-8
# @Author: WenDesi
# @Date:   09-08-16
# @Email:  wendesi@foxmail.com
# @Last modified by:   WenDesi
# @Last modified time: 08-11-16


import pandas as pd
import numpy as np
# import cv2
import random
import time
import copy

from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score


class Perceptron(object):

    def __init__(self, pocket=False):
        self.learning_step = 0.00001
        self.max_iteration = 5000
        self.pocket = pocket

    def predict_(self, x, pocket=False):
        if pocket:
            wx = sum([self.pocket_w[j] * x[j] for j in xrange(len(self.pocket_w))])
        else:
            wx = sum([self.w[j] * x[j] for j in xrange(len(self.w))])
        return np.where(wx > 0, 1, -1).take(0)

    def train(self, features, labels):

        self.w = [0.0] * (len(features[0]) + 1)

        if self.pocket:
            self.pocket_w = [0.0] * (len(features[0]) + 1)

        correct_count = 0
        time = 0
        best = 0.0

        while time < self.max_iteration:
            index = random.randint(0, len(labels) - 1)
            x = list(features[index])
            x.append(1.0)
            y = 2 * labels[index] - 1
            wx = sum([self.w[j] * x[j] for j in xrange(len(self.w))])

            if wx * y > 0:
                correct_count += 1
                if correct_count > self.max_iteration:
                    break
                continue

            for i in xrange(len(self.w)):
                self.w[i] += self.learning_step * (y * x[i])

            if self.pocket:
                test_predict = self.predict(features)
                score = accuracy_score(labels, test_predict)
                if score > best:
                    print "The accruacy socre is ---", score
                    best = score
                    print self.w
                    self.pocket_w = copy.deepcopy(self.w)

    def predict(self, features, pocket=False):
        labels = []
        for feature in features:
            x = list(feature)
            x.append(1)
            labels.append(self.predict_(x, pocket))
        return labels


if __name__ == '__main__':
    print 'Start read data'

    time_1 = time.time()

    raw_data = pd.read_csv('../data/train_binary.csv', header=0)
    data = raw_data.values

    imgs = data[0::, 1::]
    labels = data[::, 0]

    # 选取 2/3 数据作为训练集， 1/3 数据作为测试集
    train_features, test_features, train_labels, test_labels = train_test_split(
        imgs, labels, test_size=0.33, random_state=23323)
    # print train_features.shape
    # print train_features.shape

    time_2 = time.time()
    print 'read data cost ', time_2 - time_1, ' second', '\n'

    print 'Start training'
    p = Perceptron()
    p.train(train_features, train_labels)

    time_3 = time.time()
    print 'training cost ', time_3 - time_2, ' second', '\n'

    print 'Start predicting'
    test_predict = p.predict(test_features)
    time_4 = time.time()
    print 'predicting cost ', time_4 - time_3, ' second', '\n'

    score = accuracy_score(test_labels, test_predict)
    print "The accruacy socre is ", score
