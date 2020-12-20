# print("python") # 字符串
# print(123) # 整数
# print(True) # 布尔值
# print(()) # 元组
# print([]) # 数组
# print({}) # 字典
# print("python"+"haha") # 字符串的拼接
# print("python"*10) # 字符串的重复
# print(2<3)
# name="aa"

# print(type("呼呼"))
# print(type(123))
# print(type(12.12))
# print(type(True))
# print(type(()))
# print(type([]))

# print(type([]))
# print(type({}))

# print(name)
# a = input("请输入：") #a为字符串
# b= input("请输入：")  #b为字符串
# print("input获取内容",a+b) # 结果只是字符串的相加

# a = float( input("请输入：")) #a为小数
# b= float(input("请输入：")) #b为小数

# print("input获取内容",a+b) # 结果是小数的相加

# a = 'qweqweqweqwe'
# print(len(a))

# a = input("请输入内容1:")
# b = input("请输入内容2:")
# print("输出:",len(a)+len(b))

# # 元组,下标，从0开始编号
# a=(1,2,3,4,5,5,4,"haha")   #空的元祖
# # print(a[4])  #选择4的下标 0.1.2.3.4 //-1未倒置，显示为haha

# print(a.index("haha")) #多个重复值时搜索的是第一个
# print(a.count(5))# 统计某个值的数量

#二维元组

# b=(a,4,5,4,5,4)  #b里面有5个值
# print(b[0][1])  #二维元组的写法

#切片

# print(a[:4])
# print(a[4:6])  #左闭右开，左边取值后边不取，6的下标未取值
# print(a[6:7]) #前面不写表现从开始计数，后面不写表示到最后，都为空就是全部

#数组

# c=[1,2,3,4,5,5,4,"haha",False] #取数组也靠下标
# print(c[4])

#区别在于元组写好过后一定不可以修改，而数组是可以修改的

# c.append("append")
# print(c)
# c.index()
# c.count()
# c.insert(0,"insect") #0表示下标，该段表示把0
# print(c)

# d=c.pop(5)  #类似于剪切的作用
# f=c.pop(4)
# print(f+d)  #输入时发现haha不见了

# c.clear() 清空数组
# print(c)

# g= ["nihao","buhao"]
# # c.extend(g)
# print(c+g)

# c.remove("haha") #移除haha
# print(c)

# true==1 false==0
# f=[0,1,True,False]
# p=f.count(0)  
# y=f.count(1)
# print(p,y)

#  下标不要超出范围=越界

# xx=[1,2,3]
# print(xx[9])

"""

python的语法的一部分：

所有的方法都是小括号结尾，比如print()

元组，数组，字典的取值，都是用中括号，比如a[0]

元组，数组，字典的定义，分别是(),[],{}
"""

"""
字典的特点
1.字典中的值没有顺序
2.字典的结构必须是键值对的结构。 key：value
  取值是通过key去取这个value
3.相当于自定义下标
"""

# q = {"w1":"张三",5:"age","age":25}
# print(q[5])          #字典的取值，取值不存在时会报错
# q["wang"] = "jiahui" #字典的新增
# print(q["wang"])
# q["wang"] = "1997"   #字典的修改
# print(q["wang"])

# 字典的常用方法：get（取值）、pop（剪切）、update（更新）、value

# w = q.get("name") #字典的取值，取值不存在时会返回空值（None）
# print(w)
# w = q.pop("name") #字典的剪切
# print(w)
# print(q)

# q.update(name=111) #字典的新增
# print(q)
# q.update(w1=222) #字典的修改
# print(q)

#怎么看代码错误？  File "D:\python bao\github\wang\inde.py", line 131 //indx文件131行 

#数组和字典的删除：del

# del q["age"]
# print(q)

# del c[5]
# print(c)

