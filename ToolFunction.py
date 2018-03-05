# -*- coding: utf-8 -*-
"""
Created on Fri Feb 02 16:56:33 2018

@author: ljg
"""

import mapnik
import math
try:
    from osgeo import gdal
    from osgeo import ogr
except ImportError:
    import gdal
    import ogr
    
#投影坐标系，第一级切片序号为1
def makeTileResolution(xRange,yRange,allZooms=17,width=256,heigt=256,xNum=1,yNum=1):
    resolution=[]    
    for i in range(1,allZooms+1):
        xr=1.0*xRange/width/xNum/(2**(allZooms-1))
        yr=1.0*yRange/heigt/yNum/(2**(allZooms-1))
        resolution.append((xr,yr))
    return resolution
 
def getResoluton(zoom,resolution= 7.2e-006):    
    resultReso=resolution*(2**(zoom-1))
    return resultReso

#根据输入参数的瓦片大小为256*256
def createGrid(envelopeParam,zoom):   
    """
    根据输入的Box2d范围 和瓦片等级zoom
    生成在该范围的上对应等级的格网1~zoom(不包含zoom 级)    
    （废弃，该方法设计的格网与分辨率有关，不符合设计）
    """
    resolution=getResoluton(zoom)
    width=256*resolution
    height=256*resolution  
    widthCount=int((envelopeParam.maxx-envelopeParam.minx)/width+1)   
    heightCont=int((envelopeParam.maxy-envelopeParam.miny)/height+1)   
    reslut={}
    for i in range(0,widthCount):
        for j in range(0,heightCont):
            reslut[(i,j)]=mapnik.Box2d(envelopeParam.minx+i*width,envelopeParam.miny+j*height,envelopeParam.minx+(i+1)*width,envelopeParam.miny+(j+1)*height)
    return reslut



def createGrid02(envelopeParam,widthCount=1,heightCont=1):
    """
    把输入的mapnik.Box2d按指定的行列数目进行划分，最后返回划分的格网
    返回值是字典{（行号，列号）：box}
    行列号从1开始
    """
    reslut={}
    print envelopeParam.minx,envelopeParam.maxx
    s=abs(envelopeParam.maxx-envelopeParam.minx)
    width=abs(envelopeParam.minx-envelopeParam.maxx)/(widthCount*1.0)
    height=abs(envelopeParam.maxy-envelopeParam.miny)/(heightCont*1.0)   
    for i in range(0,widthCount):
        for j in range(0,heightCont):
            box=mapnik.Box2d(envelopeParam.minx+i*width,envelopeParam.miny+j*height,envelopeParam.minx+(i+1)*width,envelopeParam.miny+(j+1)*height)           
            reslut[(i,j)]=box
    return reslut 
    
def createGrid03(envelopeParam,zoom):
    """
    根据输入的Box2d范围 和瓦片等级zoom
    生成在该范围的上对应等级的格网1~zoom(不包含zoom 级)
    每一级对应的切片横纵坐标数目是Power(2,zoom-1)
    返回值是字典{（行号，列号，zoom）：box}
    行、列、等级号从1开始
    """
    reslut={}
    for i in range(1,zoom):
        num=2**(zoom-1)
        tempReslut=createGrid02(envelopeParam,widthCount=num,heightCont=num)
        for item in tempReslut:
            reslut[(item[0][0],item[0][1],i)]=tempReslut[item]
    return reslut

#从shpfile文件获取格网
def getBoxFromShp(shapeFile):
    """
    根据shapefile的格网生成grid列表
    返回boxs的列表(fid,Box2d)
    """
    boxlist=[]
    gdal.SetConfigOption("GDAL_FILENAME_IS_UTF8","NO")
    gdal.SetConfigOption("SHAPE_ENCODING","")
    #i=0
    ogr.RegisterAll()
    ds=ogr.Open(shapeFile,0)
    if ds==None:
        return boxlist
    olayer=ds.GetLayerByIndex(0)
    if olayer==None:
        return boxlist
    olayer.ResetReading()
    oFeature=olayer.GetNextFeature()
    if not (olayer.GetGeomType()==3):
        return boxlist    
    while oFeature is not None:
        fid=oFeature.GetFID()
        print fid
        oGeometry=oFeature.GetGeometryRef()
        envelope=oGeometry.GetEnvelope()
        box=mapnik.Box2d(envelope[0],envelope[2],envelope[1],envelope[3])       
        boxlist.append((fid,box))
        oFeature=olayer.GetNextFeature()
    return boxlist
