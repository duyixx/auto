## 逻辑封装

（浏览器操作、页面共用操作、功能业务测试操作）

- 测试代码和   页面操作 分开了。
  - 1. 通用：查找元素：def find(locator) →common包里面
       - 浏览器操作：def browser()→common包里面
  - 2. 业务代码通用操作：def login(username, pwd)→middlewares包里面
    3. 测试代码：def invert()→tests包里面
- PageObjectModel   页面对象模型
  - 登录的操作放在了一个类当中，初始化了 LoginPage 对象。
    - 优点：前端改了登录页面，只需要更改middlewares/pages/login.py这个共用的登录模块即可；
    - 其他业务测试代码（如test_invert.py）是直接调用login.py中的类的，所以不需要做修改。

## PageObject

### 定义层
- PageObject 页面对象（把页面（app页面）封装成对象）。 
- 对象
    - 属性： 元素定位器， URL ， 标题， （DOM对象→python对象）
    - 方法： 如元素定位、点击：（做了某个动作，执行了某系列操作，可以封装成一个方法）
      - 动作：由多个操作组合起来，每个操作可以进一步单独封装成动作，但可能并不必要
      - 获取页面中的数据，也是


### po定义层设计原则
- 不是所有的动作都需单独封装成页面对象的方法。
    - 可以封装但不必要这么做。
    - 遵循的原则：
      - 用到什么行为就封装什么行为。
      - 根据需要考虑行为的颗粒度，做好分层：可以重复封装行为，按需使用，但要注意方法间的依赖性进行调用
      - 定义层要避开框架属性
- 封装的页面操作的返回值→封装可以复杂，调用要简单
    - 通常返回self，或者是其他的页面对象、某个属性值
        - 如果你需要获取某个元素或者属性，就直接返回元素本身或者属性。
        - 如果一个操作它可能会有多个结果，比如结果是页面跳转或者返还本页面。需要根据结果返还不同页面，封装成多个方法（login→login_success、login_fail）：
            - 返回其他页面的好处：不需要在test方法中再初始化其他页面（实例化其他页面）
            - 返回self(本页面)：链式操作

    
### PO模式的好处
- 可维护性：
  - 前端修改了元素属性，可以只维护pageObject而不修改测试逻辑
- 可读性。
  - PO封装函数名或者类名具有注释说明的功能，体现了操作
  - pageObject对象中可以给方法加上注释，说明传参和返回值意义。这些注释在调用方法时可复用
  - 非常复杂的逻辑才需要在po调用层注释说明，不然一般在po定义层做注释（因为方法名、属性名已经做了解释）
- 易扩展性和可复用性
  - 易扩展性：有新功能、新需求需要实现，只需扩展po的属性和方法、新增po对象；
  - 可复用性：
    - 没有改动的操作逻辑>已封装的方法可复用；
    - 没有改动html属性的界面元素>已封装的定义层可复用
- 易维护性（项目迭代时）
  - 页面操作逻辑和测试操作逻辑的分离
    - po定义层：页面元素定义规则的封装(locator属性)；页面操作行为的封装(方法)；
    - po调用层：测试操作（一系列页面操作的有序调用集合）

## 测试用例代码的编写
0. 夹具、数据、标记

	```python
		@pytest.mark.parametrize("test_info",test_data)
		@pytest.mark.success
		def test_login_success(self,test_info,driver,logger)
	```
1. 初始化要用到的页面和数据

	```python
		login_page = LoginPage(driver)
	```

2. 逻辑有序的链式调用页面操作，获取实际结果

    ```python
	actual = login_page.login_success(test_info["test_data"]).get_account_name()
    ```
    
3. 断言

	```python
		try:
			assert actual == test_info["expected"]
		except AssertionError as e:
			logger.error("fail：测试用例不通过")   
			raise e
	```


## 数据分组
分组的原因：

- 和接口测试不同，ui测试的步骤繁多且各有区别，每个用例对应的步骤如果不同，数据也会不同，从而需要分组
- ui测试分正常流和异常流，测试步骤（po调用层代码）会不一样、测试数据也不一样

- 什么情况下需要分组？：用例的测试步骤（po调用层代码）不一致
  

分组的逻辑：
  - 一组步骤一组数据
  
  - 可以根据测试用例分类，把数据分组。

分组的方法：
  - 可以通过切片，根据title分组；
  - 可以通过表格直接对原始测试数据通过表单分组。
  - 也可以一个模块用一个excel文件分组
  - py文件管理测试数据：一个文件—一个功能模块：一个列表—一套操作步骤的数据；一个字典—一个用例
  - yaml同理


保存用例，建议不要通过excel 去管理，可以用py文件或者yaml文件直接准备数据
- py文件：
- yaml文件, 也支持字典的格式，

## locator 分层

- 元组形式的locator用*拆包，字典形式的locator用**拆包
  - driver.find_element(by=By.ID, value=None)

    - driver.find_element(**self.locator)
    - driver.find_element(*self.locator)
- 好处：前端修改元素属性后，只需维护PO定义层的locator
  
    

## web自动化图形化操作：

- selenium IDE
- katalon studio

