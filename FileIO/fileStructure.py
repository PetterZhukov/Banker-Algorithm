import os

saveRoad='.//data_saveResult'



def get_saveRoad_absPath(name):
    'ret 位置 + name + 后缀'
    return os.path.abspath(os.path.join(saveRoad,name+'.json'))