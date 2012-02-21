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


def addFeed(title, targetPath, plot = '', outline = '', thumbPath = 'DefaultFolder.png', fanartPath = os.path.join(__addondir__, 'fanart.jpg')):
    
    li=xbmcgui.ListItem(label = title, iconImage = thumbPath, thumbnailImage = thumbPath)
    li.setInfo( type="Video", infoLabels={ "title": title, "plot": plot, "plotoutline": outline} )
    li.setProperty( "Fanart_Image", fanartPath )
    xbmcplugin.addDirectoryItem(handle = __addonidint__, url = targetPath, listitem = li, isFolder = True)


def log(txt='', severity=xbmc.LOGDEBUG):

    """Log to txt xbmc.log at specified severity"""
    message = ('%s: %s' % (__addonid__, txt))
    xbmc.log(msg=message, level=severity)


if __name__ == "__main__":

    # BellatorMMA (Youtube)
    addFeed(    title = 'BellatorMMA (Youtube)', 
                plot = "Bellator Fighting Championships is the 2nd largest mixed martial arts promotion in the world and largest tournament-based MMA organization in the world.",
                targetPath = 'plugin://plugin.video.youtube/?path=/root/contacts&folder=true&contact=BellatorMMA&store=contact_options&',
                thumbPath = 'http://mmafrenzy.com/files/2010/04/Bellator-logo-150x150.jpg')

    # Middleeasy TV (Youtube)
    addFeed(    title = 'Middleeasy TV (Youtube)', 
                plot = "It's MiddleEasy.com only with a LOT of MMA videos",
                targetPath = 'plugin://plugin.video.youtube/?path=/root/contacts&folder=true&contact=MiddleEasyTV&store=contact_options&',
                thumbPath = 'http://b.vimeocdn.com/ps/288/288518_300.jpg')

    # MMAFighting.com (Plugin)
    addFeed(    title = 'MMAFighting.com (Plugin)',
                plot = "MMA News & results for the Ultimate Fighting Championship (UFC), Strikeforce & more Mixed Martial Arts fights",
                targetPath = 'plugin://plugin.video.mmafighting',
                thumbPath = 'http://www.blogsmithmedia.com/www.mmafighting.com/media/mma-hour-promo-bg.png')

    # MMAinterviews.tv (Youtube)
    addFeed(    title = 'MMAinterviews.tv (Youtube)',
                plot = "Your trusted source for MMA Videos and News",
                targetPath = 'plugin://plugin.video.youtube/?path=/root/contacts&folder=true&contact=MMAinterviews&store=contact_options&',
                thumbPath = 'http://b.vimeocdn.com/ps/265/835/2658355_300.jpg')
    
    # MMA Nuts (RSS)
    addFeed(    title = 'MMA Nuts (RSS)',
                plot = "MMA NUTS is a video/audio podcast hosted by Ingo Weigold and Matt Griffith covering news and events of the fastest growing sport in the world. The main focus of the show is in depth analysis and coverage of American based mixed martial arts promotions like the UFC, Strikeforce and Chicago MMA as well as Fighter and MMA Celebrity Interviews and Product Reviews.",
                targetPath = 'rss://mmanuts.com:80/feed/podcast',
                thumbPath = 'http://a1.mzstatic.com/us/r30/Podcasts/12/03/7b/ps.emtngods.170x170-75.jpg')
    
    # UFC (Youtube)
    addFeed(    title = 'UFC (Youtube)',
                plot = "Ultimate Fighting Championship is the world's leading mixed martial arts organization.",
                targetPath = 'plugin://plugin.video.youtube/?path=/root/contacts&folder=true&contact=UFC&store=contact_options&',
                thumbPath = 'http://www.mmatraining.com/wp-content/uploads/2011/08/UFC-Logo.jpg')

    ## finish adding items to list and display
    xbmcplugin.endOfDirectory(__addonidint__)
