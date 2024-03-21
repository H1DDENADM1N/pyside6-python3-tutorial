import sqlite3
import pandas as pd
from pypinyin import lazy_pinyin
import os

# 切换到当前文件的目录
os.chdir(os.path.dirname(__file__))

# 连接到SQLite数据库，如果数据库不存在，会自动创建
connect = sqlite3.connect('test.db')
# 读取数据到 pandas DataFrame
data = pd.read_sql_query("SELECT * FROM user", connect)

# 为每个中文文本生成拼音
data['xingming'] = data['姓名'].apply(lambda x: ' '.join(lazy_pinyin(x)))

# 将处理后的数据存入新的表
data.to_sql('user_with_pinyin', connect, if_exists='replace', index=False)

# 关闭数据库连接
connect.close()