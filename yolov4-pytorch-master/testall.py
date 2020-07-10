
from yolo import YOLO
from PIL import Image
import matplotlib.image as mpimg

yolo = YOLO()

#for fields in list: 
#  i=i+1;
file = open("name.txt","r")
list = file.readlines()
i=0

print(list[1])
#list = list.replace('\n', '')
for line in open("testall.txt"):
  i=i+1
  line = line.rstrip('\n')
  img = line
#    try:
  f = open('data.txt','a')
  list[i-1] = list[i-1].rstrip('\n')     
  f.writelines(['\n',str(list[i-1]),'.jpg'])  
  f.close() 
  image = Image.open(img)
#    except:
#        print('Open Error! Try again!')
#        continue
#    else:
  r_image = yolo.detect_image(image)
#  pre_savename = '/test/'
#  savename = os.path.join(pre_savename, line)
#  image.save('test/%d.jpg'%(i))
