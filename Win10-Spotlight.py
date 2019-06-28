import os
import shutil
from PIL import Image
import getpass
import time

def copyFileto(sourceDir,  targetDir): 
    shutil.copy(sourceDir,  targetDir)

if __name__ == "__main__":
        
    user = getpass.getuser()
    # print (user)
    dir1 = r'C:\Users'
    dir2 = r'\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'
    wallpaper_dir = dir1 + '\\' + user + dir2
    temp_dir = 'temp'
    if os.path.exists(temp_dir):
        pass
    else:
        os.makedirs(temp_dir)

    for filename in os.listdir(wallpaper_dir):
        source = wallpaper_dir+'\\'+filename
        
        img = Image.open(source)
        imgSize = img.size  #图片尺寸
        w = img.width   #图片的宽
        h = img.height  #图片的高
        f = img.format  #图像格式
        target = temp_dir+'\\'+str(w)+'x'+str(h)+'_'+filename+'.'+f
        print(imgSize,f,filename)
        copyFileto(source,target)