#!/usr/bin/env python3
"""
GitHub Actions优化版信息源配置 v2.1
大幅扩展信息源，确保每日收集50+条高质量科技资讯
"""

from typing import List, Dict

class GitHubOptimizedSources:
    """GitHub Actions优化版信息源管理器 - 扩展版"""
    
    def __init__(self):
        self.sources = self._load_github_optimized_sources()
    
    def get_all_sources(self) -> List[Dict]:
        """获取所有信息源"""
        return self.sources
    
    def get_sources_by_category(self, category: str) -> List[Dict]:
        """按分类获取信息源"""
        return [source for source in self.sources if source['category'] == category]
    
    def _load_github_optimized_sources(self) -> List[Dict]:
        """加载GitHub Actions优化的信息源配置 - 大幅扩展版"""
        
        sources = []
        
        # 🐙 GitHub生态 - 高可用性源
        github_sources = [
            {
                'name': 'GitHub Blog',
                'url': 'https://github.blog/feed/',
                'category': 'github',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'GitHub官方博客，产品更新和技术分享'
            },
            {
                'name': 'GitHub Changelog',
                'url': 'https://github.blog/changelog/feed/',
                'category': 'github',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'GitHub功能更新和变化'
            },
            {
                'name': 'GitHub Developer',
                'url': 'https://docs.github.com/en/developers/feed.xml',
                'category': 'github',
                'priority': 'medium',
                'reliability': 'good',
                'description': 'GitHub开发者文档更新'
            },
            {
                'name': 'GitHub Engineering',
                'url': 'https://github.blog/category/engineering/feed/',
                'category': 'github',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'GitHub工程技术博客'
            }
        ]
        
        # 🤖 AI/ML领域 - 大幅扩展
        ai_sources = [
            {
                'name': 'OpenAI Blog',
                'url': 'https://openai.com/blog/rss.xml',
                'category': 'ai',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'OpenAI官方博客'
            },
            {
                'name': 'Anthropic Blog',
                'url': 'https://www.anthropic.com/news/rss.xml',
                'category': 'ai',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'Anthropic AI研究博客'
            },
            {
                'name': 'Google AI Blog',
                'url': 'https://ai.googleblog.com/feeds/posts/default',
                'category': 'ai',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'Google AI研究博客'
            },
            {
                'name': 'DeepMind Blog',
                'url': 'https://deepmind.com/blog/feed/basic/',
                'category': 'ai',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'DeepMind研究博客'
            },
            {
                'name': 'Hugging Face Blog',
                'url': 'https://huggingface.co/blog/feed.xml',
                'category': 'ai',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'Hugging Face技术博客和模型更新'
            },
            {
                'name': 'Papers With Code',
                'url': 'https://paperswithcode.com/latest',
                'category': 'ai',
                'priority': 'high',
                'reliability': 'good',
                'description': 'AI论文和代码实现'
            },
            {
                'name': 'AI News',
                'url': 'https://artificialintelligence-news.com/feed/',
                'category': 'ai',
                'priority': 'medium',
                'reliability': 'good',
                'description': 'AI行业新闻和趋势'
            },
            {
                'name': 'Machine Learning Mastery',
                'url': 'https://machinelearningmastery.com/feed/',
                'category': 'ai',
                'priority': 'medium',
                'reliability': 'excellent',
                'description': 'ML教程和实践指南'
            },
            {
                'name': 'Towards Data Science',
                'url': 'https://towardsdatascience.com/feed',
                'category': 'ai',
                'priority': 'medium',
                'reliability': 'good',
                'description': 'Medium上的数据科学文章'
            },
            {
                'name': 'MIT Technology Review AI',
                'url': 'https://www.technologyreview.com/topic/artificial-intelligence/feed/',
                'category': 'ai',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'MIT科技评论AI专栏'
            },
            {
                'name': 'AI Research',
                'url': 'https://ai.facebook.com/blog/rss/',
                'category': 'ai',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'Meta AI研究博客'
            },
            {
                'name': 'NVIDIA AI Blog',
                'url': 'https://blogs.nvidia.com/ai/feed/',
                'category': 'ai',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'NVIDIA AI技术博客'
            }
        ]
        
        # 🚀 创业投资 - 扩展版
        startup_sources = [
            {
                'name': 'TechCrunch',
                'url': 'https://techcrunch.com/feed/',
                'category': 'startup',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'TechCrunch全站新闻'
            },
            {
                'name': 'TechCrunch Startups',
                'url': 'https://techcrunch.com/category/startups/feed/',
                'category': 'startup',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'TechCrunch创业新闻'
            },
            {
                'name': 'VentureBeat',
                'url': 'https://venturebeat.com/feed/',
                'category': 'startup',
                'priority': 'high',
                'reliability': 'excellent',
                'description': '科技创业和投资新闻'
            },
            {
                'name': 'Product Hunt',
                'url': 'https://www.producthunt.com/feed',
                'category': 'startup',
                'priority': 'high',
                'reliability': 'good',
                'description': '新产品发现平台'
            },
            {
                'name': 'Startup Grind',
                'url': 'https://startupgrind.com/feed/',
                'category': 'startup',
                'priority': 'medium',
                'reliability': 'good',
                'description': '创业社区资讯'
            },
            {
                'name': 'AngelList Blog',
                'url': 'https://angel.co/blog/feed',
                'category': 'startup',
                'priority': 'medium',
                'reliability': 'good',
                'description': '创业投资平台博客'
            },
            {
                'name': 'First Round Review',
                'url': 'https://review.firstround.com/rss',
                'category': 'startup',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'First Round创业指南'
            },
            {
                'name': 'Y Combinator Blog',
                'url': 'https://blog.ycombinator.com/feed/',
                'category': 'startup',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'Y Combinator官方博客'
            },
            {
                'name': 'a16z Blog',
                'url': 'https://a16z.com/feed/',
                'category': 'startup',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'Andreessen Horowitz投资观点'
            },
            {
                'name': 'Sequoia Capital Blog',
                'url': 'https://www.sequoiacap.com/feed/',
                'category': 'startup',
                'priority': 'high',
                'reliability': 'excellent',
                'description': '红杉资本投资洞察'
            }
        ]
        
        # 🌉 硅谷动态 - 扩展版
        silicon_valley_sources = [
            {
                'name': 'Benedict Evans',
                'url': 'https://www.ben-evans.com/benedictevans?format=rss',
                'category': 'silicon_valley',
                'priority': 'high',
                'reliability': 'excellent',
                'description': '前a16z合伙人的科技观察'
            },
            {
                'name': 'TechMeme',
                'url': 'https://www.techmeme.com/feed.xml',
                'category': 'silicon_valley',
                'priority': 'high',
                'reliability': 'excellent',
                'description': '科技新闻聚合和热门话题'
            },
            {
                'name': 'Recode',
                'url': 'https://www.vox.com/recode/rss/index.xml',
                'category': 'silicon_valley',
                'priority': 'medium',
                'reliability': 'good',
                'description': '科技商业分析'
            },
            {
                'name': 'All Things D',
                'url': 'https://allthingsd.com/feed/',
                'category': 'silicon_valley',
                'priority': 'medium',
                'reliability': 'good',
                'description': '数字化商业新闻'
            },
            {
                'name': 'The Information',
                'url': 'https://www.theinformation.com/feed',
                'category': 'silicon_valley',
                'priority': 'high',
                'reliability': 'excellent',
                'description': '硅谷深度报道'
            },
            {
                'name': 'Stratechery',
                'url': 'https://stratechery.com/feed/',
                'category': 'silicon_valley',
                'priority': 'high',
                'reliability': 'excellent',
                'description': '科技战略分析'
            }
        ]
        
        # 💻 科技媒体 - 大幅扩展
        tech_sources = [
            {
                'name': 'The Verge',
                'url': 'https://www.theverge.com/rss/index.xml',
                'category': 'tech',
                'priority': 'high',
                'reliability': 'excellent',
                'description': '科技新闻和产品评测'
            },
            {
                'name': 'Wired',
                'url': 'https://www.wired.com/feed/rss',
                'category': 'tech',
                'priority': 'high',
                'reliability': 'excellent',
                'description': '科技文化和未来趋势'
            },
            {
                'name': 'Ars Technica',
                'url': 'http://feeds.arstechnica.com/arstechnica/index',
                'category': 'tech',
                'priority': 'high',
                'reliability': 'excellent',
                'description': '深度技术分析'
            },
            {
                'name': 'Engadget',
                'url': 'https://www.engadget.com/rss.xml',
                'category': 'tech',
                'priority': 'high',
                'reliability': 'excellent',
                'description': '消费电子和科技产品'
            },
            {
                'name': 'TechRadar',
                'url': 'https://www.techradar.com/rss',
                'category': 'tech',
                'priority': 'medium',
                'reliability': 'good',
                'description': '科技产品评测和新闻'
            },
            {
                'name': 'ZDNet',
                'url': 'https://www.zdnet.com/news/rss.xml',
                'category': 'tech',
                'priority': 'medium',
                'reliability': 'good',
                'description': '企业技术新闻'
            },
            {
                'name': 'CNET',
                'url': 'https://www.cnet.com/rss/news/',
                'category': 'tech',
                'priority': 'medium',
                'reliability': 'good',
                'description': '消费科技新闻'
            },
            {
                'name': 'MIT Technology Review',
                'url': 'https://www.technologyreview.com/feed/',
                'category': 'tech',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'MIT科技评论'
            },
            {
                'name': 'IEEE Spectrum',
                'url': 'https://spectrum.ieee.org/rss/fulltext',
                'category': 'tech',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'IEEE技术前沿'
            },
            {
                'name': 'Fast Company Tech',
                'url': 'https://www.fastcompany.com/technology/rss',
                'category': 'tech',
                'priority': 'medium',
                'reliability': 'good',
                'description': '科技商业创新'
            }
        ]
        
        # 🔓 开源社区 - 新增分类
        opensource_sources = [
            {
                'name': 'Linux Foundation',
                'url': 'https://www.linuxfoundation.org/feed/',
                'category': 'opensource',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'Linux基金会新闻'
            },
            {
                'name': 'Apache Software Foundation',
                'url': 'https://blogs.apache.org/foundation/feed/entries/atom',
                'category': 'opensource',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'Apache基金会博客'
            },
            {
                'name': 'Mozilla Blog',
                'url': 'https://blog.mozilla.org/feed/',
                'category': 'opensource',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'Mozilla官方博客'
            },
            {
                'name': 'Red Hat Blog',
                'url': 'https://www.redhat.com/en/rss/blog',
                'category': 'opensource',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'Red Hat技术博客'
            },
            {
                'name': 'Docker Blog',
                'url': 'https://www.docker.com/blog/feed/',
                'category': 'opensource',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'Docker官方博客'
            },
            {
                'name': 'Kubernetes Blog',
                'url': 'https://kubernetes.io/feed.xml',
                'category': 'opensource',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'Kubernetes官方博客'
            },
            {
                'name': 'CNCF Blog',
                'url': 'https://www.cncf.io/feed/',
                'category': 'opensource',
                'priority': 'high',
                'reliability': 'excellent',
                'description': '云原生计算基金会'
            }
        ]
        
        # 🏢 企业科技 - 新增分类
        enterprise_sources = [
            {
                'name': 'Microsoft Blog',
                'url': 'https://blogs.microsoft.com/feed/',
                'category': 'enterprise',
                'priority': 'high',
                'reliability': 'excellent',
                'description': '微软官方博客'
            },
            {
                'name': 'AWS News',
                'url': 'https://aws.amazon.com/blogs/aws/feed/',
                'category': 'enterprise',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'AWS官方新闻'
            },
            {
                'name': 'Google Cloud Blog',
                'url': 'https://cloud.google.com/blog/rss/',
                'category': 'enterprise',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'Google Cloud博客'
            },
            {
                'name': 'Azure Blog',
                'url': 'https://azure.microsoft.com/en-us/blog/feed/',
                'category': 'enterprise',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'Azure云服务博客'
            },
            {
                'name': 'Salesforce Blog',
                'url': 'https://www.salesforce.com/news/feed/',
                'category': 'enterprise',
                'priority': 'medium',
                'reliability': 'good',
                'description': 'Salesforce企业解决方案'
            },
            {
                'name': 'Oracle Blog',
                'url': 'https://blogs.oracle.com/feed/',
                'category': 'enterprise',
                'priority': 'medium',
                'reliability': 'good',
                'description': 'Oracle技术博客'
            }
        ]
        
        # 📱 移动开发 - 新增分类
        mobile_sources = [
            {
                'name': 'Android Developers Blog',
                'url': 'https://android-developers.googleblog.com/feeds/posts/default',
                'category': 'mobile',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'Android开发者博客'
            },
            {
                'name': 'iOS Dev Weekly',
                'url': 'https://iosdevweekly.com/issues.rss',
                'category': 'mobile',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'iOS开发周刊'
            },
            {
                'name': 'React Native Blog',
                'url': 'https://reactnative.dev/blog/rss.xml',
                'category': 'mobile',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'React Native官方博客'
            },
            {
                'name': 'Flutter Blog',
                'url': 'https://medium.com/flutter/feed',
                'category': 'mobile',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'Flutter官方博客'
            }
        ]
        
        # 🔐 网络安全 - 新增分类
        security_sources = [
            {
                'name': 'Krebs on Security',
                'url': 'https://krebsonsecurity.com/feed/',
                'category': 'security',
                'priority': 'high',
                'reliability': 'excellent',
                'description': '网络安全深度报道'
            },
            {
                'name': 'Dark Reading',
                'url': 'https://www.darkreading.com/rss_simple.asp',
                'category': 'security',
                'priority': 'high',
                'reliability': 'excellent',
                'description': '企业安全新闻'
            },
            {
                'name': 'The Hacker News',
                'url': 'https://feeds.feedburner.com/TheHackersNews',
                'category': 'security',
                'priority': 'high',
                'reliability': 'excellent',
                'description': '网络安全新闻'
            },
            {
                'name': 'Threatpost',
                'url': 'https://threatpost.com/feed/',
                'category': 'security',
                'priority': 'medium',
                'reliability': 'good',
                'description': '威胁情报和安全新闻'
            }
        ]
        
        # 🌐 Web开发 - 新增分类
        webdev_sources = [
            {
                'name': 'CSS-Tricks',
                'url': 'https://css-tricks.com/feed/',
                'category': 'webdev',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'CSS和前端开发技巧'
            },
            {
                'name': 'Smashing Magazine',
                'url': 'https://www.smashingmagazine.com/feed/',
                'category': 'webdev',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'Web设计和开发'
            },
            {
                'name': 'A List Apart',
                'url': 'https://alistapart.com/main/feed/',
                'category': 'webdev',
                'priority': 'high',
                'reliability': 'excellent',
                'description': 'Web标准和最佳实践'
            },
            {
                'name': 'Dev.to',
                'url': 'https://dev.to/feed',
                'category': 'webdev',
                'priority': 'medium',
                'reliability': 'good',
                'description': '开发者社区文章'
            }
        ]
        
        # 合并所有源
        sources.extend(github_sources)
        sources.extend(ai_sources)
        sources.extend(startup_sources)
        sources.extend(silicon_valley_sources)
        sources.extend(tech_sources)
        sources.extend(opensource_sources)
        sources.extend(enterprise_sources)
        sources.extend(mobile_sources)
        sources.extend(security_sources)
        sources.extend(webdev_sources)
        
        return sources
    
    def get_categories(self) -> Dict[str, str]:
        """获取分类映射"""
        return {
            'github': '🐙 GitHub生态',
            'ai': '🤖 AI/机器学习',
            'startup': '🚀 创业投资',
            'silicon_valley': '🌉 硅谷动态',
            'tech': '💻 科技媒体',
            'opensource': '🔓 开源社区',
            'enterprise': '🏢 企业科技',
            'mobile': '📱 移动开发',
            'security': '🔐 网络安全',
            'webdev': '🌐 Web开发'
        }
    
    def get_high_priority_sources(self) -> List[Dict]:
        """获取高优先级源"""
        return [source for source in self.sources if source['priority'] == 'high']
    
    def get_excellent_reliability_sources(self) -> List[Dict]:
        """获取高可靠性源"""
        return [source for source in self.sources if source['reliability'] == 'excellent']
    
    def get_source_count_by_category(self) -> Dict[str, int]:
        """获取各分类的源数量统计"""
        categories = {}
        for source in self.sources:
            category = source['category']
            categories[category] = categories.get(category, 0) + 1
        return categories
    
    def print_sources_summary(self):
        """打印信息源概览"""
        total = len(self.sources)
        high_priority = len(self.get_high_priority_sources())
        excellent = len(self.get_excellent_reliability_sources())
        categories = self.get_source_count_by_category()
        
        print(f"📊 信息源统计:")
        print(f"   总计: {total} 个源")
        print(f"   高优先级: {high_priority} 个")
        print(f"   高可靠性: {excellent} 个")
        print(f"   分类分布:")
        for category, count in categories.items():
            category_name = self.get_categories().get(category, category)
            print(f"     {category_name}: {count} 个")

# 测试代码
if __name__ == "__main__":
    print("🚀 测试GitHub Actions优化版信息源配置 v2.1")
    print("=" * 60)
    
    sources_manager = GitHubOptimizedSources()
    sources_manager.print_sources_summary()
    
    print("\n🔍 详细分类信息:")
    categories = sources_manager.get_categories()
    for category_id, category_name in categories.items():
        category_sources = sources_manager.get_sources_by_category(category_id)
        print(f"\n{category_name} ({len(category_sources)} 个源):")
        
        for source in category_sources[:3]:  # 只显示前3个
            priority_icon = "🔥" if source['priority'] == 'high' else "📌"
            reliability_icon = "⭐" if source['reliability'] == 'excellent' else "✓"
            print(f"  {priority_icon}{reliability_icon} {source['name']}")
        
        if len(category_sources) > 3:
            print(f"  ... 还有 {len(category_sources) - 3} 个源")
    
    print(f"\n✅ 总计: {len(sources_manager.get_all_sources())} 个信息源")
    print(f"🔥 高优先级: {len(sources_manager.get_high_priority_sources())} 个")
    print(f"⭐ 高可靠性: {len(sources_manager.get_excellent_reliability_sources())} 个") 