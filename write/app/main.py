import os
from pathlib import Path
from settings import DATAFOLDER
from settings import FILENAME

def write():

    datapath = os.path.join(Path(__file__).parents[1], DATAFOLDER)
    Path(datapath).mkdir(parents=True, exist_ok=True)


    print('DATAFOLDER contains', os.listdir(datapath))
    with open(os.path.join(datapath, FILENAME+'.txt'), 'w') as f:
        f.write('Hello World')

    print('written {f}'.format(f=FILENAME))

    print('DATAFOLDER contains', os.listdir(datapath))

if __name__ == '__main__':

    write()