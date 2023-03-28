# python 爬虫
## pip
### 源
* 默认源：https://files.pythonhosted.org/
* 其他源头下载方式：`pip install 包名 -i https://pypi.mirrors.ustc.edu.cn/simple/`
* 常用国内源：
  * 阿里云 https://mirros.aliyun.com/pypi/simple/
  * 豆瓣 https://pypi.douban.com/simple/
  * 清华 https://pypi.tuna.tsinghua.edu.cn/simple/
  * 中科大 https://pypi.mirrors.ustc.edu.cn/simple/
### 常用指令
1. `pip -V` 查看pip版本
2. `pip install 包名` 安装包
3. `pip uninstall 包名` 卸载包
4. `pip list` 显示安装的包
5. `pip freeze` 显示安装的包,更全面
## 基础知识
### 注释
1. `#` 单行注释
2. `'''`  多行注释  `'''`
### 变量类型
1. number【数据】
   1. int
   2. long(py2之前)
   3. double
   4. float
2. boolean【布尔】
3. string【字符串】
4. list【列表】
   * 命名形式 myList = [1,2,3]
5. tuple【元组】
   * 命名形式 myTuple = (1,2,3)
6. dict【字典】
   * 命名形式 myDict = {'name':'alisa', 'age':12}
### 运算符
#### 算数运算符
1. // 取整除 9//2==4
2. ** 指数 10**20 10的20次方
3. 字符串乘法，将字符串乘多少次
4. 字符串加法，‘123’+‘456’=‘123456’
#### 赋值运算符
1. 单个赋值  a = 1
2. 多个赋值  a = b = 1
3. 逗号赋值  a,b,c = 1,2,3
### 格式化输入输出
* 输出：%s 字符串占位，  %d 数值占位
### 流程控制语句
1. if：
    ``` python
      if age > 7:
         # if下面的代码必须是一个tab或者四个空格,四个空格相当于java的大括号了，可以一直往下续
         print('ok')
   ```
   2. if else
      ``` python
         if age > 7:
            # if下面的代码必须是一个tab或者四个空格,四个空格相当于java的大括号了，可以一直往下续
            print('ok')
         else:
            print('not ok')
      ```
      3. if elif
         ``` python
            if age > 7:
               # if下面的代码必须是一个tab或者四个空格,四个空格相当于java的大括号了，可以一直往下续
               print('ok')
            elif age < 1:
               print('not ok')
         ```
         4. for 循环
         ``` python
               # for 变量 in 待遍历数据:
               # 方法体
               s = 'abcde'
               for i in s:
                  print(i)
               # 打印 0-4
               for i in range(5):
                  print(i)
               # 打印 1-4
               for i in range(1,5):
                  print(i)
               # 打印 1,4,7  3为步长
               for i in range(1,10,3):
                  print(i)
               # 打印 1,4,7  3为步长
               a_list = ['a', 'b', 'c']
               for i in range(len(a_list)):
                  print(i)
               # 打印带下表，enumerate枚举
               a_list = ['a', 'b', 'c']
               for index, i in enumerate(a_list):
               print(index, i)
         ```
### 常用方法
1. 查看数据类型： type(变量名)
2. 类型转换：
   1. int(x)
      * `float -> int` 1.23 -> 1 取小数点前的整数，无关四舍五入
      * `bool -> int` true -> 1 &nbsp;  false -> 0
      * `str -> int` '1.23b' -> int 报错，非数字字符无法转换为整数
   2. float(x)
      * `int -> float`  111 -> 111.0
      * `str -> float ` '111.1' -> 111.1
   3. str(x)
      * `bool -> str`  True -> True &nbsp; 不是 True -> 1
   4. bool(x)
      * `int -> bool` 正负数 -> True &nbsp; 0 -> False
      * `float -> bool` 正负数 -> True &nbsp; 0 -> False
      * `str -> bool` 字符串中有内容 -> True &nbsp; 字符串中没有内容 -> False 
      * `list -> bool` 列表中有内容 -> True &nbsp; 列表中没有内容 -> False 
      * `tuple -> bool` 元组中有内容 -> True &nbsp; 元组中没有内容 -> False 
      * `dict -> bool` 字典中有内容 -> True &nbsp; 字典中没有内容 -> False 
3. 输入接收：`input('请输入一些内容')`
4. 字符串：
   1. len 获取字符串长度
   2. find 查找字符串中内容是否存在，在返回第一个找到的索引位置，不在返回-1
   3. startswith,endswith 判断是否开头结束
   4. count 计算次数
   5. replace 替换后返回替换的字符串
   6. split(x) 以x为切割线返回切割后的数组
   7. upper，lower 大小写互换
   8. strip 去空格，只能去字符串前后的空格
   9. join 字符串拼接, a.join(b) 将字符串a以一个整体中插入到b的每一个字符后面