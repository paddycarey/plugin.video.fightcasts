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


def addFeed(title, url, thumbnail = 'DefaultFolder.png', fanart = os.path.join(__addondir__, 'fanart.jpg')):
    
    """Add a link to the specified feed"""
    
    li = xbmcgui.ListItem( label = title, iconImage = thumbnail, thumbnailImage = thumbnail)
    li.setProperty( "Fanart_Image", fanart )
    xbmcplugin.addDirectoryItem( handle = __addonidint__, url = url, listitem = li, isFolder = True)


def log(txt='', severity=xbmc.LOGDEBUG):

    """Log to txt xbmc.log at specified severity"""
    
    message = ( '%s: %s' % ( __addonid__, txt ) )
    xbmc.log( msg = message, level = severity )


if __name__ == "__main__":

    # add feeds to directory listing
    for feed in feeds.video:
        addFeed( title = feed['title'], url = feed['url'], thumbnail = feed['thumbnail'], fanart = feed['fanart'] )

    ## finish adding items to list and display
    xbmcplugin.endOfDirectory(__addonidint__)
