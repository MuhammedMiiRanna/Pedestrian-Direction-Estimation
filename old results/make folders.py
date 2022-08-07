from os import mkdir, chdir

""" This Script create 10 folders with the names from the angels list
    """


path = 'Script/PrespectiveFloor/result'
chdir(path)
angels = ['000', '018', '036', '054', '072',
          '090', '108', '126', '144', '162', '180']
for angel in angels:
    mkdir(angel)
