# 第10章：高级功能

本章将深入介绍 OpenClaw 的高级功能，帮助你充分利用 OpenClaw 的强大能力。

## 10.1 记忆管理

记忆系统是 OpenClaw 的核心特性之一，让它能够记住重要的信息、决策和上下文，提供更智能的服务。

### 10.1.1 MEMORY.md - 长期记忆

MEMORY.md 是 OpenClaw 的长期记忆文件，存储最重要的信息。

**文件位置：**
- `~/.openclaw/workspace/MEMORY.md`

**MEMORY.md 的作用：**
- 存储关键决策
- 记录重要偏好
- 保存长期知识
- 维护工作上下文

**MEMORY.md 结构示例：**

```markdown
# MEMORY.md - 我的长期记忆

## 个人信息
- 名字: 张三
- 职业: 软件工程师
- 时区: Asia/Shanghai
- 喜好的称呼: "叫我小张"

## 工作项目
### 项目 A - CRM 系统
- 技术栈: Python, Django, PostgreSQL
- 状态: 开发中
- 下一步: 完成用户认证模块
- 截止日期: 2024-03-15

### 项目 B - 数据分析
- 目标: 分析 Q1 销售数据
- 工具: Pandas, Matplotlib
- 优先级: 高

## 偏好设置
- 工作时间: 9:00 - 18:00
- 休息时间: 12:00 - 13:00
- 通知偏好: 仅紧急事项打扰
- 回复风格: 简洁明了

## 重要日期
- 生日: 1990-05-20
- 结婚纪念日: 2015-08-18
- 项目A截止: 2024-03-15

## 常用命令
- Git: `git pull origin main`
- Docker: `docker-compose up -d`
- 测试: `pytest tests/`

## 学习目标
- 2024 Q1: 学习 Rust
- 2024 Q2: 深入机器学习
- 2024 Q3: 掌握 Kubernetes

## 其他备注
- 不喜欢在周末讨论工作
- 偏好用 Markdown 记录笔记
- 重要事项请用邮件确认
```

**自动更新机制：**
OpenClaw 会在以下情况自动更新 MEMORY.md：
- 记住新的重要信息时
- 做出关键决策时
- 用户明确要求记录时
- 定期的心跳检查中

**手动编辑：**
你也可以直接编辑 MEMORY.md：

```bash
# 使用文本编辑器
vim ~/.openclaw/workspace/MEMORY.md

# 或使用 VS Code
code ~/.openclaw/workspace/MEMORY.md
```

### 10.1.2 记忆搜索

OpenClaw 使用语义搜索来查找记忆中的信息。

**使用方式：**
在对话中自然地询问，OpenClaw 会自动搜索相关记忆：

```
你: 我的项目A进展如何？
OpenClaw: 根据我的记忆，你的项目A是CRM系统，目前处于开发中状态，下一步是完成用户认证模块，截止日期是2024年3月15日。

你: 我的生日是什么时候？
OpenClaw: 你的生日是1990年5月20日。

你: 我喜欢什么编程语言？
OpenClaw: 根据你的工作项目，你目前主要使用Python和Django。
```

**搜索机制：**
1. 接收用户问题
2. 提取关键词
3. 语义搜索 MEMORY.md
4. 匹配相关内容
5. 整合回答

**搜索准确性：**
- 精确匹配: "生日" → "1990-05-20"
- 语义匹配: "项目A进展" → "CRM系统开发中"
- 关联匹配: "工作安排" → "工作时间9:00-18:00"

### 10.1.3 记忆维护

随着使用时间的增长，MEMORY.md 会变得庞大，需要定期维护。

**维护任务：**

**1. 清理过时信息**

```markdown
# 删除过时的内容
❌ 2023年的任务（已过期）
❌ 已取消的项目
❌ 过期的会议记录
```

**2. 整理结构化信息**

```markdown
# 使用清晰的分类
## 工作
  - 项目
  - 任务
  - 协作

## 个人
  - 偏好
  - 目标
  - 重要日期

## 技术
  - 常用命令
  - 工具配置
  - 快捷键
```

**3. 更新状态信息**

```markdown
# 更新项目状态
### 项目A - CRM 系统
- 状态: 开发中 → 已完成 ✅
- 完成日期: 2024-03-14（提前1天）
- 下一阶段: 测试和部署
```

**4. 去重和合并**

```markdown
# 合并重复信息
❌ 首选语言: Python
❌ 主要语言: Python
✅ 首选语言: Python
```

**自动维护：**
OpenClaw 会在心跳检查中自动进行以下维护：
- 去除重复内容
- 重新组织结构
- 更新状态标记
- 标记过期信息

### 10.1.4 记忆最佳实践

**1. 定期审查**
- 每周审查一次
- 更新进度状态
- 添加新信息

**2. 保持简洁**
- 只记录重要信息
- 避免冗长描述
- 使用列表和表格

**3. 分类清晰**
- 使用 Markdown 标题
- 按主题分组
- 添加标签和状态

**4. 及时更新**
- 完成任务后标记
- 改变偏好时更新
- 项目进展时记录

**5. 备份记忆**
```bash
# 定期备份 MEMORY.md
cp ~/.openclaw/workspace/MEMORY.md ~/.openclaw/workspace/backups/

# 或使用 Git
git add MEMORY.md
git commit -m "Update memory"
git push
```

## 10.2 定时任务

OpenClaw 提供强大的定时任务系统，支持一次性提醒、周期性任务和复杂的时间规则。

### 10.2.1 心跳配置

心跳机制是 OpenClaw 的自动检查功能，定期执行预设的任务。

**配置文件：** `~/.openclaw/workspace/HEARTBEAT.md`

**示例配置：**

```markdown
# HEARTBEAT.md

## 检查清单

### 每日检查
- [ ] 检查未读邮件（9:00, 14:00, 18:00）
- [ ] 检查日历事件（每2小时）
- [ ] 检查待办事项（每日早上9点）
- [ ] 天气提醒（每日早上8点）

### 每周检查
- [ ] 周报总结（周五18:00）
- [ ] 备份重要文件（周六10:00）
- [ ] 审查记忆文件（周日20:00）

### 每月检查
- [ ] 月度总结（每月最后一天）
- [ ] 账单提醒（每月1号）
- [ ] 系统更新检查（每月15号）

## 触发条件
- 消息匹配: "检查状态" 或 "任务"
- 时间间隔: 30分钟
- 仅工作时间: 9:00 - 18:00
```

**心跳执行逻辑：**
1. 定时触发（默认每30分钟）
2. 读取 HEARTBEAT.md
3. 依次检查每个任务
4. 需要时调用相应技能
5. 有重要事项时通知用户
6. 无事项时保持静默（`HEARTBEAT_OK`）

**智能触发：**
- 工作时间内频繁检查
- 非工作时间减少频率
- 优先级高的任务优先执行
- 避免重复通知

### 10.2.2 Cron 任务

Cron 是传统的 Unix 定时任务工具，OpenClaw 集成了类似的功能。

**Cron 表达式格式：**
```
* * * * *
│ │ │ │ │
│ │ │ │ └─ 星期几 (0-6, 0=周日)
│ │ │ └─── 月份 (1-12)
│ │ └───── 日期 (1-31)
│ └─────── 小时 (0-23)
└───────── 分钟 (0-59)
```

**Cron 示例：**

```yaml
# .openclaw/cron.yaml

tasks:
  # 每天早上9点提醒
  - name: "早安提醒"
    schedule: "0 9 * * *"
    action: "send_message"
    message: "早上好！今天有什么计划？"

  # 每周五下午6点提醒周报
  - name: "周报提醒"
    schedule: "0 18 * * 5"
    action: "send_message"
    message: "周五了，记得写周报！"

  # 每月1号提醒账单
  - name: "账单提醒"
    schedule: "0 10 1 * *"
    action: "send_message"
    message: "今天是月初，记得处理账单"

  # 每2小时检查邮件
  - name: "邮件检查"
    schedule: "0 */2 * * *"
    action: "check_email"

  # 工作日每小时检查日历
  - name: "日历检查"
    schedule: "0 * * * 1-5"
    action: "check_calendar"

  # 每周日凌晨3点备份
  - name: "数据备份"
    schedule: "0 3 * * 0"
    action: "backup"
    path: "/backup/data"
```

**Cron 任务管理：**

**查看所有任务：**
```bash
openclaw cron list
```

**添加任务：**
```bash
openclaw cron add "0 9 * * *" "send_message:早上好！"
```

**删除任务：**
```bash
openclaw cron remove <task-id>
```

**启用/禁用任务：**
```bash
openclaw cron enable <task-id>
openclaw cron disable <task-id>
```

**测试任务：**
```bash
openclaw cron test <task-id>
```

### 10.2.3 提醒设置

OpenClaw 支持灵活的提醒系统，可以通过对话设置提醒。

**对话式提醒：**

```
你: 明天下午3点提醒我开会
OpenClaw: 好的，已设置明天下午3点的开会提醒。

你: 每周一早上9点提醒我写周报
OpenClaw: 已设置每周一早上9点的周报提醒。

你: 2024年3月15日提醒我项目截止
OpenClaw: 已设置2024年3月15日的项目截止提醒。
```

**提醒类型：**

**1. 一次性提醒**
```
明天上午10点提醒我
3天后提醒我
2024年5月1日提醒我
```

**2. 周期性提醒**
```
每天早上8点提醒我起床
每周五下午5点提醒我周报
每月1号提醒我交房租
每个工作日9点提醒我检查邮件
```

**3. 相对时间提醒**
```
30分钟后提醒我
2小时后提醒我休息
1天后提醒我回复邮件
```

**提醒设置命令：**

**通过聊天：**
```
/remind 明天上午10点 提醒我开会
```

**通过命令：**
```bash
openclaw remind "明天上午10点" "提醒我开会"
```

**查看提醒：**
```
你: 我有哪些提醒？
OpenClaw: 你有3个提醒：
  1. 明天上午10点 - 提醒我开会
  2. 每周一早上9点 - 周报
  3. 2024年3月15日 - 项目截止
```

**删除提醒：**
```
你: 取消第一个提醒
OpenClaw: 已取消"明天上午10点 - 提醒我开会"
```

**提醒通知：**
到时间时，OpenClaw 会：
1. 发送消息通知
2. 包含提醒内容和时间
3. 可选附加操作（如确认、推迟）
4. 记录到记忆中

**智能提醒：**
- 根据日程自动调整
- 避免重复提醒
- 优先级排序
- 上下文相关

### 10.2.4 提醒和 Cron 的区别

| 特性 | 提醒 (Remind) | Cron 任务 |
|------|-------------|-----------|
| 设置方式 | 对话式 | 配置文件/命令 |
| 灵活性 | 高，自然语言 | 中，Cron 表达式 |
| 复杂性 | 简单任务 | 可执行脚本 |
| 使用场景 | 个人提醒 | 系统任务 |
| 持久化 | 自动 | 需要配置 |
| 适用人群 | 所有用户 | 高级用户 |

**推荐使用：**
- **提醒**: 个人任务、会议、截止日期
- **Cron**: 系统维护、数据备份、定期报告

## 10.3 多会话管理

OpenClaw 支持多个独立的会话，每个会话有自己的上下文、记忆和状态。

### 10.3.1 会话创建

**自动创建：**
当 OpenClaw 在新的聊天频道或与新的用户对话时，会自动创建新会话。

**手动创建：**
```
你: 创建一个新会话用于项目A
OpenClaw: 已创建新会话"项目A"，会话ID: session_12345

你: 创建会话"学习计划"
OpenClaw: 已创建会话"学习计划"，会话ID: session_12346
```

**会话命名：**
```
你: 将这个会话命名为"工作"
OpenClaw: 已将当前会话重命名为"工作"
```

### 10.3.2 会话切换

**切换到指定会话：**
```
你: 切换到项目A会话
OpenClaw: 已切换到会话"项目A"，会话ID: session_12345

你: 项目A现在进展如何？
OpenClaw: 根据该会话的上下文，项目A目前处于测试阶段...
```

**列出所有会话：**
```
你: 显示所有会话
OpenClaw: 你有以下活跃会话：
  1. 项目A (session_12345) - 最后活跃: 10分钟前
  2. 学习计划 (session_12346) - 最后活跃: 1小时前
  3. 日常 (session_12347) - 最后活跃: 昨天
```

### 10.3.3 会话监控

**查看会话状态：**
```bash
openclaw session list
```

**查看会话详情：**
```bash
openclaw session info session_12345
```

**查看会话历史：**
```bash
openclaw session history session_12345
```

**会话统计：**
```
会话名称: 项目A
会话ID: session_12345
创建时间: 2024-03-01 10:00
消息总数: 156
最后活跃: 2024-03-10 14:30
状态: 活跃
关联技能: weather, calendar, task-manager
```

### 10.3.4 会话隔离

每个会话是独立的：
- ✅ 独立的上下文记忆
- ✅ 独立的配置设置
- ✅ 独立的技能列表
- ✅ 独立的提醒任务

**示例：**
```
# 在"工作"会话中
你: 我的任务是什么？
OpenClaw: 你有3个任务：1. 完成报告 2. 修复Bug 3. 代码审查

# 切换到"学习"会话
你: 我的任务是什么？
OpenClaw: 你的学习任务：1. 阅读第5章 2. 做练习题 3. 写笔记
```

### 10.3.5 会话共享

你可以选择在会话之间共享信息：

**共享记忆：**
```yaml
sessions:
  session_12345:
    share_memory: true
    shared_with:
      - session_12346
```

**共享技能：**
```yaml
sessions:
  session_12345:
    shared_skills:
      - weather
      - calendar
```

**跨会话操作：**
```
你: 在项目A会话中记录这个
OpenClaw: 已在会话"项目A"中记录
```

### 10.3.6 会话生命周期

**会话状态：**
- `active`: 活跃，正常使用
- `paused`: 暂停，不自动处理消息
- `archived`: 归档，只读状态
- `closed`: 关闭，不再使用

**状态转换：**
```
创建 → active
active → paused
paused → active
active → archived
archived → active
any → closed
```

**管理会话状态：**
```bash
openclaw session pause session_12345
openclaw session resume session_12345
openclaw session archive session_12345
openclaw session close session_12345
```

**自动归档：**
- 30天未活跃 → 归档
- 90天未活跃 → 关闭
- 可配置

### 10.3.7 会话最佳实践

**1. 合理命名**
- 使用描述性名称
- 避免重复
- 添加标签

**2. 及时清理**
- 定期归档不用的会话
- 删除错误的会话
- 合并相似的会话

**3. 权限管理**
- 公共会话 vs 私密会话
- 团队协作会话
- 个人专属会话

**4. 定期备份**
- 导出会话历史
- 保存重要决策
- 归档完成的项目

## 10.4 智能路由

OpenClaw 的智能路由功能可以自动将消息分配到最合适的会话或处理流程。

### 10.4.1 路由规则

基于规则的路由：

```yaml
routing:
  rules:
    # 工作相关消息路由到工作会话
    - pattern: "工作|任务|项目|会议"
      target: "work_session"
      
    # 学习相关路由到学习会话
    - pattern: "学习|阅读|课程|笔记"
      target: "study_session"
      
    # 技术问题路由到技术会话
    - pattern: "代码|调试|Bug|API"
      target: "tech_session"
      
    # 默认路由
    - pattern: "*"
      target: "default_session"
```

### 10.4.2 智能分类

使用 AI 自动分类消息：

```yaml
routing:
  ai_classification:
    enabled: true
    model: "gpt-4"
    categories:
      - work
      - study
      - personal
      - entertainment
```

**示例：**
```
用户: "怎么写Python脚本？"
OpenClaw路由: tech_session (自动识别为技术问题)

用户: "周末去看电影？"
OpenClaw路由: personal_session (自动识别为个人娱乐)
```

### 10.4.3 优先级路由

根据消息优先级路由：

```yaml
routing:
  priority:
    high:
      - pattern: "紧急|重要|马上"
      target: "urgent_session"
    medium:
      - pattern: "明天|本周"
      target: "normal_session"
    low:
      - pattern: "可能|考虑"
      target: "later_session"
```

## 10.5 自动化工作流

OpenClaw 支持创建自动化工作流，连接多个操作。

### 10.5.1 工作流定义

**YAML 格式：**

```yaml
workflows:
  daily_standup:
    name: "每日站会"
    trigger:
      time: "09:00"
      weekdays: [1, 2, 3, 4, 5]
    steps:
      - type: "check_calendar"
        name: "检查今日日历"
      - type: "check_tasks"
        name: "检查待办任务"
      - type: "get_weather"
        name: "获取天气"
        params:
          location: "北京"
      - type: "send_summary"
        name: "发送晨间总结"
        template: "今日计划：{{calendar}}\n待办：{{tasks}}\n天气：{{weather}}"
```

### 10.5.2 工作流触发

**定时触发：**
```yaml
trigger:
  type: "cron"
  schedule: "0 9 * * *"
```

**事件触发：**
```yaml
trigger:
  type: "event"
  event: "email_received"
  filter:
    from: "boss@company.com"
```

**手动触发：**
```
你: 执行每日站会工作流
OpenClaw: 正在执行每日站会工作流...
```

### 10.5.3 工作流示例

**1. 晨间例行：**
```yaml
name: "Morning Routine"
steps:
  - 检查天气
  - 查看日历
  - 获取新闻
  - 发送总结
```

**2. 项目交付流程：**
```yaml
name: "Project Delivery"
steps:
  - 运行测试
  - 生成报告
  - 创建备份
  - 发送通知
  - 更新文档
```

**3. 会议准备：**
```yaml
name: "Meeting Prep"
steps:
  - 查参会人员
  - 准备议程
  - 收集资料
  - 发送提醒
```

---

## 总结

OpenClaw 的高级功能提供了强大的自动化和智能化能力，让 OpenClaw 不仅仅是一个聊天机器人，更是一个智能的数字助手。通过合理配置和使用这些功能，可以大幅提升工作效率和生活便利性。

下一章将介绍故障排除，帮助你解决使用中遇到的问题。
