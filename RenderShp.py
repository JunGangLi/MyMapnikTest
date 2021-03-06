# -*- coding: utf-8 -*-
import mapnik
import ToolFunction
import os,time
from ToolFunction import *

timeStart=time.time()
m=mapnik.Map(256,256)
m.background=mapnik.Color('white')
shpLayer=mapnik.Layer('SHP')
shpLayer.datasource=mapnik.Shapefile(file=r"D:\LIJUNGANG\work\MapServer\mapnik_data\dltb_clip.shp")
lineLayer=mapnik.Layer('Line')
lineLayer.datasource=mapnik.Shapefile(file=r"D:\LIJUNGANG\work\MapServer\mapnik_data\xzdm_clip.shp")

shpStyle=mapnik.Style()
shpStyle.filter_mode=mapnik.filter_mode.FIRST
#forestRule=mapnik.Rule()
farmlandRule011=mapnik.Rule()
filter011=mapnik.Filter("[DLBM]='011'")
farmlandRule011.filter=filter011
farmlandRule011.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(255,255,100)")))
shpStyle.rules.append(farmlandRule011)

farmlandRule012=mapnik.Rule()
filter012=mapnik.Filter("[DLBM]='012'")
farmlandRule012.filter=filter012
farmlandRule012.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(255,255,150)")))
shpStyle.rules.append(farmlandRule012)

farmlandRule013=mapnik.Rule()
filter013=mapnik.Filter("[DLBM]='013'")
farmlandRule013.filter=filter013
farmlandRule013.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(255,255,200)")))
shpStyle.rules.append(farmlandRule013)


gardenRule021=mapnik.Rule()
filter021=mapnik.Filter("[DLBM]='021'")
gardenRule021.filter=filter021
gardenRule021.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(245,210,40)")))
shpStyle.rules.append(gardenRule021)

gardenRule022=mapnik.Rule()
filter022=mapnik.Filter("[DLBM]='022'")
gardenRule022.filter=filter022
gardenRule022.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(255,220,80)")))
shpStyle.rules.append(gardenRule022)

gardenRule023=mapnik.Rule()
filter023=mapnik.Filter("[DLBM]='023'")
gardenRule023.filter=filter023
gardenRule023.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(255,185,20)")))
shpStyle.rules.append(gardenRule023)

forestRule031=mapnik.Rule()
filter031=mapnik.Filter("[DLBM]='031'")
forestRule031.filter=filter031
forestRule031.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(40,140,020)")))
shpStyle.rules.append(forestRule031)

forestRule032=mapnik.Rule()
filter032=mapnik.Filter("[DLBM]='032'")
forestRule032.filter=filter032
forestRule032.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(85,180,100)")))
shpStyle.rules.append(forestRule032)

forestRule033=mapnik.Rule()
filter033=mapnik.Filter("[DLBM]='033'")
forestRule033.filter=filter033
forestRule033.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(140,215,130)")))
shpStyle.rules.append(forestRule032)

green041=mapnik.Rule()
filter041=mapnik.Filter("[DLBM]='041'")
green041.filter=filter041
green041.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(170,190,30)")))
shpStyle.rules.append(green041)

green042=mapnik.Rule()
filter042=mapnik.Filter("[DLBM]='042'")
green042.filter=filter042
green042.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(150,210,50)")))
shpStyle.rules.append(green042)

green043=mapnik.Rule()
filter043=mapnik.Filter("[DLBM]='043'")
green043.filter=filter043
green043.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(200,220,100)")))
shpStyle.rules.append(green043)

road101=mapnik.Rule()
filter101=mapnik.Filter("[DLBM]='101'")
road101.filter=filter101
road101.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(178,170,176)")))
shpStyle.rules.append(road101)

road102=mapnik.Rule()
filter102=mapnik.Filter("[DLBM]='102'")
road102.filter=filter102
road102.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(170,85,80)")))
shpStyle.rules.append(road102)

road103=mapnik.Rule()
filter103=mapnik.Filter("[DLBM]='103'")
road103.filter=filter103
road103.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(180,80,30)")))
shpStyle.rules.append(road103)

road104=mapnik.Rule()
filter104=mapnik.Filter("[DLBM]='104'")
road104.filter=filter104
road104.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(170,85,80)")))
shpStyle.rules.append(road104)

road105=mapnik.Rule()
filter105=mapnik.Filter("[DLBM]='105'")
road105.filter=filter105
road105.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(235,130,130)")))
shpStyle.rules.append(road105)

road106=mapnik.Rule()
filter106=mapnik.Filter("[DLBM]='106'")
road106.filter=filter106
road106.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(235,130,130)")))
shpStyle.rules.append(road106)

road107=mapnik.Rule()
filter107=mapnik.Filter("[DLBM]='107'")
road107.filter=filter107
road107.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(235,130,130)")))
shpStyle.rules.append(road107)

water111=mapnik.Rule()
filter111=mapnik.Filter("[DLBM]='111' or [DLBM]='112' or [DLBM]='113'")
water111.filter=filter111
water111.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(150,240,255)")))
shpStyle.rules.append(water111)

water114=mapnik.Rule()
filter114=mapnik.Filter("[DLBM]='114'")
water114.filter=filter114
water114.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(160,204,240)")))
shpStyle.rules.append(water114)

water115=mapnik.Rule()
filter115=mapnik.Filter("[DLBM]='115' or [DLBM]='116'")
water115.filter=filter115
water115.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(215,255,255)")))
shpStyle.rules.append(water115)

water117=mapnik.Rule()
filter117=mapnik.Filter("[DLBM]='117'")
water117.filter=filter117
water117.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(160,205,240)")))
shpStyle.rules.append(water117)

water118=mapnik.Rule()
filter118=mapnik.Filter("[DLBM]='118'")
water118.filter=filter118
water118.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(230,130,240)")))
shpStyle.rules.append(water118)

water119=mapnik.Rule()
filter119=mapnik.Filter("[DLBM]='119'")
water119.filter=filter119
water119.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(135,205,240)")))
shpStyle.rules.append(water119)

unuse121=mapnik.Rule()
filter121=mapnik.Filter("[DLBM]='121'")
unuse121.filter=filter121
unuse121.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(225,220,225)")))
shpStyle.rules.append(unuse121)


unuse122=mapnik.Rule()
filter122=mapnik.Filter("[DLBM]='122'")
unuse122.filter=filter122
unuse122.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(220,180,130)")))
shpStyle.rules.append(unuse122)

unuse123=mapnik.Rule()
filter123=mapnik.Filter("[DLBM]='123'")
unuse123.filter=filter123
unuse123.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(0,0,0)")))
shpStyle.rules.append(unuse123)


unuse124=mapnik.Rule()
filter124=mapnik.Filter("[DLBM]='124'")
unuse124.filter=filter124
unuse124.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(200,205,200)")))
shpStyle.rules.append(unuse124)

unuse125=mapnik.Rule()
filter125=mapnik.Filter("[DLBM]='125'")
unuse125.filter=filter125
unuse125.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(185,185,190)")))
shpStyle.rules.append(unuse125)


unuse126=mapnik.Rule()
filter126=mapnik.Filter("[DLBM]='126'")
unuse126.filter=filter126
unuse126.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(200,190,170)")))
shpStyle.rules.append(unuse126)

unuse127=mapnik.Rule()
filter127=mapnik.Filter("[DLBM]='127'")
unuse127.filter=filter127
unuse127.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(215,200,185)")))
shpStyle.rules.append(unuse127)

building201=mapnik.Rule()
filter201=mapnik.Filter("[DLBM]='201' or [DLBM]='202'")
building201.filter=filter201
building201.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(220,100,120)")))
shpStyle.rules.append(building201)

building203=mapnik.Rule()
filter203=mapnik.Filter("[DLBM]='203'")
building203.filter=filter203
building203.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(230,140,160)")))
shpStyle.rules.append(building203)

building204=mapnik.Rule()
filter204=mapnik.Filter("[DLBM]='204' or [DLBM]='205'")
building204.filter=filter204
building204.symbols.append(mapnik.PolygonSymbolizer(mapnik.Color("rgb(230,120,130)")))
shpStyle.rules.append(building204)

lineStyle=mapnik.Style()
lineStyle.filter_mode=mapnik.filter_mode.FIRST
line104=mapnik.Rule()
lineFilter104=mapnik.Filter("[DLBM]='104'")
line104.filter=lineFilter104
line104Symbo=mapnik.LineSymbolizer()
stroke104=mapnik.Stroke(mapnik.Color("rgb(170,85,80)"),0.2)
stroke104.add_dash(1.0,3.0)
line104Symbo.stroke=stroke104
line104.symbols.append(line104Symbo)
lineStyle.rules.append(line104)

line117=mapnik.Rule()
lineFilter117=mapnik.Filter("[DLBM]='117'")
line117.filter=lineFilter117
line117Symbo=mapnik.LineSymbolizer()
stroke117=mapnik.Stroke(mapnik.Color("rgb(0,120,200)"),0.25)
line117Symbo.stroke=stroke117
line117.symbols.append(line117Symbo)
lineStyle.rules.append(line117)

line123=mapnik.Rule()
lineFilter123=mapnik.Filter("[DLBM]='123'")
line123.filter=lineFilter123
line123Symbo=mapnik.LineSymbolizer()
stroke123=mapnik.Stroke(mapnik.Color("rgb(0,0,0)"),0.2)
line123Symbo.stroke=stroke123
line123.symbols.append(line123Symbo)
lineStyle.rules.append(line123)

m.append_style("SHPStyle",shpStyle)
m.append_style("LineStyle",lineStyle)
shpLayer.styles.append('SHPStyle')
lineLayer.styles.append('LineStyle')
m.layers.append(lineLayer)
m.layers.append(shpLayer)
bufferWidth=0
index=0
boxlist=getBoxFromShp(r"D:\LIJUNGANG\work\MapServer\mapnik_data\fishnet.shp")
zoomStart=5
zoomEnd=6
for box in boxlist:
    for zoomRank in range(zoomStart,zoomEnd):
        grids=createGrid02(box[1],widthCount=2**(zoomRank-1),heightCont=2**(zoomRank-1))
        for rc in grids:            
            if not os.path.exists("{0}\{1}".format(os.path.abspath('.'),'VectorTiles')):
                os.mkdir("{0}\{1}".format(os.path.abspath('.'),'VectorTiles'))
            png='%s\%s\%s\%s\%sE%sN.png'%(os.path.abspath('.'),'VectorTiles',box[0],zoomRank,rc[0],rc[1])
            if os.path.exists(png):
                continue
            mapXml='%s\%s\%s\%s\%sE%sN.xml'%(os.path.abspath('.'),'VectorTiles',box[0],zoomRank,rc[0],rc[1])
            if(os.path.exists('%s\%s\%s' % (os.path.abspath('.'),'VectorTiles',box[0]))!=True):
                    os.makedirs('%s\%s\%s' % (os.path.abspath('.'),'VectorTiles',box[0]))
            if os.path.exists(("%s\%s\%s\%s"%(os.path.abspath('.'),"VectorTiles",box[0],zoomRank)))!=True:
                os.makedirs(("%s\%s\%s\%s"%(os.path.abspath('.'),"VectorTiles",box[0],zoomRank)))
            index=index+1
            xResolution=abs((grids[rc].maxx-grids[rc].minx)/256)
            yResolution=abs((grids[rc].maxy-grids[rc].miny)/256)
            m.zoom_to_box(mapnik.Box2d(grids[rc].minx-bufferWidth*xResolution,grids[rc].miny-bufferWidth*yResolution,grids[rc].maxx+bufferWidth*xResolution,grids[rc].maxy+bufferWidth*yResolution))
            mapnik.save_map(m,mapXml)
            mapnik.render_to_file(m,png)
log=open("log.txt",'a')
timeEnd=time.time()
print str(timeEnd-timeStart)
log.write('{0};{1};{2}\r\n'.format(zoomStart,zoomEnd,str(timeEnd-timeStart)))
log.close()

