import yaml
import os

# 获取当前脚本所在文件夹路径
curpath = os.path.dirname(os.path.realpath(__file__))

# 获取yaml文件路径
yamlpath = os.path.join(curpath,"cfg.yaml")

# open方法打开直接读出来
file = open(yamlpath,"r",encoding="utf-8")
cfg = file.read()
print(type(cfg),cfg)  # 读出来是字符串

"""
Loader的几种加载方式: 
BaseLoader--仅加载最基本的YAML
SafeLoader--安全地加载YAML语言的子集。建议用于加载不受信任的输入。
FullLoader--加载完整的YAML语言。避免任意代码执行。这是当前（PyYAML 5.1）默认加载器调用 yaml.load(input)（发出警告后）。
UnsafeLoader--（也称为Loader向后兼容性）原始的Loader代码，可以通过不受信任的数据输入轻松利用。
"""

# 用load方法转字典 --把文件的内容读取出来
data = yaml.load(cfg,Loader=yaml.FullLoader)
print(type(data),data)

