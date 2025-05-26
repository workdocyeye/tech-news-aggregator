#!/usr/bin/env python3
"""
科技资讯聚合系统 v2.1 - GitHub Actions优化版
专为GitHub Actions环境优化，提供更好的稳定性和错误处理
支持60+信息源，生成SRT字幕文件
"""

import os
import sys
import time
import json
import feedparser
import requests
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional
import traceback
import re

# 导入自定义模块
from premium_sources import GitHubOptimizedSources
from intelligent_classifier import IntelligentClassifier
from report_generator import ReportGenerator
from notification_system import NotificationSystem

class GitHubOptimizedAggregator:
    """GitHub Actions优化版科技资讯聚合器 v2.1"""
    
    def __init__(self):
        print("🚀 初始化GitHub Actions优化版聚合器 v2.1...")
        
        # 初始化组件
        self.sources_manager = GitHubOptimizedSources()
        self.classifier = IntelligentClassifier()
        self.report_generator = ReportGenerator()
        self.notification_system = NotificationSystem()
        
        # 配置参数
        self.max_retries = 3
        self.retry_delay = 2  # 秒
        self.timeout = 30  # 秒
        self.min_articles_threshold = 10  # 最少文章数量（提高阈值）
        
        # 打印信息源统计
        self.sources_manager.print_sources_summary()
        
        print("✅ 初始化完成")
    
    def run_daily_collection(self):
        """运行每日收集任务 - GitHub Actions优化版 v2.1"""
        print("\n🚀 开始每日科技资讯收集 (v2.1)")
        print("📊 信息源已扩展至60+个优质科技媒体")
        print("🎬 新增SRT字幕文件生成功能")
        print("🎯 专注十大核心领域：AI、GitHub、创业、硅谷、科技、开源、企业、移动、安全、Web开发")
        print("🛡️ 增强错误处理和重试机制")
        print("=" * 80)
        
        try:
            # 1. 收集RSS数据（带重试机制）
            print("📡 正在收集RSS数据...")
            news_data = self._collect_rss_data_with_retry()
            print(f"✅ 收集完成，共获取 {len(news_data)} 条资讯")
            
            # 检查最少文章数量
            if len(news_data) < self.min_articles_threshold:
                print(f"⚠️ 文章数量过少 ({len(news_data)} < {self.min_articles_threshold})")
                print("🔄 尝试使用备用策略...")
                news_data = self._fallback_collection_strategy()
            
            # 2. 智能分类和处理
            print("🧠 正在进行智能分类和处理...")
            classified_data = self._classify_and_process(news_data)
            print(f"✅ 分类完成，保留 {len(classified_data)} 条高质量资讯")
            
            # 3. 生成分类统计
            self._print_classification_stats(classified_data)
            
            # 4. 生成三个版本的报告（包含SRT字幕）
            print("📝 正在生成多版本报告...")
            versions = self.report_generator.generate_all_versions(classified_data)
            print("✅ 报告生成完成")
            
            # 打印版本信息
            self._print_versions_info(versions)
            
            # 5. 发送邮件通知（带错误处理）
            print("📧 正在发送邮件通知...")
            try:
                success = self.notification_system.send_daily_reports(versions)
                if success:
                    print("✅ 邮件发送成功")
                else:
                    print("⚠️ 邮件发送失败，但系统继续运行")
            except Exception as e:
                print(f"⚠️ 邮件发送异常: {e}")
                print("📧 邮件功能可能需要配置环境变量")
            
            # 6. 保存到GitHub
            self._save_for_github(versions, classified_data)
            
            print("🎉 每日收集任务完成！")
            print("💡 基于GitHub Actions优化的高质量信息源")
            print("🎬 SRT字幕文件已生成，可直接用于播客制作")
            
        except Exception as e:
            print(f"❌ 任务执行失败: {e}")
            traceback.print_exc()
            
            # 尝试生成错误报告
            self._generate_error_report(str(e))
            sys.exit(1)
    
    def _collect_rss_data_with_retry(self) -> List[Dict]:
        """带重试机制的RSS数据收集"""
        all_news = []
        sources = self.sources_manager.get_all_sources()
        
        # 按可靠性排序，优先处理高可靠性源
        sources.sort(key=lambda x: (
            x.get('reliability') == 'excellent',
            x.get('priority') == 'high'
        ), reverse=True)
        
        successful_sources = 0
        failed_sources = []
        
        for source in sources:
            print(f"📡 处理: {source['name']}...", end=' ')
            
            success = False
            for attempt in range(self.max_retries):
                try:
                    # 设置超时和用户代理
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (compatible; TechNewsBot/2.1; +https://github.com/tech-news-bot)'
                    }
                    
                    # 使用requests获取RSS内容
                    response = requests.get(
                        source['url'], 
                        headers=headers, 
                        timeout=self.timeout
                    )
                    response.raise_for_status()
                    
                    # 解析RSS
                    feed = feedparser.parse(response.content)
                    
                    if not feed.entries:
                        print(f"❌ 无内容 (尝试 {attempt + 1}/{self.max_retries})")
                        if attempt < self.max_retries - 1:
                            time.sleep(self.retry_delay)
                        continue
                    
                    # 处理RSS条目
                    recent_count = 0
                    for entry in feed.entries[:20]:  # 限制处理数量
                        try:
                            news_item = self._parse_rss_entry(entry, source)
                            if news_item and self._is_recent_news(news_item.get('time')):
                                all_news.append(news_item)
                                recent_count += 1
                        except Exception as parse_error:
                            print(f"解析条目错误: {parse_error}")
                            continue
                    
                    print(f"✅ {recent_count}条")
                    successful_sources += 1
                    success = True
                    break
                    
                except requests.exceptions.Timeout:
                    print(f"⏰ 超时 (尝试 {attempt + 1}/{self.max_retries})")
                except requests.exceptions.RequestException as e:
                    print(f"🌐 网络错误 (尝试 {attempt + 1}/{self.max_retries}): {str(e)[:30]}...")
                except Exception as e:
                    print(f"❌ 错误 (尝试 {attempt + 1}/{self.max_retries}): {str(e)[:30]}...")
                
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay * (attempt + 1))  # 递增延迟
            
            if not success:
                failed_sources.append(source['name'])
        
        print(f"\n📊 收集统计:")
        print(f"   ✅ 成功源: {successful_sources}/{len(sources)}")
        print(f"   ❌ 失败源: {len(failed_sources)}")
        if failed_sources:
            print(f"   失败列表: {', '.join(failed_sources[:5])}{'...' if len(failed_sources) > 5 else ''}")
        
        return all_news
    
    def _fallback_collection_strategy(self) -> List[Dict]:
        """备用收集策略"""
        print("🔄 执行备用收集策略...")
        
        # 1. 扩展时间窗口到48小时
        print("   📅 扩展时间窗口到48小时")
        all_news = []
        
        # 只使用最可靠的源
        reliable_sources = self.sources_manager.get_excellent_reliability_sources()
        
        for source in reliable_sources[:10]:  # 限制数量
            try:
                feed = feedparser.parse(source['url'])
                for entry in feed.entries[:30]:  # 增加处理数量
                    try:
                        news_item = self._parse_rss_entry(entry, source)
                        if news_item:
                            # 扩展时间窗口
                            cutoff_time = datetime.now() - timedelta(hours=48)
                            if news_item.get('time') and news_item['time'] > cutoff_time:
                                all_news.append(news_item)
                    except:
                        continue
            except:
                continue
        
        print(f"   📰 备用策略收集到 {len(all_news)} 条资讯")
        return all_news
    
    def _parse_rss_entry(self, entry, source: Dict) -> Optional[Dict]:
        """解析RSS条目"""
        try:
            # 获取基本信息
            title = entry.get('title', '').strip()
            if not title:
                return None
            
            summary = entry.get('summary', entry.get('description', '')).strip()
            link = entry.get('link', '')
            
            # 解析时间
            pub_time = self._parse_time(entry.get('published', ''))
            
            return {
                'title': title,
                'summary': summary[:500],  # 限制摘要长度
                'url': link,
                'source': source['name'],
                'category': source['category'],
                'time': pub_time,
                'priority': source.get('priority', 'medium'),
                'reliability': source.get('reliability', 'good')
            }
        except Exception as e:
            print(f"解析RSS条目错误: {e}")
            return None
    
    def _parse_time(self, time_str: str) -> datetime:
        """解析时间字符串"""
        try:
            import dateutil.parser
            parsed_time = dateutil.parser.parse(time_str)
            if parsed_time.tzinfo is not None:
                parsed_time = parsed_time.replace(tzinfo=None)
            return parsed_time
        except:
            return datetime.now()
    
    def _is_recent_news(self, news_time) -> bool:
        """检查是否为最近的新闻"""
        if not isinstance(news_time, datetime):
            return True
        
        cutoff_time = datetime.now() - timedelta(hours=24)
        return news_time > cutoff_time
    
    def _classify_and_process(self, news_data: List[Dict]) -> List[Dict]:
        """分类和处理新闻数据"""
        if not news_data:
            return []
        
        # 去重
        unique_news = self._remove_duplicates(news_data)
        print(f"   🔄 去重后: {len(unique_news)} 条")
        
        # 智能分类
        classified_news = []
        for news in unique_news:
            try:
                classified = self.classifier.classify_news(news)
                classified_news.append(classified)
            except Exception as e:
                print(f"分类错误: {e}")
                classified_news.append(news)  # 保留原始数据
        
        # 按综合评分排序
        classified_news.sort(
            key=lambda x: x.get('综合评分', 0), 
            reverse=True
        )
        
        return classified_news
    
    def _remove_duplicates(self, news_data: List[Dict]) -> List[Dict]:
        """去重处理"""
        seen_titles = set()
        unique_news = []
        
        for news in news_data:
            title_key = news.get('title', '').lower().strip()
            if title_key and title_key not in seen_titles:
                seen_titles.add(title_key)
                unique_news.append(news)
        
        return unique_news
    
    def _print_classification_stats(self, classified_data: List[Dict]):
        """打印分类统计 - 优化版"""
        if not classified_data:
            print("⚠️ 没有分类数据")
            return
        
        # 统计分类
        category_stats = {}
        priority_stats = {}
        reliability_stats = {}
        
        for news in classified_data:
            # 分类统计
            main_cat = news.get('主分类', news.get('category', '未分类'))
            category_stats[main_cat] = category_stats.get(main_cat, 0) + 1
            
            # 优先级统计
            priority = news.get('priority', 'medium')
            priority_stats[priority] = priority_stats.get(priority, 0) + 1
            
            # 可靠性统计
            reliability = news.get('reliability', 'good')
            reliability_stats[reliability] = reliability_stats.get(reliability, 0) + 1
        
        print("\n📊 分类统计:")
        
        # 分类分布
        print("   📂 分类分布:")
        categories = self.sources_manager.get_categories()
        for category, count in sorted(category_stats.items(), key=lambda x: x[1], reverse=True):
            category_name = categories.get(category, category)
            percentage = count / len(classified_data) * 100
            print(f"      {category_name}: {count} 条 ({percentage:.1f}%)")
        
        # 优先级分布
        print("   🔥 优先级分布:")
        for priority, count in sorted(priority_stats.items(), key=lambda x: x[1], reverse=True):
            percentage = count / len(classified_data) * 100
            icon = "🔥" if priority == "high" else "📌" if priority == "medium" else "📝"
            print(f"      {icon} {priority}: {count} 条 ({percentage:.1f}%)")
    
    def _print_versions_info(self, versions: Dict[str, str]):
        """打印版本信息"""
        print("📋 生成版本信息:")
        for version_name, content in versions.items():
            char_count = len(content)
            line_count = content.count('\n')
            
            if version_name == 'english':
                print(f"   📄 英文版: {char_count:,} 字符, {line_count} 行")
            elif version_name == 'bilingual':
                print(f"   🌏 中英混合版: {char_count:,} 字符, {line_count} 行")
            elif version_name == 'srt':
                # 统计SRT字幕条数
                srt_count = content.count('\n\n') if content else 0
                print(f"   🎬 SRT字幕版: {srt_count} 条字幕, {char_count:,} 字符")
    
    def _save_for_github(self, versions: Dict[str, str], classified_data: List[Dict]):
        """保存文件供GitHub Actions使用 - 优化版"""
        print("💾 正在保存文件...")
        
        # 创建输出目录
        output_dir = Path('output')
        output_dir.mkdir(exist_ok=True)
        
        date_str = datetime.now().strftime('%Y-%m-%d')
        
        try:
            # 保存英文版
            if 'english' in versions:
                english_file = output_dir / f"daily_news_english_{date_str}.md"
                with open(english_file, 'w', encoding='utf-8') as f:
                    f.write(versions['english'])
                print(f"   📄 英文版: {english_file}")
            
            # 保存中英混合版
            if 'bilingual' in versions:
                bilingual_file = output_dir / f"daily_news_bilingual_{date_str}.md"
                with open(bilingual_file, 'w', encoding='utf-8') as f:
                    f.write(versions['bilingual'])
                print(f"   🌏 中英混合版: {bilingual_file}")
            
            # 保存SRT字幕版
            if 'srt' in versions:
                srt_file = output_dir / f"podcast_subtitles_{date_str}.srt"
                with open(srt_file, 'w', encoding='utf-8') as f:
                    f.write(versions['srt'])
                print(f"   🎬 SRT字幕版: {srt_file}")
            
            # 保存最新报告（用于GitHub Pages）
            latest_file = Path("latest_report.md")
            with open(latest_file, 'w', encoding='utf-8') as f:
                f.write(f"""# 📰 最新科技简报 - {date_str}

## 🔗 今日报告

- [📄 英文原版](output/daily_news_english_{date_str}.md)
- [🌏 中英混合版](output/daily_news_bilingual_{date_str}.md)  
- [🎬 SRT字幕文件](output/podcast_subtitles_{date_str}.srt)

## 📊 统计信息

- **收集时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **资讯总数**: {len(classified_data)} 条
- **信息源**: 60+ 个优质科技媒体
- **覆盖领域**: AI、GitHub、创业、硅谷、科技、开源、企业、移动、安全、Web开发

## 🎬 SRT字幕使用说明

SRT字幕文件可直接导入以下视频编辑软件：
- Adobe Premiere Pro
- Final Cut Pro
- DaVinci Resolve
- Camtasia
- OBS Studio

使用方法：
1. 录制播客音频
2. 在视频编辑软件中导入音频和SRT文件
3. 软件会自动同步字幕时间轴
4. 根据需要调整字幕样式和位置

---
*由科技资讯聚合系统 v2.1 自动生成*
""")
            print(f"   📋 最新报告: {latest_file}")
            
            # 保存统计数据
            stats_file = output_dir / f"stats_{date_str}.json"
            stats_data = {
                'date': date_str,
                'total_articles': len(classified_data),
                'generation_time': datetime.now().isoformat(),
                'versions': {
                    'english_chars': len(versions.get('english', '')),
                    'bilingual_chars': len(versions.get('bilingual', '')),
                    'srt_subtitles': versions.get('srt', '').count('\n\n') if versions.get('srt') else 0
                },
                'categories': {}
            }
            
            # 统计分类
            for item in classified_data:
                category = item.get('category', item.get('主分类', 'unknown'))
                stats_data['categories'][category] = stats_data['categories'].get(category, 0) + 1
            
            with open(stats_file, 'w', encoding='utf-8') as f:
                json.dump(stats_data, f, ensure_ascii=False, indent=2)
            print(f"   📊 统计数据: {stats_file}")
            
        except Exception as e:
            print(f"   ❌ 保存文件失败: {e}")
        
        # 生成运行统计
        stats = {
            'date': date_str,
            'total_articles': len(classified_data),
            'categories': {},
            'sources': {},
            'timestamp': datetime.now().isoformat()
        }
        
        for news in classified_data:
            # 统计分类
            main_cat = news.get('主分类', '未分类')
            stats['categories'][main_cat] = stats['categories'].get(main_cat, 0) + 1
            
            # 统计来源
            source = news.get('source', '未知')
            stats['sources'][source] = stats['sources'].get(source, 0) + 1
        
        stats_file = output_dir / f"stats_{date_str}.json"
        with open(stats_file, 'w', encoding='utf-8') as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
        print(f"   💾 已保存: {stats_file}")
    
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
4. GitHub Actions权限是否充足

## 技术支持
如需帮助，请在GitHub仓库提交Issue。
"""
            
            with open('error_report.md', 'w', encoding='utf-8') as f:
                f.write(error_report)
            print("📝 已生成错误报告: error_report.md")
        except:
            pass

def main():
    """主函数"""
    print("🌟 科技资讯聚合系统 v2.1")
    print("🎯 专注十大核心领域，60+优质信息源")
    print("🎬 支持SRT字幕文件生成")
    print("=" * 60)
    
    try:
        aggregator = GitHubOptimizedAggregator()
        aggregator.run_daily_collection()
        
        print("\n🎉 系统运行完成！")
        print("💡 查看生成的文件:")
        print("   - output/ 目录下的报告文件")
        print("   - latest_report.md 最新报告索引")
        print("   - SRT字幕文件可直接用于播客制作")
        
    except KeyboardInterrupt:
        print("\n⚠️ 用户中断程序")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ 程序异常退出: {e}")
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main() 