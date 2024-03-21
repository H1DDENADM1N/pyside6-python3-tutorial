import sqlite3
import pandas as pd
from faker import Faker
import os

# 切换到当前文件的目录
os.chdir(os.path.dirname(__file__))

# 创建一个Faker生成器，设置为中文区域
fake = Faker(locale='zh_CN')

# 生成包含50000条记录的假数据
# 每条记录包括姓名、地址和邮箱
data = pd.DataFrame([{'姓名': fake.name(), '地址': fake.address(), '邮箱': fake.email()} for _ in range(50000)])

# 连接到SQLite数据库，如果数据库不存在，会自动创建
connect = sqlite3.connect('test.db')

# 将数据写入SQLite数据库中的'user'表
# 如果表已经存在，则替换（删除并重新创建）
# 将DataFrame的索引作为数据库表的列
data.to_sql('user', connect, if_exists='replace', index=True)

# 关闭数据库连接
connect.close()
