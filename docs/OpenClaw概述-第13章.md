# 第13章：技能开发指南

OpenClaw 的技能系统是其最强大的特性之一。通过开发自定义技能，你可以扩展 OpenClaw 的功能，使其满足特定的需求。本章将详细介绍如何开发和发布技能。

## 13.1 技能结构

### 13.1.1 标准目录结构

一个标准的 OpenClaw 技能目录如下：

```
my-skill/
├── SKILL.md              # 技能说明文档（必需）
├── __init__.py           # Python 包初始化（可选）
├── main.py               # 主代码文件（Python 技能）
├── config.yml            # 配置文件（可选）
├── requirements.txt      # Python 依赖（可选）
├── test.py               # 测试文件（可选）
├── references/           # 参考资料目录（可选）
│   ├── api.md
│   ├── examples.md
│   └── images/
└── scripts/              # 辅助脚本（可选）
    ├── install.sh
    └── setup.py
```

### 13.1.2 必需文件

**SKILL.md** - 技能说明文档，必须包含：

```markdown
# 技能名称

## 描述
简要描述技能的功能

## 适用条件
明确说明何时应该使用此技能

## 工具
列出技能提供的工具函数及其参数
```

### 13.1.3 可选文件

- **main.py**: Python 技能的主实现文件
- **config.yml**: 技能配置文件
- **requirements.txt**: Python 依赖包列表
- **test.py**: 单元测试文件
- **references/**: 参考文档和资料
- **scripts/**: 安装和辅助脚本

## 13.2 SKILL.md 规范详解

### 13.2.1 基本结构

SKILL.md 是技能的核心文档，定义了技能的所有信息。以下是完整的结构：

```markdown
# Skill Name - 技能名称

## 描述
技能的简短描述，1-2句话说明功能

## 适用条件
详细说明何时应该使用此技能，包括：
- 触发条件
- 用户意图
- 适用场景

## 工具
列出技能提供的所有工具函数，格式如下：

### tool_name(arg1, arg2)
- **描述**: 工具函数的详细说明
- **参数**:
  - arg1: 参数说明
  - arg2: 参数说明
- **返回**: 返回值说明
- **示例**: 使用示例

## 依赖
列出技能所需的依赖包：
- Python 包
- 系统库
- 外部 API

## 配置
说明需要配置的项目：
- 环境变量
- 配置文件
- API 密钥

## 使用示例
提供具体的使用示例：
```
用户：示例问题
助手：示例回答
```

## 注意事项
使用时需要注意的事项：
- 限制条件
- 常见错误
- 最佳实践

## 故障排除
常见问题和解决方案：
- 问题1: 描述 → 解决方案
- 问题2: 描述 → 解决方案

## 参考资料
相关的文档链接：
- 官方文档
- API 参考
- 示例代码
```

### 13.2.2 完整示例

以下是一个完整的天气技能 SKILL.md 示例：

```markdown
# Weather - 天气查询

## 描述
获取全球任意城市的当前天气和预报信息，支持中英文城市名查询，提供详细的气象数据。

## 适用条件
当用户询问以下信息时使用此技能：
- 当前天气（"北京天气怎么样"）
- 未来预报（"上海明天天气"）
- 具体数据（"深圳的温度、风力、湿度"）
- 历史天气（"广州昨天下雨了吗"）

## 工具

### get_current_weather(city)
- **描述**: 获取指定城市的当前天气信息
- **参数**:
  - city: 城市名称（中文或英文）
- **返回**: 天气信息 JSON，包含：
  - 温度（摄氏度）
  - 天气状况（晴、阴、雨等）
  - 风力和风向
  - 湿度
  - 气压
  - 可见度
- **示例**: `get_current_weather("北京")` 返回 `{"temp": 25, "condition": "晴", "wind": "北风 3级", "humidity": 60}`

### get_forecast(city, days=3)
- **描述**: 获取未来几天的天气预报
- **参数**:
  - city: 城市名称
  - days: 预报天数（1-7天，默认3天）
- **返回**: 预报信息数组，每天包含：
  - 日期
  - 最高/最低温度
  - 天气状况
  - 降水概率
- **示例**: `get_forecast("上海", days=5)` 返回5天的预报

### get_air_quality(city)
- **描述**: 获取城市的空气质量指数
- **参数**:
  - city: 城市名称
- **返回**: AQI 指数和等级
- **示例**: `get_air_quality("深圳")` 返回 `{"aqi": 45, "level": "优"}`

## 依赖
- requests: HTTP 请求库
- 无需 API 密钥（使用免费的 wttr.in 和 Open-Meteo API）

## 配置
无需额外配置，开箱即用。

## 使用示例

### 示例1：查询当前天气
```
用户：北京今天天气怎么样？

助手：北京今天的天气是晴，温度25°C，北风3级，湿度60%。
```

### 示例2：查询未来预报
```
用户：上海未来三天会下雨吗？

助手：根据预报，上海未来三天天气如下：
- 今天：晴，最高28°C，最低20°C
- 明天：多云，最高27°C，最低19°C
- 后天：小雨，最高25°C，最低18°C

后天有小雨，记得带伞哦！
```

### 示例3：查询空气质量
```
用户：深圳的空气质量好吗？

助手：深圳当前的空气质量指数（AQI）为45，等级为"优"，空气非常好，适合户外活动。
```

## 注意事项
- 支持中英文城市名，但建议使用中文以获得更准确的结果
- wttr.in API 有请求频率限制，建议不要过于频繁查询
- 某些小城市或偏远地区可能无法查询到详细信息
- 天气预报的准确性会随时间变化，建议在出发前再次确认

## 故障排除

### 问题：查询失败或返回错误信息
**解决方案**：
1. 检查城市名称是否正确
2. 确认网络连接正常
3. 稍后再试，可能是 API 限流

### 问题：天气信息不准确
**解决方案**：
1. 尝试使用更具体的城市名（如"北京市朝阳区"）
2. 查询多个天气源进行对比
3. 查询官方气象网站确认

### 问题：无法查询到历史天气
**解决方案**：
- 此技能主要提供当前天气和未来预报，历史天气功能有限
- 可以尝试查询官方气象网站的历史数据

## 参考资料
- wttr.in API: https://wttr.in
- Open-Meteo API: https://open-meteo.com
- 中国天气网: http://www.weather.com.cn
```

### 13.2.3 编写技巧

**1. 描述要准确**
- 使用清晰、简洁的语言
- 避免模糊的描述
- 说明技能的核心价值

**2. 适用条件要明确**
- 列出具体的触发场景
- 说明用户的意图
- 避免过于宽泛

**3. 工具文档要详细**
- 每个参数都要说明类型和含义
- 提供返回值的结构说明
- 包含实用的示例

**4. 使用示例要真实**
- 模拟真实的对话场景
- 展示技能的实际效果
- 包含多种使用方式

## 13.3 技能实现

### 13.3.1 Python 技能

**基本框架：**

```python
# my-skill/main.py

def tool_name(arg1, arg2):
    """
    工具函数的说明

    Args:
        arg1: 参数1说明
        arg2: 参数2说明

    Returns:
        返回值说明
    """
    # 实现逻辑
    result = do_something(arg1, arg2)
    return result
```

**完整示例：**

```python
# weather/main.py

import requests

def get_current_weather(city):
    """
    获取当前天气

    Args:
        city: 城市名称

    Returns:
        dict: 天气信息
    """
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        current = data['current_condition'][0]

        return {
            'temp': current['temp_C'],
            'condition': current['weatherDesc'][0]['value'],
            'wind': f"{current['winddir16Point']} {current['windspeedKmph']}km/h",
            'humidity': current['humidity']
        }
    else:
        return {'error': 'Failed to fetch weather'}

def get_forecast(city, days=3):
    """
    获取天气预报

    Args:
        city: 城市名称
        days: 天数

    Returns:
        list: 预报信息
    """
    url = f"https://wttr.in/{city}?format=j1&days={days}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        forecast = []

        for day in data['weather']:
            forecast.append({
                'date': day['date'],
                'max_temp': day['maxtempC'],
                'min_temp': day['mintempC'],
                'condition': day['hourly'][0]['weatherDesc'][0]['value']
            })

        return forecast
    else:
        return {'error': 'Failed to fetch forecast'}
```

### 13.3.2 ACP 技能

ACP (Agent Coding Protocol) 技能与 Python 技能不同，它使用特定的协议和格式。

**基本结构：**

```yaml
# .acp/config.yml
name: my-acp-skill
description: My ACP Skill
version: 1.0.0
model: gpt-4
temperature: 0.7
max_tokens: 2048

tools:
  - name: search
    description: Search the web
    type: function
    parameters:
      type: object
      properties:
        query:
          type: string
          description: Search query
      required: ["query"]

  - name: analyze
    description: Analyze data
    type: function
    parameters:
      type: object
      properties:
        data:
          type: string
          description: Data to analyze
      required: ["data"]
```

**实现文件：**

```python
# .acp/tools/search.py

import requests

def search(query):
    """
    Web search function

    Args:
        query: Search query

    Returns:
        Search results
    """
    # 实现搜索逻辑
    api_url = f"https://api.searchengine.com/search?q={query}"
    response = requests.get(api_url)
    return response.json()
```

### 13.3.3 Shell 技能

Shell 技能使用 Bash 脚本实现，适合简单的系统任务。

**基本结构：**

```bash
#!/bin/bash
# my-skill.sh

# 技能名称
SKILL_NAME="my-shell-skill"
SKILL_VERSION="1.0.0"

# 技能描述
SKILL_DESC="My Shell Skill"

# 初始化
init() {
    echo "Initializing $SKILL_NAME..."
}

# 主功能
execute() {
    local action=$1
    shift

    case $action in
        search)
            do_search "$@"
            ;;
        analyze)
            do_analyze "$@"
            ;;
        *)
            echo "Unknown action: $action"
            return 1
            ;;
    esac
}

# 搜索功能
do_search() {
    local query="$1"
    echo "Searching for: $query"
    # 实现搜索逻辑
}

# 分析功能
do_analyze() {
    local data="$1"
    echo "Analyzing: $data"
    # 实现分析逻辑
}

# 主函数
main() {
    init
    execute "$@"
}

# 执行
main "$@"
```

### 13.3.4 技能注册

Python 技能需要注册到 OpenClaw：

```python
# my-skill/__init__.py

from .main import get_current_weather, get_forecast

__all__ = ['get_current_weather', 'get_forecast']
```

## 13.4 技能测试

### 13.4.1 单元测试

```python
# test.py

import unittest
from main import get_current_weather, get_forecast

class TestWeatherSkill(unittest.TestCase):

    def test_get_current_weather(self):
        """测试获取当前天气"""
        result = get_current_weather("北京")
        self.assertIn('temp', result)
        self.assertIn('condition', result)

    def test_get_forecast(self):
        """测试获取预报"""
        result = get_forecast("上海", days=3)
        self.assertEqual(len(result), 3)

    def test_invalid_city(self):
        """测试无效城市"""
        result = get_current_weather("不存在的城市")
        self.assertIn('error', result)

if __name__ == '__main__':
    unittest.main()
```

**运行测试：**

```bash
python test.py
```

### 13.4.2 集成测试

在 OpenClaw 中测试技能：

```bash
# 1. 将技能复制到扩展目录
cp -r my-skill ~/.openclaw/extensions/

# 2. 重启 Gateway
openclaw gateway restart

# 3. 在对话中测试
```

测试要点：
- 功能是否正常工作
- 错误处理是否完善
- 性能是否满足要求

### 13.4.3 测试检查清单

- [ ] 所有工具函数都能正常工作
- [ ] 错误处理完善
- [ ] 边界条件测试通过
- [ ] 性能满足要求
- [ ] 文档准确完整
- [ ] SKILL.md 规范正确

## 13.5 技能发布

### 13.5.1 准备发布

发布前的检查清单：

- [ ] 代码质量检查
- [ ] 测试全部通过
- [ ] 文档完整准确
- [ ] 示例代码可运行
- [ ] 无安全漏洞
- [ ] 无敏感信息

### 13.5.2 发布到官方仓库

**步骤：**

1. **Fork 官方仓库**
   ```bash
   # 在 GitHub 上 fork
   # https://github.com/openclaw/awesome-openclaw-skills
   ```

2. **克隆你的 fork**
   ```bash
   git clone https://github.com/your-username/awesome-openclaw-skills.git
   cd awesome-openclaw-skills
   ```

3. **创建技能目录**
   ```bash
   mkdir -p skills/my-skill
   cd skills/my-skill
   ```

4. **复制技能文件**
   ```bash
   cp -r /path/to/my-skill/* .
   ```

5. **提交更改**
   ```bash
   cd ../..
   git add skills/my-skill
   git commit -m "Add my-skill: description"
   ```

6. **推送到你的 fork**
   ```bash
   git push origin master
   ```

7. **创建 Pull Request**
   - 访问 https://github.com/openclaw/awesome-openclaw-skills
   - 点击 "Pull requests"
   - 点击 "New pull request"
   - 选择你的分支
   - 填写 PR 信息
   - 提交

8. **等待审核**
   - 社区和官方审核
   - 可能需要修改
   - 审核通过后合并

### 13.5.3 独立发布

如果你想独立发布技能：

1. **创建 GitHub 仓库**
   ```bash
   # 在 GitHub 上创建新仓库
   # https://github.com/new
   ```

2. **上传技能**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/your-username/my-skill.git
   git push -u origin master
   ```

3. **完善 README.md**
   ```markdown
   # My Skill

   ## 简介
   技能的简要介绍

   ## 安装
   安装步骤

   ## 使用
   使用说明

   ## 配置
   配置说明

   ## 示例
   使用示例

   ## 许可证
   MIT License
   ```

4. **发布版本**
   ```bash
   git tag v1.0.0
   git push --tags
   ```

5. **在社区分享**
   - 在 OpenClaw 社区分享
   - 在相关论坛发布
   - 通过社交媒体宣传

## 13.6 技能维护

### 13.6.1 版本管理

使用语义化版本号：
- **主版本**: 重大变更，不兼容
- **次版本**: 新增功能，向后兼容
- **修订版本**: Bug 修复，向后兼容

示例：
- 1.0.0 - 初始版本
- 1.1.0 - 新增功能
- 1.1.1 - Bug 修复
- 2.0.0 - 重大变更

### 13.6.2 更新维护

**定期检查：**
- 依赖是否有更新
- API 是否有变更
- 是否有安全问题

**用户反馈：**
- 收集用户反馈
- 分析问题
- 及时修复

**性能优化：**
- 监控性能
- 优化算法
- 减少资源使用

### 13.6.3 文档更新

**更新时机：**
- 功能变更时
- Bug 修复时
- 新增示例时
- 用户反馈问题时

**更新内容：**
- SKILL.md
- README.md
- 示例代码
- 参考资料

## 总结

本章详细介绍了 OpenClaw 技能的开发流程，包括技能结构、SKILL.md 规范、技能实现、测试、发布和维护。通过掌握这些内容，你可以开发出高质量的技能，为 OpenClaw 社区做出贡献。

下一章将介绍插件开发。
