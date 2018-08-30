import os
import shutil


def mkdir():
    path = '/home/[PC]/data/SRAD2018_Test_1/'
    to_path = '/home/[PC]/data/result/'

    dir_list = os.listdir(path)

    for i in dir_list:
        os.mkdir(to_path+i)


def rmdir():
    path = '/home/[PC]/data/officalEnv/testData/'
    dirlist = checkdir()
    for i in dirlist:
        image_list = os.listdir(path+i+'/temp')
        image_list = sorted(image_list)
        for j in image_list[31:]:
            print(j)
            os.remove(path+i+'/temp/'+j)


def checkdir():
    path = '/home/[PC]/data/officalEnv/testData/'
    dir_list = os.listdir(path)
    empty_list = []
    print(dir_list)
    for dir in dir_list:
        # print(path)
        # print(dir)
        tem_list = os.listdir(path+dir+'/temp/')
        if len(tem_list) > 31:
            empty_list.append(dir)
    print(empty_list)
    return empty_list


def toAnotherDir():
    path = '/home/[PC]/data/officalEnv/testData/'
    to_path = '/home/[PC]/data/secondTest/'
    dir_list = os.listdir(path)
    locate = [4, 9, 14, 19, 24, 29]
    for dir in dir_list:
        tem_list = os.listdir(path+dir)
        tem_list = sorted(tem_list)
        j = 1
        for i in locate:
            print(path+dir+tem_list[i])
            shutil.copyfile(path+dir+'/'+tem_list[i], (to_path+'%s_f00%d.png'%(dir, j)))
            j += 1


def countDir():
    to_path = ''
    count = len(os.listdir(to_path))
    print(count)
