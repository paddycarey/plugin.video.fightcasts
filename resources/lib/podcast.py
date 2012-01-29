import urllib2
from resources.lib.utils import log
from elementtree import ElementTree as ET

import urllib
import re
import os
import xbmc

from BeautifulSoup import BeautifulSoup


class parsePodcast:


    def __init__(self, podcastURL, podcastParseType = 'rss'):

        """
        Initialise and run required actions to parse and return usable data from a given podcast url
        """
        
        # set url
        self.url = podcastURL
        
        # check podcast type and set correct parse method
        if podcastParseType == 'rss':
            
            # set correct getEpisodes function
            self.getEpisodes = lambda: self.getEpisodesRSS()
                    
        elif podcastParseType == 'ustream':
            
            self.getEpisodes = lambda: self.getEpisodesUStream()


    def getRemoteData(self, url):

        """
        Retrieve a given url and return its data as a string
        """

        # open url
        client = urllib2.urlopen(url)
        
        # read data from url
        data = client.read()
        
        # close connection
        client.close()
        
        # return the data read from url
        return data


    def getEpisodesRSS(self):
        
        """
        Parse RSS feed using element tree to return a list of episodes which can be added to a list in xbmc and played
        """
        
        # declare empty list to store episodes
        episodeList = []
        
        # retrieve data from podcast url
        data = self.getRemoteData(self.url)
        
        #log(data)
        
        # initialise the tree object using the returned data so it can be parsed
        tree = ET.fromstring(data)
                
        # loop over each found item in the feed
        for rssItem in tree.findall('.//item'):
            
            log('#########################')
            
            # declare empty dict to store episode info
            episode = {}
            
            # set episode title
            episode['title'] = rssItem.findtext('title').encode('utf-8')
            log("Episode Title: %s" % episode['title'])
            
            # set episode url
            try:
                episode['url'] = rssItem.find('enclosure').attrib.get('url')
            except Exception, e:
                log(str(e), xbmc.LOGERROR)
                episode['url'] = None
            log("Episode URL: %s" % episode['url'])
            
            # set episode description
            try:
                episode['description'] = rssItem.findtext('{http://www.itunes.com/dtds/podcast-1.0.dtd}summary').encode('utf-8')
            except Exception, e:
                log(str(e), xbmc.LOGERROR)
                episode['description'] = None
            log("Episode Description: %s" % episode['description'])

            # set episode description
            episode['date'] = rssItem.findtext('pubDate')
            log("Episode Date: %s" % episode['date'])
            
            # add episode to list
            episodeList.append(episode)
        
        log('#########################')
            
        #return list of all episodes found in feed
        return episodeList


    def getEpisodesUStream(self):
        
        """
        Parse RSS feed using element tree to return a list of episodes which can be added to a list in xbmc and played
        """
        
        # declare empty list to store episodes
        episodeList = []
        
        # retrieve data from podcast url
        data = self.getRemoteData(self.url)
        
        #log(data)
        
        # initialise the tree object using the returned data so it can be parsed
        tree = ET.fromstring(data)
        
        # loop over each found item in the feed
        for rssItem in tree.findall('.//array'):
            
            log('#########################')
            try:
                # declare empty dict to store episode info
                episode = {}
                # set episode title
                episode['title'] = rssItem.findtext('title')
                log("Episode Title: %s" % episode['title'])
                # set episode url
                epURL = rssItem.findtext('mp4Url')
                if not epURL == None:
                    episode['url'] = epURL.split("?")[0]
                else:
                    episode['url'] = epURL
                log("Episode URL: %s" % episode['url'])
                # set episode description
                episode['description'] = rssItem.findtext('description')
                log("Episode Description: %s" % episode['description'])
                # set episode id
                episode['id'] = int(rssItem.findtext('id'))
                log("Episode ID: %s" % str(episode['id']))
                # set episode length
                episode['runtime'] = "%s:%s" % (str(int(rssItem.findtext('lengthInSecond').split('.')[0]) / 60), str(int(rssItem.findtext('lengthInSecond').split('.')[0]) % 60))
                log("Episode Runtime: %s" % str(episode['runtime']))
                # set episode date
                episode['date'] = rssItem.findtext('createdAt').split(' ')[0]
                log("Episode Date: %s" % episode['date'])
                # set episode rating
                episode['rating'] = float(rssItem.findtext('rating'))
                log("Episode Rating: %s" % episode['rating'])
                # set episode thumb
                episode['thumb'] = rssItem.findtext('imageUrl/medium')
                log("Episode Thumb: %s" % episode['thumb'])
                # add episode to list
                episodeList.append(episode)
            except:
                pass
        log('#########################')
            
        #return list of all episodes found in feed
        return episodeList
