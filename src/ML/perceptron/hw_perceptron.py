# encoding=utf-8
# @Author: WenDesi
# @Date:   09-08-16
# @Email:  wendesi@foxmail.com
# @Last modified by:   WenDesi
# @Last modified time: 08-11-16
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import time

from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

from binary_perceptron import Perceptron

import matplotlib.pyplot as plt


def hw_15():
    print 'Start read data'

    time_1 = time.time()
    raw_data = np.loadtxt("../data/perceptron/hw1_15_train.dat")
    # raw_data = pd.read_csv('../data/train_binary.csv', header=0)
    # data = raw_data.values

    data = raw_data[0:, 0:-1]
    labels = raw_data[:, -1]

    # plt.plot(raw_data[0::, 0::])

    # 选取 2/3 数据作为训练集， 1/3 数据作为测试集
    train_features, test_features, train_labels, test_labels = train_test_split(
        data, labels, test_size=0.2, random_state=23323)
    # print train_features.shape
    # print train_features.shape

    time_2 = time.time()
    print 'read data cost ', time_2 - time_1, ' second', '\n'

    print 'Start training'
    p = Perceptron(True)
    p.train(train_features, train_labels)

    time_3 = time.time()
    print 'training cost ', time_3 - time_2, ' second', '\n'

    print 'Start predicting'
    test_predict = p.predict(test_features, True)
    time_4 = time.time()
    print 'predicting cost ', time_4 - time_3, ' second', '\n'

    score = accuracy_score(test_labels, test_predict)
    print p.pocket_w
    print test_labels
    print test_predict
    print "The accruacy socre is ", score


def hw_18():
    print 'Start read data'

    time_1 = time.time()
    train = np.loadtxt("../data/perceptron/hw1_18_train.dat")
    test = np.loadtxt("../data/perceptron/hw1_18_test.dat")
    # raw_data = pd.read_csv('../data/train_binary.csv', header=0)
    # data = raw_data.values

    train_features = train[:, :-1]
    train_labels = train[:, -1]

    test_features = test[0:, :-1]
    test_labels = test[:, -1]

    time_2 = time.time()
    print 'read data cost ', time_2 - time_1, ' second', '\n'

    print 'Start training'
    p = Perceptron(True)
    p.train(train_features, train_labels)

    time_3 = time.time()
    print 'training cost ', time_3 - time_2, ' second', '\n'

    print 'Start predicting'
    test_predict = p.predict(test_features, True)
    time_4 = time.time()
    print 'predicting cost ', time_4 - time_3, ' second', '\n'

    score = accuracy_score(test_labels, test_predict)
    print test_labels
    print test_predict
    print "The accruacy socre is ", score


def plot_data():
    train = np.loadtxt("../data/perceptron/hw1_18_train.dat")
    test = np.loadtxt("../data/perceptron/hw1_18_test.dat")
    print train
    print np.where(train[:, -1] == -1)
    print train[np.where(train[:, -1] == -1), 0]

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    plt.scatter(train[np.where(train[:, -1] == 1), 0], train[np.where(train[:, -1] == 1), 1],
                train[np.where(train[:, -1] == 1), 3], color='green')
    plt.scatter(train[np.where(train[:, -1] == -1), 0], train[np.where(train[:, -1] == -1), 1],
                train[np.where(train[:, -1] == -1), 3], color='red')
    plt.show()


if __name__ == '__main__':
    # hw_15()
    hw_18()
    # plot_data()