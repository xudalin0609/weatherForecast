from scipy.misc import imsave
import numpy as np
import os
import json


def generatePic(data, path):
    # data[data < 1] = 0
    data[data == 0] = 255
    data = data.reshape(501, 501)
    image = np.stack((data, data, data), axis=2)
    imsave(path, image)


def generatePoint(data, locate):
    point_list = []
    while len(data[locate]) > 31:
        for i in range(32):
            point_list.append(data[locate][i:i+32])
        data[locate] = data[locate][i+32:]
    return point_list


def generateFile():
    with open('/home/[PC]/data/officalEnv/trainData/RAD_Train_data.json', 'r') as f:
        data = json.loads(f.read())
    for locate in data.keys():
        with open('/home/[PC]/data/officalEnv/points/%s' % (locate), 'w+') as f:
            print('begin:', locate)
            pixels = generatePoint(data, locate)
            json.dump(pixels, f)
        print(locate)


def getTrainData():
    points_path = '/home/[PC]/data/officalEnv/points'
    points_list = os.listdir(points_path)
    stack_data = ''
    i = 0
    for point in points_list[10:30]:
        print('begin to stack point, ', point)
        with open(points_path+'/'+point, 'r+') as f:
            data = json.loads(f.read())
        if isinstance(stack_data, str):
            stack_data = pd.DataFrame(data)
        else:
            df_tem = pd.DataFrame(data)
            stack_data = pd.concat([stack_data, df_tem])
        i += 1
    return stack_data


class testloadData():
    def __int__(self, file_path, dumps_path):
        self.file_path = file_path
        self.dumps_path = dumps_path

    def image_load(self, test_load_path, test_dumps_path):
        dir_list = os.listdir(test_load_path)
        for dir in dir_list:
            image_list = os.listdir(test_load_path+dir)
            for i in image_list:
                if not os.path.exists(test_dumps_path + dir + '/temp/' + i):
                    print('dir %s:%s' %(dir, i))
                    image = imread(test_load_path+dir+'/'+i)
                    image = np.split(image, 3, axis=2)[0].flatten()
                    np.save(test_dumps_path + dir + '/temp/' + i, image)
                else:
                    continue