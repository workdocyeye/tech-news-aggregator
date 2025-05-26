import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
from pathlib import Path

class NotificationSystem:
    """邮件通知系统 v2.1 - 支持SRT字幕文件"""
    
    def __init__(self):
        # 支持多种环境变量名称配置
        self.smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
        self.smtp_port = int(os.getenv('SMTP_PORT', '587'))
        
        # 发送者邮箱配置（支持多种变量名）
        self.sender_email = (
            os.getenv('GMAIL_USER') or 
            os.getenv('SENDER_EMAIL') or 
            os.getenv('EMAIL_USER')
        )
        
        # 发送者密码配置（支持多种变量名）
        self.sender_password = (
            os.getenv('GMAIL_APP_PASSWORD') or 
            os.getenv('SENDER_PASSWORD') or 
            os.getenv('EMAIL_PASSWORD') or
            os.getenv('GMAIL_PASSWORD')
        )
        
        # 接收者邮箱配置（支持多种变量名）
        self.receiver_email = (
            os.getenv('RECIPIENT_EMAIL') or 
            os.getenv('RECEIVER_EMAIL') or 
            os.getenv('TO_EMAIL')
        )
        
        # 打印配置状态
        self._print_config_status()
    
    def _print_config_status(self):
        """打印邮件配置状态"""
        print("📧 邮件配置状态:")
        print(f"   SMTP服务器: {self.smtp_server}:{self.smtp_port}")
        print(f"   发送者邮箱: {'✅ 已配置' if self.sender_email else '❌ 未配置'}")
        print(f"   发送者密码: {'✅ 已配置' if self.sender_password else '❌ 未配置'}")
        print(f"   接收者邮箱: {'✅ 已配置' if self.receiver_email else '❌ 未配置'}")
        
        if not all([self.sender_email, self.sender_password, self.receiver_email]):
            print("⚠️ 邮件配置不完整，需要设置以下环境变量:")
            if not self.sender_email:
                print("   - GMAIL_USER (发送者Gmail邮箱)")
            if not self.sender_password:
                print("   - GMAIL_APP_PASSWORD (Gmail应用专用密码)")
            if not self.receiver_email:
                print("   - RECIPIENT_EMAIL (接收者邮箱)")
    
    def send_daily_reports(self, versions: dict):
        """发送每日报告（三个版本：英文、中英混合、SRT字幕）"""
        
        if not all([self.sender_email, self.sender_password, self.receiver_email]):
            print("❌ 邮箱配置不完整，跳过邮件发送")
            print("💡 请在GitHub Secrets中配置以下变量:")
            print("   - GMAIL_USER: 发送者Gmail邮箱")
            print("   - GMAIL_APP_PASSWORD: Gmail应用专用密码")
            print("   - RECIPIENT_EMAIL: 接收者邮箱")
            return False
        
        try:
            print("📧 开始发送邮件...")
            
            # 保存版本到文件
            files = self._save_versions_to_files(versions)
            
            # 发送邮件
            self._send_email_with_attachments(files)
            
            print("✅ 邮件发送成功！")
            return True
            
        except Exception as e:
            print(f"❌ 邮件发送失败: {e}")
            print("💡 请检查:")
            print("   1. Gmail邮箱和应用专用密码是否正确")
            print("   2. 是否开启了Gmail的两步验证")
            print("   3. 是否生成了应用专用密码")
            print("   4. 网络连接是否正常")
            return False
    
    def _save_versions_to_files(self, versions: dict) -> dict:
        """保存版本到文件"""
        date_str = datetime.now().strftime('%Y-%m-%d')
        files = {}
        
        # 保存英文版
        if 'english' in versions:
            english_file = f"daily_news_english_{date_str}.md"
            with open(english_file, 'w', encoding='utf-8') as f:
                f.write(versions['english'])
            files['english'] = english_file
            print(f"📄 英文版已保存: {english_file}")
        
        # 保存中英混合版
        if 'bilingual' in versions:
            bilingual_file = f"daily_news_bilingual_{date_str}.md"
            with open(bilingual_file, 'w', encoding='utf-8') as f:
                f.write(versions['bilingual'])
            files['bilingual'] = bilingual_file
            print(f"🌏 中英混合版已保存: {bilingual_file}")
        
        # 保存SRT字幕版（替代播客版）
        if 'srt' in versions:
            srt_file = f"podcast_subtitles_{date_str}.srt"
            with open(srt_file, 'w', encoding='utf-8') as f:
                f.write(versions['srt'])
            files['srt'] = srt_file
            print(f"🎬 SRT字幕文件已保存: {srt_file}")
        
        # 兼容旧版本的podcast字段
        elif 'podcast' in versions:
            srt_file = f"podcast_subtitles_{date_str}.srt"
            with open(srt_file, 'w', encoding='utf-8') as f:
                f.write(versions['podcast'])
            files['srt'] = srt_file
            print(f"🎬 SRT字幕文件已保存: {srt_file}")
        
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

3. 🎬 **SRT字幕文件** (podcast_subtitles_*.srt)
   - 专为播客音频制作的字幕文件
   - 标准SRT格式，可直接导入视频编辑软件
   - 包含时间轴和播客脚本内容
   - 支持Premiere、Final Cut Pro、DaVinci Resolve等

💡 使用建议：
- 播客制作：将SRT文件导入视频编辑软件作为字幕
- 音频录制：参考SRT文件中的脚本内容
- 深度学习：结合英文版和中英版阅读
- 快速浏览：查看中英版的概览部分

🎥 SRT文件使用方法：
1. 录制播客音频
2. 在视频编辑软件中导入音频和SRT文件
3. 软件会自动同步字幕时间轴
4. 可根据需要调整字幕样式和位置

🔄 系统将每日自动运行，为您持续提供高质量科技资讯！

---
🤖 科技资讯聚合系统 v2.1
📊 信息源已扩展至60+个优质科技媒体
🎯 专注AI、开源、创业、硅谷、科技等核心领域
        """
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # 添加附件
        attachment_count = 0
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
                attachment_count += 1
                print(f"📎 已添加附件: {os.path.basename(file_path)}")
        
        print(f"📧 准备发送邮件，共 {attachment_count} 个附件")
        
        # 发送邮件
        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.sender_email, self.sender_password)
        text = msg.as_string()
        server.sendmail(self.sender_email, self.receiver_email, text)
        server.quit()
        
        print(f"📧 邮件已发送至: {self.receiver_email}")

# 测试代码
if __name__ == "__main__":
    # 模拟版本数据
    test_versions = {
        'english': "# Daily Tech News\n\nTest content...",
        'bilingual': "# 每日科技简报\n\nTest content...",
        'srt': """1
00:00:00,000 --> 00:00:05,000
大家好，欢迎收听今日科技播客。

2
00:00:05,500 --> 00:00:10,000
今天为您带来最新科技资讯。
"""
    }
    
    notifier = NotificationSystem()
    notifier.send_daily_reports(test_versions) 