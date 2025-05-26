# 📰 科技资讯聚合系统 v3.0 部署指南

## 🌟 项目简介

科技资讯聚合系统 v3.0 是一个基于GitHub Actions的自动化科技新闻收集和处理系统，专为播客制作和内容创作者设计。

### ✨ 核心特性

- **🔄 自动化收集**: 每日自动从50+个优质科技媒体收集最新资讯
- **📝 三版本输出**: 
  - 📄 英文原版报告
  - 🇨🇳 中文翻译版报告  
  - 🎬 SRT中文字幕文件（播客专用）
- **🎯 智能筛选**: 自动去重、时间过滤、质量筛选
- **🌍 多领域覆盖**: AI/ML、开源、创业、移动、安全、Web开发、云计算等
- **💰 完全免费**: 基于GitHub Actions免费额度运行

### 📊 信息源覆盖

- **主流科技媒体**: TechCrunch, The Verge, Wired, Engadget, Gizmodo
- **技术研究**: MIT Technology Review, IEEE Spectrum
- **AI/ML**: OpenAI Blog, Google AI Blog, VentureBeat AI
- **开源社区**: GitHub Blog, Stack Overflow, Dev.to, Hacker News
- **创业投资**: VentureBeat, Crunchbase News, Y Combinator
- **企业技术**: ZDNet, InfoWorld, ComputerWorld
- **移动应用**: Android Police, 9to5Mac, 9to5Google, MacRumors
- **网络安全**: Krebs on Security, The Hacker News, Security Week
- **Web开发**: CSS-Tricks, Smashing Magazine, A List Apart
- **云计算**: AWS News, Google Cloud, Microsoft Azure, Docker, Kubernetes
- **数据科学**: KDnuggets, Towards Data Science, Analytics Vidhya
- **游戏技术**: Gamasutra, Unity Blog

## 🚀 快速开始

### 1. Fork 仓库

点击右上角的 "Fork" 按钮，将仓库复制到您的GitHub账户。

### 2. 配置环境变量

在您的GitHub仓库中，进入 `Settings` > `Secrets and variables` > `Actions`，添加以下环境变量：

#### 必需配置（翻译功能）
```
DEEPSEEK_API_KEY=your_deepseek_api_key
```

#### 可选配置（邮件通知）
```
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password
RECEIVER_EMAIL=recipient@example.com
```

### 3. 启用GitHub Actions

1. 进入仓库的 `Actions` 标签页
2. 点击 "I understand my workflows, enable them"
3. 系统将每天UTC 0点自动运行

### 4. 手动触发测试

1. 进入 `Actions` 标签页
2. 选择 "Daily Tech News Aggregator v3.0"
3. 点击 "Run workflow" 进行测试

## 📋 输出文件说明

### 📄 英文版报告 (`tech_news_english_YYYY-MM-DD.md`)
- 原始英文新闻内容
- 按重要性排序的前15条重点新闻
- 按分类整理的其他新闻
- 包含原文链接和来源信息

### 🇨🇳 中文版报告 (`tech_news_chinese_YYYY-MM-DD.md`)
- 智能翻译的中文版本
- 保护技术术语不被翻译
- 保留原文链接便于查证
- 适合中文读者阅读

### 🎬 SRT字幕文件 (`tech_news_subtitles_YYYY-MM-DD.srt`)
- 播客专用的中文字幕格式
- 包含开场白、新闻播报、结束语
- 时间轴自动计算
- 可直接导入视频编辑软件

## 🔧 高级配置

### 自定义RSS源

编辑 `rss_sources.py` 文件，添加或修改RSS源：

```python
{
    'name': '媒体名称',
    'url': 'RSS链接',
    'category': '分类',
    'language': 'en'
}
```

### 调整输出数量

在 `main.py` 中修改：
```python
return unique_news[:30]  # 修改数字调整输出数量
```

### 自定义翻译设置

在 `smart_translator.py` 中调整翻译参数和保护词汇。

## 🎬 SRT字幕使用指南

### 支持的视频编辑软件
- Adobe Premiere Pro
- Final Cut Pro
- DaVinci Resolve
- Camtasia
- OBS Studio

### 使用步骤
1. 录制播客音频
2. 在视频编辑软件中导入音频文件
3. 导入对应日期的SRT字幕文件
4. 软件会自动同步字幕时间轴
5. 根据需要调整字幕样式和位置

### 字幕格式说明
- 每条字幕2-6秒显示时间
- 每行最多80个字符
- 自动计算播报节奏
- 包含完整的播客脚本结构

## 🔍 故障排除

### 常见问题

**Q: 翻译功能不工作？**
A: 检查DEEPSEEK_API_KEY是否正确配置，确保API密钥有效。

**Q: 收集到的新闻数量很少？**
A: 某些RSS源可能暂时不可用，系统会自动跳过并继续处理其他源。

**Q: GitHub Actions运行失败？**
A: 检查仓库权限设置，确保Actions有写入权限。

**Q: SRT字幕时间不准确？**
A: 可以在视频编辑软件中手动调整时间轴，或修改`srt_generator.py`中的时间参数。

### 日志查看

在GitHub Actions的运行日志中可以看到：
- 每个RSS源的收集状态
- 去重和过滤结果
- 文件生成情况
- 错误信息（如有）

## 📈 系统监控

### 运行统计
- 每次运行会生成统计信息
- 显示成功/失败的RSS源数量
- 记录处理的新闻总数
- 按分类统计新闻分布

### 性能优化
- 自动重试机制处理网络问题
- 智能去重避免重复内容
- 时间过滤确保新闻时效性
- 限制输出数量控制文件大小

## 🤝 贡献指南

欢迎提交Issue和Pull Request来改进项目：

1. 报告Bug或建议新功能
2. 添加新的RSS源
3. 改进翻译质量
4. 优化SRT字幕格式
5. 完善文档说明

## 📄 许可证

本项目采用MIT许可证，详见LICENSE文件。

---

**🌟 如果这个项目对您有帮助，请给个Star支持一下！** 