#!/usr/bin/env python

import os
import sys
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

### get addon info
__addon__             = xbmcaddon.Addon()
__addonidint__        = int(sys.argv[1])
__addonid__         = __addon__.getAddonInfo('id')
__addondir__          = xbmc.translatePath(__addon__.getAddonInfo('path'))


def addFeed(title, targetPath, thumbPath = 'DefaultFolder.png', fanartPath = os.path.join(__addondir__, 'fanart.jpg')):
    
    """Add a link to the specified feed"""
    
    li = xbmcgui.ListItem( label = title, iconImage = thumbPath, thumbnailImage = thumbPath)
    li.setProperty( "Fanart_Image", fanartPath )
    xbmcplugin.addDirectoryItem( handle = __addonidint__, url = targetPath, listitem = li, isFolder = True)


def log(txt='', severity=xbmc.LOGDEBUG):

    """Log to txt xbmc.log at specified severity"""
    
    message = ( '%s: %s' % ( __addonid__, txt ) )
    xbmc.log( msg = message, level = severity )


if __name__ == "__main__":

    # BellatorMMA (Youtube)
    addFeed(    title = 'BellatorMMA (Youtube)', 
                targetPath = 'plugin://plugin.video.youtube/?path=/root/contacts&folder=true&contact=BellatorMMA&store=contact_options&',
                thumbPath = 'http://mmaartwork.wackwack.co.uk/fightcasts/bellator.jpg')

    # HDNet Fights (Youtube)
    addFeed(    title = 'HDNet Fights (Youtube)',
                targetPath = 'plugin://plugin.video.youtube/?path=/root/contacts&folder=true&contact=HDNetFights&store=contact_options&',
                thumbPath = 'http://mmaartwork.wackwack.co.uk/fightcasts/hdnetfights.jpg')

    # Middleeasy TV (Youtube)
    addFeed(    title = 'Middleeasy TV (Youtube)', 
                targetPath = 'plugin://plugin.video.youtube/?path=/root/contacts&folder=true&contact=MiddleEasyTV&store=contact_options&',
                thumbPath = 'http://mmaartwork.wackwack.co.uk/fightcasts/middleeasy.jpg')

    # MMAFighting.com (Plugin)
    addFeed(    title = 'MMAFighting.com (Plugin)',
                targetPath = 'plugin://plugin.video.mmafighting',
                thumbPath = 'http://mmaartwork.wackwack.co.uk/fightcasts/mmafighting.png')

    # MMAinterviews.tv (Youtube)
    addFeed(    title = 'MMAinterviews.tv (Youtube)',
                targetPath = 'plugin://plugin.video.youtube/?path=/root/contacts&folder=true&contact=MMAinterviews&store=contact_options&',
                thumbPath = 'http://mmaartwork.wackwack.co.uk/fightcasts/mmainterviews.jpg')
    
    # MMA Nuts (RSS)
    addFeed(    title = 'MMA Nuts (RSS)',
                targetPath = 'rss://mmanuts.com:80/feed/podcast',
                thumbPath = 'http://mmaartwork.wackwack.co.uk/fightcasts/mmanuts.jpg')
    
    # UFC (Youtube)
    addFeed(    title = 'UFC (Youtube)',
                targetPath = 'plugin://plugin.video.youtube/?path=/root/contacts&folder=true&contact=UFC&store=contact_options&',
                thumbPath = 'http://mmaartwork.wackwack.co.uk/fightcasts/ufc.jpg')

    ## finish adding items to list and display
    xbmcplugin.endOfDirectory(__addonidint__)
