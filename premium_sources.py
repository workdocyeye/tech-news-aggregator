#!/usr/bin/env python3
"""
GitHub Actions优化版信息源配置
专为GitHub Actions环境优化，确保高可用性和稳定性
"""

from typing import List, Dict

class GitHubOptimizedSources:
    """GitHub Actions优化版信息源管理器"""
    
    def __init__(self):
        self.sources = self._load_github_optimized_sources()
    
    def get_all_sources(self) -> List[Dict]:
        """获取所有信息源"""
        return self.sources
    
    def get_sources_by_category(self, category: str) -> List[Dict]:
        """按分类获取信息源"""
        return [source for source in self.sources if source['category'] == category]
    
    def _load_github_optimized_sources(self) -> List[Dict]:
        """加载GitHub Actions优化的信息源配置"""
        
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
            }
        ]
        
        # 🤖 AI领域 - 稳定可访问的源
        ai_sources = [
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
            }
        ]
        
        # 🚀 创业投资 - 高更新频率源
        startup_sources = [
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
            }
        ]
        
        # 🌉 硅谷动态 - 可靠的分析源
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
            }
        ]
        
        # 💻 科技媒体 - 高频更新源
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
                'name': 'ZDNet',
                'url': 'https://www.zdnet.com/news/rss.xml',
                'category': 'tech',
                'priority': 'medium',
                'reliability': 'excellent',
                'description': '企业科技新闻'
            },
            {
                'name': 'TechRadar',
                'url': 'https://www.techradar.com/rss',
                'category': 'tech',
                'priority': 'medium',
                'reliability': 'good',
                'description': '科技产品资讯'
            },
            {
                'name': 'Engadget',
                'url': 'https://www.engadget.com/rss.xml',
                'category': 'tech',
                'priority': 'medium',
                'reliability': 'excellent',
                'description': '消费科技新闻'
            }
        ]
        
        # 合并所有源
        sources.extend(github_sources)
        sources.extend(ai_sources)
        sources.extend(startup_sources)
        sources.extend(silicon_valley_sources)
        sources.extend(tech_sources)
        
        return sources
    
    def get_categories(self) -> Dict[str, str]:
        """获取分类说明"""
        return {
            'github': '🐙 GitHub生态',
            'ai': '🤖 AI前沿',
            'startup': '🚀 创业投资',
            'silicon_valley': '🌉 硅谷动态',
            'tech': '💻 科技资讯'
        }
    
    def get_high_priority_sources(self) -> List[Dict]:
        """获取高优先级信息源"""
        return [source for source in self.sources if source['priority'] == 'high']
    
    def get_excellent_reliability_sources(self) -> List[Dict]:
        """获取高可靠性信息源"""
        return [source for source in self.sources if source.get('reliability') == 'excellent']

if __name__ == "__main__":
    # 测试GitHub优化版信息源
    sources = GitHubOptimizedSources()
    
    print("🚀 GitHub Actions优化版信息源配置")
    print("=" * 50)
    
    categories = sources.get_categories()
    for category, name in categories.items():
        category_sources = sources.get_sources_by_category(category)
        print(f"\n{name} ({len(category_sources)}个源):")
        
        for source in category_sources:
            priority_icon = "🔥" if source['priority'] == 'high' else "📌"
            reliability_icon = "⭐" if source.get('reliability') == 'excellent' else "✓"
            print(f"  {priority_icon}{reliability_icon} {source['name']}")
    
    print(f"\n📊 总计: {len(sources.get_all_sources())} 个信息源")
    print(f"🔥 高优先级: {len(sources.get_high_priority_sources())} 个")
    print(f"⭐ 高可靠性: {len(sources.get_excellent_reliability_sources())} 个") 