from shutil import copytree, rmtree

DIR1 = "temp"
DIR2 = "backup"

copytree(DIR1,DIR2)
rmtree(DIR1)