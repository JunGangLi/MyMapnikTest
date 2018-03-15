# -*- coding: utf-8 -*-
"""
Created on Tue Feb 06 14:21:40 2018

@author: ljg
"""

import mapnik
import os
#import ToolFunction
from ToolFunction import *

bufferWidth=0;
map = mapnik.Map(256+bufferWidth, 256+bufferWidth)
#加入缓冲区可以避免在拼接时出现缝隙
map.background = mapnik.Color('white')
style=mapnik.Style()
rule=mapnik.Rule()
rule.symbols.append(mapnik.RasterSymbolizer())
#rule.symbols.append(mapnik.RasterSymbolizer())
style.rules.append(rule)
map.append_style('Raster Style',style)
lyr = mapnik.Layer('GDAL Layer from TIFF file')
lyr.datasource = mapnik.Gdal(file='D:/LIJUNGANG/work/MapServer/data/anhui_huaiyuanxian.tif',band=-1)
lyr.styles.append('Raster Style')
#map.srs = '+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs'
map.layers.append(lyr)
map.zoom_all()
boxlist=getBoxFromShp("D:/LIJUNGANG/work/MapServer/data/fishOne.shp")
index=0

"""
for box in boxlist:
    print box
    for zoomRank in range(1,14):
        grids=createGrid(box[1],zoomRank)        
        print len(grids)
        for rc in grids:      
            png='%s\%s\%s\%s\%sE%sN.png'%(os.path.abspath('.'),'tiles',box[0],zoomRank,rc[0],rc[1])                  
            if(os.path.exists('%s\%s\%s' % (os.path.abspath('.'),'tiles',box[0]))!=True):
                os.makedirs('%s\%s\%s' % (os.path.abspath('.'),'tiles',box[0]))
            if os.path.exists(("%s\%s\%s\%s"%(os.path.abspath('.'),"tiles",box[0],zoomRank)))!=True:
                os.makedirs(("%s\%s\%s\%s"%(os.path.abspath('.'),"tiles",box[0],zoomRank)))
            index=index+1
            map.zoom_to_box(grids[rc])
            mapnik.render_to_file(map,png)
"""

for box in boxlist:
    for zoomRank in range(1,3):
        grids=createGrid02(box[1],widthCount=2**(zoomRank-1),heightCont=2**(zoomRank-1))
        for rc in grids:
            png='%s\%s\%s\%s\%sE%sN.png'%(os.path.abspath('.'),'tiles',box[0],zoomRank,rc[0],rc[1])
            if(os.path.exists(png)==True):
                continue
            mapXml='%s\%s\%s\%s\%sE%sN.xml'%(os.path.abspath('.'),'tiles',box[0],zoomRank,rc[0],rc[1])
            print mapXml
            if(os.path.exists(mapXml)==True):
                os.remove(mapxml)                        
            if(os.path.exists('%s\%s\%s' % (os.path.abspath('.'),'tiles',box[0]))!=True):
                os.makedirs('%s\%s\%s' % (os.path.abspath('.'),'tiles',box[0]))
            if os.path.exists(("%s\%s\%s\%s"%(os.path.abspath('.'),"tiles",box[0],zoomRank)))!=True:
                os.makedirs(("%s\%s\%s\%s"%(os.path.abspath('.'),"tiles",box[0],zoomRank)))
            index=index+1      
            xResolution=abs((grids[rc].maxx-grids[rc].minx)/256)
            yResolution=abs((grids[rc].maxY-grids[rc].minY)/256)
            map.zoom_to_box(mapnik.Box2d(grids[rc].minx-bufferWidth*xResolution,grids[rc].miny-bufferWidth*yResolution,grids[rc].maxx+bufferWidth*xResolution,grids[rc].maxy+bufferWidth*yResolution))
            #map.zoom_to_box(grids[rc])
            mapnik.save_map(map,mapXml)
            mapnik.render_to_file(map,png)

print "********"
print len(boxlist)
print index
