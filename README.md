# 🌟 科技资讯聚合系统 v2.0

> 专注五大核心领域的高质量科技资讯聚合系统，基于GitHub Actions自动化运行

## 🎯 核心理念

**专业化 · 智能化 · 自动化**

v2.0版本专注于最具价值的五大科技领域，通过智能分类和评分系统，为技术创业者、投资人、开发者和科技爱好者提供高质量的每日科技简报。

## 🚀 五大核心领域

### 🐙 GitHub生态
- **GitHub官方动态** - 产品更新、功能发布
- **开源项目趋势** - 热门项目、技术栈演进
- **开发者工具** - 效率提升、协作优化

### 🤖 AI前沿
- **大语言模型** - GPT、Claude、Gemini最新进展
- **AI应用落地** - 实际场景、商业化进程
- **研究突破** - 学术论文、技术创新

### 🚀 创业投资
- **融资动态** - 轮次、估值、投资机构
- **商业模式** - 创新思路、市场策略
- **创业指导** - YC经验、成功案例

### 🌉 硅谷动态
- **行业洞察** - 战略分析、趋势预测
- **技术社区** - Hacker News热门讨论
- **专家观点** - 知名投资人、技术领袖

### 💻 科技资讯
- **产品发布** - 新品上市、功能更新
- **技术趋势** - 前沿技术、标准制定
- **行业新闻** - 并购重组、政策影响

## ✨ 核心特性

### 🧠 智能分析引擎
- **多维度分类**: 主分类 + 次分类 + 技术栈识别
- **重要性评分**: 基于关键词、公司知名度、数据规模
- **趋势性评分**: 识别热门话题和新兴趋势
- **综合评分**: 信息源权威性 + 内容质量

### 📊 高质量信息源
- **24个精选源**: 覆盖五大核心领域
- **17个高优先级源**: 确保内容权威性
- **实时更新**: 24小时内最新资讯
- **智能去重**: 避免重复内容

### 📰 三版本输出
- **英文原版**: 保持原汁原味
- **中英混合版**: 智能翻译，保护技术术语
- **播客制作版**: 专为播客优化的脚本格式

### 🔄 全自动化
- **每日定时运行**: 北京时间8点自动执行
- **邮件自动推送**: 三版本报告直达邮箱
- **GitHub自动存储**: 历史记录完整保存
- **零维护成本**: 基于GitHub Actions免费运行

## 📊 信息源详情

### 🐙 GitHub生态 (3个源)
- **GitHub Blog** - 官方产品更新和技术分享
- **GitHub Changelog** - 功能更新和变化记录
- **GitHub Engineering** - 工程团队技术博客

### 🤖 AI前沿 (6个源)
- **OpenAI Blog** - GPT等前沿AI技术
- **Anthropic News** - Claude AI开发者动态
- **Google AI Blog** - 谷歌AI研究成果
- **DeepMind Blog** - 深度学习前沿研究
- **Hugging Face Blog** - 开源AI工具和模型
- **arXiv AI Research** - 学术研究论文

### 🚀 创业投资 (6个源)
- **Y Combinator Blog** - 创业指导和案例分享
- **Andreessen Horowitz** - a16z投资观点和趋势
- **Sequoia Capital** - 红杉资本投资洞察
- **First Round Review** - 创业经验和方法论
- **Product Hunt** - 新产品发现平台
- **TechCrunch Startups** - 创业公司新闻

### 🌉 硅谷动态 (4个源)
- **Hacker News** - 硅谷技术社区热门讨论
- **Stratechery** - Ben Thompson的科技战略分析
- **Benedict Evans** - 前a16z合伙人的科技观察
- **The Information** - 硅谷内幕新闻和深度报道

### 💻 科技资讯 (5个源)
- **The Verge** - 科技新闻和产品评测
- **Wired** - 科技文化和未来趋势
- **Ars Technica** - 深度技术分析
- **IEEE Spectrum** - 工程技术前沿
- **MIT Technology Review** - 权威技术评论

## 🚀 快速开始

### 1. Fork项目
点击右上角的 "Fork" 按钮，将项目复制到您的GitHub账号下。

### 2. 配置环境变量
在仓库设置的 "Secrets and variables" → "Actions" 中添加：

#### 邮件通知配置（必需）
```
SMTP_SERVER = smtp.gmail.com
SMTP_PORT = 587
SENDER_EMAIL = your_email@gmail.com
SENDER_PASSWORD = your_app_password
RECEIVER_EMAIL = your_receiver@gmail.com
```

#### 翻译功能配置（可选）
```
DEEPSEEK_API_KEY = your_deepseek_api_key
```

### 3. 启用GitHub Actions
1. 进入仓库的 "Actions" 标签
2. 点击 "I understand my workflows, go ahead and enable them"
3. 手动运行一次测试工作流

### 4. 验证运行
系统将每日北京时间8点自动运行，您会收到包含三个版本的邮件报告。

## 📧 Gmail配置指南

### 获取应用专用密码
1. 登录Gmail，进入 "管理您的Google账户"
2. 选择 "安全性" → 开启 "两步验证"
3. 在 "应用专用密码" 中生成新密码
4. 将生成的16位密码用作 `SENDER_PASSWORD`

## 🔧 自定义配置

### 修改信息源
编辑 `premium_sources.py` 文件，添加或修改RSS源：

```python
{
    'name': '新信息源',
    'url': 'https://example.com/feed.xml',
    'category': 'tech',
    'priority': 'high',
    'description': '信息源描述'
}
```

### 调整运行时间
修改 `.github/workflows/daily-tech-news.yml` 中的cron表达式：

```yaml
# 每天早上8点（北京时间）
- cron: '0 0 * * *'

# 每12小时运行一次
- cron: '0 */12 * * *'
```

### 自定义分类规则
编辑 `intelligent_classifier.py` 文件，调整分类关键词和评分规则。

## 📊 输出示例

### 📄 英文原版
```markdown
# 🌟 Daily Tech News - 2025-05-26

## 📊 Today's Overview
- **Total Articles**: 26
- **AI/ML**: 4 articles
- **GitHub/Dev**: 3 articles
- **Startup/Investment**: 3 articles

## 🔥 Top Stories
### 1. OpenAI Releases GPT-5 with Revolutionary Capabilities
**Source**: OpenAI Blog | **Score**: 0.85
**Summary**: OpenAI today announced GPT-5...
```

### 📄 中英混合版
```markdown
# 🌟 每日科技简报 - 2025-05-26

## 📊 今日概览 (Today's Overview)
- **总计资讯**: 26条 (Total: 26 articles)
- **AI/ML**: 4条 (AI/ML: 4)
- **GitHub/开发**: 3条 (GitHub/Dev: 3)

## 🔥 今日热点 (Top Stories)
### 1. OpenAI发布具有革命性能力的GPT-5
**原标题**: OpenAI Releases GPT-5 with Revolutionary Capabilities
**来源**: OpenAI Blog | **评分**: 0.85
```

### 🎙️ 播客制作版
```markdown
# 🎙️ 播客脚本素材 - 2025-05-26

## 🎬 节目规划
**建议时长**: 15-20分钟
**核心话题**: 3个
**讨论深度**: 中等

## 📋 开场白建议
"大家好，欢迎收听今日科技播客。今天我们将聊聊OpenAI的最新突破..."

## 🎯 话题一：AI前沿突破 (5-7分钟)
**核心内容**: OpenAI发布GPT-5
**讨论要点**:
- 技术突破的具体表现
- 对行业的潜在影响
- 与竞争对手的差异化
```

## 🛠️ 技术架构

```
高质量信息源 → 智能分类系统 → 多维度评分 → 三版本生成 → 自动推送
      ↓              ↓            ↓           ↓          ↓
   24个精选源      AI分类器      综合评分     英文版     邮件通知
   5大核心领域     技术栈识别    重要性评分   中英版     GitHub存储
   权威性保证      趋势性分析    去重排序     播客版     历史记录
```

## 📈 系统优势

### 🎯 专业化
- 聚焦五大核心领域，避免信息过载
- 精选权威信息源，确保内容质量
- 智能分类评分，突出重要资讯

### 🧠 智能化
- 多维度内容分析和分类
- 重要性和趋势性自动评分
- 技术术语保护的智能翻译

### 🔄 自动化
- 完全基于GitHub Actions运行
- 零服务器成本，零维护负担
- 每日定时执行，结果自动推送

## 🎯 适用场景

- **🎙️ 播客制作者**: 获取结构化脚本素材和话题灵感
- **💼 技术创业者**: 跟踪行业动态和投资趋势
- **👨‍💻 开发者**: 了解技术前沿和工具更新
- **📈 投资人**: 发现投资机会和市场趋势
- **📰 科技媒体**: 获取新闻线索和深度素材

## 📝 版本历史

- **v2.0.0**: 重构架构，专注五大核心领域，智能分类系统
- **v1.3.0**: 增强邮件通知系统
- **v1.2.0**: 优化播客版本格式
- **v1.1.0**: 添加智能翻译功能
- **v1.0.0**: 基础RSS聚合和报告生成

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

1. Fork项目到您的账号
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 发起Pull Request

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

- 感谢所有RSS源提供商的优质内容
- 感谢GitHub Actions提供的免费自动化服务
- 感谢开源社区的技术支持和灵感

---

**🚀 开始您的高质量科技资讯之旅吧！**

*专业 · 智能 · 自动化 - 让科技资讯触手可及* 