# arg 1 old string, arg 2 new string , arg 3 path
import os 
import sys

print('from ', sys.argv[1],' to ', sys.argv[2])
toold = sys.argv[1]
tonew = sys.argv[2]

counter = 0
path = os.getcwd() + "\\"+sys.argv[3]
print('path to use', path)
for file in os.listdir(path):    
    if file.find(toold) > -1:
        counter = counter + 1
        print(file)
        f = open(os.path.join(path, file),'r',encoding='utf-8')
        filedata = f.read()
        f.close()

        newFile = filedata.replace(toold, tonew)
        
        f = open(os.path.join(path, file), 'w', encoding='utf-8')
        f.write(newFile)
        f.close()

        os.rename(os.path.join(path, file), os.path.join(path, file.replace(toold, tonew)))
if counter == 0:
    print("files not found")
else :
    print("done ", counter)
