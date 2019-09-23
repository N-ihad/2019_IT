import numpy as np
import cv2
import math


img_in = cv2.imread('noisy_image.jpg', cv2.IMREAD_GRAYSCALE)
img_out = img_in.copy()
height = img_in.shape[0]
width = img_in.shape[1]


def gaussFilter2D(image, w, sigma):
    gauss = np.array([[[math.exp(-((w // 2 - k) ** 2 + (w // 2 - l) ** 2) / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma) for l in range(w)] for k in range(w)] for i in range(3)])
    gaussNorm = (gauss/sum(sum(gauss[0])))[0]
    if(w%2)==0:
        end = w//2
    else:
        end = (w//2) + 1
    for i in np.arange(w//2, height - (w//2)):
        for j in np.arange(w//2, width - (w//2)):
            totalSum = 0
            for k in np.arange(-(w//2), end):
                for l in np.arange(-(w//2), end):
                    a = img_in.item(i + k, j + l)
                    p = gaussNorm[(w//2) + k, (w//2) + l]
                    totalSum = totalSum + (p * a)
            b = totalSum
            img_out.itemset((i, j), b)
    outputImageName = 'gaussFilteredImage_w=' + str(w) + '_sigma=' + str(sigma) + '.jpg'
    cv2.imwrite(outputImageName, img_out)
    cv2.imshow('filteredImage', img_out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




#gaussFilter2D(img_in, 9, 5.0)




#def gaussOneD(n=5,sigma=1.0):
 #   r = range(-int(n/2),int(n/2)+1)
  #  return [1 / (sigma * math.sqrt(2*math.pi)) * math.exp(-float(x)**2/(2*sigma**2)) for x in r]