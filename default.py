#!/usr/bin/env python

import os
import sys
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

from resources.lib import feeds

### get addon info
__addon__             = xbmcaddon.Addon()
__addonidint__        = int(sys.argv[1])
__addonid__         = __addon__.getAddonInfo('id')
__addondir__          = xbmc.translatePath(__addon__.getAddonInfo('path'))


def addFeed(title, url, thumbnail = '', fanart = ''):
    
    """Add a link to the specified feed"""
    
    if thumbnail == '':
        thumbnail = 'DefaultFolder.png'

    if fanart == '':
        fanart = os.path.join(__addondir__, 'fanart.jpg')

    li = xbmcgui.ListItem( label = title, iconImage = thumbnail, thumbnailImage = thumbnail)
    li.setProperty( "Fanart_Image", fanart )
    xbmcplugin.addDirectoryItem( handle = __addonidint__, url = url, listitem = li, isFolder = True)


def log(txt='', severity=xbmc.LOGDEBUG):

    """Log to txt xbmc.log at specified severity"""
    
    message = ( '%s: %s' % ( __addonid__, txt ) )
    xbmc.log( msg = message, level = severity )


if __name__ == "__main__":
    
    feedType = sys.argv[2].lstrip('?')
    
    if feedType == 'video':
        # add feeds to directory listing
        for feed in feeds.video:
            addFeed( title = feed['title'], url = feed['url'], thumbnail = feed['thumbnail'], fanart = feed['fanart'] )
    elif feedType == 'audio':
        # add feeds to directory listing
        for feed in feeds.audio:
            addFeed( title = feed['title'], url = feed['url'], thumbnail = feed['thumbnail'], fanart = feed['fanart'] )
    else:
        addFeed( title = 'Audio', url = 'plugin://plugin.video.fightcasts/?audio', thumbnail = 'DefaultAudio.png')
        addFeed( title = 'Video', url = 'plugin://plugin.video.fightcasts/?video', thumbnail = 'DefaultVideo.png')

    ## finish adding items to list and display
    xbmcplugin.endOfDirectory(__addonidint__)
