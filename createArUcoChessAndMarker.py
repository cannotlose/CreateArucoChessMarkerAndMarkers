
import cv2
import numpy as np
from cv2 import aruco


dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
board = cv2.aruco.CharucoBoard_create(8,8,.025,.0125,dictionary)
BigImage = board.draw((150*8,150*8))


cv2.imwrite('charuco.png',BigImage)

print (BigImage.shape)

BigImage[0:BigImage.shape[0] , 0:BigImage.shape[1]]= 255

aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)

for x in np.mgrid[0:20]:
    img1 = aruco.drawMarker(aruco_dict,x, 200)
    x_offset = 40 +  (x % 5) * 230
    y_offset = 40 +  (int(x / 5)) * 230
    print ( "%d "%x_offset)
    BigImage[y_offset:y_offset+img1.shape[0], x_offset:x_offset+img1.shape[1]] = img1


cv2.imwrite('charucoMarker%d.png'%2,BigImage)

#plt.savefig("_data/markers.pdf")
#plt.show()








