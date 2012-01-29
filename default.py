#!/usr/bin/env python

import os
import sys
import urllib
import xbmc
import xbmcaddon
import xbmcplugin

import resources.lib.podcast as pc

from resources.lib.utils import *

### get addon info
__addon__             = xbmcaddon.Addon()
__addonidint__        = int(sys.argv[1])
__addonname__         = __addon__.getAddonInfo('name')
__addondir__          = xbmc.translatePath(__addon__.getAddonInfo('path'))

def getUstreamEpisodes(showname, studio, username):
    pageNum = 1
    epList = []
    while True:
        try:
            url = 'http://api.ustream.tv/xml/user/%s/listAllVideos?key=A5379FCD5891A9F9A029F84422CAC98C&limit=100&page=%s' % (username, str(pageNum))
            log("Parsing page: %s" % url)
            pageNum = pageNum + 1
            podcast = pc.parsePodcast(podcastURL = url, podcastParseType = 'ustream')
            episodes = podcast.getEpisodes()
        except Exception, e:
            log(str(e), xbmc.LOGERROR)
        else:
            if not episodes == []:
                for ep in episodes:
                    if ep['url']:
                        epList.append(ep)
            else:
                break
    epList.reverse()
    for ep in epList:
        addVideo(linkName = ep['title'], url = ep['url'], plot = ep['description'], thumbPath = ep['thumb'], date = ep['date'], rating = ep['rating'], epID = ep['id'], tvshowtitle = showname, studio = studio, duration = ep['runtime'], username = username)

## parse plugin arguments
params = get_params()

## get path
try:
    path = urllib.unquote_plus(params["path"])
except:
    path = "/"

log('Script path: %s' % path)

## check path and generate desired list
if path == "/":
    
    xbmcplugin.setContent(__addonidint__, 'tvshows') 
    addFolder(title = 'Fight Day', plot = "Fight Day is a UFC pre-show that previews all major UFC events - providing expert analysis, live interviews with the sport's best fighters, and exclusive videos with prominent MMA personalities. ", targetPath = '/fightday', thumbPath = 'http://static-cdn2.ustream.tv/i/channel/picture/7/3/4/3/7343051/7343051_ustreameditorializedpi_1299640720.jpg')
    addFolder(title = 'MMA Junkie Radio', plot = 'MMAjunkie.com Radio broadcasts Monday-Friday at noon ET (9 a.m. PT) live from Mandalay Bay Resort & Casino\'s Race & Sports Book. The show is hosted by "Gorgeous" George Garcia, MMAjunkie.com lead reporter John Morgan and producer Brian "Goze" Garcia.', targetPath = '/mmajunkieradio', thumbPath = 'http://static-cdn1.ustream.tv/i/channel/picture/2/0/1/6/201638/201638_mmashowlogo.jpg')
    addFolder(title = 'The MMA Hour', plot = "The MMA Hour is MMA Fighting's weekly show that discusses the latest in mixed martial arts with fighters and top MMA personalities.", targetPath = '/themmahour', thumbPath = 'http://www.blogsmithmedia.com/www.mmafighting.com/media/mma-hour-promo-bg.png')
    addFolder(title = 'MMA Nation', plot = "This is the live stream of MMA Nation, the radio show on CBS Radio's 106.7 The Fan in Washington, D.C. We cover UFC, MMA, boxing and all forms of combat sports. For more, go to MMANation.com. ", targetPath = '/mmanation', thumbPath = 'http://static-cdn2.ustream.tv/i/channel/picture/3/3/9/3/3393655/3393655_mmanationlogo_12686084.jpg')
    addFolder(title = 'MMA Nuts', plot = "MMA NUTS is a video/audio podcast hosted by Ingo Weigold and Matt Griffith covering news and events of the fastest growing sport in the world. The main focus of the show is in depth analysis and coverage of American based mixed martial arts promotions like the UFC, Strikeforce and Chicago MMA as well as Fighter and MMA Celebrity Interviews and Product Reviews.", targetPath = '/mmanuts', thumbPath = 'http://a1.mzstatic.com/us/r30/Podcasts/12/03/7b/ps.emtngods.170x170-75.jpg')

else:
    
    if path == '/themmahour':
    
        getUstreamEpisodes('The MMA Hour', 'SBNation', 'MMAHour')
            
    elif path == '/fightday':
    
        getUstreamEpisodes('Fight Day', 'Heavy.com', 'HeavyMMA')
            
    elif path == '/mmajunkieradio':
    
        getUstreamEpisodes('MMAJunkie Radio', 'USA Today', 'taggradio')

    elif path == '/mmanation':
    
        getUstreamEpisodes('MMA Nation', '106.7 The Fan DC', 'MMANation')

    elif path == '/mmanuts':
    
        podcast = pc.parsePodcast(podcastURL = 'http://www.mmanuts.com/feed/')
        episodes = podcast.getEpisodes()
        for ep in episodes:
            if ep['url']:
                addVideo(linkName = ep['title'], url = ep['url'], plot = ep['description'], date = ep['date'], tvshowtitle = "MMA Nuts", thumbPath = 'http://a1.mzstatic.com/us/r30/Podcasts/12/03/7b/ps.emtngods.170x170-75.jpg')

    xbmcplugin.setContent(__addonidint__, 'episodes')
    
## finish adding items to list and display
xbmcplugin.endOfDirectory(__addonidint__)
