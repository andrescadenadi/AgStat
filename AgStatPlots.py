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

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches
import matplotlib.colors as colors
import numpy as np
import seaborn as sns
import os


#PLOT SHAPEFILE
def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap


def plotDiagnosisMap(window, diagnosis):
    cmap = plt.get_cmap('Spectral')
    new_cmap = truncate_colormap(cmap, 0, 0.9)

    mapDir = os.path.join(diagnosis.dir, 'Map', 'Map.shp')
    
    window.an_vi_dMa_plot.canvas.ax.clear()    
    gdf = gpd.read_file(mapDir)
    
    gdf.plot(column = 'MYFLD',
             ax = window.an_vi_dMa_plot.canvas.ax, 
             categorical=True, 
             cmap = new_cmap,
             legend = True)
    
    window.an_vi_dMa_plot.canvas.ax.set_axis_off()
    p1 = mpatches.Patch(color=(0.6196,0.0039,0.2588),
                        label=diagnosis.ranges[0])
    p2 = mpatches.Patch(color=(0.9647,0.4941,0.2941),
                        label=diagnosis.ranges[1])
    p3 = mpatches.Patch(color=(1, 0.9411, 0.6509),
                        label=diagnosis.ranges[2])
    p4 = mpatches.Patch(color=(0.7215,0.8862,0.6313),
                        label=diagnosis.ranges[3])
    p5 = mpatches.Patch(color=(0.2,0.5294,0.7372),
                        label=diagnosis.ranges[4])
    window.an_vi_dMa_plot.canvas.ax.legend(handles=[p1, p2, p3, p4, p5],
                                           title = diagnosis.units,
                                           ncol = 3,
                                           loc = 'upper center',
                                           bbox_to_anchor=(0.5, 0),
                                           edgecolor = (0.9254,0.9372,0.9411))
                                           
    
    window.an_vi_dMa_plot.canvas.draw() 
    
    
    
def plotRx(window, cycle):
    mapDir = os.path.join(cycle.dir, 'Rx', 'Map.shp')
    window.an_gRx5_plot.canvas.ax.clear()   
    
    gdf = gpd.read_file(mapDir)
    doses = np.sort(gdf.MYFLD.unique())
    proj = gdf.geometry.estimate_utm_crs()
    gdf.geometry = gdf.geometry.to_crs(proj)
    gdf['area'] = gdf.geometry.area

    adf = round((gdf.groupby('MYFLD').sum()/10000),1).reset_index()


    colors = np.array([[197,189,171],
                      [237,248,177],
                      [198,233,180],
                      [126,205,187],
                      [64,181,196],
                      [29,144,192],
                      [34,93,168],
                      [36,51,146],
                      [8,29,88]])/255

    def assign_color(value):
        nonlocal doses, colors
        idx = [idx for (idx , dose) in enumerate(doses) if  dose == value][0]
        c = colors[idx]
        return (c[0],c[1],c[2])


    gdf['Color'] = gdf['MYFLD'].apply(assign_color)
    patchList = []
        
    for i in range(9):
        c = colors[i]
        rx = str(adf.iloc[i,0])
        
        if len(rx) == 1:
            rx = rx + '    '
        elif len(rx) == 2:
            rx = rx + '  '
        
        ha = adf.iloc[i,1]
        lab = f'{rx} | {ha}ha'
        patch = mpatches.Patch(color=(c[0],c[1],c[2]), label=lab)
        patchList.append(patch) 

    gdf.plot(column = 'MYFLD',
              ax = window.an_gRx5_plot.canvas.ax, 
              categorical=True, 
              color=gdf['Color'],
              legend = True)

    window.an_gRx5_plot.canvas.ax.set_axis_off()

    window.an_gRx5_plot.canvas.ax.legend(handles=patchList, 
                                         title = 'Urea (kg/ha)',
                                         ncol = 3,
                                         loc = 'upper center',
                                         bbox_to_anchor=(0.5, 0))  
    
    window.an_gRx5_plot.canvas.draw() 


def plotHist(window, diagnosis):
    dataDir = os.path.join(diagnosis.dir, 'Interpolated Data',
                           'Dropped.csv')
    
    window.an_vi_di_plot.canvas.ax.clear()
    window.an_vi_di_plot.canvas.ax.grid(zorder=0, color=(0.8,0.8,0.8))
    
    df = pd.read_csv(dataDir)
    
    nBins = int(window.an_vi_di_comboBox_nBins.currentText())

    window.an_vi_di_plot.canvas.ax.hist(df['Value'],
                                        color = (0.6274,0.7098,0.1960,0.7),
                                        edgecolor=(0.9254,0.9372,0.9411,0),
                                        bins = nBins,
                                        zorder=3)
    window.an_vi_di_plot.canvas.ax.set_xlabel(diagnosis.units)
    
    window.an_vi_di_plot.canvas.draw()
    
    
    
def plotScatter(window, cycle):
    dataDir = os.path.join(cycle.dir, 'Diagnosis','Combined','Combined.csv')
    window.an_vi_sc_plot.canvas.ax.clear()
    window.an_vi_sc_plot.canvas.ax.grid(zorder=0, color=(0.8,0.8,0.8))
    
    x = window.an_vi_sc_comboBox_variableX.currentText()
    y = window.an_vi_sc_comboBox_variableY.currentText()
    
    df = pd.read_csv(dataDir)
    window.an_vi_sc_plot.canvas.ax.scatter(x = df[x],
                                      y = df[y],
                                      color=(0.6274,0.7098,0.1960,0.7),
                                      edgecolor=(0.9254,0.9372,0.9411,0),
                                      zorder=3,
                                      s=10)
    unitsX = cycle.getDiagnosis(x).units
    unitsY = cycle.getDiagnosis(y).units
    window.an_vi_sc_plot.canvas.ax.set_xlabel(unitsX)
    window.an_vi_sc_plot.canvas.ax.set_ylabel(unitsY)
      
    window.an_vi_sc_plot.canvas.draw()     


def plotReg(window, cycle):
    dataDir = os.path.join(cycle.dir, 'Diagnosis','Combined','Combined.csv')
    window.an_vi_re_plot.canvas.ax.clear()
    window.an_vi_re_plot.canvas.ax.grid(zorder=0, color=(0.8,0.8,0.8))
    
    x = window.an_vi_re_comboBox_variableX.currentText()
    y = window.an_vi_re_comboBox_variableY.currentText()
    order = int(window.an_vi_re_comboBox_order.currentText())
    
    df = pd.read_csv(dataDir)
    sns.regplot(x = df[x], y = df[y], order = order,
                scatter_kws={'color':(0.6274,0.7098,0.1960, 0.7),
                             's':10,
                             'zorder':3},
                line_kws={'color':(0.9098,0.2666,0.2666),
                          'zorder':4},                        
                ax = window.an_vi_re_plot.canvas.ax)

    unitsX = cycle.getDiagnosis(x).units
    unitsY = cycle.getDiagnosis(y).units
    window.an_vi_re_plot.canvas.ax.set_xlabel(unitsX)
    window.an_vi_re_plot.canvas.ax.set_ylabel(unitsY)    
    
    window.an_vi_re_plot.canvas.draw()              
             
    
    
