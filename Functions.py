



import numpy as np
from numpy import *
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
from skimage.color import *
from PIL import Image
import cv2
class Functions:
    def __init__(self,image):
        super().__init__()
        self.image=image

    def Histo(self):
        h = zeros(256, dtype=float32)
        s = self.image.shape
        for j in range(s[0]):
            for i in range(s[1]):
                valeur = self.image[j, i]
                h[valeur] += 1
        return h
    
    def HistMoy(self):
        m, n = self.image.shape
        h = [0.0] * 256
        for i in range(m):
            for j in range(n):
                h[self.image[i, j]] += 1
        return np.array(h) / (m * n)
    def Cumulation(self,h):
        return [sum(h[:i + 1]) for i in range(len(h))]

    def eqHisto(self):
        h = self.HistMoy()
        Hcumuler = np.array(self.Cumulation(h))
        map = np.uint8(Hcumuler*255)
        s1, s2 = self.image.shape
        Y = np.zeros_like(self.image)
        for i in range(0, s1):
            for j in range(0, s2):
                Y[i, j] = map[self.image[i, j]]
        return Y

    def etire(self):
        MaxV = np.max(self.image)
        MinV = np.min(self.image)
        Y = np.zeros_like(self.image)
        m = self.image.shape
        for i in range(m[0]):
            for j in range(m[1]):
                Y[i, j] = (255 / (MaxV - MinV) * self.image[i, j] - MinV)
        plt.plot(Y)
        plt.show()
        return Y
    def Seuillage(self,s):
        imageX = self.image.copy()
        for i in range(1,imageX.shape[0]):
            for j in range(1,imageX.shape[1]):
                if imageX[i,j] < s:
                    imageX[i, j] = 0
                else:
                    imageX[i, j] = 255
        return imageX

    def Otsu(self):
        pixel_number = self.image.shape[0] * self.image.shape[1]
        mean_weigth = 1.0 / pixel_number
        his, bins = np.histogram(self.image, np.arange(0, 257))
        final_thresh = -1
        final_value = -1
        intensity_arr = np.arange(256)
        for t in bins[1:-1]:  #  1 -> 254 in  uint8 
            pcb = np.sum(his[:t])
            pcf = np.sum(his[t:])
            Wb = pcb * mean_weigth
            Wf = pcf * mean_weigth

            mub = np.sum(intensity_arr[:t] * his[:t]) / float(pcb)
            muf = np.sum(intensity_arr[t:] * his[t:]) / float(pcf)
            value = Wb * Wf * (mub - muf) ** 2

            if value > final_value:
                final_thresh = t
                final_value = value
        final_img = self.image.copy()
        print(final_thresh)
        final_img[self.image > final_thresh] = 255
        final_img[self.image < final_thresh] = 0
        return final_img
    
    def h(self,x,y,v):
        x =(1/(2*math.pi*math.pow(v,2)))*(math.exp(-(math.pow(x,2)+math.pow(y,2))/(2*math.pow(v,2))))
        return x
    
    def Gaussien(self,v):
        imagefiltrage = self.image.copy()
        x = 1
        for i in range(x, self.image.shape[0] - x):
            for j in range(x, self.image.shape[1] - x):
                s=0
                for a in range(-x, x):
                    for b in range(-x, x):
                        s = s + self.h(a, b, v)*self.image[i+a, j+b]
                imagefiltrage[i, j] = s
                s=0
        return imagefiltrage
    
    def Median(self, taille):
        imagefiltrage = self.image.copy()
        x = int((taille - 1) / 2)
        for i in range(x, self.image.shape[0] - x):
            for j in range(x, self.image.shape[1] - x):
                liste = []
                if imagefiltrage[i, j] == 0 or imagefiltrage[i, j] == 255:
                    for n in range(-x, x):
                        for m in range(-x, x):
                            liste.append(imagefiltrage[i + n, j + m])
                    liste.sort()
                    imagefiltrage[i, j] = liste[x + 1]
                    while len(liste) > 0: liste.pop()
        return imagefiltrage

    def Moyenneur(self, taille):
        imagefiltrage= self.image.copy()
        x = int((taille - 1 )/2)
        for i in range(x, self.image.shape[0] - x):
            for j in range(x, self.image.shape[1] - x):
                s=0
                for n in range(-x, x):
                    for m in range(-x, x):
                        s += self.image[i+n,j+m]/(taille*taille)
                imagefiltrage[i,j] = s
                s=0
        return imagefiltrage

    def Gradiant(self,seuil):
        imageX = self.image.copy()
        imageY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageY[i, j] = self.image[i, j+1] -self.image[i, j]
                imageX[i, j] = self.image[i+1,j] -self.image[i, j]
        imageXY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageXY[i, j] = sqrt(imageX[i, j] ** 2 + imageY[i, j] ** 2)
                if imageXY[i, j] < seuil:
                    imageXY[i, j] = 0
                else:
                    imageXY[i, j] = 255
        return imageXY

    def Sobel(self):
        image=self.image.copy()
        Gx = np.array([(-1, 0, 1), (-2, 0, 2), (-1, 0, 1)])
        Gy = np.array([(-1, -2, -1), (0, 0, 0), (1, 2, 1)])
        ligne=image.shape[0];
        colonne=image.shape[1];
        imgX=image.copy();
        imgY=image.copy();
        imgFin = image.copy();
        for i in range(1, ligne-1 ):
            for j in range(1,colonne-1):
                x_sum = (Gx.item(0, 0) * image.item(i-1, j-1)) + (Gx.item(0, 2) * image.item(i-1, j+1)) + (Gx.item(1, 0) * image.item(i, j-1)) + (Gx.item(1, 2) * image.item(i, j+1)) + (Gx.item(2, 0) * image.item(i+1, j-1)) + (Gx.item(2, 2) * image.item(i+1, j+1))
                y_sum = (Gy.item(0, 0) * image.item(i-1, j-1)) + (Gy.item(0, 1) * image.item(i-1, j)) + (Gy.item(0, 2) * image.item(i-1, j+1)) + (Gy.item(2, 0) * image.item(i+1, j-1)) + (Gy.item(2, 1) * image.item(i+1, j)) + (Gy.item(2, 2) * image.item(i+1, j+1))
                imgX.itemset((i-1, j-1), x_sum)
                imgY.itemset((i-1, j-1), y_sum)
                imgFin.itemset((i-1,j-1),np.sqrt(x_sum ** 2 +y_sum ** 2))
        f=Functions(imgFin)
        img=f.Seuillage(100)
        return img

    def Laplacien(self,seuil):
        imageXY = self.image.copy()
        for i in range(1, self.image.shape[0] - 1):
            for j in range(1, self.image.shape[1] - 1):
                imageXY[i, j] = -4*self.image[i, j] +self.image[i-1, j] +self.image[i+1, j] \
                               + self.image[i , j - 1] +self.image[i, j + 1]
                if imageXY[i, j] < seuil:
                    imageXY[i, j] = 0
                else:
                    imageXY[i, j] = 255
        return imageXY


# =============================================================================
# =============================================================================
# # Segmentation
# =============================================================================
# =============================================================================
    def k_means(self):
        pixel_values = self.image.reshape((-1, 3))
        pixel_values = np.float32(pixel_values)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
        k = 3
        ret, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        centers = np.uint8(centers)
        segmented_image = centers[labels.flatten()]
        segmented_image = segmented_image.reshape(self.image.shape)
        return segmented_image

    def partition_regions(self):
        gray_r = self.image.reshape(self.image.shape[0] * self.image.shape[1])
        for i in range(gray_r.shape[0]):
            if gray_r[i] > gray_r.mean():
                gray_r[i] = 3
            elif gray_r[i] > 0.5:
                gray_r[i] = 2
            elif gray_r[i] > 0.25:
                gray_r[i] = 1
            else:
                gray_r[i] = 0
        gray = gray_r.reshape(self.image.shape[0], self.image.shape[1])
        plt.imshow(gray, cmap='gray')
        return gray