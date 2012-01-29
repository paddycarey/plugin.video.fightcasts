#!/usr/bin/env python

import os
import sys

import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin


### get addon info
__addon__             = xbmcaddon.Addon()
__addonid__           = __addon__.getAddonInfo('id')
__addonidint__        = int(sys.argv[1])
__addondir__          = xbmc.translatePath(__addon__.getAddonInfo('path'))

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

def log(txt='', severity=xbmc.LOGDEBUG):

    """Log to txt xbmc.log at specified severity"""
    message = ('FightCasts: %s' % txt)
    xbmc.log(msg=message, level=severity)

def addFolder(title, targetPath, plot = '', outline = '', thumbPath = 'DefaultFolder.png', fanartPath = os.path.join(__addondir__, 'fanart.jpg')):
    url = sys.argv[0] + "?path=%s" % targetPath
    li=xbmcgui.ListItem(label = title, iconImage = thumbPath, thumbnailImage = thumbPath)
    li.setInfo( type="Video", infoLabels={ "title": title, "plot": plot, "plotoutline": outline} )
    li.setProperty( "Fanart_Image", fanartPath )
    xbmcplugin.addDirectoryItem(handle = __addonidint__, url = url, listitem = li, isFolder = True)

def addExternalLink(title, targetPath, plot = '', outline = '', thumbPath = 'DefaultFolder.png', fanartPath = os.path.join(__addondir__, 'fanart.jpg')):
    li=xbmcgui.ListItem(label = title, iconImage = thumbPath, thumbnailImage = thumbPath)
    li.setInfo( type="Video", infoLabels={ "title": title, "plot": plot, "plotoutline": outline} )
    li.setProperty( "Fanart_Image", fanartPath )
    xbmcplugin.addDirectoryItem(handle = __addonidint__, url = targetPath, listitem = li, isFolder = True)

def addVideo(linkName = '', plot = '', url = '', thumbPath = '', fanartPath = os.path.join(__addondir__, 'fanart.jpg'), plotoutline = '', genre = '', date = '', rating = 0.0, epID = 1, tvshowtitle = '', studio = '', duration = '', username = ''):
    li = xbmcgui.ListItem(linkName, iconImage = thumbPath, thumbnailImage = thumbPath)
    li.setProperty("IsPlayable", 'true')
    li.setInfo( type="Video", infoLabels={ "title": linkName, "plot": plot, "rating":rating, "season":1, "episode":epID, "tvshowtitle":tvshowtitle, "aired":date, "premiered":date, "date":date, "studio":studio, "duration":duration, "director":username, "writer":username} )
    li.setProperty( "Fanart_Image", fanartPath)
    xbmcplugin.addDirectoryItem(handle = __addonidint__, url = url, listitem = li, isFolder = False)
