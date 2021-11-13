#####################
###Benali Abdelhak###
#####################
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from operation import *
from filtrage import *
from contour import *
from random import randint

from Binarisation import *
from Morphologie import *
from segmentation import *
from Functions import *

class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(944, 623)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.benali = QtWidgets.QLabel(self.centralwidget)
        self.benali.setGeometry(QtCore.QRect(170, -10, 531, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.benali.setFont(font)
        self.benali.setAlignment(QtCore.Qt.AlignCenter)
        self.benali.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 40, 951, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(460, 50, 20, 661))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 560, 951, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.ImageOrigine = QtWidgets.QLabel(self.centralwidget)
        self.ImageOrigine.setGeometry(QtCore.QRect(10, 130, 441, 421))
        self.ImageOrigine.setAutoFillBackground(True)
        self.ImageOrigine.setText("")
        self.ImageOrigine.setObjectName("imageInitiale")
        self.ImageFinale = QtWidgets.QLabel(self.centralwidget)
        self.ImageFinale.setGeometry(QtCore.QRect(480, 130, 441, 421))
        self.ImageFinale.setAutoFillBackground(True)
        self.ImageFinale.setText("")
        self.ImageFinale.setObjectName("imageInitiale_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(600, 40, 501, 71))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_8")
        self.avant = QtWidgets.QLabel(self.centralwidget)
        self.avant.setGeometry(QtCore.QRect(120, 40, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.avant.setFont(font)
        self.avant.setObjectName("label_9")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(-10, 100, 951, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 944, 26))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuOperation = QtWidgets.QMenu(self.menubar)
        self.menuOperation.setObjectName("menuTraitement")
        self.menuBinarisation = QtWidgets.QMenu(self.menubar)
        self.menuBinarisation.setObjectName("menuBinarisation")
        self.menuFiltrage = QtWidgets.QMenu(self.menubar)
        self.menuFiltrage.setObjectName("menuFiltrage")
        self.menuMoyanneur = QtWidgets.QMenu(self.menuFiltrage)
        self.menuMoyanneur.setObjectName("menuMoyenneur")
        self.menuMedian = QtWidgets.QMenu(self.menuFiltrage)
        self.menuMedian.setObjectName("menuMedian")
        self.menuExtraction_contour = QtWidgets.QMenu(self.menubar)
        self.menuExtraction_contour.setObjectName("menuContour")
        self.menuMorphologie = QtWidgets.QMenu(self.menubar)
        self.menuMorphologie.setObjectName("menuMorphologie")
        self.menuSegmentation = QtWidgets.QMenu(self.menubar)
        self.menuSegmentation.setObjectName("menuSegmentation")
        self.menuPoint_d_interet = QtWidgets.QMenu(self.menubar)
        self.menuPoint_d_interet.setObjectName("menuPoint_d_interet")
        self.menuGraphe = QtWidgets.QMenu(self.menubar)
        self.menuGraphe.setObjectName("menuGraphe")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOuvrir = QtWidgets.QAction(MainWindow)
        self.actionOuvrir.setObjectName("actionOuvrir")
        self.actionEnregistrer = QtWidgets.QAction(MainWindow)
        self.actionEnregistrer.setObjectName("actionEnregistrer")
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionRotation = QtWidgets.QAction(MainWindow)
        self.actionRotation.setObjectName("actionRotation")
        self.actionZoom = QtWidgets.QAction(MainWindow)
        self.actionZoom.setObjectName("actionZoom")
        self.menuRedimentionnenemt = QtWidgets.QAction(MainWindow)
        self.menuRedimentionnenemt.setObjectName("actionredimensionner")
        self.actionhistogramme = QtWidgets.QAction(MainWindow)
        self.actionhistogramme.setObjectName("actionHistogramme")
        self.actionErosion = QtWidgets.QAction(MainWindow)
        self.actionhistogramme_color = QtWidgets.QAction(MainWindow)
        self.actionhistogramme_color.setObjectName("actionHistogramme")
        self.actionEgalization = QtWidgets.QAction(MainWindow)
        self.actionEgalization.setObjectName("action_galisation")
        self.actionEtirement = QtWidgets.QAction(MainWindow)
        self.actionEtirement.setObjectName("action_tirement")
        self.reset = QtWidgets.QAction(MainWindow)
        self.reset.setObjectName("actionR_initialisation")
        self.actionbinarisation_local = QtWidgets.QAction(MainWindow)
        self.actionbinarisation_local.setObjectName("actionBinarisation_Local")
        self.actionbinarisation_global = QtWidgets.QAction(MainWindow)
        self.actionbinarisation_global.setObjectName("actionBinarisation_global")
        self.actionhistogramme_color = QtWidgets.QAction(MainWindow)
        self.actionhistogramme_color.setObjectName("actionHistogramme_color")
        self.moyenneur3x3 = QtWidgets.QAction(MainWindow)
        self.moyenneur3x3.setObjectName("moyenneur3x3")
        self.moyenneur5x5 = QtWidgets.QAction(MainWindow)
        self.moyenneur5x5.setObjectName("moyenneur5x5")
        self.median3x3 = QtWidgets.QAction(MainWindow)
        self.median3x3.setObjectName("median3x3")
        self.median5x5 = QtWidgets.QAction(MainWindow)
        self.median5x5.setObjectName("median5x5")
        
        self.actionGaussien = QtWidgets.QAction(MainWindow)
        self.actionGaussien.setObjectName("gaussien")
        self.actionGradiant = QtWidgets.QAction(MainWindow)
        self.actionGradiant.setObjectName("actionGradient")
        self.actionSobel = QtWidgets.QAction(MainWindow)
        self.actionSobel.setObjectName("actionSobel")
        self.actionRobert = QtWidgets.QAction(MainWindow)
        self.actionSobel.setObjectName("actionSobel")
        self.actionKirsh = QtWidgets.QAction(MainWindow)
        self.actionKirsh.setObjectName("actionKirsh")
        self.actionrobi = QtWidgets.QAction(MainWindow)
        self.actionrobi.setObjectName("actionKirsh")
        self.actionLaplacien = QtWidgets.QAction(MainWindow)
        self.actionLaplacien.setObjectName("actionLaplacien")
        
        self.actionErosion = QtWidgets.QAction(MainWindow)
        self.actionErosion.setObjectName("actionErosion")
        self.actionDilatation = QtWidgets.QAction(MainWindow)
        self.actionDilatation.setObjectName("actionDilatation")
        self.actionOuverture = QtWidgets.QAction(MainWindow)
        self.actionOuverture.setObjectName("actionOuverture")
        self.actionFermeture = QtWidgets.QAction(MainWindow)
        self.actionFermeture.setObjectName("actionFermeture")
        self.actionCroissance_de_r_gions = QtWidgets.QAction(MainWindow)
        self.actionCroissance_de_r_gions.setObjectName("actionCroissance_de_region")
        self.actionPartition_de_regions = QtWidgets.QAction(MainWindow)
        self.actionPartition_de_regions.setObjectName("actionPartition_de_r_gion")
        self.actionM_thode_des_k_means = QtWidgets.QAction(MainWindow)
        self.actionM_thode_des_k_means.setObjectName("actionM_thode_des_k_means")
        self.actionM_thode_Sift = QtWidgets.QAction(MainWindow)
        self.actionM_thode_Sift.setObjectName("actionM_thode_Sift")
        self.actionM_thode_Harris = QtWidgets.QAction(MainWindow)
        self.actionM_thode_Harris.setObjectName("actionM_thode_Harris")
        self.actionM_thode_Hough = QtWidgets.QAction(MainWindow)
        self.actionM_thode_Hough.setObjectName("actionM_thode_Hough")
        self.hough_cercle = QtWidgets.QAction(MainWindow)
        self.hough_cercle.setObjectName("actionhough_cerce")
        self.zoomx2 = QtWidgets.QAction(MainWindow)
        self.zoomx2.setObjectName("zoomx2")
        self.zoomx4 = QtWidgets.QAction(MainWindow)
        self.zoomx4.setObjectName("zoomx4")
        self.actionNegatif = QtWidgets.QAction(MainWindow)
        self.actionNegatif.setObjectName("actionNegatif")
        self.redimentx2 = QtWidgets.QAction(MainWindow)
        self.redimentx2.setObjectName("redimentx2")
        self.redimentx4 = QtWidgets.QAction(MainWindow)
        self.redimentx4.setObjectName("redimentx4")
        self.action90 = QtWidgets.QAction(MainWindow)
        self.action90.setObjectName("action90")
        self.action180 = QtWidgets.QAction(MainWindow)
        self.action180.setObjectName("action180")
        self.menuFichier.addAction(self.actionOuvrir)
        self.menuFichier.addAction(self.actionEnregistrer)
        self.menuFichier.addAction(self.reset)
        self.menuFichier.addAction(self.actionQuitter)
        self.menuOperation.addAction(self.actionRotation)
        self.menuOperation.addAction(self.actionZoom)
        self.menuOperation.addAction(self.menuRedimentionnenemt)
        self.menuBinarisation.addAction(self.actionbinarisation_local)
        self.menuBinarisation.addAction(self.actionbinarisation_global)
        self.menuMedian.addAction(self.median5x5)
        self.menuMedian.addAction(self.median3x3)
        self.menuMoyanneur.addAction(self.moyenneur3x3)
        self.menuMoyanneur.addAction(self.moyenneur5x5)
        self.menuFiltrage.addAction(self.menuMoyanneur.menuAction())
        self.menuFiltrage.addAction(self.actionGaussien)
        self.menuFiltrage.addAction(self.menuMedian.menuAction())
        self.menuExtraction_contour.addAction(self.actionGradiant)
        self.menuExtraction_contour.addAction(self.actionKirsh)
        self.menuExtraction_contour.addAction(self.actionrobi)
        self.menuExtraction_contour.addAction(self.actionSobel)
        self.menuExtraction_contour.addAction(self.actionRobert)
        self.menuExtraction_contour.addAction(self.actionLaplacien)
        self.menuMorphologie.addAction(self.actionErosion)
        self.menuMorphologie.addAction(self.actionDilatation)
        self.menuMorphologie.addAction(self.actionOuverture)
        self.menuMorphologie.addAction(self.actionFermeture)
        self.menuSegmentation.addAction(self.actionCroissance_de_r_gions)
        self.menuSegmentation.addAction(self.actionPartition_de_regions)
        self.menuSegmentation.addAction(self.actionM_thode_des_k_means)
        self.menuPoint_d_interet.addAction(self.actionM_thode_Sift)
        self.menuPoint_d_interet.addAction(self.actionM_thode_Harris)
        self.menuPoint_d_interet.addAction(self.actionM_thode_Hough)
        self.menuPoint_d_interet.addAction(self.hough_cercle)
        self.menuGraphe.addAction(self.actionhistogramme)
        self.menuGraphe.addAction(self.actionhistogramme_color)
        self.menuGraphe.addAction(self.actionEgalization)
        self.menuGraphe.addAction(self.actionEtirement)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuOperation.menuAction())
        self.menubar.addAction(self.menuGraphe.menuAction())
        self.menubar.addAction(self.menuBinarisation.menuAction())
        self.menubar.addAction(self.menuFiltrage.menuAction())
        self.menubar.addAction(self.menuExtraction_contour.menuAction())
        self.menubar.addAction(self.menuMorphologie.menuAction())
        self.menubar.addAction(self.menuSegmentation.menuAction())
        self.menubar.addAction(self.menuPoint_d_interet.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.benali.setText(_translate("MainWindow", "Traitement de l\'image | Benali Abdelhak"))
        self.label_2.setText(_translate("MainWindow", "Après traitement"))
        self.avant.setText(_translate("MainWindow", "Avant traitement"))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier"))
        self.menuOperation.setTitle(_translate("MainWindow", "Traitement"))
        self.menuBinarisation.setTitle(_translate("MainWindow", "Binarisation"))
        self.menuFiltrage.setTitle(_translate("MainWindow", "Filtrage"))
        self.menuMoyanneur.setTitle(_translate("MainWindow", "Moyenneur"))
        self.menuMedian.setTitle(_translate("MainWindow", "Median"))
        self.menuExtraction_contour.setTitle(_translate("MainWindow", "Contour"))
        self.menuMorphologie.setTitle(_translate("MainWindow", "Morphologie"))
        self.menuSegmentation.setTitle(_translate("MainWindow", "Segmentation"))
        self.menuPoint_d_interet.setTitle(_translate("MainWindow", "Point d\'interet"))
        self.menuGraphe.setTitle(_translate("MainWindow", "Graphe"))
        self.actionOuvrir.setText(_translate("MainWindow", "Ouvrir"))
        self.actionEnregistrer.setText(_translate("MainWindow", "Enregistrer"))
        self.actionEnregistrer.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))
        self.actionQuitter.setShortcut(_translate("MainWindow", "Ctrl+F5"))
        self.actionRotation.setText(_translate("MainWindow", "Pivoter"))
        self.actionZoom.setText(_translate("MainWindow", "Zoom"))
        self.menuRedimentionnenemt.setText(_translate("MainWindow", "Redimensionner"))
        self.actionhistogramme.setText(_translate("MainWindow", "Histo_gris"))
        self.actionhistogramme_color.setText(_translate("MainWindow", "Histo_color"))
        self.actionEgalization.setText(_translate("MainWindow", "Égalisation"))
        self.actionEtirement.setText(_translate("MainWindow", "Etirement"))
        self.reset.setText(_translate("MainWindow", "Réinitialisation"))
        self.actionbinarisation_local.setText(_translate("MainWindow", "Binarisation Local"))
        self.actionbinarisation_global.setText(_translate("MainWindow", "Binarisation Global"))
        self.actionGaussien.setText(_translate("MainWindow", "Gaussien"))
        self.moyenneur3x3.setText(_translate("MainWindow", "5x5"))
        self.moyenneur5x5.setText(_translate("MainWindow", "7x7"))
        self.median3x3.setText(_translate("MainWindow", "3x3"))
        self.median5x5.setText(_translate("MainWindow", "5x5"))
        self.actionGradiant.setText(_translate("MainWindow", "Gradient"))
        self.actionKirsh.setText(_translate("MainWindow", "Kirsh"))
        self.actionSobel.setText(_translate("MainWindow", "Sobel"))
        self.actionRobert.setText(_translate("MainWindow", "Robert"))
        self.actionLaplacien.setText(_translate("MainWindow", "Laplacien"))
        self.actionErosion.setText(_translate("MainWindow", "Erosion"))
        self.actionDilatation.setText(_translate("MainWindow", "Dilatation"))
        self.actionOuverture.setText(_translate("MainWindow", "Ouverture"))
        self.actionFermeture.setText(_translate("MainWindow", "Fermeture"))
        self.actionCroissance_de_r_gions.setText(_translate("MainWindow", "Croissance de régions"))
        self.actionPartition_de_regions.setText(_translate("MainWindow", "Partition de régions"))
        self.actionM_thode_des_k_means.setText(_translate("MainWindow", "Méthode des k-means"))
        self.actionM_thode_Sift.setText(_translate("MainWindow", "Méthode Sift"))
        self.actionM_thode_Harris.setText(_translate("MainWindow", "Méthode Harris"))
        self.actionM_thode_Hough.setText(_translate("MainWindow", "Méthode Hough "))
        self.actionrobi.setText(_translate("MainWindow", "Robirson"))
        self.hough_cercle.setText(_translate("MainWindow", "Hough cercle"))
        self.actionOuvrir.triggered.connect(self.openFile)
        self.actionNegatif.triggered.connect(self.negatif)
        self.moyenneur3x3.triggered.connect(self.Moyenneur5)
        self.moyenneur5x5.triggered.connect(self.Moyenneur7)
       
        self.median3x3.triggered.connect(self.median3)
        self.median5x5.triggered.connect(self.median5)
        self.actionGradiant.triggered.connect(self.grad)
        self.actionRobert.triggered.connect(self.Robert)
        self.actionSobel.triggered.connect(self.Sobel)
        self.actionLaplacien.triggered.connect(self.laplacien)
        self.actionErosion.triggered.connect(self.Erosion)
        self.actionDilatation.triggered.connect(self.dilatation)
        self.actionOuverture.triggered.connect(self.ouverture)
        self.actionFermeture.triggered.connect(self.fermeture)
        self.actionbinarisation_global.triggered.connect(self.BinarisationOtsu)
        self.actionbinarisation_local.triggered.connect(self.BinarisationLocal)
        self.actionM_thode_des_k_means.triggered.connect(self.kmeans)
        self.actionPartition_de_regions.triggered.connect(self.partRegion)
        self.zoomx2.triggered.connect(self.partRegion)
        self.reset.triggered.connect(self.rest)
        self.actionEnregistrer.triggered.connect(self.Save)
        self.actionhistogramme.triggered.connect(self.Histo_Gray)
        self.actionhistogramme_color.triggered.connect(self.Histo_Color)
        self.menuRedimentionnenemt.triggered.connect(self.Redimention)
        self.actionRotation.triggered.connect(self.rotate)
        self.actionGaussien.triggered.connect(self.Gauss)
        self.actionM_thode_Hough.triggered.connect(self.Hough)
        self.actionM_thode_Harris.triggered.connect(self.Haris)
        self.actionM_thode_Sift.triggered.connect(self.Sift)
        self.actionEgalization.triggered.connect(self.egalisation)
        self.actionEtirement.triggered.connect(self.etirement)
        self.actionKirsh.triggered.connect(self.kirsh)
        self.actionrobi.triggered.connect(self.Robirson)
        self.hough_cercle.triggered.connect(self.Hough_cercles)
        
    
    def rest(self):
        self.ImageOrigine.setText(" ")
        self.ImageFinale.setText(" ")
        self.label_2.setText("Apres traitement")
        

    def openFile(self):
        nom_fichier = QFileDialog.getOpenFileName()
        self.path = nom_fichier[0]
        pathx = self.path
        pixmap = QtGui.QPixmap(pathx)
        pixmap4 = pixmap.scaled(441, 421)

        self.ImageOrigine.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageOrigine.adjustSize()
    
    def Save(self):
        fileName = QFileDialog.getSaveFileName(None, 'some text', "untitled.png", "Image Files (*.jpg *.gif *.bmp *.png)")
        self.fileName = fileName[0]
        print(fileName[0]+"file name")
        cv2.imwrite(fileName[0], self.mat)

    def rotate(self):
     angleRotation, done = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'saisir le porcentage')
     if done:
        
        
        image = cv2.imread(self.path)
        o = Operation(image)
        img = o.rotate_image(angleRotation)
        self.mat = img
        height, width, byteValue = img.shape
        print(byteValue)
        if byteValue == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("Rotation par "+str(angleRotation)+"°")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))

    

    def negatif(self):
        image = cv2.imread(self.path)
        img = 255 - image
        height, width, byteValue = img.shape
        self.mat=img
        print(byteValue)
        if byteValue == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("Apres traitement : Negatif")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))

    def Moyenneur5(self):
        image = cv2.imread(self.path)
        f = Filtrage(image)
        img = f.Moyenneur(5)
        height, width, byteValue = img.shape
        self.mat=img
        print(byteValue)
        if byteValue == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("Apres traitement : moyenneur 5x5")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))

    def Moyenneur7(self):
        image = cv2.imread(self.path)
        f = Filtrage(image)
        img = f.Moyenneur(7)
        self.mat=img
        height, width, byteValue = img.shape
        print(byteValue)
        if byteValue == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("Apres traitement : moyenneur 7x7")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))

    def gaussian5(self):
        image = cv2.imread(self.path)
        f = Filtrage(image)
        img = f.Gaussien(0.1)
        self.mat=img
        height, width, byteValue = img.shape
        print(byteValue)
        if byteValue == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("Apres traitement : gaussien 5x5")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))

    def gaussian7(self):
        image = cv2.imread(self.path)
        f = Filtrage(image)
        img = f.Gaussien(0.8)
        self.mat=img
        height, width, byteValue = img.shape
        print(byteValue)
        if byteValue == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("Apres traitement : gaussien 7x7")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))

    def median3(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        if byteValue == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            f = Filtrage(image)
            img = f.Median(5)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
            self.mat=img
        else:
            f = Filtrage(image)
            img = f.Median(5)
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
            self.mat=img
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("Apres traitement : median 3x3")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))

    def median5(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        if byteValue == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            f = Filtrage(image)
            img = f.Median(5)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
            self.mat=img
        else:
            f = Filtrage(image)
            img = f.Median(5)
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
            self.mat=img
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("Apres traitement : median 5x5")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))

    def grad(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            img = c.grad(20)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            self.mat=img
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            c = Contours(image)
            img = c.grad(20)
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
            self.mat=img
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("Apres traitement : gradient")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))
        
    def etirement(self):
        image = cv2.imread(self.path)
        imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        o = Operation(imag)
        img = o.etire()
        self.mat = img
        imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("Apres traitement : Etirement")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))
        
    def Gauss(self):
        segma, done = QtWidgets.QInputDialog.getDouble(self, 'Input Dialog', 'saisir segma', 12, 0, 1, 1)
        if done:
            image = cv2.imread(self.path)
            f = Functions(image)
            img = f.Gaussien(segma)
            self.mat = img
            height, width, byteValue = img.shape
            print(byteValue)
            if byteValue == 3:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
            else:
                imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
            pixmap = QtGui.QPixmap(imag)
            pixmap4 = pixmap.scaled(441, 421, QtCore.Qt.KeepAspectRatio)
            self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
            self.ImageFinale.adjustSize()
            self.label_2.setText("Gaussien avec segma="+str(segma))
            self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))
    
    def Hough(self):
        img = cv2.imread(self.path)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray,50,150,apertureSize = 3)
        lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
        for line in lines:
            x1,y1,x2,y2 = line[0]
            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
        self.mat=img
        height, width, byteValue = img.shape
        imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421, QtCore.Qt.KeepAspectRatio)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("Apres traitement : Hough")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))

    def Haris(self):
        img = cv2.imread(self.path)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        gray = np.float32(gray)
        dst = cv2.cornerHarris(gray,2,3,0.04)
        #result is dilated for marking the corners, not important
        dst = cv2.dilate(dst,None)
        height, width, byteValue = img.shape

        # Threshold for an optimal value, it may vary depending on the image.
        img[dst>0.01*dst.max()]=[0,0,255]
        self.mat=img
        imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421, QtCore.Qt.KeepAspectRatio)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("Apres traitement : Harris")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))

    def Sift(self):
        img = cv2.imread(self.path)
        height, width, byteValue = img.shape
        gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        sift = cv2.SIFT_create()
        kp = sift.detect(gray,None)
        img=cv2.drawKeypoints(gray,kp,img)
        self.mat=img
        imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421, QtCore.Qt.KeepAspectRatio)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("Apres traitement : Sift")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))

    def Robert(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            img = c.Robert(20)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            self.mat=img
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            c = Contours(image)
            img = c.Robert(20)
            self.mat=img
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)

        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("Apres traitement : Robert")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))

    def Sobel(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            img = c.Sobel(50)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            self.mat=img
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            c = Contours(image)
            img = c.Sobel(50)
            self.mat=img
            imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)

        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("Apres traitement : Sobel")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))

    def laplacien(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            c = Contours(imag)
            img = c.Laplacien(20)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            self.mat=img
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            c = Contours(image)
            img = c.Laplacien(20)
            imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
            self.mat=img
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("Apres traitement : laplacien")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))

    def partRegion(self):
        image = cv2.imread(self.path)
        imag = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, byteValue = imag.shape
        s = Segmentation(imag)
        img = s.partition_regions()
        self.mat = img
        imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("Apres traitement :Partition des regions")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))
        
        
    def Erosion(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            m = Morphologie(imag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m.Erosion(h)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            self.mat=img
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            m = Morphologie(image)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m.Erosion(h)
            self.mat=img
            imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.label_2.setText("Apres traitement : Erosion")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))

    def dilatation(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            m = Morphologie(imag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m.dilatation(h)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            self.mat=img
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            m = Morphologie(image)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m.dilatation(h)
            self.mat=img
            imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.label_2.setText("Apres traitement : Dilatation")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))

    def ouverture(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            m = Morphologie(imag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            imaag = m.Erosion(h)
            m1 = Morphologie(imaag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m1.dilatation(h)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            self.mat=img
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            m = Morphologie(image)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            imaag = m.Erosion(h)
            m1 = Morphologie(imaag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m1.dilatation(h)
            self.mat=img
            imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.label_2.setText("Apres traitement : Ouverture")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))

    def fermeture(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        print(byteValue)
        if byteValue == 3:
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            m = Morphologie(imag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            imaag = m.dilatation(h)
            m1 = Morphologie(imaag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m1.Erosion(h)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            self.mat=img
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            m = Morphologie(image)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            imaag = m.dilatation(h)
            m1 = Morphologie(imaag)
            h = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
            img = m1.Erosion(h)
            self.mat=img
            imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.label_2.setText("Apres traitement : Fermeture")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))

    def BinarisationOtsu(self):
        image = cv2.imread(self.path)
        height, width, byteValue = image.shape
        if byteValue == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            b = Binarisation(image)
            print('hello')
            img = b.Otsu()
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
            self.mat=img
            imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        else:
            b = Binarisation(image)
            img = b.Otsu()
            self.mat=img
            imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("Apres traitement :Binarisation global")
        self.label_2.setGeometry(QtCore.QRect(470, 40, 501, 71))

       

    def BinarisationLocal(self):
        name, done1 = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'Entrez le seuil: ', 127, 1, 255, 1)
        if done1:
            image = cv2.imread(self.path)
            height, width, byteValue = image.shape
            print(byteValue)
            if byteValue == 3:
                imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                f = Binarisation(imag)
                img = f.Seuillage(name)
                self.mat = img
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
                imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
            else:
                f = Binarisation(image)
                img = f.Seuillage(name)
                self.mat = img
                imag = QtGui.QImage(img, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
            pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("Apres traitement :Binarisation local")
        self.label_2.setGeometry(QtCore.QRect(480, 40, 501, 71))

    def kmeans(self):
        image = cv2.imread(self.path)
        imag = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, byteValue = imag.shape
        s = Segmentation(imag)
        img = s.k_means()
        self.mat=img
        imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("Apres traitement : k-means")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))

    def partRegion(self):
        image = cv2.imread(self.path)
        imag = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, byteValue = imag.shape
        s = Segmentation(imag)
        img = s.partition_regions()
        self.mat=img
        imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("Apres traitement :Partition de regions")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))
   
    def histo(self):
        img = cv2.imread(self.path)
        imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
        b=Functions(imgGray)
        h = b.Histo()
        plt.subplot(1, 1, 1)
        plt.plot(h)
        random = randint(1, 2000)
        print(random)
        self.mat=img
        x = "image" + str(random)
        plt.savefig("resultat//" + x + ".png")
        pixmap = QtGui.QPixmap("resultat//"+ x + ".png")
        pixmap4 = pixmap.scaled(441, 420, QtCore.Qt.KeepAspectRatio)
        self.ImageFinale.setPixmap(pixmap4)
        plt.show()
        plt.clf()
        
    def Histo_Gray(self):
        img = cv2.imread(self.path)
        imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
        b=Functions(imgGray)
        h = b.Histo()
        plt.subplot(1, 1, 1)
        plt.plot(h)
        self.mat=img
        random = randint(1, 2000)
        print(random)
        x = "image" + str(random)
        plt.savefig("" + x + ".png")
        pixmap = QtGui.QPixmap(""+ x + ".png")
        pixmap4 = pixmap.scaled(441, 421, QtCore.Qt.KeepAspectRatio)
        self.ImageFinale.setPixmap(pixmap4)
        plt.show()
        plt.clf()
        
    def Histo_Color(self):
        img = cv2.imread(self.path)
        imr=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);

        print("azsassa",imr.shape)
        self.mat=img
        k = 0
        try:
            test = img.shape[2]
        except IndexError:
            k = 1
        if k == 1:
            self.Histo_Gray()

        else:
            color = ("b","g","r")
            red, green, blue = img[:,:,0], img[:,:,1], img[:,:,2]
            b=Functions(red)
            plt.figure(1)
            hr=b.Histo() 
            plt.subplot(3,1,1)
            plt.plot(hr,color="r")
            plt.title("Hisogramme")
            b=Functions(green)
            hg=b.Histo()   
            plt.subplot(3,1,2)
            plt.plot(hr,color="g")
            b=Functions(blue)
            hb=b.Histo()
            plt.subplot(3,1,3)
            plt.plot(hr,color="b")           
        random = randint(1, 2000)
        print(random)
        x = "image" + str(random)
        plt.savefig("" + x + ".png")
        pixmap = QtGui.QPixmap(""+ x + ".png")
        pixmap4 = pixmap.scaled(441, 421, QtCore.Qt.KeepAspectRatio)
        self.ImageFinale.setPixmap(pixmap4)
        plt.show()
        plt.clf()

    def Redimention(self):
        porcentage, done = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'saisir le porcentage', 12, 1, 255, 1)
        if done:
            image = cv2.imread(self.path)
            scale_percent = porcentage
            width = int(image.shape[1] * scale_percent / 100)
            height = int(image.shape[0] * scale_percent / 100)
            dim = (width, height)
            img = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
            self.mat = img
            height, width, byteValue = img.shape
            print(byteValue)
            if byteValue == 3:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
            else:
                imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
            pixmap = QtGui.QPixmap(imag)
            pixmap4 = pixmap.scaled(441, 421, QtCore.Qt.KeepAspectRatio)
            self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("Redimensionnement")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))
        
    def egalisation(self):
        image = cv2.imread(self.path)
        imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        b=Functions(imag)
        img = b.eqHisto()
        self.mat = img
        imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421, QtCore.Qt.KeepAspectRatio)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("Apres traitement :Egalisation")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))
        
    def kirsh(self):
        seuil, done = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'saisir le porcentage', 12, 1, 255, 1)
        if done:
            image = cv2.imread(self.path)
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            b=Operation(imag)
            img = b.kirsch(seuil)
            self.mat = img
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
            pixmap = QtGui.QPixmap(imag)
            pixmap4 = pixmap.scaled(441, 421, QtCore.Qt.KeepAspectRatio)
            self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
            self.ImageFinale.adjustSize()
            self.label_2.setText("Apres traitement :Kirsh")
            self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))  
            
    def Robirson(self):
        seuil, done = QtWidgets.QInputDialog.getInt(self, 'Input Dialog', 'saisir le porcentage', 12, 1, 255, 1)
        if done:
            image = cv2.imread(self.path)
            imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            b=Operation(imag)
            img = b.Robirson(seuil)
            self.mat = img
            imag = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_Grayscale8)
            pixmap = QtGui.QPixmap(imag)
            pixmap4 = pixmap.scaled(441, 421, QtCore.Qt.KeepAspectRatio)
            self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
            self.ImageFinale.adjustSize()
            self.label_2.setText("Apres traitement :Robirson")
            self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71))        
        
    def Hough_cercles(self,argv):
    
        default_file = self.path
        filename = default_file
        # Loads an image
        src = cv2.imread(cv2.samples.findFile(filename), cv2.IMREAD_COLOR)
        # Check if image is loaded fine
        if src is None:
            print ('Error opening image!')
            print ('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
            return -1 
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  
        gray = cv2.medianBlur(gray, 5)  
        rows = gray.shape[0]
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
                                   param1=100, param2=30,
                                   minRadius=1, maxRadius=30) 
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                center = (i[0], i[1])
                # circle center
                cv2.circle(src, center, 1, (0, 100, 100), 3)
                # circle outline
                radius = i[2]
                cv2.circle(src, center, radius, (255, 0, 255), 3) 
        img=src
        self.mat=img
        height, width, byteValue = img.shape
        imag = QtGui.QImage(img, width, height, byteValue * width, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap(imag)
        pixmap4 = pixmap.scaled(441, 421, QtCore.Qt.KeepAspectRatio)
        self.ImageFinale.setPixmap(QtGui.QPixmap(pixmap4))
        self.ImageFinale.adjustSize()
        self.label_2.setText("Apres traitement :Hough cercle")
        self.label_2.setGeometry(QtCore.QRect(490, 40, 501, 71)) 
        
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
