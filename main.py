#!/usr/bin/env python3
"""
科技资讯聚合系统 v3.0
简化版本 - 只生成三个文件：中文版本、英文版本、SRT中文字幕
"""

import feedparser
import requests
from datetime import datetime, timedelta
from pathlib import Path
import json
import sys
import traceback
from typing import List, Dict, Optional
import time
import re
from bs4 import BeautifulSoup

# 导入模块
from rss_sources import get_rss_sources
from smart_translator import SmartTranslator
from srt_generator import SRTGenerator

class TechNewsAggregator:
    """科技资讯聚合器 - 简化版"""
    
    def __init__(self):
        self.sources = get_rss_sources()
        
        # 初始化翻译器
        try:
            self.translator = SmartTranslator()
            self.translation_enabled = True
            print("✅ 智能翻译器已启用")
        except Exception as e:
            print(f"⚠️ 翻译器初始化失败: {e}")
            self.translator = None
            self.translation_enabled = False
        
        # 初始化SRT生成器
        self.srt_generator = SRTGenerator()
        print("✅ SRT字幕生成器已启用")
    
    def run_daily_collection(self):
        """运行每日收集任务"""
        print(f"🚀 开始收集科技资讯...")
        print(f"📡 RSS源数量: {len(self.sources)}")
        
        # 收集RSS数据
        news_data = self._collect_rss_data()
        
        if not news_data:
            print("❌ 未收集到任何新闻数据")
            self._generate_error_report("未收集到任何新闻数据")
            return
        
        print(f"📰 收集到 {len(news_data)} 条新闻")
        
        # 去重和过滤
        filtered_data = self._remove_duplicates(news_data)
        print(f"🔄 去重后剩余 {len(filtered_data)} 条新闻")
        
        # 生成三个版本的报告
        self._generate_reports(filtered_data)
        
        print("✅ 任务完成！")
    
    def _collect_rss_data(self) -> List[Dict]:
        """收集RSS数据"""
        all_news = []
        
        for source in self.sources:
            try:
                print(f"📡 正在收集: {source['name']}")
                
                # 设置请求头
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }
                
                # 解析RSS
                feed = feedparser.parse(source['url'], request_headers=headers)
                
                if not feed.entries:
                    print(f"   ⚠️ {source['name']}: 无数据")
                    continue
                
                # 处理每个条目
                for entry in feed.entries:
                    news_item = self._parse_rss_entry(entry, source)
                    if news_item and self._is_recent_news(news_item.get('published_time')):
                        all_news.append(news_item)
                
                print(f"   ✅ {source['name']}: 收集到 {len([e for e in feed.entries if self._parse_rss_entry(e, source)])} 条")
                time.sleep(1)  # 避免请求过快
                
            except Exception as e:
                print(f"   ❌ {source['name']}: 收集失败 - {e}")
                continue
        
        return all_news
    
    def _parse_rss_entry(self, entry, source: Dict) -> Optional[Dict]:
        """解析RSS条目"""
        try:
            # 获取标题
            title = entry.get('title', '').strip()
            if not title:
                return None
            
            # 获取摘要
            summary = ''
            if hasattr(entry, 'summary'):
                summary = entry.summary
            elif hasattr(entry, 'description'):
                summary = entry.description
            
            # 清理HTML标签
            if summary:
                summary = BeautifulSoup(summary, 'html.parser').get_text().strip()
            
            # 获取链接
            link = entry.get('link', '')
            
            # 获取发布时间
            published_time = None
            if hasattr(entry, 'published_parsed') and entry.published_parsed:
                published_time = datetime(*entry.published_parsed[:6])
            
            return {
                'title': title,
                'summary': summary[:300] if summary else '',  # 限制摘要长度
                'url': link,
                'source': source['name'],
                'category': source['category'],
                'published_time': published_time,
                'time': published_time.strftime('%Y-%m-%d %H:%M') if published_time else ''
            }
            
        except Exception as e:
            return None
    
    def _is_recent_news(self, news_time) -> bool:
        """检查是否为最近的新闻（24小时内）"""
        if not news_time:
            return True  # 如果没有时间信息，默认包含
        
        try:
            if isinstance(news_time, str):
                return True  # 简化处理
            
            now = datetime.now()
            time_diff = now - news_time
            return time_diff.days <= 1
        except:
            return True
    
    def _remove_duplicates(self, news_data: List[Dict]) -> List[Dict]:
        """去除重复新闻"""
        seen_titles = set()
        unique_news = []
        
        for news in news_data:
            title = news.get('title', '').lower().strip()
            if title and title not in seen_titles:
                seen_titles.add(title)
                unique_news.append(news)
        
        # 按时间排序
        unique_news.sort(key=lambda x: x.get('published_time') or datetime.min, reverse=True)
        
        return unique_news  # 保留全部新闻，不做数量限制
    
    def _generate_reports(self, news_data: List[Dict]):
        """生成三个版本的报告"""
        date_str = datetime.now().strftime('%Y-%m-%d')
        
        # 创建输出目录
        output_dir = Path('output')
        output_dir.mkdir(exist_ok=True)
        
        print("📝 正在生成报告...")
        
        # 1. 生成英文版
        english_content = self._generate_english_report(news_data)
        english_file = output_dir / f"tech_news_english_{date_str}.md"
        with open(english_file, 'w', encoding='utf-8') as f:
            f.write(english_content)
        print(f"   📄 英文版: {english_file}")
        
        # 2. 生成中文版
        chinese_content = self._generate_chinese_report(news_data)
        chinese_file = output_dir / f"tech_news_chinese_{date_str}.md"
        with open(chinese_file, 'w', encoding='utf-8') as f:
            f.write(chinese_content)
        print(f"   🇨🇳 中文版: {chinese_file}")
        
        # 3. 生成SRT字幕
        srt_content = self.srt_generator.generate_srt_from_news(news_data)
        srt_file = output_dir / f"tech_news_subtitles_{date_str}.srt"
        with open(srt_file, 'w', encoding='utf-8') as f:
            f.write(srt_content)
        print(f"   🎬 SRT字幕: {srt_file}")
        
        # 生成索引文件
        self._generate_index_file(date_str, len(news_data))
        
        print("✅ 所有报告生成完成")
    
    def _generate_english_report(self, news_data: List[Dict]) -> str:
        """生成英文版报告"""
        date_str = datetime.now().strftime('%Y-%m-%d')
        
        content = f"""# 🌍 Daily Tech News - {date_str}

## 📊 Today's Overview
- **Total Articles**: {len(news_data)}
- **Sources**: {len(set(item['source'] for item in news_data))} tech media outlets
- **Last Updated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 🔥 Top Stories

"""
        
        # 添加前20条重点新闻
        for i, item in enumerate(news_data[:20], 1):
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
        categories = {}
        for item in news_data[20:]:
            category = item.get('category', 'Other')
            if category not in categories:
                categories[category] = []
            categories[category].append(item)
        
        for category, items in categories.items():
            if items:
                content += f"\n## 💻 {category}\n\n"
                for item in items[:15]:  # 每个分类增加到15条
                    title = item.get('title', 'No Title')
                    url = item.get('url', '#')
                    source = item.get('source', 'Unknown')
                    
                    content += f"- **[{title}]({url})** - *{source}*\n"
        
        content += f"""
---
*Generated on {date_str} by Tech News Aggregator v3.0*
*Total sources processed: {len(news_data)} articles*
"""
        
        return content
    
    def _generate_chinese_report(self, news_data: List[Dict]) -> str:
        """生成中文版报告"""
        date_str = datetime.now().strftime('%Y-%m-%d')
        
        content = f"""# 🌟 每日科技简报 - {date_str}

## 📊 今日概览
- **资讯总数**: {len(news_data)} 条
- **信息源**: {len(set(item['source'] for item in news_data))} 个科技媒体
- **更新时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 🔥 重点新闻

"""
        
        # 添加前20条重点新闻（翻译版本）
        for i, item in enumerate(news_data[:20], 1):
            title = item.get('title', 'No Title')
            summary = item.get('summary', 'No summary available')
            source = item.get('source', 'Unknown')
            time_str = item.get('time', 'Unknown')
            url = item.get('url', '#')
            
            # 翻译标题和摘要
            if self.translation_enabled:
                try:
                    title_cn = self.translator.translate_content(title)
                    summary_cn = self.translator.translate_content(summary) if summary else '暂无摘要'
                except:
                    title_cn = title
                    summary_cn = summary
            else:
                title_cn = title
                summary_cn = summary
            
            content += f"""### {i}. {title_cn}
**来源**: {source} | **时间**: {time_str}
**摘要**: {summary_cn}
**原文**: [查看详情]({url})

"""
        
        # 按分类添加其他新闻
        categories = {}
        for item in news_data[20:]:
            category = item.get('category', 'Other')
            if category not in categories:
                categories[category] = []
            categories[category].append(item)
        
        # 分类名称映射
        category_map = {
            'Tech News': '科技新闻',
            'Tech Research': '技术研究',
            'Open Source': '开源项目',
            'Tech Community': '技术社区',
            'Startups': '创业资讯',
            'Enterprise Tech': '企业技术',
            'Mobile': '移动应用',
            'Security': '网络安全',
            'Web Dev': 'Web开发',
            'Cloud': '云计算',
            'Data Science': '数据科学',
            'Gaming Tech': '游戏技术',
            'AI/ML': 'AI/机器学习',
            'Silicon Valley': '硅谷动态'
        }
        
        for category, items in categories.items():
            if items:
                category_cn = category_map.get(category, category)
                content += f"\n## 💻 {category_cn}\n\n"
                for item in items[:15]:  # 每个分类增加到15条
                    title = item.get('title', 'No Title')
                    url = item.get('url', '#')
                    source = item.get('source', 'Unknown')
                    
                    # 翻译标题
                    if self.translation_enabled:
                        try:
                            title_cn = self.translator.translate_content(title)
                        except:
                            title_cn = title
                    else:
                        title_cn = title
                    
                    content += f"- **[{title_cn}]({url})** - *{source}*\n"
        
        content += f"""
---
*由科技资讯聚合系统 v3.0 于 {date_str} 自动生成*
*共处理 {len(news_data)} 条资讯*
"""
        
        return content
    
    def _generate_index_file(self, date_str: str, total_count: int):
        """生成索引文件"""
        index_content = f"""# 📰 科技资讯聚合系统

## 🔗 今日报告 - {date_str}

- [📄 英文版](output/tech_news_english_{date_str}.md)
- [🇨🇳 中文版](output/tech_news_chinese_{date_str}.md)
- [🎬 SRT字幕](output/tech_news_subtitles_{date_str}.srt)

## 📊 统计信息

- **生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **资讯总数**: {total_count} 条
- **信息源**: {len(self.sources)} 个优质科技媒体

## 🎬 SRT字幕使用说明

SRT字幕文件可直接用于视频编辑软件：
- Adobe Premiere Pro
- Final Cut Pro
- DaVinci Resolve
- Camtasia
- OBS Studio

---
*由科技资讯聚合系统 v3.0 自动生成*
"""
        
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(index_content)
        print(f"   📋 索引文件: README.md")
    
    def _generate_error_report(self, error_message: str):
        """生成错误报告"""
        try:
            error_report = f"""# 🚨 系统错误报告

**时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**错误**: {error_message}

## 建议检查项目
1. 网络连接是否正常
2. RSS源是否可访问
3. 环境变量是否正确配置

---
*由科技资讯聚合系统 v3.0 生成*
"""
            
            with open('error_report.md', 'w', encoding='utf-8') as f:
                f.write(error_report)
            print("📝 已生成错误报告: error_report.md")
        except:
            pass

def main():
    """主函数"""
    print("🌟 科技资讯聚合系统 v3.0")
    print("🎯 生成三个版本：中文版、英文版、SRT字幕")
    print("=" * 50)
    
    try:
        aggregator = TechNewsAggregator()
        aggregator.run_daily_collection()
        
        print("\n🎉 系统运行完成！")
        print("💡 查看生成的文件:")
        print("   - output/ 目录下的三个文件")
        print("   - README.md 索引文件")
        
    except KeyboardInterrupt:
        print("\n⚠️ 用户中断程序")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ 程序异常退出: {e}")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main() 