#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

###############################################################################
# (c) francois.schnell  francois.schnell@gmail.com
#                       http://francois.schnell.free.fr 
#  
# This script is released under the GPL v2 license
#
###############################################################################

"""
A class to read longitude, latitude, time&date from track points in a gpx file.
"""

import xml.etree.ElementTree as ET,re,sys

class Gpx(object):
    def __init__(self,gpxFile):
        " create a list with a gpx file line per list element "
        self.gpx=""
        gpx_file = open(gpxFile,'r').read()
        regex=re.compile('(<trkseg>.*?</trkseg>)',re.S)
        gpx_trksegs=regex.findall(gpx_file)
        print "Number of <trkseg>...</trkseg> found: ",len(gpx_trksegs)
        i=1
        for trkseg in gpx_trksegs:
            if trkseg.find("time")<1: pass
            if trkseg.find("time")>1:
                self.gpx=trkseg
                print "Found a trakseg with time informations: "+str(i)
                break
            i=i+1
        if self.gpx=="":print "Didn't find an appropriate trkseg :("
        #print self.gpx

    def extract(self):
        """
        Create a list with a  dictionary per gps track point.
        Dictionary keys:
        'date': returns a string date like '2006-11-05'
        'lat': returns a string latitude like '48.5796761739'
        'lon': returns a string longitude like '7.2847080265'
        'time': returns a string 24h time (hh mm sss) like '15:21:27'
        """
        print "Extracting data from the gpx file ..."
        self.geoData=[]
        regex=re.compile('(<trkpt.*?</trkpt>)',re.S)
        gpx_trkpts=regex.findall(self.gpx)
        for line in gpx_trkpts:
            lineTree=ET.fromstring(line)
            self.geoData.append({
            'date':lineTree[1].text[0:10],
            'time':lineTree[1].text[11:-1],
            'lat':lineTree.attrib["lat"],
            'lon':lineTree.attrib["lon"]
            })
        #print self.geoData
        return self.geoData
    
if __name__=="__main__":
    myGpx=Gpx("test.gpx") 
    myGpx.extract()     
