import os,sys
import time
DIR1 = "temp暫存"
print(os.getcwd())
os.mkdir(DIR1)
os.chdir(DIR1)
print(os.getcwd())
time.sleep(2)
os.chdir("..")
os.rmdir(DIR1)
print("Done")
