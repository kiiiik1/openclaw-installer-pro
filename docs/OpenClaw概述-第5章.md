# 第5章：技能系统详解

技能系统是 OpenClaw 最强大的特性之一，它使得 OpenClaw 能够不断扩展和增强能力，而无需修改核心代码。通过技能系统，社区贡献者和开发者可以轻松地为 OpenClaw 添加新功能。

## 5.1 技能概念

### 5.1.1 什么是技能？

技能是 OpenClaw 的可插拔功能模块，类似于操作系统的"应用"或"插件"。每个技能提供特定的功能，例如：

- **工具类技能**: 网络搜索、天气查询、文件操作
- **集成类技能**: 日历同步、邮件发送、数据库访问
- **专业类技能**: 代码生成、翻译、文本分析
- **娱乐类技能**: 讲故事、语音合成、图像生成

### 5.1.2 技能 vs Agent

| 特性 | 技能 (Skill) | Agent (智能体) |
|------|-------------|---------------|
| 定位 | 功能模块 | 整体智能 |
| 职责 | 提供特定功能 | 协调和决策 |
| 数量 | 多个，可扩展 | 通常一个或少数几个 |
| 独立性 | 独立开发和维护 | 核心系统 |
| 交互方式 | 被动调用 | 主动决策 |
| 示例 | 天气查询、网络搜索 | 主聊天机器人 |

**协作关系：**
- Agent 是大脑，负责理解用户意图
- 技能是手脚，负责执行具体任务
- Agent 根据需要调用相应的技能

### 5.1.3 技能的价值

1. **模块化**: 每个技能独立开发和维护
2. **可扩展**: 社区可以贡献新技能
3. **可组合**: 多个技能可以组合使用
4. **易维护**: 修改一个技能不影响其他功能
5. **灵活性**: 用户可以选择安装需要的技能
6. **可升级**: 技能可以独立更新

## 5.2 技能生态

### 5.2.1 官方技能库

OpenClaw 官方维护了一个核心技能库，包含常用功能：

**内置核心技能：**
1. **weather** - 天气查询
   - 支持全球城市天气查询
   - 提供当前天气和预报
   - 使用 wttr.in 和 Open-Meteo API

2. **qqbot-cron** - 定时提醒
   - 一次性提醒
   - 周期性提醒
   - 提醒管理（查询、取消）

3. **qqbot-media** - 媒体处理
   - 图片接收和发送
   - 语音消息处理
   - 视频和文件传输

4. **healthcheck** - 系统健康检查
   - 安全审计
   - 风险评估
   - 定期检查

**安装方式：**
```bash
# 这些技能默认包含在 OpenClaw 中
# 无需额外安装
```

### 5.2.2 社区技能

社区贡献的技能托管在 GitHub 上：

**社区技能仓库：**
- GitHub: https://github.com/openclaw/awesome-openclaw-skills
- 包含数百个社区贡献的技能
- 涵盖各种使用场景

**热门社区技能：**
1. **code-assistant** - 代码助手
   - 代码生成
   - 代码审查
   - 调试帮助

2. **finance-tracker** - 财务追踪
   - 记账功能
   - 预算管理
   - 财务报表

3. **productivity-booster** - 生产力工具
   - 任务管理
   - 时间追踪
   - 工作提醒

4. **language-learner** - 语言学习
   - 单词记忆
   - 语法练习
   - 对话练习

**安装方式：**
```bash
# 从社区仓库克隆技能
git clone https://github.com/username/skill-name.git ~/.openclaw/extensions/

# 重启 Gateway 使技能生效
openclaw gateway restart
```

### 5.2.3 技能质量标准

为了确保技能的质量和安全性，OpenClaw 定义了技能质量标准：

**功能标准：**
- ✅ 功能完整，可以正常使用
- ✅ 错误处理完善
- ✅ 性能良好，响应及时
- ✅ 资源使用合理

**文档标准：**
- ✅ 包含完整的 SKILL.md 说明
- ✅ 提供使用示例
- ✅ 说明依赖和要求
- ✅ 包含故障排除指南

**安全标准：**
- ✅ 不包含恶意代码
- ✅ 不泄露用户隐私
- ✅ 正确处理敏感信息
- ✅ 遵循安全最佳实践

**代码标准：**
- ✅ 代码清晰易读
- ✅ 遵循命名规范
- ✅ 包含必要的注释
- ✅ 通过测试验证

**社区技能审核：**
- 提交 PR 到官方仓库
- 由社区和官方审核
- 审核通过后合并
- 审核不通过的技能仍可独立分发

## 5.3 技能开发

### 5.3.1 开发流程

```
1. 需求分析
   ↓
2. 设计技能架构
   ↓
3. 创建技能目录
   ↓
4. 编写 SKILL.md
   ↓
5. 实现技能代码
   ↓
6. 编写测试
   ↓
7. 本地测试
   ↓
8. 编写文档
   ↓
9. 提交发布
```

### 5.3.2 技能类型详解

#### Python 技能

**适用场景：**
- 需要复杂逻辑处理
- 需要访问系统资源
- 需要与外部 API 交互
- 需要数据库操作

**结构示例：**
```
my-skill/
├── SKILL.md              # 技能说明（必需）
├── skill.py              # 主代码文件
├── references/           # 参考文档（可选）
│   ├── api.md
│   └── examples.md
└── scripts/              # 辅助脚本（可选）
    └── setup.sh
```

**SKILL.md 模板：**
```markdown
# My Skill

## 描述
简要描述技能的功能

## 适用条件
说明何时使用此技能

## 工具
列出技能提供的工具函数

## 使用说明
详细的使用说明

## 依赖
列出所需的依赖包

## 注意事项
使用时的注意事项
```

**代码示例：**
```python
# skill.py

def search_web(query):
    """网络搜索功能"""
    # 实现搜索逻辑
    pass

def get_weather(city):
    """天气查询功能"""
    # 实现天气查询
    pass
```

#### ACP 技能

**适用场景：**
- 需要远程执行
- 需要独立的运行环境
- 需要与其他系统深度集成

**ACP (Agent Coding Protocol) 特点：**
- 基于 OpenAI 的 Assistant API
- 支持多轮对话
- 支持工具调用
- 支持代码执行

**创建 ACP 技能：**
```yaml
# .acp/config.yml
name: my-acp-skill
description: My ACP Skill
model: gpt-4
tools:
  - name: search
    description: Search web
    parameters:
      type: object
      properties:
        query:
          type: string
```

#### Shell 技能

**适用场景：**
- 简单的系统任务
- 快速原型开发
- 依赖外部命令行工具

**示例：**
```bash
#!/bin/bash
# skill.sh

# 技能名称
SKILL_NAME="my-shell-skill"

# 技能描述
SKILL_DESC="My Shell Skill"

# 执行逻辑
execute() {
    echo "Executing skill..."
    # 实现功能
}

# 主函数
main() {
    execute
}

main "$@"
```

### 5.3.3 SKILL.md 规范详解

**必需字段：**

```markdown
# 技能名称

## 描述
技能的功能描述，1-2句话

## 适用条件
明确说明何时应该使用此技能

## 工具
列出技能提供的工具函数及其参数
```

**可选字段：**

```markdown
## 依赖
列出所需的 Python 包或其他依赖

## 配置
说明需要配置的环境变量或配置文件

## 使用示例
提供具体的使用示例

## 注意事项
使用时需要注意的事项

## 故障排除
常见问题和解决方案

## 参考资料
相关的文档链接
```

**完整示例：**

```markdown
# Weather - 天气查询技能

## 描述
获取全球任意城市的当前天气和预报信息，支持中文查询。

## 适用条件
当用户询问天气信息、气温、风力、降水等时使用此技能。

## 工具
- get_weather(location, forecast_days=1)
  - location: 城市名称或英文城市名
  - forecast_days: 预报天数，默认 1 天
  - 返回: 天气信息（JSON 格式）

## 依赖
- requests: HTTP 请求库
- 无 API key 需求（使用 wttr.in）

## 使用示例
```
get_weather("北京")
get_weather("Shanghai", forecast_days=3)
```

## 注意事项
- 支持中文城市名
- wttr.in 有请求频率限制
- 某些小城市可能无法查询

## 参考资料
- wttr.in: https://wttr.in
- Open-Meteo: https://open-meteo.com
```

### 5.3.4 技能测试

**单元测试：**
```python
import unittest
from skill import search_web

class TestSkill(unittest.TestCase):
    def test_search(self):
        result = search_web("OpenClaw")
        self.assertIsNotNone(result)
        
if __name__ == '__main__':
    unittest.main()
```

**集成测试：**
- 在 OpenClaw 中加载技能
- 测试各种使用场景
- 验证错误处理

**性能测试：**
- 测试响应时间
- 测试资源使用
- 测试并发处理

### 5.3.5 技能发布

**发布到社区仓库：**
```bash
# 1. Fork 官方仓库
# 2. 创建技能分支
git checkout -b my-skill

# 3. 提交技能
git add .
git commit -m "Add my skill"

# 4. 推送到你的 fork
git push origin my-skill

# 5. 创建 Pull Request
```

**独立发布：**
- 将技能放到自己的 GitHub 仓库
- 编写详细的 README.md
- 提供安装说明
- 在社区分享链接

## 5.4 技能管理

### 5.4.1 查看已安装技能

```bash
# 列出所有技能
ls ~/.openclaw/extensions/

# 查看技能信息
cat ~/.openclaw/extensions/skill-name/SKILL.md
```

### 5.4.2 启用/禁用技能

```bash
# 禁用技能
mv ~/.openclaw/extensions/skill-name ~/.openclaw/extensions/.skill-name.disabled

# 启用技能
mv ~/.openclaw/extensions/.skill-name.disabled ~/.openclaw/extensions/skill-name
```

### 5.4.3 更新技能

```bash
# 更新技能
cd ~/.openclaw/extensions/skill-name
git pull origin main

# 重启 Gateway
openclaw gateway restart
```

### 5.4.4 卸载技能

```bash
# 删除技能目录
rm -rf ~/.openclaw/extensions/skill-name

# 重启 Gateway
openclaw gateway restart
```

## 5.5 技能案例研究

### 案例1：网络搜索技能

**需求：** 让 OpenClaw 能够搜索互联网获取信息

**实现：**
```python
import requests

def search_web(query):
    """使用 Google 搜索"""
    api_url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'q': query
    }
    response = requests.get(api_url, params=params)
    return response.json()
```

**SKILL.md:**
```markdown
# Web Search - 网络搜索

## 描述
搜索互联网获取最新信息

## 适用条件
用户需要实时信息、新闻、知识查询时使用

## 工具
- search_web(query): 搜索网络
```

### 案例2：代码生成技能

**需求：** 根据描述生成代码

**实现：**
```python
def generate_code(description, language="python"):
    """生成代码"""
    prompt = f"生成{language}代码：{description}"
    response = llm.complete(prompt)
    return response
```

### 案例3：翻译技能

**需求：** 多语言翻译

**实现：**
```python
def translate(text, source_lang, target_lang):
    """翻译文本"""
    # 使用 Google Translate API 或 LLM
    pass
```

## 5.6 技能最佳实践

### 5.6.1 命名规范
- 使用小写字母和连字符
- 名称要描述功能
- 避免使用已有名称

### 5.6.2 错误处理
- 捕获所有可能的异常
- 提供友好的错误信息
- 记录详细的错误日志

### 5.6.3 性能优化
- 避免重复计算
- 使用缓存
- 异步处理耗时操作

### 5.6.4 安全考虑
- 验证用户输入
- 不泄露敏感信息
- 限制资源使用

## 总结

技能系统是 OpenClaw 的核心优势之一，通过灵活的技能架构，OpenClaw 可以不断扩展和增强能力。无论是官方技能还是社区技能，都遵循相同的标准和规范，确保了系统的稳定性和可维护性。

下一章将详细介绍 OpenClaw 的配置管理。
