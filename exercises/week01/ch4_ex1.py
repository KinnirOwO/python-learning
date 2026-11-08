# 第4章 练习1：列表操作
names = ['John', 'Allen', 'Black', 'Raj', 'Krish', 'Peter', 'Mike']
print("原列表：", names)

# 1. 在列表末尾添加 "安"
names.append("安")
print("append 后：", names)

# 2. 在索引 3 的位置插入 "Ricky"
names.insert(3, "Ricky")
print("insert 后：", names)

# 3. 打印 "Peter" 的索引
print("Peter 的索引：", names.index("Peter"))
