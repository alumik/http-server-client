# 简易 http-server & http-client

项目基于 [Python](https://www.python.org/) 语言制作。

# 说明

## http-server

### 默认启动

默认启动将让服务器运行在 localhost:8080 ，网站根目录为 *./www/* 。

#### Windows

```
.\http-server
```

#### Linux

```
python ./http-server.py
```

### 带参数启动

使用以下命令自定义启动服务。

其中 `host` 为服务器地址， `server_port` 为服务器端口， `www_root` 为网站根目录。

```
python ./http-server.py <host> <server_port> <www_root>
```

## http-client

使用以下命令启动测试用客户端。

其中 `host` 为服务器地址， `server_port` 为服务器端口， `filename` 为要访问的文件。

```
python ./http-client.py <host> <server_port> <filename>
```
