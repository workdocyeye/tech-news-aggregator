import json
from datetime import datetime
from typing import Dict, List, Any
from smart_translator import SmartTranslator

class ReportGenerator:
    """多版本报告生成器"""
    
    def __init__(self, enable_translation: bool = True):
        self.translator = SmartTranslator() if enable_translation else None
        self.enable_translation = enable_translation
    
    def generate_all_versions(self, news_data: List[Dict]) -> Dict[str, str]:
        """生成所有版本的报告"""
        
        # 处理和分类新闻数据
        processed_data = self._process_news_data(news_data)
        
        # 生成三个版本
        versions = {
            'english': self._generate_english_version(processed_data),
            'bilingual': self._generate_bilingual_version(processed_data),
            'podcast': self._generate_podcast_version(processed_data)
        }
        
        return versions
    
    def _process_news_data(self, news_data: List[Dict]) -> Dict:
        """处理和分类新闻数据"""
        
        # 按分类整理新闻
        categories = {
            'AI/ML': [],
            'Open Source': [],
            'Startups': [],
            'Security': [],
            'Mobile': [],
            'Web Dev': [],
            'Other': []
        }
        
        for item in news_data:
            category = self._categorize_news(item)
            categories[category].append(item)
        
        # 统计信息
        stats = {
            'total': len(news_data),
            'by_category': {k: len(v) for k, v in categories.items() if v},
            'date': datetime.now().strftime('%Y-%m-%d')
        }
        
        return {
            'stats': stats,
            'categories': categories,
            'top_stories': news_data[:10]  # 前10条作为重点新闻
        }
    
    def _categorize_news(self, item: Dict) -> str:
        """新闻分类"""
        title = item.get('title', '').lower()
        content = item.get('summary', '').lower()
        text = f"{title} {content}"
        
        if any(keyword in text for keyword in ['ai', 'artificial intelligence', 'machine learning', 'gpt', 'llm']):
            return 'AI/ML'
        elif any(keyword in text for keyword in ['open source', 'github', 'repository']):
            return 'Open Source'
        elif any(keyword in text for keyword in ['startup', 'funding', 'investment', 'ipo']):
            return 'Startups'
        elif any(keyword in text for keyword in ['security', 'vulnerability', 'breach', 'hack']):
            return 'Security'
        elif any(keyword in text for keyword in ['mobile', 'ios', 'android', 'app']):
            return 'Mobile'
        elif any(keyword in text for keyword in ['web', 'javascript', 'react', 'frontend']):
            return 'Web Dev'
        else:
            return 'Other'
    
    def _generate_english_version(self, data: Dict) -> str:
        """生成英文原版"""
        stats = data['stats']
        categories = data['categories']
        
        content = f"""# 🌍 Daily Tech News - {stats['date']}

## 📊 Today's Overview
- **Total Articles**: {stats['total']}
"""
        
        # 添加分类统计
        for category, count in stats['by_category'].items():
            content += f"- **{category}**: {count} articles\n"
        
        content += "\n## 🔥 Top Stories\n\n"
        
        # 添加重点新闻
        for i, item in enumerate(data['top_stories'], 1):
            content += f"""### {i}. {item.get('title', 'No Title')}
**Source**: {item.get('source', 'Unknown')} | **Time**: {item.get('time', 'Unknown')}
**Summary**: {item.get('summary', 'No summary available')}
**Link**: [{item.get('title', 'Read More')}]({item.get('url', '#')})

"""
        
        # 按分类添加其他新闻
        for category, items in categories.items():
            if items and category != 'Other':
                content += f"\n## 💻 {category}\n\n"
                for item in items[:5]:  # 每个分类最多5条
                    content += f"- **[{item.get('title', 'No Title')}]({item.get('url', '#')})**\n"
                    content += f"  {item.get('summary', 'No summary')[:100]}...\n\n"
        
        return content
    
    def _generate_bilingual_version(self, data: Dict) -> str:
        """生成中英混合版"""
        stats = data['stats']
        
        content = f"""# 🌟 每日科技简报 - {stats['date']}

## 📊 今日概览 (Today's Overview)
- **总计资讯**: {stats['total']}条 (Total: {stats['total']} articles)
"""
        
        # 添加分类统计
        for category, count in stats['by_category'].items():
            if self.enable_translation and self.translator:
                cn_category = self.translator.translate_content(category)
            else:
                cn_category = category
            content += f"- **{cn_category}**: {count}条 ({category}: {count})\n"
        
        content += "\n## 🔥 今日热点 (Top Stories)\n\n"
        
        # 添加重点新闻（中英对照）
        for i, item in enumerate(data['top_stories'], 1):
            title = item.get('title', 'No Title')
            summary = item.get('summary', 'No summary available')
            
            # 翻译标题和摘要
            if self.enable_translation and self.translator:
                cn_title = self.translator.translate_content(title)
                cn_summary = self.translator.translate_content(summary)
            else:
                cn_title = title
                cn_summary = summary
            
            content += f"""### {i}. {cn_title}
**原标题**: {title}
**来源**: {item.get('source', 'Unknown')} | **时间**: {item.get('time', 'Unknown')}
**摘要**: {cn_summary}
**原文摘要**: {summary}
**链接**: [查看详情]({item.get('url', '#')})

"""
        
        return content
    
    def _generate_podcast_version(self, data: Dict) -> str:
        """生成播客制作版"""
        stats = data['stats']
        top_stories = data['top_stories']
        
        # 处理没有新闻的情况
        if not top_stories:
            return f"""# 🎙️ 播客脚本素材 - {stats['date']}

## ⚠️ 今日无新闻数据
今天暂时没有收集到新的科技资讯，请稍后再试。

## 📋 备用开场白
"大家好，欢迎收听今日科技播客。我是[主持人]，今天是{stats['date']}。今天我们暂时没有新的资讯更新，但我们会继续为大家关注科技动态。"
"""
        
        content = f"""# 🎙️ 播客脚本素材 - {stats['date']}

## 🎬 节目概览
**建议时长**: 15-20分钟
**主要话题**: {min(3, len(top_stories))}个
**快讯数量**: {min(5, max(0, stats['total'] - 3))}条
**深度讨论**: 2个话题

## 📋 开场白素材
"大家好，欢迎收听今日科技播客。我是[主持人]，今天是{stats['date']}。今天我们为大家带来{stats['total']}条最新科技资讯，其中包括{top_stories[0].get('title', '重要新闻')[:30]}...等重磅消息。"

## 🔥 主要话题讨论

"""
        
        # 生成主要话题
        for i, story in enumerate(top_stories[:3], 1):
            title = story.get('title', 'No Title')
            summary = story.get('summary', 'No summary')
            
            content += f"""### 话题{i}：{title}（建议讨论时间：5-7分钟）

**核心要点**：
- {summary[:100]}...
- 对行业的潜在影响
- 技术发展趋势分析

**讨论角度**：
- 技术分析：深入解读技术细节
- 商业影响：对市场和用户的意义
- 未来展望：可能的发展方向

**引用来源**：{story.get('source', 'Unknown')}
**详细链接**：{story.get('url', '#')}

"""
        
        # 生成快讯部分
        content += "## ⚡ 科技快讯（建议时间：3-4分钟）\n\n"
        
        quick_news = top_stories[3:8]  # 第4-8条作为快讯
        for i, news in enumerate(quick_news, 1):
            content += f"""### 快讯{i}：{news.get('title', 'No Title')[:50]}...
"{news.get('summary', 'No summary')[:150]}..."

"""
        
        # 结束语
        content += f"""## 🎯 结束语素材
"以上就是今天的科技资讯。从{top_stories[0].get('title', '主要新闻')[:30]}...到{top_stories[1].get('title', '其他新闻')[:30]}...，我们可以看到科技行业正在快速发展。我们明天同一时间再见，感谢收听！"

## 📊 补充数据和引用
- 今日资讯总数：{stats['total']}条
- 主要来源：{', '.join(set(item.get('source', 'Unknown') for item in top_stories[:5]))}
- 热门话题：{', '.join(stats['by_category'].keys())}

## 🔗 相关链接（供深度了解）
"""
        
        for i, story in enumerate(top_stories[:5], 1):
            content += f"{i}. [{story.get('title', 'No Title')}]({story.get('url', '#')})\n"
        
        return content

# 测试代码
if __name__ == "__main__":
    # 模拟新闻数据
    sample_data = [
        {
            'title': 'OpenAI releases GPT-4 Turbo with enhanced capabilities',
            'summary': 'OpenAI today announced GPT-4 Turbo, featuring longer context windows and 50% cost reduction.',
            'url': 'https://example.com/news1',
            'source': 'TechCrunch',
            'time': '2024-01-15 09:30'
        },
        {
            'title': 'Google open-sources new AI framework',
            'summary': 'Google has released Gemini Framework, an open-source AI development framework.',
            'url': 'https://example.com/news2', 
            'source': 'Google AI Blog',
            'time': '2024-01-15 08:45'
        }
    ]
    
    generator = ReportGenerator(enable_translation=False)  # 测试时关闭翻译
    versions = generator.generate_all_versions(sample_data)
    
    print("=== 英文版 ===")
    print(versions['english'][:500])
    print("\n=== 播客版 ===")
    print(versions['podcast'][:500]) 