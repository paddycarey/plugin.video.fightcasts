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

    # Bellator MMA (Youtube)
    addFeed(    title = 'Bellator MMA (Youtube)', 
                targetPath = 'plugin://plugin.video.youtube/?path=/root/contacts&folder=true&contact=BellatorMMA&store=contact_options&',
                thumbPath = 'http://mmaartwork.wackwack.co.uk/fightcasts/bellator.jpg')

    # Eddie Bravo (Youtube)
    addFeed(    title = 'Eddie Bravo (Youtube)', 
                targetPath = 'plugin://plugin.video.youtube/?path=/root/contacts&folder=true&contact=twistereddie&store=contact_options&',
                thumbPath = 'http://mmaartwork.wackwack.co.uk/fightcasts/twistereddie.jpg')

    # Evolve Mixed Martial Arts (Youtube)
    addFeed(    title = 'Evolve Mixed Martial Arts (Youtube)', 
                targetPath = 'plugin://plugin.video.youtube/?path=/root/contacts&folder=true&contact=evolvemma&store=contact_options&',
                thumbPath = 'http://mmaartwork.wackwack.co.uk/fightcasts/evolvemma.jpg')

    # HDNet Fights (Youtube)
    addFeed(    title = 'HDNet Fights (Youtube)',
                targetPath = 'plugin://plugin.video.youtube/?path=/root/contacts&folder=true&contact=HDNetFights&store=contact_options&',
                thumbPath = 'http://mmaartwork.wackwack.co.uk/fightcasts/hdnetfights.jpg')

    # Iron Forges Iron (Youtube)
    addFeed(    title = 'Iron Forges Iron (Youtube)',
                targetPath = 'plugin://plugin.video.youtube/?path=/root/contacts&folder=true&contact=ironforgesiron&store=contact_options&',
                thumbPath = 'http://mmaartwork.wackwack.co.uk/fightcasts/ironforgesiron.jpg')

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

    # MMAWeekly.com Videos (Youtube)
    addFeed(    title = 'MMAWeekly.com Videos (Youtube)',
                targetPath = 'plugin://plugin.video.youtube/?path=/root/contacts&folder=true&contact=MMAWeeklyVideos&store=contact_options&',
                thumbPath = 'http://mmaartwork.wackwack.co.uk/fightcasts/mmaweekly.jpg')

    # MMA H.E.A.T. (Youtube)
    addFeed(    title = 'MMA H.E.A.T. (Youtube)',
                targetPath = 'plugin://plugin.video.youtube/?path=/root/contacts&folder=true&contact=mmaheat&store=contact_options&',
                thumbPath = 'http://mmaartwork.wackwack.co.uk/fightcasts/mmaheat.jpg')

    # MMA: Inside the Cage (Youtube)
    addFeed(    title = 'MMA: Inside the Cage (Youtube)',
                targetPath = 'plugin://plugin.video.youtube/?path=/root/contacts&folder=true&contactMMAInsideTheCageTV&store=contact_options&',
                thumbPath = 'http://mmaartwork.wackwack.co.uk/fightcasts/MMAInsideTheCageTV.jpg')

    # MMA Nuts (RSS)
    addFeed(    title = 'MMA Nuts (RSS)',
                targetPath = 'rss://mmanuts.com:80/feed/podcast',
                thumbPath = 'http://mmaartwork.wackwack.co.uk/fightcasts/mmanuts.jpg')

    # Disabled until Vimeo login is working again
    ## The Reem (Vimeo)
    #addFeed(    title = 'The Reem (Vimeo)',
    #            targetPath = 'plugin://plugin.video.vimeo/?path=/root/contacts&folder=true&contact=thereem&store=contact_options&',
    #            thumbPath = 'http://mmaartwork.wackwack.co.uk/fightcasts/thereem.jpg')    

    # StillW1ll (Youtube)
    addFeed(    title = 'StillW1ll (Youtube)',
                targetPath = 'plugin://plugin.video.youtube/?path=/root/contacts&folder=true&contact=StillW1ll&store=contact_options&',
                thumbPath = 'http://mmaartwork.wackwack.co.uk/fightcasts/stillwill.jpg')

    # UFC (Youtube)
    addFeed(    title = 'UFC (Youtube)',
                targetPath = 'plugin://plugin.video.youtube/?path=/root/contacts&folder=true&contact=UFC&store=contact_options&',
                thumbPath = 'http://mmaartwork.wackwack.co.uk/fightcasts/ufc.jpg')

    # Whoa! TV (Youtube)
    addFeed(    title = 'WHOA! TV (Youtube)',
                targetPath = 'plugin://plugin.video.youtube/?path=/root/contacts&folder=true&contact=whoatv&store=contact_options&',
                thumbPath = 'http://mmaartwork.wackwack.co.uk/fightcasts/whoatv.jpg')

    # www.MMA30.com (Youtube)
    addFeed(    title = 'www.MMA30.com (Youtube)',
                targetPath = 'plugin://plugin.video.youtube/?path=/root/contacts&folder=true&contact=MMA30tv&store=contact_options&',
                thumbPath = 'http://mmaartwork.wackwack.co.uk/fightcasts/MMA30tv.jpg')

    ## finish adding items to list and display
    xbmcplugin.endOfDirectory(__addonidint__)
