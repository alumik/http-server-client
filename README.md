# http-server & http-client

简易的 HTTP 服务器与客户端。

## http-server

### 默认启动

默认启动将让服务器运行在 localhost:8080 ，网站根目录为 *./web* 。

```
python ./http-server.py
```

### 带参数启动

```
python ./http-server.py <host> <port> <www_root>
```

其中 `host` 为服务器地址， `port` 为服务器端口， `www_root` 为网站根目录。

## http-client

```
python ./http-client.py <host> <port> <filename>
```

其中 `host` 为服务器地址， `port` 为服务器端口， `filename` 为要访问的文件。
