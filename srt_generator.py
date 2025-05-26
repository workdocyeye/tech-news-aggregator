#!/usr/bin/env python3
"""
SRT字幕生成器
将科技资讯转换为SRT字幕格式，方便播客音频制作
"""

import re
from datetime import datetime, timedelta
from typing import List, Dict

class SRTGenerator:
    """SRT字幕生成器"""
    
    def __init__(self):
        # 字幕配置
        self.words_per_minute = 150  # 每分钟字数
        self.chars_per_subtitle = 80  # 每条字幕最大字符数
        self.min_duration = 2.0  # 最短显示时间（秒）
        self.max_duration = 6.0  # 最长显示时间（秒）
        
    def generate_srt_from_news(self, news_data: List[Dict]) -> str:
        """从新闻数据生成SRT字幕"""
        
        if not news_data:
            return self._generate_empty_srt()
        
        # 处理新闻数据
        processed_data = self._process_news_data(news_data)
        
        # 生成播客脚本内容
        script_content = self._generate_podcast_script(processed_data)
        
        # 转换为SRT格式
        srt_content = self._convert_to_srt(script_content)
        
        return srt_content
    
    def _process_news_data(self, news_data: List[Dict]) -> Dict:
        """处理新闻数据"""
        # 按时间排序
        sorted_news = sorted(news_data, key=lambda x: x.get('time', ''), reverse=True)
        
        # 选择前10条作为主要内容
        top_stories = sorted_news[:10]
        
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
        
        if any(keyword in text for keyword in ['ai', 'artificial intelligence', 'machine learning', 'gpt', 'llm']):
            return 'AI/ML'
        elif any(keyword in text for keyword in ['github', 'open source', 'repository']):
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
            return 'Tech News'
    
    def _generate_podcast_script(self, data: Dict) -> List[str]:
        """生成播客脚本内容"""
        stats = data['stats']
        top_stories = data['top_stories']
        
        script_segments = []
        
        # 开场白
        opening = f"大家好，欢迎收听今日科技播客。今天是{stats['date']}，我为大家带来{stats['total']}条最新科技资讯。"
        script_segments.append(opening)
        
        # 主要新闻介绍
        if top_stories:
            script_segments.append("首先，让我们来看看今天的重点新闻。")
            
            for i, story in enumerate(top_stories[:5], 1):
                title = story.get('title', 'No Title')
                summary = story.get('summary', 'No summary')
                source = story.get('source', 'Unknown')
                
                # 清理和简化内容
                title = self._clean_text(title)
                summary = self._clean_text(summary)
                
                segment = f"第{i}条新闻：{title}。"
                
                # 添加摘要（限制长度）
                if summary and len(summary) > 20:
                    summary_short = summary[:150] + "..." if len(summary) > 150 else summary
                    segment += f"据{source}报道，{summary_short}"
                
                script_segments.append(segment)
        
        # 快讯部分
        if len(top_stories) > 5:
            script_segments.append("接下来是今日科技快讯。")
            
            for i, story in enumerate(top_stories[5:8], 1):
                title = self._clean_text(story.get('title', 'No Title'))
                segment = f"快讯{i}：{title}。"
                script_segments.append(segment)
        
        # 结束语
        closing = f"以上就是今天的科技资讯播报。感谢大家的收听，我们明天同一时间再见。"
        script_segments.append(closing)
        
        return script_segments
    
    def _clean_text(self, text: str) -> str:
        """清理文本，移除特殊字符和HTML标签"""
        if not text:
            return ""
        
        # 移除HTML标签
        text = re.sub(r'<[^>]+>', '', text)
        
        # 移除多余的空白字符
        text = re.sub(r'\s+', ' ', text)
        
        # 移除特殊字符，保留中文、英文、数字和基本标点
        text = re.sub(r'[^\w\s\u4e00-\u9fff.,!?;:()[\]{}"\'-]', '', text)
        
        return text.strip()
    
    def _convert_to_srt(self, script_segments: List[str]) -> str:
        """将脚本转换为SRT格式"""
        srt_lines = []
        current_time = timedelta(seconds=0)
        subtitle_index = 1
        
        for segment in script_segments:
            if not segment.strip():
                continue
            
            # 分割长句子
            subtitles = self._split_text_for_subtitles(segment)
            
            for subtitle_text in subtitles:
                # 计算显示时间
                char_count = len(subtitle_text)
                duration = max(
                    self.min_duration,
                    min(self.max_duration, char_count / (self.words_per_minute / 60 * 3))
                )
                
                start_time = current_time
                end_time = current_time + timedelta(seconds=duration)
                
                # 格式化时间
                start_time_str = self._format_srt_time(start_time)
                end_time_str = self._format_srt_time(end_time)
                
                # 添加SRT条目
                srt_lines.append(str(subtitle_index))
                srt_lines.append(f"{start_time_str} --> {end_time_str}")
                srt_lines.append(subtitle_text)
                srt_lines.append("")  # 空行分隔
                
                subtitle_index += 1
                current_time = end_time + timedelta(seconds=0.5)  # 间隔0.5秒
        
        return "\n".join(srt_lines)
    
    def _split_text_for_subtitles(self, text: str) -> List[str]:
        """将长文本分割为适合字幕的短句"""
        if len(text) <= self.chars_per_subtitle:
            return [text]
        
        subtitles = []
        sentences = re.split(r'[。！？.!?]', text)
        
        current_subtitle = ""
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue
            
            # 添加标点符号
            if sentence and not sentence.endswith(('。', '！', '？', '.', '!', '?')):
                if any('\u4e00' <= char <= '\u9fff' for char in sentence):
                    sentence += "。"
                else:
                    sentence += "."
            
            # 检查是否超过长度限制
            if len(current_subtitle + sentence) <= self.chars_per_subtitle:
                current_subtitle += sentence
            else:
                if current_subtitle:
                    subtitles.append(current_subtitle)
                current_subtitle = sentence
        
        if current_subtitle:
            subtitles.append(current_subtitle)
        
        # 处理仍然过长的字幕
        final_subtitles = []
        for subtitle in subtitles:
            if len(subtitle) <= self.chars_per_subtitle:
                final_subtitles.append(subtitle)
            else:
                # 强制分割
                words = subtitle.split()
                current_line = ""
                for word in words:
                    if len(current_line + " " + word) <= self.chars_per_subtitle:
                        current_line += " " + word if current_line else word
                    else:
                        if current_line:
                            final_subtitles.append(current_line)
                        current_line = word
                if current_line:
                    final_subtitles.append(current_line)
        
        return final_subtitles
    
    def _format_srt_time(self, td: timedelta) -> str:
        """格式化SRT时间格式 (HH:MM:SS,mmm)"""
        total_seconds = int(td.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        milliseconds = int((td.total_seconds() - total_seconds) * 1000)
        
        return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"
    
    def _generate_empty_srt(self) -> str:
        """生成空内容的SRT"""
        return """1
00:00:00,000 --> 00:00:05,000
大家好，欢迎收听今日科技播客。

2
00:00:05,500 --> 00:00:10,000
今天暂时没有新的科技资讯更新。

3
00:00:10,500 --> 00:00:15,000
我们会继续为大家关注科技动态。

4
00:00:15,500 --> 00:00:20,000
感谢收听，我们明天再见。

"""

# 测试代码
if __name__ == "__main__":
    # 模拟新闻数据
    sample_news = [
        {
            'title': 'OpenAI发布GPT-4 Turbo，性能大幅提升',
            'summary': 'OpenAI今天宣布推出GPT-4 Turbo，具有更长的上下文窗口和50%的成本降低。',
            'url': 'https://example.com/news1',
            'source': 'TechCrunch',
            'time': '2024-01-15 09:30'
        },
        {
            'title': 'Google开源新AI框架',
            'summary': 'Google发布了Gemini Framework，一个开源的AI开发框架。',
            'url': 'https://example.com/news2',
            'source': 'Google AI Blog',
            'time': '2024-01-15 08:45'
        }
    ]
    
    generator = SRTGenerator()
    srt_content = generator.generate_srt_from_news(sample_news)
    
    print("=== 生成的SRT字幕 ===")
    print(srt_content) 