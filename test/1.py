import akshare as ak
import re
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
futures_comm_info_df = ak.futures_comm_info(symbol="所有")
# print(futures_comm_info_df[['合约代码','备注','每跳毛利']])

# 关键字列表
keywords = ['sa','fg','i','p','ao','sh','sp','rb','ta']
date_keywords = ['01','03', '05','07', '09', '10', '11']

# 构造正则，匹配开头是列表中任意一个字母 + 4位数字
futures_comm_info_df['字母前缀'] = futures_comm_info_df['合约代码'].str.replace(r'\d', '', regex=True).str.lower()
futures_comm_info_df['数字后缀'] = futures_comm_info_df['合约代码'].str[-2:]
result = futures_comm_info_df[(futures_comm_info_df['字母前缀'].isin(keywords)) & (futures_comm_info_df['数字后缀'].isin(date_keywords)) & (futures_comm_info_df['备注'] == '主力合约')]


# print(futures_comm_info_df['合约代码'])
print(result[['合约名称','合约代码','手续费','保证金-每手','保证金-买开','价格更新时间','备注']])