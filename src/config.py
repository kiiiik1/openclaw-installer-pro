#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置管理模块
负责保存和加载用户配置
"""

import os
import json
from pathlib import Path


class ConfigManager:
    """配置管理器"""

    def __init__(self, config_path=None):
        if config_path:
            self.config_path = Path(config_path)
        else:
            # 默认配置文件位置
            home = Path.home()
            self.config_path = home / '.openclaw-installer' / 'config.json'

        self.config_dir = self.config_path.parent
        self.config = {}

        # 确保配置目录存在
        self.config_dir.mkdir(parents=True, exist_ok=True)

    def load(self):
        """加载配置"""
        if self.config_path.exists():
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    self.config = json.load(f)
            except Exception as e:
                print(f"加载配置失败: {e}")
                self.config = {}
        return self.config

    def save(self, config):
        """保存配置"""
        self.config = config
        try:
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"保存配置失败: {e}")
            return False

    def get(self, key, default=None):
        """获取配置项"""
        return self.config.get(key, default)

    def set(self, key, value):
        """设置配置项"""
        self.config[key] = value
        return self.save(self.config)

    def get_install_path(self):
        """获取安装路径"""
        path = self.config.get('install_path', '')
        if not path:
            path = os.path.expanduser('~/openclaw')
        return os.path.expanduser(path)

    def get_api_config(self):
        """获取 API 配置"""
        return {
            'api_url': self.config.get('api_url', ''),
            'model_id': self.config.get('model_id', ''),
            'api_key': self.config.get('api_key', ''),
        }

    def get_proxy(self):
        """获取代理配置"""
        return self.config.get('proxy', '')
