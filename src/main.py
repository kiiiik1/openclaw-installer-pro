#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OpenClaw Installer Pro - 主程序
一键部署 OpenClaw 的图形化工具
"""

import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit, QProgressBar,
    QGroupBox, QMessageBox, QFileDialog, QTabWidget
)
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QFont, QIcon

from config import ConfigManager
from downloader import OpenClawDownloader
from installer import OpenClawInstaller


class InstallThread(QThread):
    """安装线程"""
    progress = pyqtSignal(int, str)  # 进度, 信息
    finished = pyqtSignal(bool, str)  # 成功/失败, 消息

    def __init__(self, config):
        super().__init__()
        self.config = config

    def run(self):
        try:
            self.progress.emit(10, "开始下载 OpenClaw...")

            # 下载 OpenClaw
            downloader = OpenClawDownloader(self.config)
            downloader.download(self.progress)

            self.progress.emit(60, "正在配置...")

            # 配置 OpenClaw
            installer = OpenClawInstaller(self.config)
            installer.install(self.progress)

            self.progress.emit(90, "正在安装技能...")

            # 安装内置技能
            installer.install_skills(self.progress)

            self.progress.emit(100, "安装完成！")
            self.finished.emit(True, "OpenClaw 安装成功！")

        except Exception as e:
            self.finished.emit(False, f"安装失败：{str(e)}")


class MainWindow(QMainWindow):
    """主窗口"""

    def __init__(self):
        super().__init__()
        self.config = ConfigManager()
        self.install_thread = None

        self.init_ui()

    def init_ui(self):
        """初始化界面"""
        self.setWindowTitle('OpenClaw Installer Pro')
        self.setMinimumSize(800, 600)

        # 主窗口部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 标题
        title_label = QLabel('OpenClaw 一键部署工具')
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title_label.setFont(title_font)
        layout.addWidget(title_label)

        # 创建选项卡
        tab_widget = QTabWidget()

        # 配置选项卡
        config_tab = self.create_config_tab()
        tab_widget.addTab(config_tab, "配置")

        # 文档选项卡
        doc_tab = self.create_doc_tab()
        tab_widget.addTab(doc_tab, "文档")

        layout.addWidget(tab_widget)

        # 进度条
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        layout.addWidget(self.progress_bar)

        # 日志输出
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setMaximumHeight(150)
        layout.addWidget(self.log_text)

        # 按钮区域
        button_layout = QHBoxLayout()

        self.install_btn = QPushButton('开始安装')
        self.install_btn.clicked.connect(self.start_install)
        self.install_btn.setEnabled(False)
        button_layout.addWidget(self.install_btn)

        self.close_btn = QPushButton('关闭')
        self.close_btn.clicked.connect(self.close)
        button_layout.addWidget(self.close_btn)

        layout.addLayout(button_layout)

        # 加载已保存的配置
        self.load_config()

    def create_config_tab(self):
        """创建配置选项卡"""
        widget = QWidget()
        layout = QVBoxLayout(widget)

        # 配置说明
        info_label = QLabel('只需填写以下3项即可使用，其他全部自动配置：')
        info_label.setStyleSheet("color: #666;")
        layout.addWidget(info_label)

        # 模型地址
        model_group = QGroupBox('模型配置')
        model_layout = QVBoxLayout()

        api_url_label = QLabel('模型地址 (API URL):')
        self.api_url_input = QLineEdit()
        self.api_url_input.setPlaceholderText('https://open.bigmodel.cn/api/paas/v4/chat/completions')
        self.api_url_input.textChanged.connect(self.check_config)
        model_layout.addWidget(api_url_label)
        model_layout.addWidget(self.api_url_input)

        model_id_label = QLabel('模型 ID:')
        self.model_id_input = QLineEdit()
        self.model_id_input.setPlaceholderText('glm-4')
        self.model_id_input.textChanged.connect(self.check_config)
        model_layout.addWidget(model_id_label)
        model_layout.addWidget(self.model_id_input)

        api_key_label = QLabel('API Key:')
        self.api_key_input = QLineEdit()
        self.api_key_input.setPlaceholderText('你的 API Key')
        self.api_key_input.textChanged.connect(self.check_config)
        model_layout.addWidget(api_key_label)
        model_layout.addWidget(self.api_key_input)

        model_group.setLayout(model_layout)
        layout.addWidget(model_group)

        # 安装路径
        path_group = QGroupBox('安装路径')
        path_layout = QHBoxLayout()

        self.install_path_input = QLineEdit()
        self.install_path_input.setText(os.path.expanduser('~/openclaw'))
        path_layout.addWidget(self.install_path_input)

        browse_btn = QPushButton('浏览...')
        browse_btn.clicked.connect(self.browse_path)
        path_layout.addWidget(browse_btn)

        path_group.setLayout(path_layout)
        layout.addWidget(path_group)

        # 代理设置（可选）
        proxy_group = QGroupBox('代理设置（可选）')
        proxy_layout = QHBoxLayout()

        proxy_label = QLabel('HTTP 代理:')
        self.proxy_input = QLineEdit()
        self.proxy_input.setPlaceholderText('http://192.168.48.1:7890')
        proxy_layout.addWidget(proxy_label)
        proxy_layout.addWidget(self.proxy_input)

        proxy_group.setLayout(proxy_layout)
        layout.addWidget(proxy_group)

        layout.addStretch()

        return widget

    def create_doc_tab(self):
        """创建文档选项卡"""
        widget = QWidget()
        layout = QVBoxLayout(widget)

        doc_text = QTextEdit()
        doc_text.setReadOnly(True)
        doc_text.setHtml("""
        <h2>使用说明</h2>

        <h3>1. 配置模型信息</h3>
        <p>在"配置"选项卡中填写你的大模型信息：</p>
        <ul>
            <li><b>模型地址</b>：大模型 API 的完整 URL</li>
            <li><b>模型 ID</b>：要使用的模型名称</li>
            <li><b>API Key</b>：你的访问密钥</li>
        </ul>

        <h3>2. 开始安装</h3>
        <p>点击"开始安装"按钮，程序会自动：</p>
        <ul>
            <li>下载 OpenClaw 最新版本</li>
            <li>配置模型和 API</li>
            <li>安装内置技能</li>
            <li>启动 OpenClaw 服务</li>
        </ul>

        <h3>3. 使用 OpenClaw</h3>
        <p>安装完成后，OpenClaw 会自动启动。你可以：</p>
        <ul>
            <li>通过网页界面访问 OpenClaw</li>
            <li>配置 QQ、微信等聊天平台</li>
            <li>添加你需要的技能</li>
        </ul>

        <h3>4. 内置技能</h3>
        <p>程序已内置以下技能：</p>
        <ul>
            <li><b>qqbot-cron</b> - QQ 定时提醒</li>
            <li><b>qqbot-media</b> - QQ 媒体收发</li>
            <li><b>weather</b> - 天气查询</li>
            <li><b>healthcheck</b> - 系统健康检查</li>
        </ul>

        <h3>常见问题</h3>
        <p><b>Q: 下载速度慢怎么办？</b><br>
        A: 在"代理设置"中配置代理，可以加速下载。</p>

        <p><b>Q: 支持哪些模型？</b><br>
        A: 支持所有兼容 OpenAI API 格式的大模型，如智谱 GLM、百度文心等。</p>

        <p><b>Q: 如何卸载？</b><br>
        A: 直接删除安装目录即可，不会有残留。</p>
        """)
        layout.addWidget(doc_text)

        return widget

    def browse_path(self):
        """浏览安装路径"""
        path = QFileDialog.getExistingDirectory(self, '选择安装目录')
        if path:
            self.install_path_input.setText(path)

    def check_config(self):
        """检查配置是否完整"""
        api_url = self.api_url_input.text().strip()
        model_id = self.model_id_input.text().strip()
        api_key = self.api_key_input.text().strip()

        self.install_btn.setEnabled(bool(api_url and model_id and api_key))

    def load_config(self):
        """加载已保存的配置"""
        config = self.config.load()
        self.api_url_input.setText(config.get('api_url', ''))
        self.model_id_input.setText(config.get('model_id', ''))
        self.api_key_input.setText(config.get('api_key', ''))
        self.install_path_input.setText(config.get('install_path', os.path.expanduser('~/openclaw')))
        self.proxy_input.setText(config.get('proxy', ''))
        self.check_config()

    def save_config(self):
        """保存配置"""
        config = {
            'api_url': self.api_url_input.text().strip(),
            'model_id': self.model_id_input.text().strip(),
            'api_key': self.api_key_input.text().strip(),
            'install_path': self.install_path_input.text().strip(),
            'proxy': self.proxy_input.text().strip(),
        }
        self.config.save(config)

    def start_install(self):
        """开始安装"""
        self.save_config()

        # 创建安装目录
        install_path = self.install_path_input.text().strip()
        if not os.path.exists(install_path):
            try:
                os.makedirs(install_path, exist_ok=True)
            except Exception as e:
                QMessageBox.critical(self, '错误', f'无法创建安装目录：{str(e)}')
                return

        # 禁用按钮
        self.install_btn.setEnabled(False)
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)

        # 启动安装线程
        self.install_thread = InstallThread(self.config.config)
        self.install_thread.progress.connect(self.on_progress)
        self.install_thread.finished.connect(self.on_finished)
        self.install_thread.start()

    def on_progress(self, value, message):
        """更新进度"""
        self.progress_bar.setValue(value)
        self.log_text.append(f"[{value}%] {message}")

    def on_finished(self, success, message):
        """安装完成"""
        self.install_btn.setEnabled(True)
        self.progress_bar.setValue(100)

        if success:
            QMessageBox.information(self, '成功', message)
            self.log_text.append('\n' + '='*50)
            self.log_text.append(message)
            self.log_text.append('='*50)
        else:
            QMessageBox.critical(self, '错误', message)
            self.log_text.append(f'\n错误：{message}')


def main():
    """主函数"""
    app = QApplication(sys.argv)
    app.setApplicationName('OpenClaw Installer Pro')

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
