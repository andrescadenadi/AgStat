# -*- coding: utf-8 -*-
"""
Copyright 2023 Andrés Cadena Díaz

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import os 
from PyQt5 import QtCore, QtWidgets


class FolderLabel(QtWidgets.QPushButton):
    def __init__(self, sys, level, fDir, upperF=None, idx=0, parent=None):
        super().__init__(parent)
        self.sys = sys
        self.level = level
        self.dir = fDir
        self.upperF = upperF
        self.idx = idx
        self.parent = parent
                     
        self.displayIdx = None        
        self.isActive = False
        
        self.subFolderList = []
       
                       
        self.clicked.connect(self.click)
                
    def click(self):
        if self.isActive:
            #self.sys.selectedFolderIdx = None
            self.isActive = False 
            self.sys.updateRows(self)
            self.subFolderList = []
            
        else:
            self.isActive = True
            if os.path.isdir(self.dir):
                self.setSubFolders()
            self.nSubFolder = len(self.subFolderList)   
            self.sys.updateRows(self)
            
    def setSubFolders(self): 
        self.subFolderList = []
        
        names = os.listdir(self.dir)
        
        newLevel = self.level + 1
        
        for idx in range(len(names)):
          
            newDir = os.path.join(self.dir, names[idx])
            subFolder = FolderLabel(self.sys, newLevel, newDir, self, idx, self.parent)
            subFolder.setStyleSheet(styleSheet)
            subFolder.setText(names[idx]) 
            subFolder.hide()              
            self.subFolderList.append(subFolder)            
            

        

class FileSystem():
    def __init__(self, rootDir, parent):
        self.dir = rootDir
        self.parent = parent       
        self.rows = []        
        self.createHomeFolder(rootDir, parent)        
        self.x = 0
        self.y = 0        
        self.selectedFolderIdx = 0
        self.previousSelectedFolderIdx = 0
        self.updateRows(self.homeFolder)


    def createHomeFolder(self, rootDir, parent):  
        self.homeFolder =  FolderLabel(self, 0, rootDir, parent = parent)
        
        self.homeFolder.setStyleSheet(styleSheet)
        self.homeFolder.setText(rootDir.split(sep='\\')[-1])
        self.homeFolder.isActive = True #Home folder open by default
        self.homeFolder.setSubFolders()
        self.rows.append(self.homeFolder) #add home folder to screen
        
        
    def nextFolderIdx(self, folder):
        level = folder.level
        
        #Folder index in rows list
        fIdx = [index for (index , item) in enumerate(self.rows) if item == folder][0]
        
       
        for l in range(level):
            #List of indexes of folders with specified level
            o = [index for (index , item) in enumerate(self.rows) if item.level == level]
            
            if l == 0:
                #index to locate next index in index list, only applies when searching in same level
                i1 = [index for (index , item) in enumerate(o) if item == fIdx]
                if len(i1) > 0: #if there are any elements in list
                    i2 = i1[0] + 1 #Next index
            else:                 
                #index to locate next index in index list
                i1 = [index for (index , item) in enumerate(o) if item > fIdx]
            
                if len(i1) > 0: #if there are any elements in list
                    i2 = i1[0] #this will be the new goal index, is already greater than fIdx  
                
            if i2 < len(o):
                #Index of next folder with specified level
                goalIdx = o[i2]
                return goalIdx
                break
            
            level -= 1
        
        #If next object not found, return last possible idx
        return len(self.rows)
            

        
    def updateRows(self, folder):
        """
        Updates position of folders on screen
        """
        #De - highlight previous selected folder
        self.rows[self.selectedFolderIdx].setStyleSheet(styleSheet)
        
        upIdx = [index for (index , item) in enumerate(self.rows) if item == folder][0] 
        self.previousSelectedFolderIdx = self.selectedFolderIdx
        self.selectedFolderIdx = upIdx
        
        # print('current:  ' + str(self.selectedFolderIdx))
        # print('previous: ' + str(self.previousSelectedFolderIdx))
        # print('-----------------------------------------------')
        
        sIdx = upIdx + 1 #Process idexes after up folder
        if folder.isActive:                                    
            for subFolder in folder.subFolderList:                
                self.rows.insert(sIdx, subFolder)
                sIdx += 1
        else:
            endIdx = self.nextFolderIdx(folder)
            ran = range(sIdx,endIdx)           
            
            for idx in ran:  
                folder = self.rows[sIdx]              
                del self.rows[sIdx]
                folder.hide() 
             

                
        #show Folders        
        for idx in range(len(self.rows)):
            folder = self.rows[idx]
            #folder.hide()
            xPos = self.x + ((folder.level) * 15)
            yPos = self.y + ((idx) * 30)
            folder.setGeometry(QtCore.QRect(xPos, yPos, 200, 41))            
            
            if idx == self.selectedFolderIdx:
                folder.setStyleSheet(styleSheetSelected) #Highlight selected folder            
            
                
            folder.show()
            
    def resetFolder(self, folder):
        """
        Erases subFolders to avoid repeated subfolders after copy operation
        """
        parentIdx = [index for (index , item) in enumerate(self.rows) if item == folder][0]
        delIdx = parentIdx + 1
                
        for idx in range(len(folder.subFolderList)):  
            folder = self.rows[delIdx]              
            del self.rows[delIdx]
            folder.hide() 
        
        
        
            
            
            
            
            
styleSheet =("font: 18pt \"MS Shell Dlg 2\";\n"
                                  "color: rgb(236, 239, 240);"
"border-radius: 25px;\n"
"text-align: left;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"FolderLabel::pressed\n"
"{\n"
"color: rgb(150, 150, 150);\n")



styleSheetSelected =("font: 18pt \"MS Shell Dlg 2\";\n"
                                  "color: rgb(205, 220, 50);"
"border-radius: 25px;\n"
"text-align: left;\n"
"text-decoration: underline;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"FolderLabel::pressed\n"
"{\n"
"color: rgb(150, 150, 150);\n")
