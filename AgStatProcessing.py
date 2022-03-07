# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 17:22:11 2021

@author: andre
"""
from osgeo import gdal,ogr,os,osr
import pandas as pd
import geopandas as gpd
import numpy as np
from ClientDatabase import *


def getBoundariesDir(diagnosis):
    client = diagnosis.client
    farm = diagnosis.farm
    field = diagnosis.field
    fieldDir = db1.getClient(client).getFarm(farm).getField(field).dir
    boundariesDir = os.path.join(fieldDir, 'Boundaries', 'Boundaries.shp')
    return boundariesDir
    

def paddedGrid(gdf):
    """Generates parameters for interpolation"""
    bounds = gdf.total_bounds
    padding = 0.0004 #aprox 40m
    xmin = bounds[0] - padding
    xmax = bounds[2] + padding
    ymin = bounds[1] - padding
    ymax = bounds[3] + padding
    
    ulx = xmin
    uly = ymax
    lrx = xmax
    lry = ymin
    
    pixRes = 1.8e-5 #2m aprox
    
    width = int((xmax - xmin) / pixRes)
    height = int((ymax - ymin) / pixRes)
    
    return [[ulx, uly, lrx, lry], width, height]


def scatterToDiagnosisMap(diagnosis):
    """
    input argument types:
        df : pandas dataframe
        diagnosis : diagnosis class
        
    """
    #Set directories
    scatteredDir = os.path.join(diagnosis.dir, 
                                'Scattered Data', 'Scattered.csv')
    interpolatedDir = os.path.join(diagnosis.dir,
                                   'Interpolated Data', 'Interpolated.csv')
    
    droppedDir = os.path.join(diagnosis.dir,
                              'Interpolated Data', 'Dropped.csv')
    
    mapDir = os.path.join(diagnosis.dir, 'Map', 'Map.shp')
    rangesDir = os.path.join(diagnosis.dir, 'Map', 'Ranges.csv')
    
    maskDir = getBoundariesDir(diagnosis)


    #Delete previous files
    if os.path.exists(interpolatedDir):
        os.remove(interpolatedDir)
        
    if os.path.exists(droppedDir):
        os.remove(droppedDir)    
    
    if os.path.exists(mapDir):
        os.remove(mapDir)
        
    if os.path.exists(rangesDir):
        os.remove(rangesDir)
        
    # if os.path.exists('Interpolated.tif'):
    #     os.remove('Interpolated.tif')

    #Read file and get parameters
    df = pd.read_csv(scatteredDir)
    gdf = gpd.read_file(maskDir)
    p = paddedGrid(gdf)
    
    if len(df) > 100:        
        #Delete extreme values 
        lower = df['Value'].quantile(0.05)
        upper = df['Value'].quantile(0.95)
        df = df[df['Value'].gt(lower) & df['Value'].lt(upper)]
    
    #Export csv
    df.to_csv('Clipped.csv', index=False)
    
    noData = df.Value.mean()
    
    
    
    
    if len(df) > 100:
        algorithmParameters = 'average:radius1=0.00025:radius2=0.00025:angle=0:nodata={}'.format(noData)
    elif len(df) in range(10,100):
        algorithmParameters = 'invdist:power=3.0:radius1=0:radius2=0:angle=0:nodata={}'.format(noData)
    else: 
        algorithmParameters = 'invdistnn:power=2.0:radius1=0:radius2=0:angle=0:nodata={}'.format(noData)
    
    
    
    #Read new csv and convert to 
    gdal.Grid('Interpolated.tif', 'virtualHeader.vrt', zfield='Value',
                      algorithm=(algorithmParameters),
                      outputBounds = p[0],
                      width = p[1], height = p[2],
                      outputSRS = 'EPSG:4326')
    
    
    #Cut raster with mask
    gridClip = gdal.Warp('Unused\InterpolatedClip.tif',
                          'Interpolated.tif',
                          cutlineDSName = maskDir,
                          cropToCutline = True)
    
    
   
    xyz = gdal.Translate('Unused\grid.xyz', gridClip)
    
    df = pd.read_csv('Unused\grid.xyz', sep=' ')
    
    
    df.columns = ['Longitude', 'Latitude', 'Value']      
       
    df.to_csv(interpolatedDir, index=False)
    
    mod = df['Value'].mode()[0]
    dropped_df = df[df['Value'] != mod] #Get rid of nodata values assigned to xyz file
    
    dropped_df.to_csv(droppedDir, index=False)
    
    
    bins = 5
    
    dif = df.Value.max() - df.Value.min()        
    limits = np.linspace(df.Value.min(), df.Value.max(), bins+1)
    
    if dif > 100:
        limits = limits.astype(int)
    elif round(dif) in range(20,100):
        limits = limits.round(1)
    elif dif < 21:
        limits = limits.round(2)
    
    ranges = {}
    for idx in range(len(limits)-1):
        ranges[idx+1] = (str(limits[idx]) + ' - ' + str(limits[idx+1]))
    
    r = pd.DataFrame.from_dict(data = ranges, orient='index')
    r.to_csv(rangesDir, index = False)
        
    #Classify
    df['Category'] = pd.cut(df.Value, 5, labels = False)
    
    #Sort
    dfs = df.sort_values(by=['Latitude', 'Longitude'], ascending = [False, True])[['Longitude','Latitude','Category']]
    
    #Export sorted csv as xyz
    dfs.to_csv('Unused\dfs.xyz', index=False, header=None, sep=' ')
    
    
    sourceRaster = gdal.Translate('Unused\ClassRaster.tif','Unused\dfs.xyz', outputSRS = 'EPSG:4326')
    
    
    
    #Classified raster to shape
    band = sourceRaster.GetRasterBand(1)
    
    driver = ogr.GetDriverByName("ESRI Shapefile")
    
    proj = osr.SpatialReference(wkt=sourceRaster.GetProjection())
    
    
    #CLIPSHP
    if os.path.exists('Unused\Polygonized.shp'):
        driver.DeleteDataSource('Unused\Polygonized.shp')
    outDatasource = driver.CreateDataSource('Unused\Polygonized.shp')
    outLayer = outDatasource.CreateLayer("map", proj)
    newField = ogr.FieldDefn('MYFLD', ogr.OFTInteger)
    outLayer.CreateField(newField)
    gdal.Polygonize(band, None, outLayer, 0, [], callback=None )
    outDatasource.Destroy()
    
    
   
    gdf = gpd.read_file('Unused\Polygonized.shp')
    gdf['geometry'] = gdf.buffer(0)
    mask = gpd.read_file(maskDir)
    #mask['geometry'] = mask.buffer(0)
    clippedMap = gpd.clip(gdf, mask)
    
    clippedMap.to_file(mapDir)
    
    
    
    #Delete garbage files
    sourceRaster = None    
    gridClip = None
    xyz = None
    df = None
    gdf = None
    mask = None
    
    os.remove('Interpolated.tif')
    os.remove('Unused\ClassRaster.tif')
    os.remove('Unused\grid.xyz')
    os.remove('Unused\dfs.xyz')
    os.remove('Clipped.csv')
    os.remove('Unused\Polygonized.shp')
    os.remove('Unused\Polygonized.shx')
    os.remove('Unused\Polygonized.dbf')
    os.remove('Unused\Polygonized.prj')
    os.remove('Unused\InterpolatedClip.tif')   
    
    
    
def generateRx(cycle, crop, ag_input, app_method, yield_goal):
    data_dir = os.path.join(cycle.dir, 'Diagnosis', 
                            'Combined', 'Combined.csv')
    
    maskDir = 'C:\\Users\\andre\\Documents\\UAAAN\\PROYECTO\\App\\Ag_Stat\\clientFiles\\AgroAG\\Montoro\\Pivote1\\Boundaries\\Boundaries.shp'
    mapDir = os.path.join(cycle.dir, 'Rx', 'Map.shp')
    
    if app_method == 'Fertirriego':
        efficiency = 0.8
    
    if os.path.exists(mapDir):
        os.remove(mapDir)

    df = pd.read_csv(data_dir)
    df['Crop'] = crop
    df['Efficiency'] = efficiency
    df['Yield Goal'] = yield_goal
    df['Input'] = ag_input

    def rx_N(nitrates_ppm, organic_matter, bulk_density, yield_goal, crop, ef_application, ag_input):
        om = organic_matter / 100
        mineral_N = om * (5/100) * (1.25/100) * 3000 * bulk_density * 1000
        inorganic_N = nitrates_ppm * bulk_density * 3
        
        if crop == 'Maíz Forrajero':
            ef_N = 0.6
            extraction = 4.2
        
        rx = ((yield_goal * extraction) - (mineral_N + inorganic_N) * ef_N) / ef_application
        
        if (rx > 0) & (ag_input == 'Urea'):
            return int(rx/0.46)
        else:
            return 0

    rxV = np.vectorize(rx_N)

    df['rx'] = rxV(df['Nitratos'], df['Materia O.'], df['Densidad Aparente'],
                   df['Yield Goal'], df['Crop'], df['Efficiency'], df['Input']) 
    

    dfRx = df[['Longitude', 'Latitude', 'rx']].copy()


    doses = np.linspace(dfRx.rx.min(), dfRx.rx.max(), 9).astype(int)

    def snap(value):
        """
        assigns closest value of doses array
        """
        nonlocal doses
        doses = np.asarray(doses)
        idx = (np.abs(doses - value)).argmin()
        return doses[idx]


    dfRx['rxc'] = dfRx.rx.apply(snap)

    dfRx = dfRx[['Longitude', 'Latitude', 'rxc']]



    #Export sorted csv as xyz
    dfRx.to_csv('Unused\dfs.xyz', index=False, header=None, sep=' ')



    
    generateMap(mapDir, maskDir)
    
    #Delete garbage files
    sourceRaster = None   
    xyz = None
    df = None
    gdf = None
    mask = None


    os.remove('Unused\ClassRaster.tif')
    os.remove('Unused\dfs.xyz')
    os.remove('Unused\Polygonized.shp')
    os.remove('Unused\Polygonized.shx')
    os.remove('Unused\Polygonized.dbf')
    os.remove('Unused\Polygonized.prj')
    




"""--------------------------------------------------------------------------"""

def generateMap(mapDir, maskDir):
    
    sourceRaster = gdal.Translate('Unused\ClassRaster.tif','Unused\dfs.xyz',
                                  outputSRS = 'EPSG:4326')
    #Classified raster to shape
    band = sourceRaster.GetRasterBand(1)
    driver = ogr.GetDriverByName("ESRI Shapefile")
    proj = osr.SpatialReference(wkt=sourceRaster.GetProjection())
    
    if os.path.exists('Unused\Polygonized.shp'):
        driver.DeleteDataSource('Unused\Polygonized.shp')
    outDatasource = driver.CreateDataSource('Unused\Polygonized.shp')
    outLayer = outDatasource.CreateLayer("map", proj)
    newField = ogr.FieldDefn('MYFLD', ogr.OFTInteger)
    outLayer.CreateField(newField)
    gdal.Polygonize(band, None, outLayer, 0, [], callback=None )
    outDatasource.Destroy()
    
    
       
    gdf = gpd.read_file('Unused\Polygonized.shp')
    gdf['geometry'] = gdf.buffer(0)
    mask = gpd.read_file(maskDir)
    #mask['geometry'] = mask.buffer(0)
    clippedMap = gpd.clip(gdf, mask)
    
    clippedMap.to_file(mapDir)
    

    

    
    
    
    
    
    





def refreshDatabase(cycle):
    diagList = cycle.getDiagnosisNames()    
    
    combDir = os.path.join(cycle.dir, 'Diagnosis', 'Combined', 'Combined.csv')
    
    if os.path.exists(combDir):
        os.remove(combDir)
    
    dfbDir = os.path.join(cycle.dir, 'Diagnosis', diagList[0], 
                          'Interpolated Data', 'Interpolated.csv')
    dfb = pd.read_csv(dfbDir)
    dfb.columns = ['Longitude', 'Latitude', diagList[0]]
    
    for idx in range(1, len(diagList)):
        dfDir = os.path.join(cycle.dir, 'Diagnosis', diagList[idx], 
                             'Interpolated Data', 'Interpolated.csv')
        df = pd.read_csv(dfDir)
        df.columns = ['Longitude', 'Latitude', diagList[idx]]
        dfb = pd.merge(left = dfb, right = df, how = 'left',
                       left_on = ['Longitude','Latitude'],
                       right_on = ['Longitude','Latitude'])         
    
    dfb.to_csv(combDir, index=False)











































#### END OF FUNCTIONS

gdal.AllRegister()
gdal.UseExceptions()


# n = (db1.getClient('Pedro Andrade').getFarm('Arizona').getField('CampoAZ')
#       .getCycle('OI-2019').getDiagnosis('Conductividad'))
# scatterToDiagnosisMap(n)

# n = (db1.getClient('Pedro Andrade').getFarm('Arizona').getField('CampoAZ')
#       .getCycle('OI-2019').getDiagnosis('NDVI'))
# scatterToDiagnosisMap(n)


# n = (db1.getClient('Pedro Andrade').getFarm('Arizona').getField('CampoAZ')
#       .getCycle('OI-2019').getDiagnosis('Rendimiento'))
# scatterToDiagnosisMap(n)

# c = (db1.getClient('Pedro Andrade').getFarm('Arizona')
#       .getField('CampoAZ').getCycle('OI-2019'))

# refreshDatabase(c)


# n = (db1.getClient('Easy Agro').getFarm('Cosaco').getField('CampoCo')
#       .getCycle('OI-2019').getDiagnosis('Conductividad'))
# scatterToDiagnosisMap(n)

# n = (db1.getClient('Easy Agro').getFarm('Cosaco').getField('CampoCo')
#       .getCycle('OI-2019').getDiagnosis('Altimetría'))
# scatterToDiagnosisMap(n)


# n = (db1.getClient('Easy Agro').getFarm('Cosaco').getField('CampoCo')
#       .getCycle('OI-2019').getDiagnosis('Rendimiento'))
# scatterToDiagnosisMap(n)

# c = (db1.getClient('Easy Agro').getFarm('Cosaco').getField('CampoCo').getCycle('OI-2019'))
      
# refreshDatabase(c)


# n = (db1.getClient('Easy Agro').getFarm('Mazolla').getField('CampoMz')
#       .getCycle('OI-2019').getDiagnosis('Conductividad'))
# scatterToDiagnosisMap(n)

# n = (db1.getClient('Easy Agro').getFarm('Mazolla').getField('CampoMz')
#       .getCycle('OI-2019').getDiagnosis('Altimetría'))
# scatterToDiagnosisMap(n)


# n = (db1.getClient('Easy Agro').getFarm('Mazolla').getField('CampoMz')
#       .getCycle('OI-2019').getDiagnosis('Rendimiento'))
# scatterToDiagnosisMap(n)

# c = (db1.getClient('Easy Agro').getFarm('Mazolla').getField('CampoMz').getCycle('OI-2019'))
      
# refreshDatabase(c)



# n = (db1.getClient('Easy Agro').getFarm('Cabrera').getField('CampoCa')
#       .getCycle('OI-2019').getDiagnosis('Conductividad'))
# scatterToDiagnosisMap(n)

# n = (db1.getClient('Easy Agro').getFarm('Cabrera').getField('CampoCa')
#       .getCycle('OI-2019').getDiagnosis('Altimetría'))
# scatterToDiagnosisMap(n)


# n = (db1.getClient('Easy Agro').getFarm('Cabrera').getField('CampoCa')
#       .getCycle('OI-2019').getDiagnosis('Rendimiento'))
# scatterToDiagnosisMap(n)

# c = (db1.getClient('Easy Agro').getFarm('Cabrera').getField('CampoCa').getCycle('OI-2019'))
      
# refreshDatabase(c)


# n = (db1.getClient('AgroAG').getFarm('Montoro').getField('Pivote1')
#       .getCycle('PV-2021').getDiagnosis('Nitratos'))
# scatterToDiagnosisMap(n)


# n = (db1.getClient('AgroAG').getFarm('Montoro').getField('Pivote1')
#       .getCycle('PV-2021').getDiagnosis('Nitratos'))
# scatterToDiagnosisMap(n)

# n = (db1.getClient('AgroAG').getFarm('Montoro').getField('Pivote1')
#       .getCycle('PV-2021').getDiagnosis('Densidad Aparente'))
# scatterToDiagnosisMap(n)

# n = (db1.getClient('AgroAG').getFarm('Montoro').getField('Pivote1')
#       .getCycle('PV-2021').getDiagnosis('Fósforo'))
# scatterToDiagnosisMap(n)

# n = (db1.getClient('AgroAG').getFarm('Montoro').getField('Pivote1')
#       .getCycle('PV-2021').getDiagnosis('Materia O.'))
# scatterToDiagnosisMap(n)

# n = (db1.getClient('AgroAG').getFarm('Montoro').getField('Pivote1')
#       .getCycle('PV-2021').getDiagnosis('Potasio'))
# scatterToDiagnosisMap(n)

# n = (db1.getClient('AgroAG').getFarm('Montoro').getField('Pivote1')
#       .getCycle('PV-2021').getDiagnosis('Rend (materia seca)'))
# scatterToDiagnosisMap(n)


# c = (db1.getClient('AgroAG').getFarm('Montoro').getField('Pivote1')
#       .getCycle('PV-2021'))


# generateRx(cycle = c, crop='Maíz Forrajero', ag_input = 'Urea', 
#            app_method = 'Fertirriego', yield_goal= 70)


# refreshDatabase(c)








