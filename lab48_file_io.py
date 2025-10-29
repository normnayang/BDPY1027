file = open('data/Python_Introduction','r',encoding='utf-8')
#print(file.read())
data = file.read()
print(data)
file.close()
print("********************************")
with open('data/Python_Introduction','r',encoding='utf-8') as file2 :
    data2 = file2.read()
    print(data2)

file3 = open('data/clone1','w',encoding='utf-8')
file3.write(data)
file3.close()

with open('data/clone2','w',encoding='utf8') as file4:
    file4.write(data)