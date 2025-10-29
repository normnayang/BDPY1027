import csv

sampleFile = open('data/lab50.csv')
sampleFileReader = csv.reader(sampleFile)
sampleFileData = list(sampleFileReader)
sampleFile.close()
print(type(sampleFileData))
for row in sampleFileData:
    print(row)
    for col in row :
        print(col)