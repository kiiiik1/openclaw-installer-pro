# 第16章：部署最佳实践

将 OpenClaw 部署到生产环境需要仔细的规划和配置。本章将详细介绍生产环境部署的最佳实践，包括配置优化、安全加固、性能调优和监控告警。

## 16.1 生产环境配置

### 16.1.1 系统要求

**硬件要求：**

**最小配置：**
- CPU: 2核
- 内存: 4GB
- 磁盘: 20GB SSD
- 网络: 10Mbps

**推荐配置：**
- CPU: 4核+
- 内存: 8GB+
- 磁盘: 50GB+ SSD
- 网络: 100Mbps+

**高性能配置：**
- CPU: 8核+
- 内存: 16GB+
- 磁盘: 100GB+ NVMe SSD
- 网络: 1Gbps+

**操作系统：**
- Ubuntu 20.04 LTS 或更高
- Debian 11 或更高
- CentOS 8 或更高
- 其他主流 Linux 发行版
- Windows Server（需要额外配置）

**软件要求：**
- Python 3.8+
- Docker（可选，用于容器化部署）
- Nginx（可选，用于反向代理）
- PostgreSQL（可选，用于数据持久化）
- Redis（可选，用于缓存）

### 16.1.2 网络配置

**端口配置：**

OpenClaw 默认使用以下端口：

```yaml
# config/network.yml
gateway:
  port: 8080              # Gateway API 端口
  metrics_port: 9090     # 监控指标端口
  health_port: 8081      # 健康检查端口

agent:
  port: 8082             # Agent 端口

skills:
  port: 8083             # 技能端口
```

**防火墙配置：**

```bash
# Ubuntu/Debian
sudo ufw allow 8080/tcp   # Gateway
sudo ufw allow 9090/tcp   # Metrics
sudo ufw allow 8081/tcp   # Health
sudo ufw enable

# CentOS/RHEL
sudo firewall-cmd --permanent --add-port=8080/tcp
sudo firewall-cmd --permanent --add-port=9090/tcp
sudo firewall-cmd --permanent --add-port=8081/tcp
sudo firewall-cmd --reload
```

**反向代理配置：**

使用 Nginx 作为反向代理：

```nginx
# /etc/nginx/conf.d/openclaw.conf

upstream openclaw_gateway {
    server 127.0.0.1:8080;
}

server {
    listen 80;
    server_name openclaw.yourdomain.com;

    # 重定向到 HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name openclaw.yourdomain.com;

    # SSL 证书
    ssl_certificate /etc/letsencrypt/live/openclaw.yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/openclaw.yourdomain.com/privkey.pem;

    # SSL 配置
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    # 代理配置
    location / {
        proxy_pass http://openclaw_gateway;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # 超时配置
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }

    # WebSocket 支持
    location /ws {
        proxy_pass http://openclaw_gateway;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

**获取 SSL 证书：**

```bash
# 使用 Certbot 获取免费证书
sudo apt-get install certbot python3-certbot-nginx
sudo certbot --nginx -d openclaw.yourdomain.com
```

### 16.1.3 数据库配置

**PostgreSQL 配置：**

```sql
-- 创建数据库
CREATE DATABASE openclaw;

-- 创建用户
CREATE USER openclaw_user WITH PASSWORD 'your_strong_password';

-- 授权
GRANT ALL PRIVILEGES ON DATABASE openclaw TO openclaw_user;

-- 退出
\q
```

**配置 OpenClaw 使用 PostgreSQL：**

```yaml
# config/database.yml
database:
  type: postgresql
  host: localhost
  port: 5432
  database: openclaw
  username: openclaw_user
  password: ${DB_PASSWORD}  # 从环境变量读取
  pool_size: 10
  max_overflow: 20

# 或在环境变量中设置
export DB_PASSWORD="your_strong_password"
```

**Redis 配置：**

```yaml
# config/cache.yml
cache:
  type: redis
  host: localhost
  port: 6379
  password: ${REDIS_PASSWORD}
  db: 0
  ttl: 3600
  max_memory: 256mb
```

### 16.1.4 日志配置

**日志级别：**
- **DEBUG**: 详细的调试信息（开发环境）
- **INFO**: 一般信息（生产环境推荐）
- **WARNING**: 警告信息
- **ERROR**: 错误信息
- **CRITICAL**: 严重错误

**日志配置：**

```yaml
# config/logging.yml
logging:
  version: 1
  disable_existing_loggers: false

  formatters:
    standard:
      format: '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
      datefmt: '%Y-%m-%d %H:%M:%S'

    json:
      class: 'pythonjsonlogger.jsonlogger.JsonFormatter'
      format: '%(asctime)s %(name)s %(levelname)s %(message)s'

  handlers:
    console:
      class: logging.StreamHandler
      level: INFO
      formatter: standard
      stream: ext://sys.stdout

    file:
      class: logging.handlers.RotatingFileHandler
      level: INFO
      formatter: standard
      filename: /var/log/openclaw/openclaw.log
      maxBytes: 10485760  # 10MB
      backupCount: 10

    error_file:
      class: logging.handlers.RotatingFileHandler
      level: ERROR
      formatter: standard
      filename: /var/log/openclaw/error.log
      maxBytes: 10485760  # 10MB
      backupCount: 10

  loggers:
    openclaw:
      level: INFO
      handlers: [console, file, error_file]
      propagate: false

    root:
      level: INFO
      handlers: [console]
```

**创建日志目录：**

```bash
sudo mkdir -p /var/log/openclaw
sudo chown openclaw:openclaw /var/log/openclaw
sudo chmod 755 /var/log/openclaw
```

## 16.2 安全配置

### 16.2.1 认证和授权

**API 密钥管理：**

```yaml
# config/security.yml
security:
  api_key:
    enabled: true
    header_name: X-API-Key
    keys:
      - name: main
        key: ${MAIN_API_KEY}
        permissions:
          - read
          - write
          - admin
      - name: limited
        key: ${LIMITED_API_KEY}
        permissions:
          - read

  jwt:
    enabled: true
    secret: ${JWT_SECRET}
    algorithm: HS256
    expiration: 3600  # 1小时
```

**环境变量存储敏感信息：**

```bash
# .env 文件
MAIN_API_KEY=your_main_api_key_here
LIMITED_API_KEY=your_limited_api_key_here
JWT_SECRET=your_jwt_secret_here
DB_PASSWORD=your_db_password_here
REDIS_PASSWORD=your_redis_password_here
OPENAI_API_KEY=your_openai_key_here

# 设置权限
chmod 600 .env
```

**生成安全的密钥：**

```bash
# 生成 API 密钥
openssl rand -hex 32

# 生成 JWT 密钥
openssl rand -base64 64
```

### 16.2.2 数据加密

**加密敏感数据：**

```yaml
# config/encryption.yml
encryption:
  enabled: true
  algorithm: AES-256-GCM
  key: ${ENCRYPTION_KEY}
  key_derivation:
    algorithm: PBKDF2
    iterations: 100000
    salt_length: 32
```

**加密数据库字段：**

```python
# 加密工具类
from cryptography.fernet import Fernet

class EncryptionManager:
    def __init__(self, key):
        self.cipher = Fernet(key)

    def encrypt(self, data):
        return self.cipher.encrypt(data.encode())

    def decrypt(self, encrypted_data):
        return self.cipher.decrypt(encrypted_data).decode()
```

### 16.2.3 访问控制

**IP 白名单：**

```yaml
# config/access_control.yml
access_control:
  ip_whitelist:
    enabled: true
    allowed_ips:
      - 192.168.1.0/24
      - 10.0.0.0/8
      - specific_ip_address

  rate_limiting:
    enabled: true
    requests_per_minute: 60
    requests_per_hour: 1000

  blocked_ips:
    - malicious_ip_address
```

**角色和权限：**

```yaml
# config/rbac.yml
rbac:
  enabled: true
  roles:
    admin:
      permissions:
        - "*"
      description: Full access

    user:
      permissions:
        - message:read
        - message:write
        - skill:execute
      description: Standard user access

    readonly:
      permissions:
        - message:read
      description: Read-only access
```

### 16.2.4 安全最佳实践

**1. 最小权限原则**
- 只授予必要的权限
- 定期审查权限
- 及时撤销不需要的权限

**2. 定期更新**
- 保持系统和依赖最新
- 及时应用安全补丁
- 定期更新 OpenClaw

**3. 监控和审计**
- 记录所有关键操作
- 监控异常行为
- 定期审计日志

**4. 备份和恢复**
- 定期备份配置和数据
- 测试恢复流程
- 保留多个备份版本

## 16.3 性能优化

### 16.3.1 并发配置

**Gateway 并发：**

```yaml
# config/gateway.yml
gateway:
  workers: 4
  max_connections: 100
  max_requests_per_worker: 1000
  connection_timeout: 60
  request_timeout: 120

  thread_pool:
    size: 20
    max_queue: 100
```

**Agent 并发：**

```yaml
# config/agent.yml
agent:
  max_concurrent_requests: 10
  request_timeout: 60
  retry:
    max_attempts: 3
    backoff: exponential
    initial_delay: 1
```

### 16.3.2 缓存策略

**多层缓存：**

```yaml
# config/cache.yml
cache:
  # L1 缓存：内存缓存
  l1:
    type: memory
    ttl: 60  # 60秒
    max_size: 1000

  # L2 缓存：Redis
  l2:
    type: redis
    host: localhost
    port: 6379
    ttl: 3600  # 1小时
    max_memory: 256mb

  # 缓存策略
  strategy:
    user_messages: l2
    agent_responses: l1
    skill_results: l2
    weather_data: l2  # ttl: 1800  # 30分钟
```

**缓存失效策略：**

```python
# 当数据更新时清除缓存
def update_user_data(user_id, data):
    # 更新数据
    db.update(user_id, data)

    # 清除缓存
    cache.delete(f"user:{user_id}")
```

### 16.3.3 资源限制

**内存限制：**

```yaml
# config/resources.yml
resources:
  memory:
    max_per_worker: 512MB
    max_total: 4GB

    gc:
      enabled: true
      threshold: 80  # 80% memory usage
```

**CPU 限制：**

```yaml
  cpu:
    max_per_worker: 50%
    max_total: 200%
```

**磁盘限制：**

```yaml
  disk:
    max_log_size: 10GB
    max_cache_size: 5GB
    monitor:
      enabled: true
      threshold: 80  # 80% disk usage
```

### 16.3.4 性能监控

**关键指标：**

```yaml
# config/metrics.yml
metrics:
  enabled: true
  port: 9090

  # 系统指标
  system:
    - cpu_usage
    - memory_usage
    - disk_usage
    - network_io

  # 应用指标
  application:
    - request_count
    - response_time
    - error_rate
    - cache_hit_rate

  # 业务指标
  business:
    - active_sessions
    - messages_processed
    - skills_executed
```

**Prometheus 集成：**

```python
# Prometheus metrics exporter
from prometheus_client import start_http_server, Counter, Histogram

request_count = Counter('openclaw_requests_total', 'Total requests')
response_time = Histogram('openclaw_response_time_seconds', 'Response time')

def process_request(request):
    request_count.inc()
    with response_time.time():
        # 处理请求
        pass
```

## 16.4 监控和告警

### 16.4.1 健康检查

**健康检查端点：**

```python
# health.py
import psutil
import requests

def check_health():
    checks = {
        'database': check_database(),
        'redis': check_redis(),
        'llm': check_llm(),
        'disk': check_disk(),
    }

    healthy = all(checks.values())
    status = 'healthy' if healthy else 'unhealthy'

    return {
        'status': status,
        'checks': checks,
        'timestamp': datetime.now().isoformat()
    }

def check_database():
    try:
        db.execute("SELECT 1")
        return True
    except:
        return False
```

**定期健康检查：**

```bash
# 添加到 crontab
*/5 * * * * curl -f http://localhost:8081/health || send_alert "Health check failed"
```

### 16.4.2 日志监控

**集中式日志管理：**

```yaml
# config/logging.yml
logging:
  outputs:
    - type: file
      path: /var/log/openclaw/openclaw.log

    - type: elasticsearch
      hosts:
        - elasticsearch:9200
      index: openclaw-logs

    - type: loki
      url: http://loki:3100/loki/api/v1/push
```

**错误日志告警：**

```python
# 监控 ERROR 日志
if level == 'ERROR':
    send_alert(f"Error in {logger}: {message}")
```

### 16.4.3 告警配置

**邮件告警：**

```yaml
# config/alerts.yml
alerts:
  email:
    enabled: true
    smtp_server: smtp.gmail.com
    smtp_port: 587
    username: your-email@gmail.com
    password: ${SMTP_PASSWORD}
    recipients:
      - admin@yourdomain.com

  rules:
    - name: high_error_rate
      condition: error_rate > 5%
      duration: 5m
      action: send_email

    - name: high_memory_usage
      condition: memory_usage > 90%
      duration: 2m
      action: send_email

    - name: service_down
      condition: health_check != 'healthy'
      action: send_email
```

**Slack 告警：**

```python
import requests

def send_slack_alert(message):
    webhook_url = "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
    payload = {"text": message}
    requests.post(webhook_url, json=payload)
```

### 16.4.4 仪表板

**Grafana 仪表板：**

```json
{
  "dashboard": {
    "title": "OpenClaw Dashboard",
    "panels": [
      {
        "title": "Request Rate",
        "targets": [
          {
            "expr": "rate(openclaw_requests_total[5m])"
          }
        ]
      },
      {
        "title": "Response Time",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, openclaw_response_time_seconds)"
          }
        ]
      },
      {
        "title": "Error Rate",
        "targets": [
          {
            "expr": "rate(openclaw_errors_total[5m])"
          }
        ]
      }
    ]
  }
}
```

## 16.5 容器化部署

### 16.5.1 Docker 配置

**Dockerfile：**

```dockerfile
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件
COPY requirements.txt .

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY . .

# 设置环境变量
ENV PYTHONUNBUFFERED=1
ENV OPENCLAW_LOG_LEVEL=INFO

# 暴露端口
EXPOSE 8080 9090 8081

# 启动命令
CMD ["python", "-m", "openclaw.gateway"]
```

**docker-compose.yml：**

```yaml
version: '3.8'

services:
  gateway:
    build: .
    ports:
      - "8080:8080"
      - "9090:9090"
      - "8081:8081"
    environment:
      - DB_PASSWORD=${DB_PASSWORD}
      - REDIS_PASSWORD=${REDIS_PASSWORD}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    volumes:
      - ./config:/app/config
      - ./logs:/var/log/openclaw
    depends_on:
      - postgres
      - redis
    restart: unless-stopped

  postgres:
    image: postgres:15
    environment:
      - POSTGRES_DB=openclaw
      - POSTGRES_USER=openclaw_user
      - POSTGRES_PASSWORD=${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    command: redis-server --requirepass ${REDIS_PASSWORD}
    volumes:
      - redis_data:/data
    restart: unless-stopped

  prometheus:
    image: prom/prometheus
    ports:
      - "9091:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    restart: unless-stopped

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
    volumes:
      - grafana_data:/var/lib/grafana
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:
  prometheus_data:
  grafana_data:
```

### 16.5.2 Kubernetes 部署

**部署配置：**

```yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: openclaw-gateway
spec:
  replicas: 3
  selector:
    matchLabels:
      app: openclaw-gateway
  template:
    metadata:
      labels:
        app: openclaw-gateway
    spec:
      containers:
      - name: gateway
        image: openclaw/gateway:latest
        ports:
        - containerPort: 8080
        - containerPort: 9090
        - containerPort: 8081
        env:
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: openclaw-secrets
              key: db-password
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: openclaw-secrets
              key: openai-api-key
        resources:
          requests:
            memory: "512Mi"
            cpu: "500m"
          limits:
            memory: "1Gi"
            cpu: "1000m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8081
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8081
          initialDelaySeconds: 5
          periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: openclaw-gateway
spec:
  selector:
    app: openclaw-gateway
  ports:
  - port: 8080
    targetPort: 8080
    name: http
  - port: 9090
    targetPort: 9090
    name: metrics
  - port: 8081
    targetPort: 8081
    name: health
  type: LoadBalancer
```

**Secret 配置：**

```yaml
# k8s/secrets.yaml
apiVersion: v1
kind: Secret
metadata:
  name: openclaw-secrets
type: Opaque
stringData:
  db-password: your-db-password
  redis-password: your-redis-password
  openai-api-key: your-openai-api-key
  jwt-secret: your-jwt-secret
```

## 总结

本章详细介绍了 OpenClaw 在生产环境部署的最佳实践，包括：

1. **生产环境配置**：系统要求、网络配置、数据库配置、日志配置
2. **安全配置**：认证授权、数据加密、访问控制、安全最佳实践
3. **性能优化**：并发配置、缓存策略、资源限制、性能监控
4. **监控告警**：健康检查、日志监控、告警配置、仪表板
5. **容器化部署**：Docker 配置、docker-compose、Kubernetes 部署

通过遵循这些最佳实践，你可以构建一个稳定、安全、高性能的 OpenClaw 生产环境。

下一章将介绍使用 OpenClaw 的最佳实践。
