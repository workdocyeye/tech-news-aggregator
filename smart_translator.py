import os
import re
import requests
import json
from typing import Dict, List

class SmartTranslator:
    """智能翻译器 - 保护技术术语"""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('DEEPSEEK_API_KEY')
        self.base_url = "https://api.deepseek.com/chat/completions"
        
        # 技术术语保护列表
        self.protected_terms = [
            # 编程语言和框架
            'React', 'Vue', 'Angular', 'TypeScript', 'JavaScript', 'Python',
            'Java', 'Go', 'Rust', 'Swift', 'Kotlin', 'Flutter', 'Django',
            'Flask', 'FastAPI', 'Express', 'Next.js', 'Nuxt.js',
            
            # AI和机器学习
            'OpenAI', 'GPT', 'ChatGPT', 'Claude', 'Gemini', 'LLM', 'AI',
            'Machine Learning', 'Deep Learning', 'Neural Network', 'Transformer',
            'PyTorch', 'TensorFlow', 'Hugging Face', 'LangChain',
            
            # 云服务和工具
            'AWS', 'Azure', 'Google Cloud', 'Docker', 'Kubernetes', 'GitHub',
            'GitLab', 'API', 'SDK', 'CLI', 'REST', 'GraphQL', 'WebSocket',
            
            # 公司和产品名称
            'Google', 'Microsoft', 'Apple', 'Meta', 'Tesla', 'SpaceX',
            'Anthropic', 'Stability AI', 'Midjourney', 'Figma', 'Notion',
            
            # 技术概念
            'DevOps', 'MLOps', 'CI/CD', 'SaaS', 'PaaS', 'IaaS', 'API Gateway',
            'Microservices', 'Serverless', 'Edge Computing', 'Blockchain',
            'Web3', 'DeFi', 'NFT', 'DAO'
        ]
    
    def translate_content(self, text: str) -> str:
        """翻译内容，保护技术术语"""
        if not self.api_key:
            return text  # 如果没有API密钥，返回原文
        
        try:
            # 保护技术术语
            protected_text = self._protect_terms(text)
            
            # 调用翻译API
            translated = self._call_translation_api(protected_text)
            
            # 恢复技术术语
            final_text = self._restore_terms(translated)
            
            return final_text
            
        except Exception as e:
            print(f"翻译失败: {e}")
            return text  # 翻译失败时返回原文
    
    def _protect_terms(self, text: str) -> str:
        """保护技术术语"""
        protected_text = text
        for i, term in enumerate(self.protected_terms):
            # 使用占位符替换术语
            placeholder = f"[TERM_{i}]"
            protected_text = re.sub(
                rf'\b{re.escape(term)}\b', 
                placeholder, 
                protected_text, 
                flags=re.IGNORECASE
            )
        return protected_text
    
    def _restore_terms(self, text: str) -> str:
        """恢复技术术语"""
        restored_text = text
        for i, term in enumerate(self.protected_terms):
            placeholder = f"[TERM_{i}]"
            restored_text = restored_text.replace(placeholder, term)
        return restored_text
    
    def _call_translation_api(self, text: str) -> str:
        """调用翻译API"""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "deepseek-chat",
            "messages": [
                {
                    "role": "system",
                    "content": "你是一个专业的技术翻译助手。请将英文技术文章翻译成中文，保持专业性和准确性。对于已经用占位符保护的技术术语，请保持占位符不变。"
                },
                {
                    "role": "user", 
                    "content": f"请翻译以下内容：\n\n{text}"
                }
            ],
            "temperature": 0.1
        }
        
        response = requests.post(self.base_url, headers=headers, json=data)
        response.raise_for_status()
        
        result = response.json()
        return result['choices'][0]['message']['content']

# 测试代码
if __name__ == "__main__":
    translator = SmartTranslator()
    test_text = "OpenAI releases new GPT-4 model with improved React integration"
    translated = translator.translate_content(test_text)
    print(f"原文: {test_text}")
    print(f"译文: {translated}") 