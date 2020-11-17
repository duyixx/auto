## adb shell
- 进入了一个 linux 系统
- android系统 是基于 linux 系统开发
- 进入了我们连接的手机系统

## appium 是基于 selenium 实现的
selenium 在源码层面是怎么完成客户端到服务端的

Chrome()

```python
from appium import webdriver

# 初始化客户端
caps = {
    "platformName": "Android",
    "deviceName": "774a0b78",
    "app": r"D:\Pythonauto\Python_Workspace\web\加密\工具和环境\app环境\应用apk包\Future-release-2018.apk"  # 可以是本地app文件地址，可以是url下载地址(会自动下载安装)
}
driver = webdriver.Remote(
    command_executor = "http://127.0.0.1:4723/wd/hub",  # appium server 的接口地址
    desired_capabilities = caps

)
```


## 元素定位
- app 当中属性名是固定的，所有的元素都具备这些属性，
id, class, content-desc, clickable, checkable, 都在辅助工具会显示的。

- id 可以不唯一， web 当中 id 是唯一。
- class 是表示组件的名称，类似于 web 当中 tagname,
在 app 自动化测试当中，很少用单独的 class 定位


# 如何选择元素定位方式。
- id, 确认什么时候唯一， inpect 查找元素。

- content-desc 元素标识， 经常没有。

- uiautomator 原生定位方式

- xpath (相对路径，一般用。手机解析页面素速度比较慢)
