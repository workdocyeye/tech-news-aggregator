#!/usr/bin/env python3
"""
智能分类系统
基于关键词和内容分析进行多维度分类
"""

import re
from typing import Dict, List, Set, Tuple
from dataclasses import dataclass

@dataclass
class ClassificationResult:
    """分类结果"""
    primary_category: str
    secondary_categories: List[str]
    tech_stack: List[str]
    importance_score: float
    trending_score: float
    keywords: List[str]

class IntelligentClassifier:
    """智能分类器"""
    
    def __init__(self):
        self.category_keywords = self._load_category_keywords()
        self.tech_stack_keywords = self._load_tech_stack_keywords()
        self.importance_keywords = self._load_importance_keywords()
        self.trending_keywords = self._load_trending_keywords()
    
    def classify_article(self, title: str, content: str, source_category: str) -> ClassificationResult:
        """分类文章"""
        
        # 合并标题和内容进行分析
        full_text = f"{title} {content}".lower()
        
        # 提取关键词
        keywords = self._extract_keywords(full_text)
        
        # 主分类（基于信息源和内容）
        primary_category = self._determine_primary_category(full_text, source_category)
        
        # 次分类
        secondary_categories = self._determine_secondary_categories(full_text)
        
        # 技术栈识别
        tech_stack = self._identify_tech_stack(full_text)
        
        # 重要性评分
        importance_score = self._calculate_importance_score(full_text, keywords)
        
        # 趋势性评分
        trending_score = self._calculate_trending_score(full_text, keywords)
        
        return ClassificationResult(
            primary_category=primary_category,
            secondary_categories=secondary_categories,
            tech_stack=tech_stack,
            importance_score=importance_score,
            trending_score=trending_score,
            keywords=keywords
        )
    
    def _load_category_keywords(self) -> Dict[str, List[str]]:
        """加载分类关键词"""
        return {
            'ai_ml': [
                'artificial intelligence', 'machine learning', 'deep learning', 'neural network',
                'gpt', 'llm', 'transformer', 'chatgpt', 'claude', 'gemini', 'openai',
                'anthropic', 'deepmind', 'hugging face', 'pytorch', 'tensorflow',
                'computer vision', 'nlp', 'natural language processing', 'generative ai'
            ],
            'github_dev': [
                'github', 'git', 'repository', 'open source', 'pull request', 'commit',
                'copilot', 'actions', 'codespace', 'developer', 'programming', 'code',
                'software development', 'version control', 'collaboration'
            ],
            'startup_funding': [
                'startup', 'funding', 'investment', 'venture capital', 'vc', 'series a',
                'series b', 'ipo', 'acquisition', 'merger', 'valuation', 'unicorn',
                'y combinator', 'accelerator', 'incubator', 'entrepreneur'
            ],
            'product_launch': [
                'launch', 'release', 'announcement', 'new product', 'feature',
                'update', 'beta', 'preview', 'coming soon', 'available now'
            ],
            'tech_trends': [
                'trend', 'future', 'innovation', 'breakthrough', 'revolution',
                'disruption', 'emerging', 'next generation', 'cutting edge'
            ],
            'security': [
                'security', 'privacy', 'cybersecurity', 'hack', 'breach', 'vulnerability',
                'encryption', 'authentication', 'malware', 'phishing'
            ],
            'cloud_infra': [
                'cloud', 'aws', 'azure', 'gcp', 'kubernetes', 'docker', 'serverless',
                'microservices', 'infrastructure', 'devops', 'ci/cd'
            ]
        }
    
    def _load_tech_stack_keywords(self) -> Dict[str, List[str]]:
        """加载技术栈关键词"""
        return {
            'languages': [
                'python', 'javascript', 'typescript', 'java', 'go', 'rust', 'c++',
                'swift', 'kotlin', 'php', 'ruby', 'scala', 'r', 'julia'
            ],
            'frameworks': [
                'react', 'vue', 'angular', 'django', 'flask', 'fastapi', 'express',
                'spring', 'rails', 'laravel', 'nextjs', 'nuxt', 'svelte'
            ],
            'databases': [
                'postgresql', 'mysql', 'mongodb', 'redis', 'elasticsearch',
                'cassandra', 'dynamodb', 'sqlite', 'neo4j'
            ],
            'cloud_platforms': [
                'aws', 'azure', 'gcp', 'vercel', 'netlify', 'heroku', 'digitalocean'
            ],
            'ai_tools': [
                'pytorch', 'tensorflow', 'keras', 'scikit-learn', 'pandas',
                'numpy', 'jupyter', 'hugging face', 'langchain', 'llamaindex'
            ]
        }
    
    def _load_importance_keywords(self) -> List[str]:
        """加载重要性关键词"""
        return [
            'breakthrough', 'revolutionary', 'game-changing', 'major', 'significant',
            'important', 'critical', 'milestone', 'historic', 'unprecedented',
            'billion', 'million', 'record', 'largest', 'first', 'new'
        ]
    
    def _load_trending_keywords(self) -> List[str]:
        """加载趋势性关键词"""
        return [
            'trending', 'viral', 'popular', 'hot', 'rising', 'growing',
            'emerging', 'latest', 'new', 'fresh', 'recent', 'today',
            'this week', 'breaking', 'just announced', 'now available'
        ]
    
    def _extract_keywords(self, text: str) -> List[str]:
        """提取关键词"""
        # 简单的关键词提取（可以后续优化为更复杂的NLP方法）
        words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
        
        # 过滤常见停用词
        stop_words = {
            'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'can', 'had',
            'her', 'was', 'one', 'our', 'out', 'day', 'get', 'has', 'him', 'his',
            'how', 'its', 'may', 'new', 'now', 'old', 'see', 'two', 'who', 'boy',
            'did', 'man', 'men', 'put', 'say', 'she', 'too', 'use', 'way', 'will'
        }
        
        keywords = [word for word in words if word not in stop_words and len(word) > 3]
        
        # 返回频率最高的关键词
        from collections import Counter
        word_counts = Counter(keywords)
        return [word for word, count in word_counts.most_common(10)]
    
    def _determine_primary_category(self, text: str, source_category: str) -> str:
        """确定主分类"""
        
        # 基于信息源的初始分类
        category_mapping = {
            'github': 'github_dev',
            'ai': 'ai_ml',
            'startup': 'startup_funding',
            'silicon_valley': 'tech_trends',
            'tech': 'product_launch'
        }
        
        base_category = category_mapping.get(source_category, 'tech_trends')
        
        # 基于内容的分类调整
        max_score = 0
        best_category = base_category
        
        for category, keywords in self.category_keywords.items():
            score = sum(1 for keyword in keywords if keyword in text)
            if score > max_score:
                max_score = score
                best_category = category
        
        return best_category
    
    def _determine_secondary_categories(self, text: str) -> List[str]:
        """确定次分类"""
        secondary = []
        
        for category, keywords in self.category_keywords.items():
            score = sum(1 for keyword in keywords if keyword in text)
            if score >= 2:  # 至少匹配2个关键词
                secondary.append(category)
        
        return secondary[:3]  # 最多3个次分类
    
    def _identify_tech_stack(self, text: str) -> List[str]:
        """识别技术栈"""
        tech_stack = []
        
        for stack_type, technologies in self.tech_stack_keywords.items():
            for tech in technologies:
                if tech in text:
                    tech_stack.append(tech)
        
        return list(set(tech_stack))[:5]  # 去重，最多5个
    
    def _calculate_importance_score(self, text: str, keywords: List[str]) -> float:
        """计算重要性评分 (0-1)"""
        score = 0.0
        
        # 基于重要性关键词
        importance_matches = sum(1 for keyword in self.importance_keywords if keyword in text)
        score += importance_matches * 0.1
        
        # 基于数字（金额、用户数等）
        numbers = re.findall(r'\b\d+(?:\.\d+)?\s*(?:billion|million|thousand|k|m|b)\b', text.lower())
        if numbers:
            score += 0.2
        
        # 基于公司知名度
        famous_companies = [
            'google', 'microsoft', 'apple', 'amazon', 'meta', 'tesla', 'nvidia',
            'openai', 'anthropic', 'github', 'vercel', 'stripe'
        ]
        company_matches = sum(1 for company in famous_companies if company in text)
        score += company_matches * 0.1
        
        return min(score, 1.0)
    
    def _calculate_trending_score(self, text: str, keywords: List[str]) -> float:
        """计算趋势性评分 (0-1)"""
        score = 0.0
        
        # 基于趋势性关键词
        trending_matches = sum(1 for keyword in self.trending_keywords if keyword in text)
        score += trending_matches * 0.15
        
        # 基于时间相关词汇
        time_words = ['today', 'yesterday', 'this week', 'recently', 'just', 'now']
        time_matches = sum(1 for word in time_words if word in text)
        score += time_matches * 0.1
        
        # 基于社交媒体相关词汇
        social_words = ['viral', 'trending', 'popular', 'buzz', 'hype']
        social_matches = sum(1 for word in social_words if word in text)
        score += social_matches * 0.2
        
        return min(score, 1.0)
    
    def classify_news(self, news_item: Dict) -> Dict:
        """分类新闻条目（兼容接口）"""
        title = news_item.get('title', '')
        summary = news_item.get('summary', '')
        source_category = news_item.get('category', 'tech')
        
        # 使用现有的分类方法
        result = self.classify_article(title, summary, source_category)
        
        # 转换为兼容格式
        classified_news = news_item.copy()
        classified_news.update({
            '主分类': result.primary_category,
            '次分类': result.secondary_categories,
            '技术栈': result.tech_stack,
            '重要性评分': result.importance_score,
            '趋势性评分': result.trending_score,
            '关键词': result.keywords,
            '综合评分': (result.importance_score + result.trending_score) / 2
        })
        
        return classified_news

if __name__ == "__main__":
    # 测试分类器
    classifier = IntelligentClassifier()
    
    # 测试文章
    test_articles = [
        {
            'title': 'OpenAI Releases GPT-5 with Revolutionary Capabilities',
            'content': 'OpenAI today announced GPT-5, a breakthrough in artificial intelligence that demonstrates unprecedented reasoning capabilities. The new model shows significant improvements in coding, mathematics, and creative writing.',
            'source_category': 'ai'
        },
        {
            'title': 'GitHub Copilot Gets Major Update with AI Pair Programming',
            'content': 'GitHub has released a major update to Copilot, introducing new AI-powered features for developers. The update includes better code suggestions and integration with popular IDEs.',
            'source_category': 'github'
        },
        {
            'title': 'Startup Raises $100M Series B for Revolutionary Cloud Platform',
            'content': 'A promising startup has secured $100 million in Series B funding to develop their next-generation cloud infrastructure platform. The investment was led by Andreessen Horowitz.',
            'source_category': 'startup'
        }
    ]
    
    print("🧠 智能分类系统测试")
    print("=" * 50)
    
    for i, article in enumerate(test_articles, 1):
        print(f"\n📰 测试文章 {i}: {article['title']}")
        
        result = classifier.classify_article(
            article['title'],
            article['content'],
            article['source_category']
        )
        
        print(f"🎯 主分类: {result.primary_category}")
        print(f"📋 次分类: {', '.join(result.secondary_categories) if result.secondary_categories else '无'}")
        print(f"💻 技术栈: {', '.join(result.tech_stack) if result.tech_stack else '无'}")
        print(f"⭐ 重要性: {result.importance_score:.2f}")
        print(f"🔥 趋势性: {result.trending_score:.2f}")
        print(f"🔑 关键词: {', '.join(result.keywords[:5])}") 