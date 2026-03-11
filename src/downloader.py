#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
下载器模块
负责下载 OpenClaw 及相关资源
"""

import os
import requests
from pathlib import Path


class OpenClawDownloader:
    """OpenClaw 下载器"""

    def __init__(self, config):
        self.config = config
        self.install_path = Path(config.get('install_path', '~/openclaw')).expanduser()
        self.proxy = config.get('proxy', '')

    def get_session(self):
        """创建会话，可选配置代理"""
        session = requests.Session()
        if self.proxy:
            session.proxies = {
                'http': self.proxy,
                'https': self.proxy,
            }
        return session

    def download_file(self, url, dest_path, progress_callback=None):
        """下载文件"""
        session = self.get_session()

        try:
            response = session.get(url, stream=True)
            response.raise_for_status()

            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0

            # 确保目标目录存在
            dest_path.parent.mkdir(parents=True, exist_ok=True)

            with open(dest_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)

                        if progress_callback and total_size > 0:
                            progress = int(downloaded / total_size * 100)
                            progress_callback(progress, f"下载中: {dest_path.name}")

            return True

        except Exception as e:
            raise Exception(f"下载失败: {str(e)}")

    def download_openclaw(self, progress_callback=None):
        """下载 OpenClaw"""
        # 这里使用 OpenClaw 的 GitHub releases
        # 实际上 OpenClaw 可能需要通过其他方式安装
        # 这里创建一个基础的安装脚本

        if progress_callback:
            progress_callback(10, "准备下载 OpenClaw...")

        # 创建安装脚本
        install_script_path = self.install_path / 'install.sh'
        install_script = '''#!/bin/bash
# OpenClaw 安装脚本

echo "开始安装 OpenClaw..."

# 检查系统
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "检测到 Linux 系统"
    curl -fsSL https://get.openclaw.ai | bash
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "检测到 macOS 系统"
    curl -fsSL https://get.openclaw.ai | bash
else
    echo "不支持的操作系统: $OSTYPE"
    exit 1
fi

echo "OpenClaw 安装完成！"
'''

        install_script_path.write_text(install_script)
        install_script_path.chmod(0o755)

        if progress_callback:
            progress_callback(30, "下载配置文件...")

        # 下载技能配置
        self.download_skills(progress_callback)

        return True

    def download_skills(self, progress_callback=None):
        """下载技能配置"""
        # 创建技能目录
        skills_dir = self.install_path / 'skills'
        skills_dir.mkdir(exist_ok=True)

        if progress_callback:
            progress_callback(35, "下载技能列表...")

        # 下载 GitHub 上的技能列表
        try:
            session = self.get_session()
            url = 'https://raw.githubusercontent.com/openclaw/awesome-openclaw-skills/main/README.md'
            response = session.get(url, timeout=10)

            if response.status_code == 200:
                skills_readme = skills_dir / 'README.md'
                skills_readme.write_text(response.text, encoding='utf-8')

                if progress_callback:
                    progress_callback(40, "技能列表下载完成")
        except Exception as e:
            print(f"下载技能列表失败: {e}")
            # 创建默认技能配置
            self.create_default_skills(skills_dir)

        # 从 Gitee 下载技能（国内更快）
        self.download_from_gitee(progress_callback)

    def download_from_gitee(self, progress_callback=None):
        """从 Gitee 下载技能"""
        try:
            session = self.get_session()
            url = 'https://gitee.com/devai/awesome-openclaw-skills/raw/main/README.md'
            response = session.get(url, timeout=10)

            if response.status_code == 200:
                skills_dir = self.install_path / 'skills'
                gitee_readme = skills_dir / 'gitee-skills.md'
                gitee_readme.write_text(response.text, encoding='utf-8')

                if progress_callback:
                    progress_callback(45, "Gitee 技能列表下载完成")
        except Exception as e:
            print(f"从 Gitee 下载失败: {e}")

    def create_default_skills(self, skills_dir):
        """创建默认技能配置"""
        default_skills = skills_dir / 'default-skills.md'
        default_skills.write_text('''# OpenClaw 默认技能

## qqbot-cron
QQBot 定时提醒技能。支持一次性和周期性提醒的创建、查询、取消。

## qqbot-media
QQBot 图片/语音/视频/文件收发能力。

## weather
获取当前天气和天气预报。

## healthcheck
系统安全加固和风险配置。

## 使用方法
这些技能会在 OpenClaw 安装时自动安装。
''', encoding='utf-8')

    def download(self, progress_callback=None):
        """下载所有需要的文件"""
        self.download_openclaw(progress_callback)
