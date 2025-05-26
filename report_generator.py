#!/usr/bin/env python3
"""
多版本报告生成器 v2.1
生成英文版、中英混合版和SRT字幕版本
"""

from typing import List, Dict
from datetime import datetime
import os

# 导入智能翻译器和SRT生成器
try:
    from smart_translator import SmartTranslator
except ImportError:
    SmartTranslator = None

try:
    from srt_generator import SRTGenerator
except ImportError:
    SRTGenerator = None

class ReportGenerator:
    """多版本报告生成器"""
    
    def __init__(self, enable_translation: bool = True):
        self.enable_translation = enable_translation and SmartTranslator is not None
        
        # 初始化翻译器
        if self.enable_translation:
            try:
                self.translator = SmartTranslator()
                print("✅ 智能翻译器已启用")
            except Exception as e:
                print(f"⚠️ 翻译器初始化失败: {e}")
                self.enable_translation = False
                self.translator = None
        else:
            self.translator = None
            print("📝 翻译功能已禁用，将生成英文版本")
        
        # 初始化SRT生成器
        if SRTGenerator:
            self.srt_generator = SRTGenerator()
            print("✅ SRT字幕生成器已启用")
        else:
            self.srt_generator = None
            print("⚠️ SRT生成器不可用")
    
    def generate_all_versions(self, news_data: List[Dict]) -> Dict[str, str]:
        """生成所有版本的报告"""
        print(f"📝 开始生成多版本报告，共 {len(news_data)} 条新闻")
        
        # 处理新闻数据
        processed_data = self._process_news_data(news_data)
        
        versions = {}
        
        # 1. 生成英文版
        print("📄 生成英文原版...")
        versions['english'] = self._generate_english_version(processed_data)
        
        # 2. 生成中英混合版
        print("🌏 生成中英混合版...")
        versions['bilingual'] = self._generate_bilingual_version(processed_data)
        
        # 3. 生成SRT字幕版（替代播客版）
        print("🎬 生成SRT字幕版...")
        if self.srt_generator:
            versions['srt'] = self.srt_generator.generate_srt_from_news(news_data)
        else:
            versions['srt'] = self._generate_fallback_srt(processed_data)
        
        print("✅ 所有版本生成完成")
        return versions
    
    def _process_news_data(self, news_data: List[Dict]) -> Dict:
        """处理新闻数据"""
        # 按时间排序
        sorted_news = sorted(news_data, key=lambda x: x.get('time', ''), reverse=True)
        
        # 选择前15条作为重点新闻
        top_stories = sorted_news[:15]
        
        # 分类统计
        categories = {}
        for item in news_data:
            category = self._categorize_news(item)
            if category not in categories:
                categories[category] = []
            categories[category].append(item)
        
        stats = {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'total': len(news_data),
            'by_category': {cat: len(items) for cat, items in categories.items()}
        }
        
        return {
            'stats': stats,
            'top_stories': top_stories,
            'categories': categories
        }
    
    def _categorize_news(self, item: Dict) -> str:
        """新闻分类"""
        title = item.get('title', '').lower()
        summary = item.get('summary', '').lower()
        text = f"{title} {summary}"
        
        if any(keyword in text for keyword in ['ai', 'artificial intelligence', 'machine learning', 'gpt', 'llm', 'neural']):
            return 'AI/ML'
        elif any(keyword in text for keyword in ['github', 'open source', 'repository', 'git']):
            return 'Open Source'
        elif any(keyword in text for keyword in ['startup', 'funding', 'investment', 'ipo', 'venture']):
            return 'Startups'
        elif any(keyword in text for keyword in ['security', 'vulnerability', 'breach', 'hack', 'cyber']):
            return 'Security'
        elif any(keyword in text for keyword in ['mobile', 'ios', 'android', 'app', 'smartphone']):
            return 'Mobile'
        elif any(keyword in text for keyword in ['web', 'javascript', 'react', 'frontend', 'css']):
            return 'Web Dev'
        elif any(keyword in text for keyword in ['cloud', 'aws', 'azure', 'google cloud', 'kubernetes']):
            return 'Cloud'
        else:
            return 'Tech News'
    
    def _generate_english_version(self, data: Dict) -> str:
        """生成英文原版"""
        stats = data['stats']
        categories = data['categories']
        
        content = f"""# 🌍 Daily Tech News - {stats['date']}

## 📊 Today's Overview
- **Total Articles**: {stats['total']}
- **Sources**: Multiple premium tech sources
- **Categories**: {len(stats['by_category'])} different topics
"""
        
        # 添加分类统计
        for category, count in stats['by_category'].items():
            content += f"- **{category}**: {count} articles\n"
        
        content += "\n## 🔥 Top Stories\n\n"
        
        # 添加重点新闻
        for i, item in enumerate(data['top_stories'], 1):
            title = item.get('title', 'No Title')
            summary = item.get('summary', 'No summary available')
            source = item.get('source', 'Unknown')
            time_str = item.get('time', 'Unknown')
            url = item.get('url', '#')
            
            content += f"""### {i}. {title}
**Source**: {source} | **Time**: {time_str}
**Summary**: {summary}
**Link**: [Read More]({url})

"""
        
        # 按分类添加其他新闻
        for category, items in categories.items():
            if items and category != 'Other' and len(items) > 0:
                content += f"\n## 💻 {category}\n\n"
                for item in items[:8]:  # 每个分类最多8条
                    title = item.get('title', 'No Title')
                    url = item.get('url', '#')
                    summary = item.get('summary', 'No summary')
                    source = item.get('source', 'Unknown')
                    
                    content += f"- **[{title}]({url})**\n"
                    content += f"  *{source}* - {summary[:120]}{'...' if len(summary) > 120 else ''}\n\n"
        
        content += f"""
---
*Generated on {stats['date']} by Tech News Aggregator v2.1*
*Total sources processed: {stats['total']} articles*
"""
        
        return content
    
    def _generate_bilingual_version(self, data: Dict) -> str:
        """生成中英混合版"""
        stats = data['stats']
        
        content = f"""# 🌟 每日科技简报 - {stats['date']}

## 📊 今日概览 (Today's Overview)
- **总计资讯**: {stats['total']}条 (Total: {stats['total']} articles)
- **信息源**: 多个优质科技媒体 (Multiple premium tech sources)
- **分类数量**: {len(stats['by_category'])}个主题 (Categories: {len(stats['by_category'])} topics)
"""
        
        # 添加分类统计
        for category, count in stats['by_category'].items():
            if self.enable_translation and self.translator:
                try:
                    cn_category = self.translator.translate_content(category)
                except:
                    cn_category = category
            else:
                cn_category = category
            content += f"- **{cn_category}**: {count}条 ({category}: {count})\n"
        
        content += "\n## 🔥 今日热点 (Top Stories)\n\n"
        
        # 添加重点新闻（中英对照）
        for i, item in enumerate(data['top_stories'][:10], 1):
            title = item.get('title', 'No Title')
            summary = item.get('summary', 'No summary available')
            source = item.get('source', 'Unknown')
            time_str = item.get('time', 'Unknown')
            url = item.get('url', '#')
            
            # 翻译标题和摘要
            if self.enable_translation and self.translator:
                try:
                    cn_title = self.translator.translate_content(title)
                    cn_summary = self.translator.translate_content(summary)
                except Exception as e:
                    print(f"翻译失败: {e}")
                    cn_title = title
                    cn_summary = summary
            else:
                cn_title = title
                cn_summary = summary
            
            content += f"""### {i}. {cn_title}
**原标题**: {title}
**来源**: {source} | **时间**: {time_str}
**摘要**: {cn_summary}
**原文摘要**: {summary}
**链接**: [查看详情]({url})

"""
        
        content += f"""
---
*生成时间: {stats['date']} | Generated by Tech News Aggregator v2.1*
*处理资讯总数: {stats['total']}条 | Total articles processed: {stats['total']}*
"""
        
        return content
    
    def _generate_fallback_srt(self, data: Dict) -> str:
        """生成备用SRT格式（当SRT生成器不可用时）"""
        stats = data['stats']
        
        return f"""1
00:00:00,000 --> 00:00:05,000
大家好，欢迎收听今日科技播客。

2
00:00:05,500 --> 00:00:10,000
今天是{stats['date']}，为您带来{stats['total']}条科技资讯。

3
00:00:10,500 --> 00:00:15,000
由于技术原因，详细字幕暂时无法生成。

4
00:00:15,500 --> 00:00:20,000
请查看英文版和中英混合版获取完整内容。

5
00:00:20,500 --> 00:00:25,000
感谢收听，我们明天再见。

"""

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
    print("\n=== SRT字幕版 ===")
    print(versions['srt'][:500]) 