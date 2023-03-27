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