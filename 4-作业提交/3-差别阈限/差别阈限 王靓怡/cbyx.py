from PIL import Image
from pylab import *
work_dir = "C:\Users\sanxing\Desktop\Inquisite experiments\"
#ת���ɾ���
im = array(Image.open("C:\Users\sanxing\Desktop\Inquisite experiments\pyt.jpg").convert('L'))
#���ɻҶ�ͼ
im1 = Image.fromarray(uint8(im))
im1.save(work_dir+"grey.bmp")
#���ɲ�ͬ�ҶȲ����ͼ
for i in range(0, 255, 32):
    image = (i/255)*im
    out = Image.fromarray(uint8(image))
    ii = 8-i/32
    out.save(work_dir+str(ii)+".bmp")