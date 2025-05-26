import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
from pathlib import Path

class NotificationSystem:
    """邮件通知系统"""
    
    def __init__(self):
        self.smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
        self.smtp_port = int(os.getenv('SMTP_PORT', '587'))
        self.sender_email = os.getenv('SENDER_EMAIL')
        self.sender_password = os.getenv('SENDER_PASSWORD')
        self.receiver_email = os.getenv('RECEIVER_EMAIL')
    
    def send_daily_reports(self, versions: dict):
        """发送每日报告（三个版本）"""
        
        if not all([self.sender_email, self.sender_password, self.receiver_email]):
            print("邮箱配置不完整，跳过邮件发送")
            return
        
        try:
            # 保存版本到文件
            files = self._save_versions_to_files(versions)
            
            # 发送邮件
            self._send_email_with_attachments(files)
            
            print("✅ 邮件发送成功！")
            
        except Exception as e:
            print(f"❌ 邮件发送失败: {e}")
    
    def _save_versions_to_files(self, versions: dict) -> dict:
        """保存版本到文件"""
        date_str = datetime.now().strftime('%Y-%m-%d')
        files = {}
        
        # 保存英文版
        english_file = f"daily_news_english_{date_str}.md"
        with open(english_file, 'w', encoding='utf-8') as f:
            f.write(versions['english'])
        files['english'] = english_file
        
        # 保存中英混合版
        bilingual_file = f"daily_news_bilingual_{date_str}.md"
        with open(bilingual_file, 'w', encoding='utf-8') as f:
            f.write(versions['bilingual'])
        files['bilingual'] = bilingual_file
        
        # 保存播客版
        podcast_file = f"podcast_script_{date_str}.md"
        with open(podcast_file, 'w', encoding='utf-8') as f:
            f.write(versions['podcast'])
        files['podcast'] = podcast_file
        
        return files
    
    def _send_email_with_attachments(self, files: dict):
        """发送带附件的邮件"""
        
        # 创建邮件
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = self.receiver_email
        msg['Subject'] = f"📰 每日科技简报 - {datetime.now().strftime('%Y-%m-%d')}"
        
        # 邮件正文
        body = f"""
🌟 每日科技简报已生成完成！

📅 生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📦 本次邮件包含三个版本：

1. 📄 **英文原版** (daily_news_english_*.md)
   - 完整的英文原始资讯
   - 保持信息原汁原味
   - 适合英文阅读和引用

2. 📄 **中英混合版** (daily_news_bilingual_*.md)  
   - 智能翻译版本
   - 技术术语保持英文
   - 适合日常阅读

3. 🎙️ **播客制作版** (podcast_script_*.md)
   - 专为播客优化的脚本格式
   - 包含讨论要点和时间建议
   - 可直接用于播客制作

💡 使用建议：
- 播客制作：使用播客版作为脚本参考
- 深度学习：结合英文版和中英版阅读
- 快速浏览：查看中英版的概览部分

🔄 系统将每日自动运行，为您持续提供高质量科技资讯！

---
🤖 科技资讯聚合系统
        """
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # 添加附件
        for version_name, file_path in files.items():
            if os.path.exists(file_path):
                with open(file_path, "rb") as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename= {os.path.basename(file_path)}'
                )
                msg.attach(part)
        
        # 发送邮件
        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.sender_email, self.sender_password)
        text = msg.as_string()
        server.sendmail(self.sender_email, self.receiver_email, text)
        server.quit()

# 测试代码
if __name__ == "__main__":
    # 模拟版本数据
    test_versions = {
        'english': "# Daily Tech News\n\nTest content...",
        'bilingual': "# 每日科技简报\n\nTest content...",
        'podcast': "# 播客脚本\n\nTest content..."
    }
    
    notifier = NotificationSystem()
    notifier.send_daily_reports(test_versions) 