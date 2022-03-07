# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 12:40:14 2021

@author: Andrés Cadena Díaz
"""
# from PyQt5.QtGui import *

# from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from AgStat_ui import *
from InfoDlg import Ui_Dialog
from ClientDatabase import *
from AgStatFileSystem import *
import AgStatPlots as asp
import AgStatProcessing as prc
import shutil, os


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.stackedWidget.setCurrentIndex(0)
              
        #Combobox indices variables
        self.clientIdx = 0
        self.farmIdx = 0
        self.fieldIdx = 0
        self.cycleIdx = 0
        self.diagnosisIdx = 0
        
        self.comboBoxesInit()
        
        
        #File system init
        global clientFilesDir
        
        usbDir = r'E:\AgStat'
        if not os.path.exists(usbDir):
            os.mkdir(usbDir)            
            
        self.fileSys_L = FileSystem(clientFilesDir, self.files_scrollArea_L)
        self.fileSys_R = FileSystem(usbDir, self.files_scrollArea_R)
        self.files_pushButton_copy.clicked.connect(self.transfer)
        
        

        """    NAVIGATION BUTTON CONNECTIONS /// START    """
        # comment format: #Window Name / variableName / index

        # Main menu / mainMe / 0
        self.mainMe_pushButton_an.clicked.connect(self.to_an_me)
        self.mainMe_pushButton_aq.clicked.connect(self.to_aq_me)
        self.mainMe_pushButton_fi.clicked.connect(self.to_files)
        # self.mainMe_pushButton_se.clicked.connects(self)

        # Analysis menu / an_me / 1
        self.an_me_pushButton_home.clicked.connect(self.to_mainMe)
        self.an_me_pushButton_gRx.clicked.connect(self.to_an_gRx1)
        self.an_me_pushButton_vi.clicked.connect(self.to_an_vi_me)
        # self.an_me_pushButton_help.clicked.connect(self)

        # Analysis - Generate Rx1 / an_gRx1 / 2
        self.an_gRx1_pushButton_home.clicked.connect(self.to_mainMe)
        self.an_gRx1_pushButton_next.clicked.connect(self.to_an_gRx2)
        self.an_gRx1_pushButton_previous.clicked.connect(self.to_an_me)
        # self.an_gRx1_pushButton_help.clicked.connect(self)

        # Analysis - Generate Rx2 / an_gRx2 / 3
        self.an_gRx2_pushButton_home.clicked.connect(self.to_mainMe)
        self.an_gRx2_pushButton_next.clicked.connect(self.to_an_gRx3)
        self.an_gRx2_pushButton_previous.clicked.connect(self.to_an_gRx1)
        # self.an_gRx2_pushButton_help.clicked.connect(self)

        # Analysis - Generate Rx3 / an_gRx3 / 4
        self.an_gRx3_pushButton_home.clicked.connect(self.to_mainMe)
        self.an_gRx3_pushButton_next.clicked.connect(self.to_an_gRx4)
        self.an_gRx3_pushButton_previous.clicked.connect(self.to_an_gRx2)
        # self.an_gRx3_pushButtohelp.clicked.connect(self)

        # Analysis - Generate Rx4 (confirm data)/ an_gRx4 / 5
        self.an_gRx4_pushButton_home.clicked.connect(self.to_mainMe)
        self.an_gRx4_pushButton_previous.clicked.connect(self.to_an_gRx3)
        #self.an_gRx4_pushButton_generateRx.clicked.connect(self.to_an_gRx5)
        # self.an_gRx4_pushButton_help.clicked.connect(self)

        # Analysis - Generate Rx5 (plot) / an_gRx5 / 6
        self.an_gRx5_pushButton_home.clicked.connect(self.to_mainMe)
        self.an_gRx5_pushButton_ecEs.clicked.connect(self.to_an_gRx6)
        self.an_gRx5_pushButton_exportRx.clicked.connect(self.to_an_gRx7)
        self.an_gRx5_pushButton_back.clicked.connect(self.to_an_gRx4)
        # self.an_gRx5_pushButton_help.clicked.connect(self)

        # Analysis - Generate Rx6 (economic estimate) / an_gRx6 / 7
        self.an_gRx6_pushButton_home.clicked.connect(self.to_mainMe)
        self.an_gRx6_pushButton_back.clicked.connect(self.to_an_gRx5)
        # self.an_gRx6_pushButton_help.clicked.connect(self)

        # Analysis - Generate Rx7 (export Rx) / an_gRx7 / 8
        self.an_gRx7_pushButton_home.clicked.connect(self.to_mainMe)
        self.an_gRx7_pushButton_back.clicked.connect(self.to_an_gRx5)
        # self.an_gRx7_pushButton_help.clicked.connect(self)

        # Analysis - Visualization menu / an_vi_me / 9
        self.an_vi_me_pushButton_home.clicked.connect(self.to_mainMe)
        (self.an_vi_me_pushButton_diagnosisMaps.clicked
         .connect(self.to_an_vi_dMa))
        (self.an_vi_me_pushButton_distribution.clicked
         .connect(self.to_an_vi_di))
        self.an_vi_me_pushButton_scatter.clicked.connect(self.to_an_vi_sc)
        self.an_vi_me_pushButton_regression.clicked.connect(self.to_an_vi_re)
        # self.an_vi_me_pushButton_help.clicked.connect(self)

        # Analysis - Visualization - Diagnosis maps / an_vi_dMa / 10
        self.an_vi_dMa_pushButton_home.clicked.connect(self.to_mainMe)
        self.an_vi_dMa_pushButton_back.clicked.connect(self.to_an_vi_me)
        # self.an_vi_dMa_pushButton_help.clicked.connect(self)

        # Analysis - Visualization - Distribution / an_vi_di / 11
        self.an_vi_di_pushButton_home.clicked.connect(self.to_mainMe)
        self.an_vi_di_pushButton_back.clicked.connect(self.to_an_vi_me)
        # self.an_vi_di_pushButton_help.clicked.connect(self)

        # Analysis - Visualization - Scatter / an_vi_sc / 12
        self.an_vi_sc_pushButton_home.clicked.connect(self.to_mainMe)
        self.an_vi_sc_pushButton_back.clicked.connect(self.to_an_vi_me)
        # self.an_vi_sc_pushButton_help.clicked.connect(self)

        # Analysis - Visualization - Regression / an_vi_re / 13
        self.an_vi_re_pushButton_home.clicked.connect(self.to_mainMe)
        self.an_vi_re_pushButton_back.clicked.connect(self.to_an_vi_me)
        # self.an_vi_re_pushButton_help.clicked.connect(self)

        # Survey screen 1 / su1 / 14
        self.su1_pushButton_home.clicked.connect(self.to_mainMe)
        self.su1_pushButton_next.clicked.connect(self.to_su2)
        self.su1_pushButton_previous.clicked.connect(self.to_mainMe)
        # self.su1_pushButton_help.clicked.connect(self)

        # Survey screen 2 / su2 / 15
        self.su2_pushButton_home.clicked.connect(self.to_mainMe)
        self.su2_pushButton_next.clicked.connect(self.to_su3)
        self.su2_pushButton_previous.clicked.connect(self.to_su1)
        # self.su2_pushButton_help.clicked.connect(self)

        # Survey screen 3 / su3 / 16
        self.su3_pushButton_home.clicked.connect(self.to_mainMe)
        self.su3_pushButton_goToCapture.clicked.connect(self.to_survey)
        self.su3_pushButton_back.clicked.connect(self.to_su2)
        # self.su3_pushButton_help.clicked.connect(self)

        # Continuous survey screen / suC / 17
        self.suC_pushButton_back.clicked.connect(self.to_su3)
        # self.suC_pushButton_help.clicked.connect(self)

        # Punctual survey screen / suP / 18
        self.suP_pushButton_back.clicked.connect(self.to_su3)
        
        # Data aquisition menu
        self.aq_menu_pushButton_field.clicked.connect(self.to_su1)
        self.aq_menu_pushButton_home.clicked.connect(self.to_mainMe)
        self.aq_menu_pushButton_scattered.clicked.connect(self.to_aq_sc1)
        
        
        # Data aquisition scattered 1
        self.aq_sc1_pushButton_home.clicked.connect(self.to_mainMe)
        self.aq_sc1_pushButton_next.clicked.connect(self.to_aq_sc2)
        self.aq_sc1_pushButton_previous.clicked.connect(self.to_aq_me)
        
        
        # Data aquisition scattered 2
        self.aq_sc2_pushButton_home.clicked.connect(self.to_mainMe)        
        self.aq_sc2_pushButton_previous.clicked.connect(self.to_aq_sc1)
        
        # File system
        self.files_pushButton_home.clicked.connect(self.to_mainMe)
       
        
        
        # self.suP_pushButton_help.clicked.connect(self)
        
        """    NAVIGATION BUTTON CONNECTIONS /// END    """

        
        """    ACTION BUTTON CONNECTIONS /// START    """
          #PLOTS
        self.an_vi_dMa_pushButton_generate.clicked.connect(self.plotDMap)
        self.an_vi_di_pushButton_generate.clicked.connect(self.plotHist)
        self.an_vi_sc_pushButton_generate.clicked.connect(self.plotScatter)
        self.an_vi_re_pushButton_generate.clicked.connect(self.plotReg)
        


        # Add scattered data
        self.aq_sc2_pushButton_add.clicked.connect(self.succesfulAdd)
        
        
        #Generate rx
        self.an_gRx4_pushButton_generateRx.clicked.connect(self.generateRx)

        # Export RX temporarily set as navigation to main menu
        self.an_gRx7_pushButton_exportRx.clicked.connect(self.exportRx)

        """    ACTION BUTTON CONNECTIONS /// END   """


        """    COMBO BOXES CONNECTIONS /// START  """

        # Generate Rx1 / gRx1
        (self.an_gRx1_comboBox_client.currentIndexChanged
         .connect(self.gRx1ClientChanged))
        (self.an_gRx1_comboBox_farm.currentIndexChanged
         .connect(self.gRx1FarmChanged))
        (self.an_gRx1_comboBox_field.currentIndexChanged
         .connect(self.gRx1FieldChanged))

        # Diagnosis Maps / an_vi_dMa
        (self.an_vi_dMa_comboBox_client.currentIndexChanged
         .connect(self.dMaClientChanged))
        (self.an_vi_dMa_comboBox_farm.currentIndexChanged
         .connect(self.dMaFarmChanged))
        (self.an_vi_dMa_comboBox_field.currentIndexChanged
         .connect(self.dMaFieldChanged))
        (self.an_vi_dMa_comboBox_cycle.currentIndexChanged
         .connect(self.dMaCycleChanged))
        (self.an_vi_dMa_comboBox_variable.currentIndexChanged
         .connect(self.dMaVariableChanged))
       
        
        # Distribution plot / an_vi_di
        (self.an_vi_di_comboBox_client.currentIndexChanged
         .connect(self.diClientChanged))
        (self.an_vi_di_comboBox_farm.currentIndexChanged
         .connect(self.diFarmChanged))
        (self.an_vi_di_comboBox_field.currentIndexChanged
         .connect(self.diFieldChanged))
        (self.an_vi_di_comboBox_cycle.currentIndexChanged
         .connect(self.diCycleChanged))
        (self.an_vi_di_comboBox_variable.currentIndexChanged
         .connect(self.diVariableChanged))

        # Scatter plot / an_vi_sc
        (self.an_vi_sc_comboBox_client.currentIndexChanged
         .connect(self.scClientChanged))
        (self.an_vi_sc_comboBox_farm.currentIndexChanged
         .connect(self.scFarmChanged))
        (self.an_vi_sc_comboBox_field.currentIndexChanged
         .connect(self.scFieldChanged))
        (self.an_vi_sc_comboBox_cycle.currentIndexChanged
         .connect(self.scCycleChanged))
        (self.an_vi_sc_comboBox_variableX.currentIndexChanged
         .connect(self.scVariableXChanged))
        (self.an_vi_sc_comboBox_variableY.currentIndexChanged
         .connect(self.scVariableYChanged))
        

        # Regression plot / an_vi_re
        (self.an_vi_re_comboBox_client.currentIndexChanged
         .connect(self.reClientChanged))
        (self.an_vi_re_comboBox_farm.currentIndexChanged
         .connect(self.reFarmChanged))
        (self.an_vi_re_comboBox_field.currentIndexChanged
         .connect(self.reFieldChanged))
        (self.an_vi_re_comboBox_cycle.currentIndexChanged
         .connect(self.reCycleChanged))
        (self.an_vi_re_comboBox_variableX.currentIndexChanged
         .connect(self.reVariableXChanged))
        (self.an_vi_re_comboBox_variableY.currentIndexChanged
         .connect(self.reVariableYChanged))
        
        
        # Survey screen 1 / su1
        (self.su1_comboBox_client.currentIndexChanged
         .connect(self.su1ClientChanged))
        (self.su1_comboBox_farm.currentIndexChanged
         .connect(self.su1FarmChanged))
        (self.su1_comboBox_field.currentIndexChanged
         .connect(self.su1FieldChanged))
        

        """    COMBO BOXES CONNECTIONS /// END    """

    ###Start of Navigation functions (go to page X)

    def to_mainMe(self):
        self.stackedWidget.setCurrentIndex(0)

    def to_an_me(self):
        self.stackedWidget.setCurrentIndex(1)

    def to_an_gRx1(self):
        self.stackedWidget.setCurrentIndex(2)

    def to_an_gRx2(self):
        self.stackedWidget.setCurrentIndex(3)

    def to_an_gRx3(self):
        self.stackedWidget.setCurrentIndex(4)

    def to_an_gRx4(self):
        self.stackedWidget.setCurrentIndex(5)
        self.fillDataLabel()

    def to_an_gRx5(self):
        self.stackedWidget.setCurrentIndex(6)

    def to_an_gRx6(self):
        self.stackedWidget.setCurrentIndex(7)

    def to_an_gRx7(self):
        self.stackedWidget.setCurrentIndex(8)

    def to_an_vi_me(self):
        self.stackedWidget.setCurrentIndex(9)

    def to_an_vi_dMa(self):
        self.stackedWidget.setCurrentIndex(10)

    def to_an_vi_di(self):
        self.stackedWidget.setCurrentIndex(11)

    def to_an_vi_sc(self):
        self.stackedWidget.setCurrentIndex(12)

    def to_an_vi_re(self):
        self.stackedWidget.setCurrentIndex(13)

    def to_su1(self):
        self.stackedWidget.setCurrentIndex(14)

    def to_su2(self):
        self.stackedWidget.setCurrentIndex(15)

    def to_su3(self):
        self.stackedWidget.setCurrentIndex(16)

    def to_survey(self):
        if (self.su2_comboBox_mode.currentIndex()) == 0:  # Punctual survey
            self.stackedWidget.setCurrentIndex(18)
        else:  # Continuous survey
            self.stackedWidget.setCurrentIndex(17)
            
    def to_aq_me(self):
        self.stackedWidget.setCurrentIndex(19)
        
    def to_aq_sc1(self):
        self.stackedWidget.setCurrentIndex(20)
    
    def to_aq_sc2(self):
        self.stackedWidget.setCurrentIndex(21)
        
    def to_files(self):
        self.stackedWidget.setCurrentIndex(22)
        
        
        

    ###End of Navigation functions (go to page X)

    ###Start of combo box functions
    
    def comboBoxesInit(self):
        self.setClientNamesCBs()
        self.setFarmNamesCBs()
        self.setFieldNamesCBs()    
        self.setCycleNamesCBs()
        self.setDiagnosisNamesCBs()
        self.an_vi_di_comboBox_nBins.setCurrentIndex(10)

    
    #Individual combobox functions
    def gRx1ClientChanged(self):
        self.clientIdx = self.an_gRx1_comboBox_client.currentIndex()
        self.clientChanged()
        
    def dMaClientChanged(self):
        self.clientIdx = self.an_vi_dMa_comboBox_client.currentIndex()
        self.clientChanged()
        
    def diClientChanged(self):
        self.clientIdx = self.an_vi_di_comboBox_client.currentIndex()
        self.clientChanged()
        
    def scClientChanged(self):
        self.clientIdx = self.an_vi_sc_comboBox_client.currentIndex()
        self.clientChanged()
        
    def reClientChanged(self):
        self.clientIdx = self.an_vi_re_comboBox_client.currentIndex()
        self.clientChanged()
        
    def su1ClientChanged(self):
        self.clientIdx = self.su1_comboBox_client.currentIndex()
        self.clientChanged()  

    def gRx1FarmChanged(self):
        self.farmIdx = self.an_gRx1_comboBox_farm.currentIndex()
        self.farmChanged()
        
    def dMaFarmChanged(self):
        self.farmIdx = self.an_vi_dMa_comboBox_farm.currentIndex()
        self.farmChanged()
        
    def diFarmChanged(self):
        self.farmIdx = self.an_vi_di_comboBox_farm.currentIndex()
        self.farmChanged()
        
    def scFarmChanged(self):
        self.farmIdx = self.an_vi_sc_comboBox_farm.currentIndex()
        self.farmChanged()
        
    def reFarmChanged(self):
        self.farmIdx = self.an_vi_re_comboBox_farm.currentIndex()
        self.farmChanged()
        
    def su1FarmChanged(self):
        self.farmIdx = self.su1_comboBox_farm.currentIndex()
        self.farmChanged()
                    
    def gRx1FieldChanged(self):
        self.fieldIdx = self.an_gRx1_comboBox_field.currentIndex()
        self.fieldChanged()
        
    def dMaFieldChanged(self):
        self.fieldIdx = self.an_vi_dMa_comboBox_field.currentIndex()
        self.fieldChanged()
        
    def diFieldChanged(self):
        self.fieldIdx = self.an_vi_di_comboBox_field.currentIndex()
        self.fieldChanged()
        
    def scFieldChanged(self):
        self.fieldIdx = self.an_vi_sc_comboBox_field.currentIndex()
        self.fieldChanged()
        
    def reFieldChanged(self):
        self.fieldIdx = self.an_vi_re_comboBox_field.currentIndex()
        self.fieldChanged()
        
    def su1FieldChanged(self):
        self.fieldIdx = self.su1_comboBox_field.currentIndex()
        self.fieldChanged()  
        
    def dMaCycleChanged(self):
        self.cycleIdx = self.an_vi_dMa_comboBox_cycle.currentIndex()
        self.cycleChanged()
        
    def diCycleChanged(self):
        self.cycleIdx = self.an_vi_di_comboBox_cycle.currentIndex()
        self.cycleChanged()
    
    def scCycleChanged(self):
        self.cycleIdx = self.an_vi_sc_comboBox_cycle.currentIndex()
        self.cycleChanged()
        
    def reCycleChanged(self):
        self.cycleIdx = self.an_vi_re_comboBox_cycle.currentIndex()
        self.cycleChanged()
        
    def dMaVariableChanged(self):
        self.diagnosisIdx = self.an_vi_dMa_comboBox_variable.currentIndex()
        self.diagnosisChanged()

    def diVariableChanged(self):
        self.diagnosisIdx = self.an_vi_di_comboBox_variable.currentIndex()
        self.diagnosisChanged()
        
    def scVariableXChanged(self):
        self.diagnosisIdx = self.an_vi_sc_comboBox_variableX.currentIndex()
        self.diagnosisChanged()
        
    def reVariableXChanged(self):
        self.diagnosisIdx = self.an_vi_re_comboBox_variableX.currentIndex()
        self.diagnosisChanged()
        
    def scVariableYChanged(self):
        idx = self.an_vi_sc_comboBox_variableY.currentIndex()
        self.an_vi_re_comboBox_variableY.setCurrentIndex(idx)

    def reVariableYChanged(self):
        idx = self.an_vi_re_comboBox_variableY.currentIndex()
        self.an_vi_sc_comboBox_variableY.setCurrentIndex(idx)      
        
   
        
        
#General combobox functions        
    def clientChanged(self):            
        self.setClientCBs() #Set client comboboxes to new index                       
        self.resetFarmCBs() #Reset remanining comboboxes 
        self.resetFieldCBs()
        self.resetCycleCBs()
        self.resetDiagnosisCBs()
        
    def farmChanged(self):
        self.setFarmCBs() #Set farm comboboxes to new index
        self.resetFieldCBs() #Reset all field comboboxes
        self.resetCycleCBs()
        self.resetDiagnosisCBs()
        
    def fieldChanged(self):
        self.setFieldCBs()  #Set remaining field comboboxes to new index            
        self.resetCycleCBs()
        self.resetDiagnosisCBs()
        
    def cycleChanged(self):
        self.setCycleCBs()
        self.resetDiagnosisCBs()
        
    def diagnosisChanged(self):
        self.setDiagnosisCBs()
        
    def resetFarmCBs(self):
        self.clearFarmCBs()
        self.setFarmNamesCBs()
        
    def resetFieldCBs(self):
        self.clearFieldCBs()
        self.setFieldNamesCBs() 
        
    def resetCycleCBs(self):
        self.clearCycleCBs()
        self.setCycleNamesCBs()
        
    def resetDiagnosisCBs(self):
        self.clearDiagnosisCBs()
        self.setDiagnosisNamesCBs()
        
    def setClientCBs(self):
        #Sets all client comboboxes to current client index
        self.an_gRx1_comboBox_client.setCurrentIndex(self.clientIdx)
        self.an_vi_dMa_comboBox_client.setCurrentIndex(self.clientIdx)
        self.an_vi_di_comboBox_client.setCurrentIndex(self.clientIdx)
        self.an_vi_sc_comboBox_client.setCurrentIndex(self.clientIdx)
        self.an_vi_re_comboBox_client.setCurrentIndex(self.clientIdx)
        self.su1_comboBox_client.setCurrentIndex(self.clientIdx)
        
    def setFarmCBs(self):
        #Sets all farm comboboxes to current farm index
        self.an_gRx1_comboBox_farm.setCurrentIndex(self.farmIdx)
        self.an_vi_dMa_comboBox_farm.setCurrentIndex(self.farmIdx)
        self.an_vi_di_comboBox_farm.setCurrentIndex(self.farmIdx)
        self.an_vi_sc_comboBox_farm.setCurrentIndex(self.farmIdx)
        self.an_vi_re_comboBox_farm.setCurrentIndex(self.farmIdx)
        self.su1_comboBox_farm.setCurrentIndex(self.farmIdx)
        
    def setFieldCBs(self):
        #Sets all field comboboxes to current field index
        self.an_gRx1_comboBox_field.setCurrentIndex(self.fieldIdx)
        self.an_vi_dMa_comboBox_field.setCurrentIndex(self.fieldIdx)
        self.an_vi_di_comboBox_field.setCurrentIndex(self.fieldIdx)
        self.an_vi_sc_comboBox_field.setCurrentIndex(self.fieldIdx)
        self.an_vi_re_comboBox_field.setCurrentIndex(self.fieldIdx)
        self.su1_comboBox_field.setCurrentIndex(self.fieldIdx) 

    def setCycleCBs(self):
        #Sets all field comboboxes to current cycle index
        self.an_gRx3_comboBox_refCycle.setCurrentIndex(self.cycleIdx)
        self.an_vi_dMa_comboBox_cycle.setCurrentIndex(self.cycleIdx)
        self.an_vi_di_comboBox_cycle.setCurrentIndex(self.cycleIdx)
        self.an_vi_sc_comboBox_cycle.setCurrentIndex(self.cycleIdx)
        self.an_vi_re_comboBox_cycle.setCurrentIndex(self.cycleIdx)
        #self.su1_comboBox_field.setCurrentIndex(self.cycleIdx) 
        
    def setDiagnosisCBs(self):
        #Sets all field comboboxes to current field index
        
        self.an_vi_dMa_comboBox_variable.setCurrentIndex(self.diagnosisIdx)
        self.an_vi_di_comboBox_variable.setCurrentIndex(self.diagnosisIdx)
        self.an_vi_sc_comboBox_variableX.setCurrentIndex(self.diagnosisIdx)
        # self.an_vi_sc_comboBox_variableY.setCurrentIndex(self.diagnosisIdx)
        self.an_vi_re_comboBox_variableX.setCurrentIndex(self.diagnosisIdx)
        # self.an_vi_re_comboBox_variableY.setCurrentIndex(self.diagnosisIdx)
        

          
    def clearFarmCBs(self):
        """Clears all farm comboboxes"""
        self.an_gRx1_comboBox_farm.clear()
        self.an_vi_dMa_comboBox_farm.clear()
        self.an_vi_di_comboBox_farm.clear()
        self.an_vi_sc_comboBox_farm.clear()
        self.an_vi_re_comboBox_farm.clear()
        self.su1_comboBox_farm.clear()           
        
    def clearFieldCBs(self):
        """ Clears all field comboboxes"""
        self.an_gRx1_comboBox_field.clear()
        self.an_vi_dMa_comboBox_field.clear()
        self.an_vi_di_comboBox_field.clear()
        self.an_vi_sc_comboBox_field.clear()
        self.an_vi_re_comboBox_field.clear()
        self.su1_comboBox_field.clear()
        
    def clearCycleCBs(self):
        """Clears all cycle comboboxes"""
        self.an_gRx3_comboBox_refCycle.clear()
        self.an_vi_dMa_comboBox_cycle.clear()
        self.an_vi_di_comboBox_cycle.clear()
        self.an_vi_sc_comboBox_cycle.clear()
        self.an_vi_re_comboBox_cycle.clear()
        #self.su1_comboBox_cycle.clear() 

    def clearDiagnosisCBs(self):
        """Clears all diagnosis comboboxes"""
       
        self.an_vi_dMa_comboBox_variable.clear()
        self.an_vi_di_comboBox_variable.clear()
        self.an_vi_sc_comboBox_variableX.clear()
        self.an_vi_sc_comboBox_variableY.clear()
        self.an_vi_re_comboBox_variableX.clear()
        self.an_vi_re_comboBox_variableY.clear()
                
        

    def setClientNamesCBs(self):
        """Sets list of clients in comboboxes"""
        clientNames = db1.getClientNames()
        self.an_gRx1_comboBox_client.addItems(clientNames)
        self.an_vi_dMa_comboBox_client.addItems(clientNames)
        self.an_vi_di_comboBox_client.addItems(clientNames)
        self.an_vi_sc_comboBox_client.addItems(clientNames)
        self.an_vi_re_comboBox_client.addItems(clientNames)
        self.su1_comboBox_client.addItems(clientNames)
        
    def setFarmNamesCBs(self):
        """Sets list of farms in comboboxes"""
        farmNames = db1.getFarmNames(self.clientIdx)
        self.an_gRx1_comboBox_farm.addItems(farmNames)
        self.an_vi_dMa_comboBox_farm.addItems(farmNames)
        self.an_vi_di_comboBox_farm.addItems(farmNames)
        self.an_vi_sc_comboBox_farm.addItems(farmNames)
        self.an_vi_re_comboBox_farm.addItems(farmNames)
        self.su1_comboBox_farm.addItems(farmNames)
        
    def setFieldNamesCBs(self):
        """Sets list of fields in comboboxes"""
        fieldNames = db1.getFieldNames(self.clientIdx, self.farmIdx)
        self.an_gRx1_comboBox_field.addItems(fieldNames)
        self.an_vi_dMa_comboBox_field.addItems(fieldNames)
        self.an_vi_di_comboBox_field.addItems(fieldNames)
        self.an_vi_sc_comboBox_field.addItems(fieldNames)
        self.an_vi_re_comboBox_field.addItems(fieldNames)
        self.su1_comboBox_field.addItems(fieldNames)
        
    def setCycleNamesCBs(self):
        """Sets list of cycles in comboboxes"""
        cycleNames = db1.getCycleNames(self.clientIdx, self.farmIdx,
                                       self.fieldIdx)
        self.an_gRx3_comboBox_refCycle.addItems(cycleNames)
        self.an_vi_dMa_comboBox_cycle.addItems(cycleNames)
        self.an_vi_di_comboBox_cycle.addItems(cycleNames)
        self.an_vi_sc_comboBox_cycle.addItems(cycleNames)
        self.an_vi_re_comboBox_cycle.addItems(cycleNames)
        #self.su1_comboBox_cycle.addItems(cycleNames)
        
    def setDiagnosisNamesCBs(self):
        """Sets list of variables in visualization comboboxes"""
        diagnosisNames = db1.getDiagnosisNames(self.clientIdx, self.farmIdx,
                                               self.fieldIdx, self.cycleIdx)
        
        self.an_vi_dMa_comboBox_variable.addItems(diagnosisNames)
        self.an_vi_di_comboBox_variable.addItems(diagnosisNames)
        self.an_vi_sc_comboBox_variableX.addItems(diagnosisNames)
        self.an_vi_sc_comboBox_variableY.addItems(diagnosisNames)
        self.an_vi_re_comboBox_variableX.addItems(diagnosisNames)
        self.an_vi_re_comboBox_variableY.addItems(diagnosisNames)
        
        if len(diagnosisNames) > 1:
            self.an_vi_sc_comboBox_variableY.setCurrentIndex(1)
            self.an_vi_re_comboBox_variableY.setCurrentIndex(1)
            
            
    ###End of combo box functions


    ###Start of plot functions
    def plotDMap(self):
        variableName = self.an_vi_dMa_comboBox_variable.currentText()
        cycle = db1.getCycleByIdx(self.clientIdx, self.farmIdx,
                              self.fieldIdx, self.cycleIdx)
        diagnosis = cycle.getDiagnosis(variableName)
        asp.plotDiagnosisMap(self, diagnosis)
        
        
    def plotHist(self):
        variableName = self.an_vi_di_comboBox_variable.currentText()
        cycle = db1.getCycleByIdx(self.clientIdx, self.farmIdx,
                              self.fieldIdx, self.cycleIdx)
        diagnosis = cycle.getDiagnosis(variableName)
        asp.plotHist(self, diagnosis)
        
    def plotScatter(self):
        cycle = db1.getCycleByIdx(self.clientIdx, self.farmIdx,
                                  self.fieldIdx, self.cycleIdx)
        asp.plotScatter(self, cycle)
        
    def plotReg(self):
        cycle = db1.getCycleByIdx(self.clientIdx, self.farmIdx,
                                  self.fieldIdx, self.cycleIdx)
        asp.plotReg(self, cycle)
        
        
    
    ###End of plot functions
    
    
    ###Start of dialog functions
    def succesfulExport(self):
        dlg = InformationDialog(self)
        dlg.label_message.setText("Archivo exportado\nexitosamente")
        #dlg.setWindowFlags(Qt.FramelessWindowHint)        
        dlg.exec()
        self.to_mainMe()   
        
    def succesfulAdd(self):
        dlg = InformationDialog(self)
        dlg.label_message.setText("Datos agregados\nexitosamente")
        #dlg.setWindowFlags(Qt.FramelessWindowHint)        
        dlg.exec()
        self.to_mainMe()  
        
    ###End of dialog functions
    
    ###Start of miscellaneous functions
    def fillDataLabel(self):
        clientN = self.an_gRx1_comboBox_client.currentText()
        farmN = self.an_gRx1_comboBox_farm.currentText()
        fieldN = self.an_gRx1_comboBox_field.currentText()
        cropN = self.an_gRx1_comboBox_crop.currentText()
        cycleN = self.an_gRx2_comboBox_cycle.currentText()
        modelN = self.an_gRx2_comboBox_model.currentText()
        inputN = self.an_gRx2_comboBox_input.currentText()
        inputUnitN = self.an_gRx2_comboBox_inputUnit.currentText()
        inputCost = self.an_gRx3_textEdit_inputCost.toPlainText()
        yieldGoal = self.an_gRx3_textEdit_yieldGoal.toPlainText()
        refCycle = self.an_gRx3_comboBox_refCycle.currentText()
        application = self.an_gRx3_comboBox_application.currentText()
        
        self.an_gRx4_label_data1.setText("  Cliente: " + clientN + "\n"
                                        "  Rancho: " + farmN + "\n"
                                        "  Campo: " + fieldN + "\n"
                                        "  Cultivo: " + cropN + "\n"
                                        "  Ciclo: " + cycleN + "\n"
                                        "  Modelo: " + modelN)
        
        self.an_gRx4_label_data2.setText("  Insumo a prescribir: " + inputN + "\n"
                                        "  Unidad de insumo: " + inputUnitN + "\n"
                                        "  Costo ud. de insumo: $" + inputCost +"\n"
                                        "  Meta rend(t/ha): " + yieldGoal + "\n"
                                        "  Ciclo referencia: " + refCycle + "\n"
                                        "  Aplicación: " + application)
        
        
    def generateRx(self):
        cycle = db1.getCycleByIdx(self.clientIdx, self.farmIdx,
                                  self.fieldIdx, self.cycleIdx)
        crop = self.an_gRx1_comboBox_crop.currentText()
        ag_input = inputN = self.an_gRx2_comboBox_input.currentText()
        app_method = self.an_gRx3_comboBox_application.currentText()
        yield_goal = int(self.an_gRx3_textEdit_yieldGoal.toPlainText())
        
        
        prc.generateRx(cycle = cycle, crop=crop, ag_input = ag_input, 
                    app_method = app_method, yield_goal= yield_goal)
        
        asp.plotRx(self, cycle)
        
        
        self.to_an_gRx5()
        
        
    def exportRx(self):
        cycle = db1.getCycleByIdx(self.clientIdx, self.farmIdx,
                                  self.fieldIdx, self.cycleIdx)
        dst = self.an_gRx7_textEdit_fileLocation.toPlainText()
        
        src = os.path.join(cycle.dir, 'Rx')
        
        #Source paths
        shpSrc = os.path.join(src, 'Map.shp')
        shxSrc = os.path.join(src, 'Map.shx')
        dbfSrc = os.path.join(src, 'Map.dbf')
        
        #Destination paths
        shpDst = os.path.join(dst, 'Rx.shp')
        shxDst = os.path.join(dst, 'Rx.shx')
        dbfDst = os.path.join(dst, 'Rx.dbf')
        
        #Copy files
        shutil.copy(shpSrc, shpDst)
        shutil.copy(shxSrc, shxDst)
        shutil.copy(dbfSrc, dbfDst)
        
        self.succesfulExport()
        
        
        
    def transfer(self):
        src = self.fileSys_L.rows[self.fileSys_L.selectedFolderIdx].dir
        fileOrFolderName = src.split(sep = '\\')[-1]
        dstBase = self.fileSys_R.rows[self.fileSys_R.selectedFolderIdx].dir
        dst = f'{dstBase}\\{fileOrFolderName}'
        
        if os.path.isdir(src):            
            shutil.copytree(src, dst)
        else:             
            shutil.copy(src, dst)
            
        #Reset subfolders to show copied file
        dstFolder = self.fileSys_R.rows[self.fileSys_R.selectedFolderIdx]
        self.fileSys_R.resetFolder(dstFolder)        
        dstFolder.setSubFolders()
        self.fileSys_R.updateRows(dstFolder)
        
        
  

class InformationDialog(QDialog, Ui_Dialog):
    """
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        #Create instance of GUI
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.centerPos() ##without this, dlg changes position 


    def centerPos(self):
        x = 0
        y = 0
        self.move(x,y)        
    

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.setWindowTitle("AgStat")
    window.show()
    app.exec_()
