from models import model
import numpy as np
import pandas as pd
import os
from .utils.utils import generatePic


class loadData():
    def __int__(self, file_path, dumps_path):
        self.file_path = file_path
        self.dumps_path = dumps_path

    def pixel_load(self, image, x, y):
        pixel = image[x][y][0]
        return int(pixel)

    def truncate_image(self, path):
        point_list = {}
        dir_list = os.listdir(path)
        locate = 11
        rate = 50

        for x in range(locate):
            for y in range(locate):
                point_list['x%dy%d' % (x*rate, y*rate)] = []

        for dir in dir_list:
            print('begin load dir:', dir)
            image_list = os.listdir(path+dir)
            image_list = sorted(image_list)
            for image_path in image_list:
                image = imread(path+dir+'/'+image_path)
                print(path+dir+'/'+image_path)
                for x in range(locate):
                    for y in range(locate):
                        point_list['x%dy%d' % (x*rate, y*rate)].append(self.pixel_load(image, x*rate, y*rate))
        return point_list

    def run(self, file_path, dumps_path):
        data = self.truncate_image(file_path)
        with open(dumps_path, 'w+') as f:
            json.dump(data, f)
            print('Finish...')


if __name__ == '__main__':
    m = model()
    trainData_path = '/home/[PC]/data/officalEnv/stackData/stackData.csv'
    trainData = pd.read_csv(trainData_path, index_col=0)
    m.trainModel(trainData[trainData.columns[:-1]], trainData[trainData.columns[-1]])
    testData_path = '/home/[PC]/data/officalEnv/testData/'
    dir_list = os.listdir(testData_path)
    residue = len(dir_list)

    for dir in dir_list:
        print('begin dir:', dir)
        current = 0
        while current < 31:
            data_list = os.listdir(testData_path+dir+'/temp/')
            data_list = sorted(data_list)
            data = []
            for i in data_list[current:]:
                data_tem = np.load(testData_path+dir+'/temp/'+i)
                data.append(data_tem)
            print(i)
            current += 1
            test_x = np.stack(data, axis=1)
            pred = m.predict(test_x)
            pred[pred>250] = 255
            pred = pred.astype(np.uint8)
            # print(pred)
            np.save(testData_path+dir+'/temp/'+'%s_0%d.png'%(dir, current+31), pred)
            generatePic(pred, (testData_path+dir+'/'+'%s_0%d.png'%(dir, current+31)))
        print('%s finished, %d residue' % (dir, residue))
        residue -= 1


