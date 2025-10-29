import csv
sampleFile = open('data/lab50_2.csv',encoding='utf-8-sig')
sampleFileReader = csv.reader(sampleFile)
sampleFileData =dict(sampleFileReader)
sampleFile.close()
print(sampleFileData)