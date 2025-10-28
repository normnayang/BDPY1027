import os,sys
import time
DIR1 = "temp"
print(os.getcwd())
os.mkdir(DIR1)
os.chdir(DIR1)
print(os.getcwd())
time.sleep(2)
print("Done")
