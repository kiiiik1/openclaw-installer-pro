#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OpenClaw Installer Pro - 安装脚本
"""

from setuptools import setup, find_packages
import os

# 读取 README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# 读取依赖
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="openclaw-installer-pro",
    version="1.0.0",
    author="kiiiik1",
    author_email="kiiiik1@users.noreply.github.com",
    description="OpenClaw 一键部署工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kiiiik1/openclaw-installer-pro",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: System :: Installation/Setup",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "openclaw-installer=src.main:main",
        ],
    },
    include_package_data=True,
)
