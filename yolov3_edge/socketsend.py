import socket

import cv2

import numpy

import time

  

def Sendimg(img):
    print(img.shape)
    #建立sock连接

    #address要连接的服务器IP地址和端口号

    address = ('140.118.122.36', 8002)

    try:

        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        #开启连接

        sock.connect(address)

    except socket.error as msg:

        print(msg)

        sys.exit(1)

    #压缩参数，后面cv2.imencode将会用到，对于jpeg来说，15代表图像质量，越高代表图像质量越好为 0-100，默认95

    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),15]

    result, imgencode = cv2.imencode('.jpg', img, encode_param)


    data = numpy.array(imgencode)
    stringData = data.tostring()
 
    #ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串

    sock.send(str.encode(str(len(stringData)).ljust(16)))
    #发送数据
    sock.sendall(stringData)
    sock.close()
       
    #读取下一帧图片

    

if __name__ == '__main__':

    Sendimg()
