# letian

#### 介绍
乐天项目

#### 软件架构
- python
- django
- html
- css
- javascript
- ajax


#### 安装教程

- 安装以下模块：
    - pymysql
    - django(我的是5.0)

- 配置好MySQL(我的是8.0)
    - 创建一个数据库名为 "letian" 的数据库  ``create database letian;``
    - 在web -> static -> 数据库文件 -> 中有一个名为：``letian.sql`` 的数据库，请将其导入进你的 letian 数据库中，导入代码： ``mysql -u账号 -p密码 letian<letian.sql的路径`` 如果出现以下提示则代表导入成功：`mysql: [Warning] Using a password on the command line interface can be insecure.`
  
- 当以上步骤操作完成后
    - 输入：`python3 manage.py runserver` 运行即可



#### 已知问题
- 无


#### 发现的消耗代码(目前技术不够无法解决)
 - 我的文档代码：255行


#### 本次更新
- 修复了已知BUG：
    - 错误代码1：用户在中奖后账号无法收取资金

- 完善了一些功能


#### 使用说明
- 安装Django    ``pip install django``
- 安装pymysql   ``pip install pymysql``
- 把 web -> static -> 数据库文件 -> letian.sql  中的数据全部导入到你的mysql数据库中(前提你的数据库名称也是letian)
    - 导入命令：source letian.sql路径
当以上步骤操作完成后直接运行一下命令将项目跑起来：``python3 manage.py runserver 20001``

#### 注意事项
- 请无论如何都要在 web_open_shengxiao(开奖表) 表中留有一行数据，否则项目会报错

##### Mysql的导入与导出
- 导出： -> mysqldump -u root -p letian > O:\letian\web\static\数据库文件\letian.sql
- 导入:  -> mysql -u账号 -p密码 letian<letian.sql的路径

##### PIP永久清华源
>  pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple 
#### 参与贡献

1. yy



