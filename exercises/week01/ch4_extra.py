# 第4章 附加练习：字典添加键、删除键
sammy = {'username': 'sammy-shark', 'online': True, 'followers': 987}

# 1. 添加一个新键，再打印
sammy['location'] = 'Haikou'
print("添加键后：", sammy)

# 2. 删除 "online" 键值对，再打印
del sammy['online']
print("删除 online 后：", sammy)
