import os

saveRoad='.//data_saveResult'



def get_saveRoad_absPath(name):
    return os.path.abspath(os.path.join(saveRoad,name+'.json'))