from PIL import Image
import numpy as np


def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1

    return chr(decimal)

def decrypt(pix):
    st = ''
    c=0
    for i in pix:
        c+=1
        if i%2 != 0 and c%9==0:
            break
        elif i%2 == 0 and c%9==0:
            st+=' '
        elif i%2 ==0:
            st+='0'
        elif i%2 !=0:
            st+='1'
    return st

if __name__ == '__main__':
    image_path = input('Please Enter Image Name:')
    im = Image.open(image_path)

    x,y = list(im.size)
    rgb = np.asarray(im).reshape(-1)

    new_img = np.array(rgb)
    de = decrypt(new_img)

    de_array = de.split(' ')

    final_masg =  ''

    for i in de_array:
        final_masg+=binaryToDecimal(int(i))

    print('Massage:',final_masg)