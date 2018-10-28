from PIL import Image
import os


path='/home/alex/PycharmProjects/untitled/图片/'

list_file=os.listdir(path)

for i in list_file:

    file_path=path+os.sep+i
    if os.path.isdir(file_path):
        continue
    print('开始转换文件：'+str(i))
    im=Image.open(file_path)
    im.save(path+os.sep+'转换'+os.sep+i.split('.')[0]+'.gif')
    im.close()
    os.remove(file_path)
