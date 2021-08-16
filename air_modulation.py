# -----------------------------------------------------------------------------------------------------
# Importación de Librerías
# -----------------------------------------------------------------------------------------------------
#from screen_air_gen import SBO04
import datetime
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
# -----------------------------------------------------------------------------------------------------
# Definición de Funciones
# -----------------------------------------------------------------------------------------------------
def flow (cad,cap):
    blower_flow = (1.2 * (cap + 0.5) * 30 * cad) / 60000
    return blower_flow
# -----------------------------------------------------------------------------------------------------
# Importación de Datos
# -----------------------------------------------------------------------------------------------------
# Sopladora 4
SBO04_0 = pd.read_csv ('https://raw.githubusercontent.com/HKlee057/Datos_Sopladoras/main/SBO04_Base.csv')
# Sopladora 12
SBO12_0 = pd.read_csv ('https://raw.githubusercontent.com/HKlee057/Datos_Sopladoras/main/SBO12_Base.csv')
# Sopladora 16
SBO16_0 = pd.read_csv ('https://raw.githubusercontent.com/HKlee057/Datos_Sopladoras/main/SBO16_Base.csv')
# Sopladora 20
SBO20_0 = pd.read_csv ('https://raw.githubusercontent.com/HKlee057/Datos_Sopladoras/main/SBO20_Base.csv')
# Sopladora 10
SBO10_0 = pd.read_csv ('https://raw.githubusercontent.com/HKlee057/Datos_Sopladoras/main/SBO10_Base.csv')
# -----------------------------------------------------------------------------------------------------

class Ui_Air_Modulation(object):
    def setupUi(self, Air_Modulation):
        Air_Modulation.setObjectName("Air_Modulation")
        Air_Modulation.resize(732, 451)
        self.centralwidget = QtWidgets.QWidget(Air_Modulation)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)
        self.cmbScene20 = QtWidgets.QComboBox(self.centralwidget)
        self.cmbScene20.setObjectName("cmbScene20")
        self.cmbScene20.addItem("")
        self.cmbScene20.addItem("")
        self.cmbScene20.addItem("")
        self.cmbScene20.addItem("")
        self.gridLayout.addWidget(self.cmbScene20, 8, 1, 1, 1)
        self.cmbScene16 = QtWidgets.QComboBox(self.centralwidget)
        self.cmbScene16.setObjectName("cmbScene16")
        self.cmbScene16.addItem("")
        self.cmbScene16.addItem("")
        self.cmbScene16.addItem("")
        self.cmbScene16.addItem("")
        self.gridLayout.addWidget(self.cmbScene16, 7, 1, 1, 1)
        self.cmbPres20 = QtWidgets.QComboBox(self.centralwidget)
        self.cmbPres20.setObjectName("cmbPres20")
        self.cmbPres20.addItem("")
        self.cmbPres20.addItem("")
        self.cmbPres20.addItem("")
        self.cmbPres20.addItem("")
        self.cmbPres20.addItem("")
        self.cmbPres20.addItem("")
        self.cmbPres20.addItem("")
        self.cmbPres20.addItem("")
        self.cmbPres20.addItem("")
        self.cmbPres20.addItem("")
        self.cmbPres20.addItem("")
        self.gridLayout.addWidget(self.cmbPres20, 8, 2, 1, 1)
        self.cmbPres16 = QtWidgets.QComboBox(self.centralwidget)
        self.cmbPres16.setObjectName("cmbPres16")
        self.cmbPres16.addItem("")
        self.cmbPres16.addItem("")
        self.cmbPres16.addItem("")
        self.cmbPres16.addItem("")
        self.cmbPres16.addItem("")
        self.cmbPres16.addItem("")
        self.cmbPres16.addItem("")
        self.cmbPres16.addItem("")
        self.cmbPres16.addItem("")
        self.cmbPres16.addItem("")
        self.cmbPres16.addItem("")
        self.gridLayout.addWidget(self.cmbPres16, 7, 2, 1, 1)
        self.cmbSceneCE3 = QtWidgets.QComboBox(self.centralwidget)
        self.cmbSceneCE3.setObjectName("cmbSceneCE3")
        self.cmbSceneCE3.addItem("")
        self.cmbSceneCE3.addItem("")
        self.cmbSceneCE3.addItem("")
        self.cmbSceneCE3.addItem("")
        self.gridLayout.addWidget(self.cmbSceneCE3, 7, 5, 1, 1)
        self.cmbSceneCE46 = QtWidgets.QComboBox(self.centralwidget)
        self.cmbSceneCE46.setObjectName("cmbSceneCE46")
        self.cmbSceneCE46.addItem("")
        self.cmbSceneCE46.addItem("")
        self.cmbSceneCE46.addItem("")
        self.cmbSceneCE46.addItem("")
        self.gridLayout.addWidget(self.cmbSceneCE46, 8, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 9, 0, 1, 1)
        self.cmbPres10 = QtWidgets.QComboBox(self.centralwidget)
        self.cmbPres10.setObjectName("cmbPres10")
        self.cmbPres10.addItem("")
        self.cmbPres10.addItem("")
        self.cmbPres10.addItem("")
        self.cmbPres10.addItem("")
        self.cmbPres10.addItem("")
        self.cmbPres10.addItem("")
        self.cmbPres10.addItem("")
        self.cmbPres10.addItem("")
        self.cmbPres10.addItem("")
        self.cmbPres10.addItem("")
        self.cmbPres10.addItem("")
        self.gridLayout.addWidget(self.cmbPres10, 9, 2, 1, 1)
        self.cmbSceneSIAD = QtWidgets.QComboBox(self.centralwidget)
        self.cmbSceneSIAD.setObjectName("cmbSceneSIAD")
        self.cmbSceneSIAD.addItem("")
        self.cmbSceneSIAD.addItem("")
        self.cmbSceneSIAD.addItem("")
        self.cmbSceneSIAD.addItem("")
        self.gridLayout.addWidget(self.cmbSceneSIAD, 9, 5, 1, 1)
        self.cmbScene10 = QtWidgets.QComboBox(self.centralwidget)
        self.cmbScene10.setObjectName("cmbScene10")
        self.cmbScene10.addItem("")
        self.cmbScene10.addItem("")
        self.cmbScene10.addItem("")
        self.cmbScene10.addItem("")
        self.gridLayout.addWidget(self.cmbScene10, 9, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 3, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lblEtiqueta = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lblEtiqueta.setFont(font)
        self.lblEtiqueta.setObjectName("lblEtiqueta")
        self.gridLayout.addWidget(self.lblEtiqueta, 1, 2, 1, 1)
        self.btnDesactiva = QtWidgets.QPushButton(self.centralwidget)
        self.btnDesactiva.setObjectName("btnDesactiva")
        self.gridLayout.addWidget(self.btnDesactiva, 2, 1, 1, 1)
        self.btnConectar = QtWidgets.QPushButton(self.centralwidget)
        self.btnConectar.setObjectName("btnConectar")
        self.gridLayout.addWidget(self.btnConectar, 2, 0, 1, 1)
        self.btnSendData = QtWidgets.QPushButton(self.centralwidget)
        self.btnSendData.setObjectName("btnSendData")
        self.gridLayout.addWidget(self.btnSendData, 10, 1, 1, 5)
        self.txtbIP = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.txtbIP.setFont(font)
        self.txtbIP.setObjectName("txtbIP")
        self.gridLayout.addWidget(self.txtbIP, 0, 2, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.cmbScene04 = QtWidgets.QComboBox(self.centralwidget)
        self.cmbScene04.setObjectName("cmbScene04")
        self.cmbScene04.addItem("")
        self.cmbScene04.addItem("")
        self.cmbScene04.addItem("")
        self.cmbScene04.addItem("")
        self.gridLayout.addWidget(self.cmbScene04, 5, 1, 1, 1)
        self.cmbPres04 = QtWidgets.QComboBox(self.centralwidget)
        self.cmbPres04.setObjectName("cmbPres04")
        self.cmbPres04.addItem("")
        self.cmbPres04.addItem("")
        self.cmbPres04.addItem("")
        self.cmbPres04.addItem("")
        self.cmbPres04.addItem("")
        self.cmbPres04.addItem("")
        self.cmbPres04.addItem("")
        self.cmbPres04.addItem("")
        self.cmbPres04.addItem("")
        self.cmbPres04.addItem("")
        self.cmbPres04.addItem("")
        self.gridLayout.addWidget(self.cmbPres04, 5, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 1, 1, 1)
        self.cmbSceneCE1 = QtWidgets.QComboBox(self.centralwidget)
        self.cmbSceneCE1.setObjectName("cmbSceneCE1")
        self.cmbSceneCE1.addItem("")
        self.cmbSceneCE1.addItem("")
        self.cmbSceneCE1.addItem("")
        self.cmbSceneCE1.addItem("")
        self.gridLayout.addWidget(self.cmbSceneCE1, 5, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.cmbScene12 = QtWidgets.QComboBox(self.centralwidget)
        self.cmbScene12.setObjectName("cmbScene12")
        self.cmbScene12.addItem("")
        self.cmbScene12.addItem("")
        self.cmbScene12.addItem("")
        self.cmbScene12.addItem("")
        self.gridLayout.addWidget(self.cmbScene12, 6, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 5, 1, 1)
        self.cmbPres12 = QtWidgets.QComboBox(self.centralwidget)
        self.cmbPres12.setObjectName("cmbPres12")
        self.cmbPres12.addItem("")
        self.cmbPres12.addItem("")
        self.cmbPres12.addItem("")
        self.cmbPres12.addItem("")
        self.cmbPres12.addItem("")
        self.cmbPres12.addItem("")
        self.cmbPres12.addItem("")
        self.cmbPres12.addItem("")
        self.cmbPres12.addItem("")
        self.cmbPres12.addItem("")
        self.cmbPres12.addItem("")
        self.gridLayout.addWidget(self.cmbPres12, 6, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.cmbSceneCE2 = QtWidgets.QComboBox(self.centralwidget)
        self.cmbSceneCE2.setObjectName("cmbSceneCE2")
        self.cmbSceneCE2.addItem("")
        self.cmbSceneCE2.addItem("")
        self.cmbSceneCE2.addItem("")
        self.cmbSceneCE2.addItem("")
        self.gridLayout.addWidget(self.cmbSceneCE2, 6, 5, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 2, 1, 2)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 5, 4, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 8, 4, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 9, 4, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 6, 4, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 7, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        Air_Modulation.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Air_Modulation)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 732, 26))
        self.menubar.setObjectName("menubar")
        Air_Modulation.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Air_Modulation)
        self.statusbar.setObjectName("statusbar")
        Air_Modulation.setStatusBar(self.statusbar)

        # ---------------------------------------------------------------------------------------
        self.btnSendData.clicked.connect(self.send_data_pressed)
        # ---------------------------------------------------------------------------------------

        self.retranslateUi(Air_Modulation)
        QtCore.QMetaObject.connectSlotsByName(Air_Modulation)
    # -------------------------------------------------------------------------------------------
    def send_data_pressed(self):
        # -----------------------------------------------------------------------------------------------------
        #                                              Sopladoras
        # -----------------------------------------------------------------------------------------------------
        # Datos Sopladora 4
        scene_SBO04 = self.cmbScene04.currentText()
        cap_SBO04 = float(self.cmbPres04.currentText())
        # Datos Sopladora 12
        scene_SBO12 = self.cmbScene12.currentText()
        cap_SBO12 = float(self.cmbPres12.currentText())
        # Datos Sopladora 16
        scene_SBO16 = self.cmbScene16.currentText()
        cap_SBO16 = float(self.cmbPres16.currentText())
        # Datos Sopladora 20
        scene_SBO20 = self.cmbScene20.currentText()
        cap_SBO20 = float(self.cmbPres20.currentText())
        # Datos Sopladora 10
        scene_SBO10 = self.cmbScene10.currentText()
        cap_SBO10 = float(self.cmbPres10.currentText())
        
        # -----------------------------------------------------------------------------------------------------
        # Proceso de Cálculo - Sopladora 4
        # -----------------------------------------------------------------------------------------------------
        SBO04 = SBO04_0.iloc[0:11, 1:3].to_numpy()
        # División de array en volumen y velocidad
        vol_SBO04 = SBO04[:, 0]                                 # Volumen
        vel_SBO04 = SBO04[:, 1]                                 # Velocidad
        # Velocidad del escenario
        index_SBO04 = np.where(vol_SBO04 == cap_SBO04)          # Indice de elemento en array
        
        if scene_SBO04 == 'Activo':
            cad_SBO04 = vel_SBO04[index_SBO04]                  # Valor respecto a presentación producida
            flow_SBO04 = float(flow(cad_SBO04, cap_SBO04))
            consumo_SBO04 = 40
        else:
            cad_SBO04 = 0                                       # Valor respecto a presentación producida
            flow_SBO04 = 0
            consumo_SBO04 = 0
        # -----------------------------------------------------------------------------------------------------
        # Proceso de Cálculo - Sopladora 12
        # -----------------------------------------------------------------------------------------------------
        SBO12 = SBO12_0.iloc[0:11, 1:3].to_numpy()
        # División de array en volumen y velocidad
        vol_SBO12 = SBO12[:, 0]                                 # Volumen
        vel_SBO12 = SBO12[:, 1]                                 # Velocidad
        # Velocidad del escenario
        index_SBO12 = np.where(vol_SBO12 == cap_SBO12)          # Indice de elemento en array
        
        if scene_SBO12 == 'Activo':
            cad_SBO12 = vel_SBO12[index_SBO12]                  # Valor respecto a presentación producida
            flow_SBO12 = float(flow(cad_SBO12, cap_SBO12))
            consumo_SBO12 = 45
        else:
            cad_SBO12 = 0                                       # Valor respecto a presentación producida
            flow_SBO12 = 0
            consumo_SBO12 = 0
        # -----------------------------------------------------------------------------------------------------
        # Proceso de Cálculo - Sopladora 16
        # -----------------------------------------------------------------------------------------------------
        SBO16 = SBO16_0.iloc[0:11, 1:3].to_numpy()
        # División de array en volumen y velocidad
        vol_SBO16 = SBO16[:, 0]                                 # Volumen
        vel_SBO16 = SBO16[:, 1]                                 # Velocidad
        # Velocidad del escenario
        index_SBO16 = np.where(vol_SBO16 == cap_SBO16)          # Indice de elemento en array
        
        if scene_SBO16 == 'Activo':
            cad_SBO16 = vel_SBO16[index_SBO16]                  # Valor respecto a presentación producida
            flow_SBO16 = float(flow(cad_SBO16, cap_SBO16))
            consumo_SBO16 = 35
        else:
            cad_SBO16 = 0                                       # Valor respecto a presentación producida
            flow_SBO16 = 0
            consumo_SBO16 = 0
        # -----------------------------------------------------------------------------------------------------
        # Proceso de Cálculo - Sopladora 20
        # -----------------------------------------------------------------------------------------------------
        SBO20 = SBO20_0.iloc[0:11, 1:3].to_numpy()
        # División de array en volumen y velocidad
        vol_SBO20 = SBO20[:, 0]                                 # Volumen
        vel_SBO20 = SBO20[:, 1]                                 # Velocidad
        # Velocidad del escenario
        index_SBO20 = np.where(vol_SBO20 == cap_SBO20)          # Indice de elemento en array

        if scene_SBO20 == 'Activo':
            cad_SBO20 = vel_SBO20[index_SBO20]                  # Valor respecto a presentación producida
            flow_SBO20 = float(flow(cad_SBO20, cap_SBO20))
            consumo_SBO20 = 120
        else:
            cad_SBO20 = 0                                       # Valor respecto a presentación producida
            flow_SBO20 = 0
            consumo_SBO20 = 0
        # -----------------------------------------------------------------------------------------------------
        # Proceso de Cálculo - Sopladora 10
        # -----------------------------------------------------------------------------------------------------
        SBO10 = SBO10_0.iloc[0:11, 1:3].to_numpy()
        # División de array en volumen y velocidad
        vol_SBO10 = SBO10[:, 0]                                 # Volumen
        vel_SBO10 = SBO10[:, 1]                                 # Velocidad
        # Velocidad del escenario
        index_SBO10 = np.where(vol_SBO10 == cap_SBO10)          # Indice de elemento en array

        if scene_SBO10 == 'Activo':
            cad_SBO10 = vel_SBO10[index_SBO10]                  # Valor respecto a presentación producida
            flow_SBO10 = float(flow(cad_SBO10, cap_SBO10))
            consumo_SBO10 = 35
        else:
            cad_SBO10 = 0                                       # Valor respecto a presentación producida
            flow_SBO10 = 0
            consumo_SBO10 = 0
        # -----------------------------------------------------------------------------------------------------
        #                                              Compresores
        # -----------------------------------------------------------------------------------------------------
        # Datos Compresor CE 680 B 1
        scene_CE680B_1 = self.cmbSceneCE1.currentText()
        # Datos Compresor CE 680 B 2
        scene_CE680B_2 = self.cmbSceneCE2.currentText()
        # Datos Compresor CE 680 B 3
        scene_CE680B_3 = self.cmbSceneCE3.currentText()
        # Datos Compresor CE 46 S
        scene_CE46S = self.cmbSceneCE46.currentText()
        # Datos Compresor SIAD
        scene_SIAD = self.cmbSceneSIAD.currentText()

        # -----------------------------------------------------------------------------------------------------
        # Proceso de Cálculo - Compresor CE 680 B 1
        # -----------------------------------------------------------------------------------------------------
        if scene_CE680B_1 == 'Activo':
            charge_CE680B_1 = (53 - 9.01) * 0.9
            consumo_CE680B_1 = 580
        else:
            charge_CE680B_1 = 0
            consumo_CE680B_1 = 0
        # -----------------------------------------------------------------------------------------------------
        # Proceso de Cálculo - Compresor CE 680 B 2
        # -----------------------------------------------------------------------------------------------------
        if scene_CE680B_2 == 'Activo':
            charge_CE680B_2 = (53 - 9.01) * 0.9
            consumo_CE680B_2 = 580
        else:
            charge_CE680B_2 = 0
            consumo_CE680B_2 = 0
        # -----------------------------------------------------------------------------------------------------
        # Proceso de Cálculo - Compresor CE 680 B 3
        # -----------------------------------------------------------------------------------------------------
        if scene_CE680B_3 == 'Activo':
            charge_CE680B_3 = (53 - 9.01) * 0.9
            consumo_CE680B_3 = 580
        else:
            charge_CE680B_3 = 0
            consumo_CE680B_3 = 0
        # -----------------------------------------------------------------------------------------------------
        # Proceso de Cálculo - Compresor CE 46 S
        # -----------------------------------------------------------------------------------------------------
        if scene_CE46S == 'Activo':
            charge_CE46S = (14 - 2.38) * 0.9
            consumo_CE46S = 185
        else:
            charge_CE46S = 0
            consumo_CE46S = 0
        # -----------------------------------------------------------------------------------------------------
        # Proceso de Cálculo - Compresor SIAD
        # -----------------------------------------------------------------------------------------------------
        if scene_SIAD == 'Activo':
            charge_SIAD = (22 - 3.74) * 0.9
            consumo_SIAD = 250
        else:
            charge_SIAD = 0
            consumo_SIAD = 0
        # -----------------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------------
        #                                     Recopilación de Datos Finales
        # -----------------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------------
        # Consumo de Sopladoras
        consumo_blowers = consumo_SBO04 + consumo_SBO10 + consumo_SBO12 + consumo_SBO16 + consumo_SBO20
        # Consumo de Compresores
        consumo_compressors = consumo_CE680B_1 + consumo_CE680B_2 + consumo_CE680B_3 + consumo_CE46S + consumo_SIAD
        # Consumo Total
        consumo_total = 1.1 * (consumo_blowers + consumo_compressors)
        # Producción Total
        total_prod = float(cad_SBO04 + cad_SBO10 + cad_SBO12 + cad_SBO16 + cad_SBO20)
        # Indicador de consumo por millar
        final_index = float(1000 * (consumo_total / total_prod))
        # Caudal Total
        total_flow = 1.05 * (flow_SBO04 + flow_SBO10 + flow_SBO12 + flow_SBO16 + flow_SBO20)
        # Exceso de Aire
        total_charge = charge_CE680B_1 + charge_CE680B_2 + charge_CE680B_3 + charge_CE46S + charge_SIAD
        air_excess = -(-total_flow + total_charge)
        # -----------------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------------
        #                                       Despliegue de Datos Finales
        # -----------------------------------------------------------------------------------------------------
        # -----------------------------------------------------------------------------------------------------
        print('Consumo de Sopladoras = ', consumo_blowers)
        print('Consumo de Compresores = ', consumo_compressors)
        print('Consumo Total = ', consumo_total)
        print('Producción Total = ', total_prod)
        print('Indicador de Consumo = ', final_index)
        print('--------------------------------------------------------------------------------')
        print('Caudal Total = ', total_flow)
        print('Exceso de Aire = ', air_excess)
        if air_excess <= 0:
            print('Suficiente Aire.')
        else:
            print('Deficiencia de Aire')
    # -------------------------------------------------------------------------------------------

    def retranslateUi(self, Air_Modulation):
        _translate = QtCore.QCoreApplication.translate
        Air_Modulation.setWindowTitle(_translate("Air_Modulation", "Air_Modulation"))
        self.label_7.setText(_translate("Air_Modulation", "SBO 20"))
        self.cmbScene20.setItemText(0, _translate("Air_Modulation", "Activo"))
        self.cmbScene20.setItemText(1, _translate("Air_Modulation", "Paro Programado"))
        self.cmbScene20.setItemText(2, _translate("Air_Modulation", "Mantenimiento"))
        self.cmbScene20.setItemText(3, _translate("Air_Modulation", "Silos Llenos"))
        self.cmbScene16.setItemText(0, _translate("Air_Modulation", "Activo"))
        self.cmbScene16.setItemText(1, _translate("Air_Modulation", "Paro Programado"))
        self.cmbScene16.setItemText(2, _translate("Air_Modulation", "Mantenimiento"))
        self.cmbScene16.setItemText(3, _translate("Air_Modulation", "Silos Llenos"))
        self.cmbPres20.setItemText(0, _translate("Air_Modulation", "0.355"))
        self.cmbPres20.setItemText(1, _translate("Air_Modulation", "0.400"))
        self.cmbPres20.setItemText(2, _translate("Air_Modulation", "0.500"))
        self.cmbPres20.setItemText(3, _translate("Air_Modulation", "0.600"))
        self.cmbPres20.setItemText(4, _translate("Air_Modulation", "0.750"))
        self.cmbPres20.setItemText(5, _translate("Air_Modulation", "1.000"))
        self.cmbPres20.setItemText(6, _translate("Air_Modulation", "1.500"))
        self.cmbPres20.setItemText(7, _translate("Air_Modulation", "2.000"))
        self.cmbPres20.setItemText(8, _translate("Air_Modulation", "2.500"))
        self.cmbPres20.setItemText(9, _translate("Air_Modulation", "3.000"))
        self.cmbPres20.setItemText(10, _translate("Air_Modulation", "3.300"))
        self.cmbPres16.setItemText(0, _translate("Air_Modulation", "0.355"))
        self.cmbPres16.setItemText(1, _translate("Air_Modulation", "0.400"))
        self.cmbPres16.setItemText(2, _translate("Air_Modulation", "0.500"))
        self.cmbPres16.setItemText(3, _translate("Air_Modulation", "0.600"))
        self.cmbPres16.setItemText(4, _translate("Air_Modulation", "0.750"))
        self.cmbPres16.setItemText(5, _translate("Air_Modulation", "1.000"))
        self.cmbPres16.setItemText(6, _translate("Air_Modulation", "1.500"))
        self.cmbPres16.setItemText(7, _translate("Air_Modulation", "2.000"))
        self.cmbPres16.setItemText(8, _translate("Air_Modulation", "2.500"))
        self.cmbPres16.setItemText(9, _translate("Air_Modulation", "3.000"))
        self.cmbPres16.setItemText(10, _translate("Air_Modulation", "3.300"))
        self.cmbSceneCE3.setItemText(0, _translate("Air_Modulation", "Activo"))
        self.cmbSceneCE3.setItemText(1, _translate("Air_Modulation", "Fuera de Servicio"))
        self.cmbSceneCE3.setItemText(2, _translate("Air_Modulation", "Mantenimiento"))
        self.cmbSceneCE3.setItemText(3, _translate("Air_Modulation", "Standby"))
        self.cmbSceneCE46.setItemText(0, _translate("Air_Modulation", "Activo"))
        self.cmbSceneCE46.setItemText(1, _translate("Air_Modulation", "Fuera de Servicio"))
        self.cmbSceneCE46.setItemText(2, _translate("Air_Modulation", "Mantenimiento"))
        self.cmbSceneCE46.setItemText(3, _translate("Air_Modulation", "Standby"))
        self.label_8.setText(_translate("Air_Modulation", "SBO 10"))
        self.cmbPres10.setItemText(0, _translate("Air_Modulation", "0.355"))
        self.cmbPres10.setItemText(1, _translate("Air_Modulation", "0.400"))
        self.cmbPres10.setItemText(2, _translate("Air_Modulation", "0.500"))
        self.cmbPres10.setItemText(3, _translate("Air_Modulation", "0.600"))
        self.cmbPres10.setItemText(4, _translate("Air_Modulation", "0.750"))
        self.cmbPres10.setItemText(5, _translate("Air_Modulation", "1.000"))
        self.cmbPres10.setItemText(6, _translate("Air_Modulation", "1.500"))
        self.cmbPres10.setItemText(7, _translate("Air_Modulation", "2.000"))
        self.cmbPres10.setItemText(8, _translate("Air_Modulation", "2.500"))
        self.cmbPres10.setItemText(9, _translate("Air_Modulation", "3.000"))
        self.cmbPres10.setItemText(10, _translate("Air_Modulation", "3.300"))
        self.cmbSceneSIAD.setItemText(0, _translate("Air_Modulation", "Activo"))
        self.cmbSceneSIAD.setItemText(1, _translate("Air_Modulation", "Fuera de Servicio"))
        self.cmbSceneSIAD.setItemText(2, _translate("Air_Modulation", "Mantenimiento"))
        self.cmbSceneSIAD.setItemText(3, _translate("Air_Modulation", "Standby"))
        self.cmbScene10.setItemText(0, _translate("Air_Modulation", "Activo"))
        self.cmbScene10.setItemText(1, _translate("Air_Modulation", "Paro Programado"))
        self.cmbScene10.setItemText(2, _translate("Air_Modulation", "Mantenimiento"))
        self.cmbScene10.setItemText(3, _translate("Air_Modulation", "Silos Llenos"))
        self.label_12.setText(_translate("Air_Modulation", "Compresores"))
        self.label_2.setText(_translate("Air_Modulation", "Estado de conexión:"))
        self.label.setText(_translate("Air_Modulation", "Direccion IP:"))
        self.lblEtiqueta.setText(_translate("Air_Modulation", "Esperando..."))
        self.btnDesactiva.setText(_translate("Air_Modulation", "Desconectar"))
        self.btnConectar.setText(_translate("Air_Modulation", "Conectar"))
        self.btnSendData.setText(_translate("Air_Modulation", "Enviar"))
        self.txtbIP.setText(_translate("Air_Modulation", "192.168.0.0"))
        self.label_6.setText(_translate("Air_Modulation", "SBO 16"))
        self.cmbScene04.setItemText(0, _translate("Air_Modulation", "Activo"))
        self.cmbScene04.setItemText(1, _translate("Air_Modulation", "Paro Programado"))
        self.cmbScene04.setItemText(2, _translate("Air_Modulation", "Mantenimiento"))
        self.cmbScene04.setItemText(3, _translate("Air_Modulation", "Silos Llenos"))
        self.cmbPres04.setItemText(0, _translate("Air_Modulation", "0.355"))
        self.cmbPres04.setItemText(1, _translate("Air_Modulation", "0.400"))
        self.cmbPres04.setItemText(2, _translate("Air_Modulation", "0.500"))
        self.cmbPres04.setItemText(3, _translate("Air_Modulation", "0.600"))
        self.cmbPres04.setItemText(4, _translate("Air_Modulation", "0.750"))
        self.cmbPres04.setItemText(5, _translate("Air_Modulation", "1.000"))
        self.cmbPres04.setItemText(6, _translate("Air_Modulation", "1.500"))
        self.cmbPres04.setItemText(7, _translate("Air_Modulation", "2.000"))
        self.cmbPres04.setItemText(8, _translate("Air_Modulation", "2.500"))
        self.cmbPres04.setItemText(9, _translate("Air_Modulation", "3.000"))
        self.cmbPres04.setItemText(10, _translate("Air_Modulation", "3.300"))
        self.label_9.setText(_translate("Air_Modulation", "Escenario"))
        self.cmbSceneCE1.setItemText(0, _translate("Air_Modulation", "Activo"))
        self.cmbSceneCE1.setItemText(1, _translate("Air_Modulation", "Fuera de Servicio"))
        self.cmbSceneCE1.setItemText(2, _translate("Air_Modulation", "Mantenimiento"))
        self.cmbSceneCE1.setItemText(3, _translate("Air_Modulation", "Standby"))
        self.label_5.setText(_translate("Air_Modulation", "SBO 12"))
        self.cmbScene12.setItemText(0, _translate("Air_Modulation", "Activo"))
        self.cmbScene12.setItemText(1, _translate("Air_Modulation", "Paro Programado"))
        self.cmbScene12.setItemText(2, _translate("Air_Modulation", "Mantenimiento"))
        self.cmbScene12.setItemText(3, _translate("Air_Modulation", "Silos Llenos"))
        self.label_11.setText(_translate("Air_Modulation", "Escenario"))
        self.cmbPres12.setItemText(0, _translate("Air_Modulation", "0.355"))
        self.cmbPres12.setItemText(1, _translate("Air_Modulation", "0.400"))
        self.cmbPres12.setItemText(2, _translate("Air_Modulation", "0.500"))
        self.cmbPres12.setItemText(3, _translate("Air_Modulation", "0.600"))
        self.cmbPres12.setItemText(4, _translate("Air_Modulation", "0.750"))
        self.cmbPres12.setItemText(5, _translate("Air_Modulation", "1.000"))
        self.cmbPres12.setItemText(6, _translate("Air_Modulation", "1.500"))
        self.cmbPres12.setItemText(7, _translate("Air_Modulation", "2.000"))
        self.cmbPres12.setItemText(8, _translate("Air_Modulation", "2.500"))
        self.cmbPres12.setItemText(9, _translate("Air_Modulation", "3.000"))
        self.cmbPres12.setItemText(10, _translate("Air_Modulation", "3.300"))
        self.label_4.setText(_translate("Air_Modulation", "SBO 04"))
        self.cmbSceneCE2.setItemText(0, _translate("Air_Modulation", "Activo"))
        self.cmbSceneCE2.setItemText(1, _translate("Air_Modulation", "Fuera de Servicio"))
        self.cmbSceneCE2.setItemText(2, _translate("Air_Modulation", "Mantenimiento"))
        self.cmbSceneCE2.setItemText(3, _translate("Air_Modulation", "Standby"))
        self.label_10.setText(_translate("Air_Modulation", "Presentación"))
        self.label_15.setText(_translate("Air_Modulation", "CE 680 B"))
        self.label_17.setText(_translate("Air_Modulation", "CE 46 S"))
        self.label_13.setText(_translate("Air_Modulation", "SIAD"))
        self.label_16.setText(_translate("Air_Modulation", "CE 680 B"))
        self.label_14.setText(_translate("Air_Modulation", "CE 680 B"))
        self.label_3.setText(_translate("Air_Modulation", "Sopladoras"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Air_Modulation = QtWidgets.QMainWindow()
    ui = Ui_Air_Modulation()
    ui.setupUi(Air_Modulation)
    Air_Modulation.show()
    sys.exit(app.exec_())
