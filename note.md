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
   * 特点：
     * 元组内元素不能修改，列表可以
     * `tuple = (1)`当只有一个元素时，元组变为整形，需要类型为元组，则以 `tuple = (1,)` 形式来命名
6. dict【字典】
   * 命名形式 myDict = {'name':'alisa', 'age':12}
#### 局部变量与全局变量
* 局部变量：
  * 定义：函数内部定义的变量
  * 特点：作用域为函数内部，不可作用与函数外部
* 全局变量：
  * 定义：函数外部定义的变量
  * 特点：既可以在函数内部也可以在外部使用
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
         
### 函数
#### 定义
def 函数名(arg1, arg2):
   代码块
#### 参数
1. def 函数名(arg1, arg2):
   代码块
2. ``` python
   # 自由的python
   def 函数名(arg2 = 1, arg1 = 2):
   代码块
   ```
#### 返回值
   ``` python
   def 函数名(arg2 = 1, arg1 = 2):
      return result
   ```
### 文件
#### 文件的读写
##### 文件的读
* 语法
  * `变量fp = open('路径',操作)`  操作为`'r','w','a'`等
  * `content = fp.read` 或者`content = fp.readline` 或者 `content = fp.readlines`
##### 文件的写
* 语法： 
  * `变量fp = open('路径',操作)`  操作为`'r','w','a'`等
  * fp.write('')
  * fp.close
  * a操作为追加
#### 文件的序列化和反序列化
* 背景：默认情况下，对象不能被序列化到文件中
* 序列化
  * 方式：
    1. dumps() 
       * 步骤：
         1. import json
         2. fp = open('路径',操作)
         3. o = json.dumps(object)
         4. fp.write(o)
         5. fp.close
    2. dump()
       * 步骤：
         1. import json
         2. fp = open('路径',操作)
         3. json.dump(object, fp)
         4. 一步到位
* 反序列化
  * 方式：
    * 方式：
      1. loads() 
         * 步骤：
           1. import json
           2. fp = open('路径',操作)
           3. content = fp.read()
           4. result = json.loads(content)
      2. load()
         * 步骤：
           1. import json
           2. fp = open('路径',操作)
           3. result = json.load(fp)
           4. 一步到位
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
   1. `len` 获取字符串长度
   2. `find` 查找字符串中内容是否存在，在返回第一个找到的索引位置，不在返回-1
   3. `startswith,endswith` 判断是否开头结束
   4. `count` 计算次数
   5. `replace` 替换后返回替换的字符串
   6. `split(x)` 以x为切割线返回切割后的数组
   7. `upper，lower` 大小写互换
   8. `strip` 去空格，只能去字符串前后的空格
   9. `join` 字符串拼接, a.join(b) 将字符串a以一个整体中插入到b的每一个字符后面
5. 数组
   1. `list.append(object)` 在列表最后面插入数据
   2. `list.insert(index, object)` 在指定位置插入数据
   3. `list.extend(list2)` 将一个列表的元素逐个插入另一个列表中
   4. `a in list` 判断a在list，返回true
   5. `a not in list` 判断a不在list，返回true
   6. `del list[index]` 根据下标删除列表数据
   7. `list.pop()` 删除列表最后一个数据
   8. `list.remove(object)` 根据内容删除列表内数据
   9. 切片
      1. `s[0]` 字符串第1个元素
      2. `s[1:5]` 截取[1，5)的元素
      3. `s[1:]` 截取[1, s.len()) 的元素
      4. `s[:5]` 截取[0, 5) 的元素
      5. `s[1:5:2]` 截取[1，5) 每隔2个位置的元素
6. 字典
   1. `dict[keyValue]` 字典存在以keyValue为key的值则返回值，不存在报错
   2. `dict.get(keyValue)` 字典存在以keyValue为key的值则返回值，不存在返回None
   3. `dict[keyValue] = newData` 修改值，get方式不可以修改
   4. `dict[newkeyValue] = Data` 添加值
   5. `del dict[keyValue]`  删除key为keyValue的值
   6. `del dict`  删除整个字典
   7. `dict.clear()` 清空整个字典
   8. ``` python
      # 遍历key
       myDict = {'name':'alisa', 'age':12}
       for key in myDict.keys():
          print(key)
      ```
   9. ``` python
      # 遍历value
       myDict = {'name':'alisa', 'age':12}
       for value in myDict.values():
          print(value)
      ```
   10. ```  python
       # 遍历key, value
       myDict = {'name':'alisa', 'age':12}
       for 遍历key,value in myDict.items():
          print(key, value)
       # 打印项， ('name','alisa')即为项
       for 遍历key,value in myDict.items():
          print(key)
       ```
