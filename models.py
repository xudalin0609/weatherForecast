import json
from sklearn.ensemble import GradientBoostingRegressor, AdaBoostRegressor, BaggingRegressor
from sklearn.tree import ExtraTreeRegressor
from sklearn.svm import SVR
import numpy as np
import matplotlib.pyplot as plt


class model():

    def __init__(self):
        self.model1 = None
        self.model2 = None

    def trainModel(self, train_x, train_y):
        print('begin train model1')
        model1 = self.AdaBoostModel(train_x, train_y)
        train_y_tem = model1.predict(train_x)
        train_y_tem = np.array(train_y_tem).reshape(-1, 1)
        print('begin train model2')
        model2 = self.ExtraTreesModel(train_y_tem, train_y)
        self.model1 = model1
        self.model2 = model2

    def GBTsModel(self, train_x, train_y):
        print('begin train GBTs')
        model = GradientBoostingRegressor()
        model.fit(train_x, train_y)
        return model

    def ExtraTreesModel(self, train_x, train_y):
        print('begin train ExtraTrees')
        model = ExtraTreeRegressor()
        model.fit(train_x, train_y)
        return model

    def SVRModel(self, train_x, train_y):
        model = SVR(kernel='linear')
        model.fit(train_x, train_y)
        return model

    def AdaBoostModel(self, train_x, train_y):
        print('begin train model 2')
        model = AdaBoostRegressor()
        model.fit(train_x, train_y)
        return model

    def predict(self, x):
        print('begin predict')
        pred_tem = self.model1.predict(x)
        pred_tem = np.array(pred_tem).reshape(-1, 1)
        pred = self.model2.predict(pred_tem)
        return pred

    def virsualDiff(self, pred, test_y):
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        colors = ['r', 'g', 'b']
        j = 0
        test_y = test_y.tolist()
        ax.scatter([i for i in range(len(pred))], pred, c=colors[j])
        ax.scatter([i for i in range(len(pred))], test_y, c='c')
        s = 0
        for i in range(len(pred)):
            a = int(float(pred[i])-float(test_y[i]))
            if a > 0:
                pass
            else:
                a = -a
            if a > 1 or a < -1:
                print('pred %d is %d test_y is %d' % (i, pred[i], test_y[i]))
                s += a
        print(s)
        plt.show()
