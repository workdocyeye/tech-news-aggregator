#!/usr/bin/env python3
"""
RSS源配置 - 优质科技媒体
"""

def get_rss_sources():
    """获取RSS源列表"""
    return [
        {
            'name': 'TechCrunch',
            'url': 'https://techcrunch.com/feed/',
            'category': 'Tech News',
            'language': 'en'
        },
        {
            'name': 'The Verge',
            'url': 'https://www.theverge.com/rss/index.xml',
            'category': 'Tech News',
            'language': 'en'
        },
        {
            'name': 'Ars Technica',
            'url': 'https://feeds.arstechnica.com/arstechnica/index',
            'category': 'Tech News',
            'language': 'en'
        },
        {
            'name': 'Wired',
            'url': 'https://www.wired.com/feed/rss',
            'category': 'Tech News',
            'language': 'en'
        },
        {
            'name': 'MIT Technology Review',
            'url': 'https://www.technologyreview.com/feed/',
            'category': 'Tech Research',
            'language': 'en'
        },
        {
            'name': 'GitHub Blog',
            'url': 'https://github.blog/feed/',
            'category': 'Open Source',
            'language': 'en'
        },
        {
            'name': 'Hacker News',
            'url': 'https://hnrss.org/frontpage',
            'category': 'Tech Community',
            'language': 'en'
        },
        {
            'name': 'VentureBeat',
            'url': 'https://venturebeat.com/feed/',
            'category': 'Startups',
            'language': 'en'
        },
        {
            'name': 'TechNews',
            'url': 'https://www.technewsworld.com/perl/syndication/rssfull.pl',
            'category': 'Tech News',
            'language': 'en'
        },
        {
            'name': 'ZDNet',
            'url': 'https://www.zdnet.com/news/rss.xml',
            'category': 'Enterprise Tech',
            'language': 'en'
        }
    ] 