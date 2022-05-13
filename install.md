# 1. 安装python环境

- 下载安装python3
- 安装virtualenv
```
python install virtualenv
python -m virtualenv venv
```
- 安装python环境
```
source venv/bin/activate
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip install -r requirement.txt

deactivate
```

```
lsof -i:8888
kill -9 PID
```

