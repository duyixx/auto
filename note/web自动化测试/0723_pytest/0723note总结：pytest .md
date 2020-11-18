## pytest 特性

### 标记 mark

- 注册一个标签：pytest.ini

 ```python
[pytest]
markers =
    success122
    fail
    
log_format = %(asctime)s %(levelname)s %(message)s
log_date_format = %Y-%m-%d %H:%M:%S
 ```

 

- 标记测试函数/测试方法/测试类
  - @pytest.mark.tagname    标记
  - 标记整个类，则在类上面加 @pytest.mark

- 调用被标记用例 
  - pytest -m "tagname"    运行标记的用例
  - 调用被标记用例时，如果要有逻辑运算的标记，要加双引号
    - and  必须同时具备两个标签
    - or  只需要满足其中的一个标签，就会运行
    - not    "success and not demo"


### 数据驱动
```python
# unitest：
@ddt.ddt
class TestClass()....
	@ddt.data(*test_data_list)
	def  test_fangfa（self, test_info）
		pass

# pytest: data_list=[{}, {}, {}]
class TestClass()...
	@pytest.mark.paramatrize("**test_info**", data_list):
	def test_demo(**test_info**):
		pass
```
#### 数据驱动注意事项
在使用pytest.mark.paramatrize 做数据驱动的时候，pytest 和 unittest 不兼容：

- 如果使用 pytest 的数据驱动装饰器，测试类不能继承 unittest.TestCase，否则就需要用ddt做数据驱动。同时断言也不能用unitest的断言self.assert，需要使用Python自带的assert
- 如果要使用unittest写用例,  就要用 unittest 的数据驱动ddt



### 断言

pytest的断言可以直接使用的 python 内置的关键字 assert



### 测试夹具

- 普通函数

- @pytest.fixture() 声明这是一个测试夹具

- 把 return 改成 yield 实现前置和后置
    - yield 前就是前置
    - yield 后的就是后置
    
- 后置清理语句放在 yield 之后。返回值跟在yield之后

    ```
    # 测试夹具定义
    @pytest.fixture(scope="function")  # 表setUp和tearDown，测试方法、函数前后执行
    # @pytest.fixture(scope="class")  # 表setUpClass、tearDownClass，测试类前后去执行
    # @pytest.fixture(scope="module")  # 模块运行前后执行
    def fixtrue_driver():
        """管理浏览器"""
        # 前置条件:打开浏览器
        from selenium import webdriver
        driver = webdriver.Chrome()
        driver.implicitly_wait(Handler.yaml["selenium"]["wait_time"])
        # driver.implicitly_wait(WAIT_TIME)
        yield driver
    	# 后置条件
        driver.quit()
        
    # 测试夹具使用：作为测试方法的形参根据scope值不同，该方法所属类、所属模块会在运行前后执行夹具代码 
    def test_login_error(self, test_info, fixtrue_driver)
    	fixtrue_driver.find.......
    	
    # 架构：所有测试夹具放在conftest.py文件中，pytest调用夹具时会自己从该文件中获取相应代码
    
    ```
    

## pytest运行

```
# cmd运行：
pytest
	--reruns 2 --reruns-delay 5 
	-m error_test11 
	-s 
	--html=ceshi.html

# ide内使用脚本运行：
pytest.main(["--reruns","2","--reruns-delay", "5",
	"-m error_test11", 
	"-s", 
	"--html=ceshi.html"])

# 参数说明：pytest插件库：http://plugincompat.herokuapp.com

# 捕获所有输出（如print()）:-s, 不加的话输出信息就不会显示
pytest.main(["--html={}.html".format(ts), "-m demo","-s"])

# 测试报告
安装模块：pip install pytest-html
使用：pytest -m "demo and not smoke" --html=report.html

# 重运行
安装：pip install pytest-rerunfailures
调用： --reruns reruntimes    --reruns-delay delaytime
pytest --reruns 2 --reruns-delay 5
pytest.main(["--reruns","5"])

```

## 认知

### pytest 两个功能不能和unittest兼容

- paramatrize  数据驱动

- fixture  测试夹具

- hook

  此外都是兼容的

### pytest 和 unittest 共用

- unittest 去编写用例
  - ddt
  - setUptearDown
  - self.assertTrue()

- pytest 运行用例
  - 自动收集
  - 用例筛选
  - 测试报告
  - 测试插件

### pytest和unittest的优劣

“unittest 过时了，pytest 才是王道”？

- unittest是标准库
  - 不需要安装；标准库不存在和 python 版本不兼容的问题。 
- pytest是三方库
  - 好用；但存在更新修复bug不及时，与Python版本不兼容的问题