# 错误、调试和测试
## 错误处理

* try ... except ... finally ...
* 所有的错误类型都继承自 BaseException
* 调用栈
* 记录错误 logging 模块
* 错误是class 用raise语句抛出一个错误的实例

## 调试

* 断言 assert
* logging 记录信息的级别
* pdb 单步
* pdb.set_trace() 断点
* IDE VS Code 安装插件  PyCharm

## 单元测试

* unittest 模块
* 编写测试类，从 nittest.TestCase继承
* 以 test 开头的方法是测试方法，不以 test 开头测试时不会被执行
* 断言 assertEqual()
* 命令行参数 -m unittest 直接运行测试单元

## 文档测试

* doctest 模块可以直接提取注释中的代码并执行测试

# IO编程
## 文件读写

* open(),read(),close()
* IOError    try ... finally
* with 语句
* 二进制文件，图片，视频，'rb'模式打开
* open()传入encoding

## StringIO和BytesIO

* StringIO 在内存中读写str，getvalue()用于获得写入的str
* BytesIO 在内存中读写bytes

## 操作文件和目录

* os模块
* os.name
* os.environ 环境变量
* os.path 模块
* os.path.join('','')
* os.path.split('') 把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
* os.path.splitext('')得到文件扩展名

## 序列化

* 变量从内存中变为可储存或者传输的过程称之为序列化
* pickle模块
* json模块
