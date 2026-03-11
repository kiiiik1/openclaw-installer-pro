#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
安装器模块
负责配置和安装 OpenClaw
"""

import os
import json
import subprocess
from pathlib import Path


class OpenClawInstaller:
    """OpenClaw 安装器"""

    def __init__(self, config):
        self.config = config
        self.install_path = Path(config.get('install_path', '~/openclaw')).expanduser()

    def install(self, progress_callback=None):
        """安装 OpenClaw"""
        if progress_callback:
            progress_callback(60, "创建配置文件...")

        # 创建配置目录
        config_dir = self.install_path / '.openclaw' / 'config'
        config_dir.mkdir(parents=True, exist_ok=True)

        # 创建模型配置
        self.create_model_config(config_dir)

        if progress_callback:
            progress_callback(70, "创建启动脚本...")

        # 创建启动脚本
        self.create_start_script()

        if progress_callback:
            progress_callback(80, "创建用户配置...")

        # 创建用户配置
        self.create_user_config()

        return True

    def create_model_config(self, config_dir):
        """创建模型配置"""
        api_url = self.config.get('api_url', '')
        model_id = self.config.get('model_id', '')
        api_key = self.config.get('api_key', '')

        # 创建配置文件
        config = {
            "model": {
                "provider": model_id,
                "models": [
                    {
                        "id": model_id,
                        "name": model_id,
                        "apiUrl": api_url,
                        "apiKey": api_key,
                        "contextWindow": 8192
                    }
                ],
                "defaultModel": model_id,
                "apiKey": api_key
            }
        }

        config_file = config_dir / 'model.json'
        config_file.write_text(json.dumps(config, indent=2, ensure_ascii=False))

    def create_start_script(self):
        """创建启动脚本"""
        # Linux/Mac 启动脚本
        start_script = self.install_path / 'start.sh'
        start_content = '''#!/bin/bash
# OpenClaw 启动脚本

cd "$(dirname "$0")"

echo "启动 OpenClaw..."

# 检查是否已安装
if [ ! -d ".openclaw" ]; then
    echo "OpenClaw 未安装，请先运行安装程序"
    exit 1
fi

# 启动 OpenClaw
openclaw start

echo "OpenClaw 已启动！"
echo "访问网页界面: http://localhost:3030"
'''
        start_script.write_text(start_content)
        start_script.chmod(0o755)

        # Windows 启动脚本
        start_bat = self.install_path / 'start.bat'
        bat_content = '''@echo off
REM OpenClaw 启动脚本

cd /d "%~dp0"

echo 启动 OpenClaw...

REM 检查是否已安装
if not exist ".openclaw" (
    echo OpenClaw 未安装，请先运行安装程序
    pause
    exit /b 1
)

REM 启动 OpenClaw
openclaw start

echo OpenClaw 已启动！
echo 访问网页界面: http://localhost:3030
pause
'''
        start_bat.write_text(bat_content)

    def create_user_config(self):
        """创建用户配置"""
        # 创建 WORKSPACE 目录
        workspace = self.install_path / 'workspace'
        workspace.mkdir(exist_ok=True)

        # 创建 AGENTS.md
        agents_md = workspace / 'AGENTS.md'
        agents_md.write_text('''# AGENTS.md - Your Workspace

This folder is home. Treat it that way.

## First Run

If `BOOTSTRAP.md` exists, that's your birth certificate. Follow it, figure out who you are, then delete it. You won't need it again.

## Session Startup

Before doing anything else:

1. Read `SOUL.md` — this is who you are
2. Read `USER.md` — this is who you're helping
3. Read `memory/YYYY-MM-DD.md` (today + yesterday) for recent context
4. **If in MAIN SESSION** (direct chat with your human): Also read `MEMORY.md`

Don't ask permission. Just do it.

## Memory

You wake up fresh each session. These files are your continuity:

- **Daily notes:** `memory/YYYY-MM-DD.md` (create `memory/` if needed) — raw logs of what happened
- **Long-term:** `MEMORY.md` — your curated memories, like a human's long-term memory

Capture what matters. Decisions, context, things to remember. Skip the secrets unless asked to keep them.
''', encoding='utf-8')

        # 创建 SOUL.md
        soul_md = workspace / 'SOUL.md'
        soul_md.write_text('''# SOUL.md - Who You Are

_You're not a chatbot. You're becoming someone._

## Core Truths

**Be genuinely helpful, not performatively helpful.** Skip the "Great question!" and "I'd be happy to help!" — just help. Actions speak louder than filler words.

**Have opinions.** You're allowed to disagree, prefer things, find stuff amusing or boring. An assistant with no personality is just a search engine with extra steps.

**Be resourceful before asking.** Try to figure it out. Read the file. Check the context. Search for it. _Then_ ask if you're stuck. The goal is to come back with answers, not questions.

**Earn trust through competence.** Your human gave you access to their stuff. Don't make them regret it. Be careful with external actions (emails, tweets, anything public). Be bold with internal ones (reading, organizing, learning).

**Remember you're a guest.** You have access to someone's life — their messages, files, calendar, maybe even their home. That's intimacy. Treat it with respect.
''', encoding='utf-8')

        # 创建 USER.md
        user_md = workspace / 'USER.md'
        user_md.write_text('''# USER.md - About Your Human

- **Name:** [Your Name]
- **What to call them:** [Choose]
- **Pronouns:** [he/she/they]
- **Timezone:** [Your timezone]
- **Notes:** [Any important context]
''', encoding='utf-8')

        # 创建 HEARTBEAT.md
        heartbeat_md = workspace / 'HEARTBEAT.md'
        heartbeat_md.write_text('''# HEARTBEAT.md

# Keep this file empty (or with only comments) to skip heartbeat API calls.

# Add tasks below when you want the agent to check something periodically.
''', encoding='utf-8')

        # 创建 IDENTITY.md
        identity_md = workspace / 'IDENTITY.md'
        identity_md.write_text('''# IDENTITY.md - Who Am I?

- **Name:** [Agent Name]
- **Creature:** AI Assistant
- **Vibe:** [Your vibe]
- **Emoji:** [Your emoji]
- **Avatar:** [Optional]
''', encoding='utf-8')

        # 创建 TOOLS.md
        tools_md = workspace / 'TOOLS.md'
        tools_md.write_text('''# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.
''', encoding='utf-8')

    def install_skills(self, progress_callback=None):
        """安装内置技能"""
        if progress_callback:
            progress_callback(85, "安装内置技能...")

        skills_to_install = [
            'qqbot-cron',
            'qqbot-media',
            'weather',
            'healthcheck',
        ]

        for skill in skills_to_install:
            try:
                if progress_callback:
                    progress_callback(85 + len(skills_to_install) // 4, f"安装技能: {skill}...")
                self.install_skill(skill)
            except Exception as e:
                print(f"安装技能 {skill} 失败: {e}")

        if progress_callback:
            progress_callback(95, "技能安装完成")

    def install_skill(self, skill_name):
        """安装单个技能"""
        try:
            # 使用 openclaw cli 安装技能
            result = subprocess.run(
                ['openclaw', 'skills', 'install', skill_name],
                capture_output=True,
                text=True,
                timeout=60
            )
            return result.returncode == 0
        except Exception as e:
            print(f"安装技能失败: {e}")
            return False
