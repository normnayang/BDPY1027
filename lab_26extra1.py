from lab13_immutable_dataset import courses
from pprint import pprint
import time
import multiprocessing

def transform(x):
    print('process record:{}'.format(x.name))
    time.sleep(3)
    result = {'name': x.name,'re'}