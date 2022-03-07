import os 
import pandas as pd

clientFilesDir = os.path.join(os.getcwd(),'clientFiles')

class clientDataBase:
    def __init__(self):
        self.clientList = []       
            
    def addClient(self, clientName):
        self.clientList.append(client(clientName))
        
    def addFarm(self, clientName, farmName):
        self.getClient(clientName).addFarm(farmName)
        
    def addField(self, clientName, farmName, fieldName):
        self.getClient(clientName).addField(farmName,fieldName)

    def addCycle(self, clientName, farmName, fieldName, cycleName, crop):
        self.getClient(clientName).addCycle(farmName, fieldName,
                                            cycleName, crop)  
        
    def addDiagnosis(self,clientName,farmName,fieldName,cycleName,variable,units):
        self.getClient(clientName).addDiagnosis(farmName, fieldName,
                                                cycleName, variable, units)
        
    def addRx(self, clientName,farmName,fieldName,cycleName, variable, model):
        self.getClient(clientName).addRx(farmName,
                                         fieldName,cycleName,variable, model)                                              
                                                
    def getClient(self, clientName):
        "Returns client that matches clientName"
        return [x for x in self.clientList if x.name == clientName][0]   

    def newElements(self, data):
        """
        Check if client, farm, etc. exist, and creates pertinent obects and 
        directories
        client data must be a dictionary containing the following data:
            clientName, farmName, fieldName, cycleName, and crop
          
        """
        
        directory = os.path.join(clientFilesDir, data['clientName'])
        
        if not os.path.exists(directory): #If client doesn't exist
            self.addClient(data['clientName'])
            self.addFarm(data['clientName'], data['farmName'])
            self.addField(data['clientName'], data['farmName'],
                          data['fieldName'])
            self.addCycle(data['clientName'], data['farmName'],
                          data['fieldName'], data['cycleName'],
                          data['crop'])
        
        directory = os.path.join(directory, data['farmName'])
        
        if not os.path.exists(directory): #If farm doesn't exist
            self.addFarm(data['clientName'], data['farmName'])
            self.addField(data['clientName'], data['farmName'],
                          data['fieldName'])
            self.addCycle(data['clientName'], data['farmName'],
                          data['fieldName'], data['cycleName'],
                          data['crop'])
            
        directory = os.path.join(directory, data['fieldName'])
        
        if not os.path.exists(directory): #If field doesn't exist
            self.addField(data['clientName'], data['farmName'],
                          data['fieldName'])
            self.addCycle(data['clientName'], data['farmName'],
                          data['fieldName'], data['cycleName'],
                          data['crop'])
            
        directory = os.path.join(directory, data['cycleName'])
        
        if not os.path.exists(directory): #If cycle doesn't exist
            self.addCycle(data['clientName'], data['farmName'],
                          data['fieldName'], data['cycleName'],
                          data['crop'])
            
             
    def getNumberOfClients(self):
        return len(self.clientList)
    
    def getClientNames(self):
        nameList = []        
        for client in self.clientList:
            nameList.append(client.name)        
        return nameList    
    
    def getFarmNames(self, clientIdx):
        nameList = []        
        for farm in self.clientList[clientIdx].farmList:
            nameList.append(farm.name)            
        return nameList    
    
    def getFieldNames(self, clientIdx, farmIdx):
        nameList = []        
        for field in self.clientList[clientIdx].farmList[farmIdx].fieldList:
            nameList.append(field.name)            
        return nameList
    
    def getCycleNames(self, clientIdx, farmIdx, fieldIdx):
        nameList = []        
        for cycle in (self.clientList[clientIdx].farmList[farmIdx]
                      .fieldList[fieldIdx].cycleList):
            nameList.append(cycle.name)            
        return nameList
    
    def getDiagnosisNames(self, clientIdx, farmIdx, fieldIdx, cycleIdx):
        nameList = []        
        for diagnosis in (self.clientList[clientIdx].farmList[farmIdx]
                          .fieldList[fieldIdx].cycleList[cycleIdx]
                          .diagnosisList):
            nameList.append(diagnosis.variable)            
        return nameList
    
    def getCycleByIdx(self, clientIdx, farmIdx, fieldIdx, cycleIdx):
        return (self.clientList[clientIdx].farmList[farmIdx]
                .fieldList[fieldIdx].cycleList[cycleIdx])



class client:
    def __init__(self, clientName):
        self.name = clientName
        self.farmList = []
        
        #Directory 
        self.dir = os.path.join(clientFilesDir, self.name)
        
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)
        
    def addFarm(self, farmName):
        self.farmList.append(farm(farmName, self.name))
        
    def addField(self, farmName, fieldName):
        self.getFarm(farmName).addField(fieldName)
        
    def addCycle(self, farmName, fieldName, cycleName, crop):
        self.getFarm(farmName).addCycle(fieldName, cycleName, crop)
        
    def addDiagnosis(self, farmName, fieldName, cycleName, variable, units):
        self.getFarm(farmName).addDiagnosis(fieldName, cycleName, 
                                            variable, units)
        
    def addRx(self, farmName, fieldName, cycleName, variable, model):
        self.getFarm(farmName).addRx(fieldName, cycleName, variable, model)
          
    def getFarm(self, farmName):
        return [x for x in self.farmList if x.name == farmName][0]

        
    
class farm:
    def __init__(self,farmName, clientName):
        self.name = farmName
        self.client = clientName
        self.fieldList = []
        
        #Directory 
        self.dir = os.path.join(clientFilesDir, self.client, self.name)
        
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)
        
    def getField(self, fieldName):
        return [x for x in self.fieldList if x.name == fieldName][0]
        
    def addField(self, fieldName):
        self.fieldList.append(field(fieldName, self.client, self.name))
       
    def addCycle(self, fieldName, cycleName, crop):
        self.getField(fieldName).addCycle(cycleName, crop)
        
    def addDiagnosis(self, fieldName, cycleName, variable, units):
        self.getField(fieldName).addDiagnosis(cycleName, variable, units)
        
    def addRx(self, fieldName, cycleName, variable, model):
        self.getField(fieldName).addRx(cycleName, variable, model)
    
    


class field:
    def __init__(self, fieldName, clientName, farmName):
        self.name = fieldName
        self.client = clientName
        self.farm = farmName
        self.boundaries = None #To do, read shapefile
        self.cycleList = []
        
        #Directory 
        self.relDir = os.path.join(self.client, self.farm, self.name)
        self.dir = os.path.join(clientFilesDir, self.relDir)
                
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)
            
    def addCycle(self, cycleName, crop):
        self.cycleList.append(cycle(cycleName, crop, self.relDir))
        
    def addDiagnosis(self, cycleName, variable, units):
        self.getCycle(cycleName).addDiagnosis(variable, units)
        
    def addRx(self, cycleName, variable, model):
        self.getCycle(cycleName).addRx(variable, model)
        
    def getCycle(self, cycleName):
        return [x for x in self.cycleList if x.name == cycleName][0]
    
    
class cycle:
    def __init__(self, cycleName, crop, relDir):
        self.name = cycleName
        self.crop = crop
        self.client = relDir.split(sep='\\')[0]
        self.farm = relDir.split(sep='\\')[1]
        self.field = relDir.split(sep='\\')[2]
        self.diagnosisList = []
        self.rxList = []
        
        self.relDir = os.path.join(relDir,self.name)
        self.dir = os.path.join(clientFilesDir, self.relDir)
        
        #Create directories
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)
            os.mkdir(os.path.join(self.dir, 'Diagnosis'))
            os.mkdir(os.path.join(self.dir, 'Diagnosis', 'Combined'))
            os.mkdir(os.path.join(self.dir, 'Rx'))
            
    def addDiagnosis(self, variable, units):
        self.diagnosisList.append(diagnosis(variable, units, 
                                            self.relDir, self.crop))
    
    def addRx(self, variable, model):
        self.diagnosisList.append(rx(variable, model, self.relDir, self.crop))
        
    def getDiagnosis(self, variable):
        return [x for x in self.diagnosisList if x.variable == variable][0]
    
    def getDiagnosisNames(self):
        diagnosisNames = []
        for diagnosis in self.diagnosisList:
            diagnosisNames.append(diagnosis.variable)  
            
        return diagnosisNames
    
    def getRx(self, variable):
        return [x for x in self.rxList if x.variable == variable][0]
                                            

        
class diagnosis:
     def __init__(self, variable, units, relDir, crop):
         self.variable = variable
         self.client = relDir.split(sep='\\')[0]
         self.farm = relDir.split(sep='\\')[1]
         self.field = relDir.split(sep='\\')[2]
         self.cycleName = relDir.split(sep='\\')[3]
         self.crop = crop
         self.units = units
                        
         self.relDir = os.path.join(relDir, 'Diagnosis', variable)
         self.dir = os.path.join(clientFilesDir, self.relDir )
         
         rangesDir = os.path.join(self.dir, 'Map', 'Ranges.csv')
         if os.path.exists(rangesDir):
             self.ranges = pd.read_csv(rangesDir).to_dict()['0']
         else:
             self.ranges = {}
         
         if not os.path.exists(self.dir):                                               
             os.mkdir(self.dir)
             os.mkdir(os.path.join(self.dir, 'Scattered Data'))
             os.mkdir(os.path.join(self.dir, 'Interpolated Data'))
             os.mkdir(os.path.join(self.dir, 'Map'))
             os.mkdir(os.path.join(self.dir, 'Report'))
             os.mkdir(os.path.join(self.dir, 'Combined'))
                
         
         #To do files
         self.scatteredData = None
         self.interpolatedData = None
         self.map = None
         self.report = None
         
         
class rx: #Check about inheritance since is almost same as diagnosis
     def __init__(self, variable, model, relDir, crop):
         self.variable = variable
         self.client = relDir.split(sep='\\')[0]
         self.farm = relDir.split(sep='\\')[1]
         self.field = relDir.split(sep='\\')[2]
         self.cycleName = relDir.split(sep='\\')[3]
         self.crop = crop
         
         self.relDir = os.path.join(relDir, 'Rx', variable)
         self.dir = os.path.join(clientFilesDir, self.relDir )
         
         if not os.path.exists(self.dir):                                               
             os.mkdir(self.dir)
             os.mkdir(os.path.join(self.dir, 'Database'))
             os.mkdir(os.path.join(self.dir, 'Map'))             
             os.mkdir(os.path.join(self.dir, 'Report'))
                
         
         #To do files
         self.database = None
         self.map = None
         self.report = None
         
        
        
        
        
        
        
        
        
"""End of classes definition"""
        

        
db1 = clientDataBase()

# db1.addClient('Pedro Andrade')
# db1.addClient('Easy Agro')
db1.addClient('AgroAG')

db1.addFarm('AgroAG', 'Montoro')
# db1.addFarm('Pedro Andrade', 'Arizona')
# db1.addFarm('Easy Agro', 'Mazolla')
# db1.addFarm('Easy Agro', 'Cabrera')
# db1.addFarm('Easy Agro', 'Cosaco')

db1.addField('AgroAG', 'Montoro', 'Pivote1')
# db1.addField('Pedro Andrade', 'Arizona', 'CampoAZ')
# db1.addField('Easy Agro', 'Mazolla', 'CampoMz')
# db1.addField('Easy Agro', 'Cabrera', 'CampoCa')
# db1.addField('Easy Agro', 'Cosaco', 'CampoCo')


db1.addCycle('AgroAG', 'Montoro', 'Pivote1', 'PV-2021', 'Maiz Forrajero')
# db1.addCycle('Pedro Andrade', 'Arizona', 'CampoAZ', 'OI-2019', 'Trigo')
# db1.addCycle('Easy Agro', 'Mazolla', 'CampoMz', 'OI-2019', 'Maíz Grano')
# db1.addCycle('Easy Agro', 'Cabrera', 'CampoCa', 'OI-2019', 'Maíz Grano')
# db1.addCycle('Easy Agro', 'Cosaco', 'CampoCo', 'OI-2019', 'Maíz Grano')



db1.addDiagnosis('AgroAG', 'Montoro', 'Pivote1', 'PV-2021', 'Nitratos', 'ppm')
db1.addDiagnosis('AgroAG', 'Montoro', 'Pivote1', 'PV-2021', 'Materia O.', '%')
db1.addDiagnosis('AgroAG', 'Montoro', 'Pivote1', 'PV-2021', 'Potasio', 'ppm')
db1.addDiagnosis('AgroAG', 'Montoro', 'Pivote1', 'PV-2021', 'Fósforo', 'ppm')
db1.addDiagnosis('AgroAG', 'Montoro', 'Pivote1', 'PV-2021',
                 'Densidad Aparente', 'g/cm3')
db1.addDiagnosis('AgroAG', 'Montoro', 'Pivote1', 'PV-2021',
                 'Rend (materia seca)', 't/ha')

# db1.addDiagnosis('Pedro Andrade', 'Arizona', 'CampoAZ', 'OI-2019', 
#                  'NDVI', 'NDVI')
# db1.addDiagnosis('Pedro Andrade', 'Arizona', 'CampoAZ', 'OI-2019', 
#                  'Conductividad', 'mS/m')
# db1.addDiagnosis('Pedro Andrade', 'Arizona', 'CampoAZ', 'OI-2019', 
#                  'Rendimiento', 't/ha')

# db1.addDiagnosis('Easy Agro', 'Mazolla', 'CampoMz', 'OI-2019', 
#                  'Conductividad', 'mS/m')
# db1.addDiagnosis('Easy Agro', 'Mazolla', 'CampoMz', 'OI-2019', 
#                  'Altimetría', 'msnm')
# db1.addDiagnosis('Easy Agro', 'Mazolla', 'CampoMz', 'OI-2019', 
#                  'Rendimiento', 't/ha')

# db1.addDiagnosis('Easy Agro', 'Cabrera', 'CampoCa', 'OI-2019', 
#                  'Conductividad', 'mS/m')
# db1.addDiagnosis('Easy Agro', 'Cabrera', 'CampoCa', 'OI-2019', 
#                  'Altimetría', 'msnm')
# db1.addDiagnosis('Easy Agro', 'Cabrera', 'CampoCa', 'OI-2019', 
#                  'Rendimiento', 't/ha')

# db1.addDiagnosis('Easy Agro', 'Cosaco', 'CampoCo', 'OI-2019', 
#                  'Conductividad', 'mS/m')
# db1.addDiagnosis('Easy Agro', 'Cosaco', 'CampoCo', 'OI-2019', 
#                  'Altimetría', 'msnm')
# db1.addDiagnosis('Easy Agro', 'Cosaco', 'CampoCo', 'OI-2019', 
#                  'Rendimiento', 't/ha')




# dataACD = {'clientName':'Andres', 'farmName':'Granja1',
#           'fieldName':'Campo1', 'cycleName':'OI-2019', 'crop':'corn'}

# db1.newElements(dataACD)








































































































