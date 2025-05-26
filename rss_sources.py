#!/usr/bin/env python3
"""
RSS源配置 - 优质科技媒体
扩展版本 - 包含50+个优质信息源
"""

def get_rss_sources():
    """获取RSS源列表"""
    return [
        # 主流科技媒体
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
            'name': 'Engadget',
            'url': 'https://www.engadget.com/rss.xml',
            'category': 'Tech News',
            'language': 'en'
        },
        {
            'name': 'Gizmodo',
            'url': 'https://gizmodo.com/rss',
            'category': 'Tech News',
            'language': 'en'
        },
        {
            'name': 'Mashable Tech',
            'url': 'https://mashable.com/feeds/rss/tech',
            'category': 'Tech News',
            'language': 'en'
        },
        
        # 技术研究和深度报道
        {
            'name': 'MIT Technology Review',
            'url': 'https://www.technologyreview.com/feed/',
            'category': 'Tech Research',
            'language': 'en'
        },
        {
            'name': 'IEEE Spectrum',
            'url': 'https://spectrum.ieee.org/rss/fulltext',
            'category': 'Tech Research',
            'language': 'en'
        },
        {
            'name': 'Nature Technology',
            'url': 'https://www.nature.com/subjects/electronic-engineering.rss',
            'category': 'Tech Research',
            'language': 'en'
        },
        
        # AI和机器学习
        {
            'name': 'AI News',
            'url': 'https://www.artificialintelligence-news.com/feed/',
            'category': 'AI/ML',
            'language': 'en'
        },
        {
            'name': 'VentureBeat AI',
            'url': 'https://venturebeat.com/ai/feed/',
            'category': 'AI/ML',
            'language': 'en'
        },
        {
            'name': 'OpenAI Blog',
            'url': 'https://openai.com/blog/rss.xml',
            'category': 'AI/ML',
            'language': 'en'
        },
        {
            'name': 'Google AI Blog',
            'url': 'https://ai.googleblog.com/feeds/posts/default',
            'category': 'AI/ML',
            'language': 'en'
        },
        
        # 开源和开发者
        {
            'name': 'GitHub Blog',
            'url': 'https://github.blog/feed/',
            'category': 'Open Source',
            'language': 'en'
        },
        {
            'name': 'GitLab Blog',
            'url': 'https://about.gitlab.com/atom.xml',
            'category': 'Open Source',
            'language': 'en'
        },
        {
            'name': 'Stack Overflow Blog',
            'url': 'https://stackoverflow.blog/feed/',
            'category': 'Open Source',
            'language': 'en'
        },
        {
            'name': 'Dev.to',
            'url': 'https://dev.to/feed',
            'category': 'Open Source',
            'language': 'en'
        },
        {
            'name': 'Hacker News',
            'url': 'https://hnrss.org/frontpage',
            'category': 'Tech Community',
            'language': 'en'
        },
        
        # 创业和投资
        {
            'name': 'VentureBeat',
            'url': 'https://venturebeat.com/feed/',
            'category': 'Startups',
            'language': 'en'
        },
        {
            'name': 'Crunchbase News',
            'url': 'https://news.crunchbase.com/feed/',
            'category': 'Startups',
            'language': 'en'
        },
        {
            'name': 'AngelList Blog',
            'url': 'https://angel.co/blog/feed',
            'category': 'Startups',
            'language': 'en'
        },
        {
            'name': 'Y Combinator Blog',
            'url': 'https://blog.ycombinator.com/feed',
            'category': 'Startups',
            'language': 'en'
        },
        
        # 企业技术
        {
            'name': 'ZDNet',
            'url': 'https://www.zdnet.com/news/rss.xml',
            'category': 'Enterprise Tech',
            'language': 'en'
        },
        {
            'name': 'InfoWorld',
            'url': 'https://www.infoworld.com/index.rss',
            'category': 'Enterprise Tech',
            'language': 'en'
        },
        {
            'name': 'ComputerWorld',
            'url': 'https://www.computerworld.com/index.rss',
            'category': 'Enterprise Tech',
            'language': 'en'
        },
        {
            'name': 'TechTarget',
            'url': 'https://www.techtarget.com/rss/news.xml',
            'category': 'Enterprise Tech',
            'language': 'en'
        },
        
        # 移动和应用
        {
            'name': 'Android Police',
            'url': 'https://www.androidpolice.com/feed/',
            'category': 'Mobile',
            'language': 'en'
        },
        {
            'name': '9to5Mac',
            'url': 'https://9to5mac.com/feed/',
            'category': 'Mobile',
            'language': 'en'
        },
        {
            'name': '9to5Google',
            'url': 'https://9to5google.com/feed/',
            'category': 'Mobile',
            'language': 'en'
        },
        {
            'name': 'MacRumors',
            'url': 'https://feeds.macrumors.com/MacRumors-All',
            'category': 'Mobile',
            'language': 'en'
        },
        
        # 网络安全
        {
            'name': 'Krebs on Security',
            'url': 'https://krebsonsecurity.com/feed/',
            'category': 'Security',
            'language': 'en'
        },
        {
            'name': 'The Hacker News',
            'url': 'https://feeds.feedburner.com/TheHackersNews',
            'category': 'Security',
            'language': 'en'
        },
        {
            'name': 'Dark Reading',
            'url': 'https://www.darkreading.com/rss_simple.asp',
            'category': 'Security',
            'language': 'en'
        },
        {
            'name': 'Security Week',
            'url': 'https://www.securityweek.com/feed',
            'category': 'Security',
            'language': 'en'
        },
        
        # Web开发和前端
        {
            'name': 'CSS-Tricks',
            'url': 'https://css-tricks.com/feed/',
            'category': 'Web Dev',
            'language': 'en'
        },
        {
            'name': 'Smashing Magazine',
            'url': 'https://www.smashingmagazine.com/feed/',
            'category': 'Web Dev',
            'language': 'en'
        },
        {
            'name': 'A List Apart',
            'url': 'https://alistapart.com/main/feed/',
            'category': 'Web Dev',
            'language': 'en'
        },
        {
            'name': 'JavaScript Weekly',
            'url': 'https://javascriptweekly.com/rss/',
            'category': 'Web Dev',
            'language': 'en'
        },
        
        # 云计算和DevOps
        {
            'name': 'AWS News',
            'url': 'https://aws.amazon.com/blogs/aws/feed/',
            'category': 'Cloud',
            'language': 'en'
        },
        {
            'name': 'Google Cloud Blog',
            'url': 'https://cloud.google.com/blog/rss',
            'category': 'Cloud',
            'language': 'en'
        },
        {
            'name': 'Microsoft Azure Blog',
            'url': 'https://azure.microsoft.com/en-us/blog/feed/',
            'category': 'Cloud',
            'language': 'en'
        },
        {
            'name': 'Docker Blog',
            'url': 'https://www.docker.com/blog/feed/',
            'category': 'Cloud',
            'language': 'en'
        },
        {
            'name': 'Kubernetes Blog',
            'url': 'https://kubernetes.io/feed.xml',
            'category': 'Cloud',
            'language': 'en'
        },
        
        # 数据科学和大数据
        {
            'name': 'KDnuggets',
            'url': 'https://www.kdnuggets.com/feed',
            'category': 'Data Science',
            'language': 'en'
        },
        {
            'name': 'Towards Data Science',
            'url': 'https://towardsdatascience.com/feed',
            'category': 'Data Science',
            'language': 'en'
        },
        {
            'name': 'Analytics Vidhya',
            'url': 'https://www.analyticsvidhya.com/feed/',
            'category': 'Data Science',
            'language': 'en'
        },
        
        # 游戏和娱乐技术
        {
            'name': 'Gamasutra',
            'url': 'https://www.gamedeveloper.com/rss.xml',
            'category': 'Gaming Tech',
            'language': 'en'
        },
        {
            'name': 'Unity Blog',
            'url': 'https://blog.unity.com/feed',
            'category': 'Gaming Tech',
            'language': 'en'
        },
        
        # 其他重要科技媒体
        {
            'name': 'TechNews',
            'url': 'https://www.technewsworld.com/perl/syndication/rssfull.pl',
            'category': 'Tech News',
            'language': 'en'
        },
        {
            'name': 'Silicon Valley Business Journal',
            'url': 'https://www.bizjournals.com/sanjose/feeds/latest.xml',
            'category': 'Silicon Valley',
            'language': 'en'
        },
        {
            'name': 'Fast Company Tech',
            'url': 'https://www.fastcompany.com/technology/rss',
            'category': 'Tech News',
            'language': 'en'
        }
    ] 