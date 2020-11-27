# Appium介绍

Appium是一个开源的自动化框架爱，可以与native、hybird、webapp一起使用

它使用WebDriver协议驱动IOS、Android应用和Windows、Mac的桌面应用程序



- 原生：手机西戎原生的组件和原生的开发语言实现的app
  - Android：java、kotlin
  - Ios：oc、swift
- web
  - HTML、css、JS
- Hybird
  - Native和web整合到一起



## 支持的平台

- ios
  - xcuitest
- Android
  - UIautomator2 ： 原生的自动化测试四框架爱
  - Espresso
  - 命令：adb shell uiautomator --help
- Windows
  - WinAPPDriver
  - Windows开始教程
- Mac
  - Mac Driver（https://github.com/appium/appium/blob/master/docs/en/drivers/mac.md）
- web端
  - 移动web页面



## 设计哲学

- 开源
- 跨平台
- 多语言
  - 没有必要为了自动化而重新编译应用或以任何方式修改它
    - 使用Android/IOS系统自带的自动化框架
      - Android→这个框架装在adt里面
  - 不应该限制咋斯特丁的语言或框架上来编写运行测试
    - API调用
  - 移动端自动化框架在自动化接口方面不应该重造轮子
    - 使用WebDriver提供的接口
  - 移动端自动化框架应该开源：不仅在名义上而且在精神和时间上都要实至名归



## 使用的协议：

- webdriver的[Json wire protocol](https://w3c.github.io/webdriver/)

  - webdriver提供了操作浏览器的接口，但没有提供操作手机的接口

- WebDriver已成为自动化Web浏览器的行业标准，并且是W3C工作草案

- Appium在webdriver上提出了[Mobile Json Wire Protocol](https://github.com/SeleniumHQ/mobile-Spec/blob/master/spec-draft.md)

  - appium在webdriver基础上封装了更多对移动端系统的操作接口

    - web原代码是HTML的，但app的原代码通常是xml，两者解析规则不一样
    - 触屏操作
    - 定位、旋屏等等

    

## 流程和原理（课堂94）

- 参考selenium原理

- 原理：selenium代码→webdriver/appium提供的接口→驱动JSAPI操作浏览器/调用adb、

  uiautomator2操作手机系统

- ![image-20200902225741978](D:\Pythonauto\Python_Workspace\web\加密\app自动化\image-20200902225741978.png)

![image-20200902231140412](D:\Pythonauto\Python_Workspace\web\加密\app自动化\image-20200902230706418.png)



## 支持的自动化测试框架

- IOS9.3: Apple [XCUITest](https://developer.apple.com/documentation/xctest)    比较通用
- IOS9.3以下：Apple's UIAutomation
- Android4.3+ Google's UIAutomator/Uiautomator2
- Windows：[Microsoft's WinAPPDriver](https://github.com/microsoft/winappdriver)
- Espresso：安卓测试
- [Mac Driver](http://appium.io/docs/en/drivers/mac/)

## Appium资料

- Appium pro https://appiumpro.com/editions

- Appium Python Docs https://appium.github.io/python-client-sphinx



### Desired Capabilities

[appium初始化参数](https://appium.io/docs/en/writing-running-appium/caps)：

- automationName    自动化测试的引擎      默认值为  Appium 或者 Selendroid

- platformName     使用的手机操作系统              IOS   Android     Firefox05

- platformVersion    手机系统的版本                  如 7.1, 4.4，不需要进行进一步的安全校验，就不需要填

- APP         本地绝对路径   或 远程http url 指向的一个安装板（.ipa   .apk   .zip）
  - 指定AppPackage、AppActivity的话，此参数将不可用
  - 与browSerName不兼容：浏览器名称
- noreset：每次重启应用不清除缓存
- chromedriverExecutableDir    混合应用要提供浏览器驱动
- unicodeKeyboard      中文键盘
- resetKeyboard           重置键盘为UnicodeKeyboard

- autoGrantPermissions         自动授权
- autoWebview        开启进入webview模式：混合应用一开始进入web页面需要用这个



### Appium调试技巧

aapt 获取包名

- adb shell am monitor
- adb logcat | findstr -i displayed
- aapt dump badging   /path/ltest.apk
- 包名：、启动类：launchable-activity



![image-20200903004110441](D:\Pythonauto\Python_Workspace\web\加密\app自动化\appium日志.png)

![image-20200903010749640](D:\Pythonauto\Python_Workspace\web\加密\app自动化\image-20200903010749640.png)





- python （appium-client）向selenium服务器（appium-server）发送请求创建会话对象
  - [BaseDriver] W3C capabilities {"alwaysMatch":{"platformNa... and MJSONWP desired capabilities {"automationName":"UiAutoma... were provided

- selenium server（appium server）接收到数据，对数据进行解析和验证
  - 验证失败——返回响应信息<--500给python客户端

- 创建会话后，从环境变量中查找adb——没有则报错
- 通过 adb 链接设备
- 检查 adb 检查 api 版本是否兼容
- 通过 adb 启动app
- uiautomator 相关操作
- 返回成功信息<<--200 

总结：使用Python通过selenium访问webdriver提供的接口，调用js/adb+uiautomator执行操作，然后根据接口返回信息(200,500)确认指令是否执行成功

  - 出现错误时，通过代码报错日志确认出问题的步骤，再在appium server端日志找到具体的报错信息具体的定位和分析（复制和百度）问题

![image-20200903012212686](D:\Pythonauto\Python_Workspace\web\加密\app自动化\image-20200903012212686.png)



# adb

安卓调试桥：用于调用安卓底层接口操作安卓系统

## adb构成（adb+adb client、adbd+adb server）

- adt、android studio：
  - client：通过adb命令调起的客户端。adt等android工具都提供了adb客户端
  - 服务器server：运行在电脑后台，负责client和daemon进行通信
- dab daemon：运行在设备上，处理adb-server发出的命令并操作device（模拟器、真机）
- [原理图](https://blog.csdn.net/viewsky11/article/details/53889143)，[原理图appium](https://www.cnblogs.com/justaman/p/11778239.html)
- ![image-20200907022423200](D:\Pythonauto\Python_Workspace\web\加密\app自动化\adb通信原理5037、appium通信原理4723 4724.png)

## 常用指令

[相关连接](https://blog.csdn.net/wuxiaobingandbob/article/details/53096475?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param)

连接设备：**adb devices**

```cmd
# 输出示例：
List of devices attached
cf264b8f    device 
emulator-5554   device

# 输出格式为`[serialNumber] [state]`，sN，state:
# offline：设备未连接成功或无响应。
# device：设备已连接。但系统未必完全启动和可操作。设备启动过程中设备实例就可连接到adb，但启动完毕才处可操作。
# no device：没有设备/模拟器连接。
```

**adb connect deviceName**

**adb pull 收集路径 本机路径**            提取文件

**adb push 本机路径 手机路径**          推送文件

**adb logcat** 			实时打印安卓的运行日志

确定和设备的通信端口：**adb tcpip 5555**

停止adb server：**adb kill-server** 

启动adb server：**adb start-server** 

**adb install /path/xx.apk**                   安装app：APPname不支持中文

- **-r** 保留数据和缓存文件覆盖安装

**adb uninstall appPackage**              卸载app

- **-k** 卸载但保留数据和缓存文件

**adb shell** (android系统底层是个简易的linux系统)

- pm 指令 管理安卓应用
- 查看已安装应用：**pm list packages** 
-  dumpsys 指令 
-  查看类：**dumpsys activity**

查看已安装应用：**adb shell pm list packages** 

看当前前台应用的activity：**adb shell dumpsys activity|find "mFocusedActivity"**    ：| 是win的管道：

adb shell dumpsys activity|find **"mResumedActivity"** 



## 远程连接：

- 连接设备：**adb connect deviceIp**

  - 操作步骤：

    ```cmd
    # 1.Android 设备与运行 adb的电脑同局域网
    # 2.将设备与电脑通过 USB 线连接。确保连接成功（可运行 `adb devices` 看是否能列出该设备）。
    # 3.让设备在 5555 端口监听 TCP/IP 连接：
    adb tcpip 5555
    # 4.断开USB连接，找到设备的 IP 地址。(一般在「设置」-「关于手机」-「状态信息」-「IP地址」)
    # 5.通过 IP 地址连接设备。
    adb connect <device-ip-address>
    # 6.确认连接状态，能看到<device-ip-address>:5555 device说明连接成功
    adb devices
    ```

- 断开连接：**adb disconnect deviceIP**





# appium 是基于 selenium 实现的（95.49分）

selenium 在源码层面是怎么完成客户端到服务端的：

- Chrome()：创建了一个service并使用chromedriver.exe开启它→初始化一个客户端（祖类RemoteWebdriver）使用urllib3库发送http请求给服务端，

appium：

- appium-desktop、或者appium命令行启动服务端

- webdriver.Remote(...)：初始化一个客户端（祖类RemoteWebdriver）向appium-server发送请求

1. Remote、Chrome 都是继承同样的类，并封装了自己独有的操作。
2. 定位到的元素也是属于webelement类
3. Mobile_By(By)

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


# 元素定位

- app 当中属性名是固定的，所有的元素都具备这些属性。但属性值不一样
  
- 辅助工具中显示：
  - id：可以不唯一， web 当中 id 是唯一的
  - class：表组件名称，类似于 web 当中 tagname,
    - 在 app 自动化测试当中，很少用单独的 class 定位
  
  - content-desc, clickable, checkable, index(组件中第几个子元素)
  
- native元素也不能用css定位（不是html）


## 如何选择元素定位方式。

- id：优先。确认什么时候唯一， inpect 查找元素。
- content-desc 元素标识， 经常没有。
- uiautomator 原生定位方式
  - UiSelector官网：https://developer.android.com/reference/android/support/test/uiautomator/UiSelector
  - 博客:http://www.cnblogs.com/jianXu/p/5158396.html
- xpath (相对路径，一般用。手机解析页面素速度比较慢)

- 其他辅助工具：
  - appium
  - uiautomatorviewer.bat  ：adt/sdk/tools，sdk自带的调试工具，页面变动后需要手动刷新
  - ueditor ：网易出的，可以直接复制xpath，显示元素坐标→用真机打开“指针位置”也可以

# App专用的操作

## app元素定位

- ID
- content-desc ===> driver.find_element_by_accessibility_id()
- uiautomator ===> driver.find_element_by_android_uiautomator()
- xpath


## 元素定位辅助工具

- uiautomatorviewer(当手机版本或者ipa版本高的时候，会出现不兼容)

- appium inspect

- weditor (网易）：

  - 安装和启动： pip install——python -m weditor

  - 作用：
    
    - 复制xpath
    - 显示一个元素的坐标
    - 自动生成python代码（python的 Uiautomator2 的代码（只支持原生的））
    
  - 踩坑

    - 1. 只有python 3.5.0 以上才支持weditor

    - 2. 下载：

        - uiautomator2：	 pip install --upgrade uiautomator2
        -  weditor：	 pip install --upgrade weditor，  

      3. 启动：单独启动weditor 获取不了客户端信息，只有先启动uiautomator2 再启动weditor才可以

        - python -m  uiautmator2 init
        - python -m weditor

        4. 关闭：uiautomator2 手机端会对应下载一个软件ATX 运行完后要关掉，否则appium 会启不来 或者基于appium的framework 无法启动
             1. 关闭weditor服务；2关闭atx里的UIautomator2,；3重启appium服务端--》执行代码



## 踩坑
- 在 appium server, log 看到 uiatumator init failed,  can't find uiautomator
  
  - 先 kill 第三方的辅助工具， weditor(不止关闭浏览器，还要关闭服务)
  
- 如果不确定，可以adb uninstall uiautomator 卸载所有uiautomator相关服务
  
  - ```linux
    - adb shell 
    - pm list package|grep uiautomator
    - pm uninstall ....
    ```
  
- quit()

  - appium在1分钟未接受到请求时会自动断开连接，但不稳定，会导致下次的session和这次session冲突的情况，引发很多问题。如uiautomatorviewer报错Error obtaining UI hierarchy（但也可能是版本不兼容）

## API 操作

- driver.start_activity()     跳转到指定的页面

  - ```python
    # 取类名;cmd：adb shell dumpsys activity|find "mResumeActivity"
    driver.start_activity('com.xxzb.fenwoo', '.activity.user.CreateGesturePwdActivity')  # 切换到九宫格所在类
    ```

    

- swipe()      滑动

```
# 滑屏
# 获取屏幕宽度width，height
w = driver.get_window_size()["width"]
h = driver.get_window_size()["height"]
# 滑屏
driver.swipe(w*0.9,h*0.5,w*0.1,h*0.1)
# 二次封装-basepage
```

- 触屏操作TouchAction

  ```python
  action = TouchAction()
  action.press().wait().move_to().wait(ms=1000).move_to().realease().perform()  # 链式调用
  # .rect  # return x y width height
  ```

  - 九宫格操作步骤
    - press 九宫格的第一个格子,  坐标确认。
    - wait
    - move_to 第二
    - wait
    - move_to 第三个
    - wait
    - move_to
    - wait
    - release()
    - perform()

- 多指操作（放大，缩小）:MultiACtion

  - a1 = TouchAction(driver)
  - a1.press(el1).move_to(el2).release()
  - a2 = TouchAction(driver)
  - a2.press(el3).move_to(el4).release()
  - MultiAction(driver).add(a1,a2).perform()

- 键盘输入driver.press_keycode()    ：

  - 方法一：查找键位对应的code码，传入键位对应的数字(https://www.jianshu.com/p/f7ec856ff56f)
  - 方法二：自己封装要传入的值，放到common中直接用

```python
class MobileKey:
    ENTER = 66
    HOME = 3
```

- 返回：driver.back()
- 原码获取：driver.page_source()     获取源码要遍历页面，比较耗时
- 坐标地址：
  - 获取：driver.get
  - 设置：driver.set_location(49,123,10)   坐标：海拔，经度，维度
- driver.set_page_load_timeout(5000)           页面加载超时时间
- driver.set_script_timeout(5000)            脚本执行超时时间
- save_screenshot_as()                  截图
- driver.current_activity                 获取当前页面名字

- driver.current_package                   获取包名
- driver.current_context                    获取上下文环境（NATIVE_APP：原生环境，WEBVIEW_包名 ：webview环境。切换环境需要用到上下文）
- driver.contexts                              获取所有上下文环境
- driver.current_url                       需要进入app的web页面才可用

- **相比于web 没有的：**current_window_handle          手机上没有
- driver.start_activity(package_name, activity_name)         迅速跳转到某个类，测试很少用
- app安装、卸载、启动
  - reset()  重置应用数据，不是重启手机
  - driver.background_app(seconds = 5)      后台运行这个app5秒，一直运行则传 -1
  - driver.background_app({"timeout":5})   可以传数字，也可以传字典
- is_app_installed()           传参：安卓是包名，ios是bundle_id
- driver.install_app(".apk")      安卓app，手机或远端路径
- driver.close_app()    关闭app
- driver.quit()        退出
- 其他操作：
  - driver.hide_keyboard()        隐藏键盘：现在只能手机都是虚拟键盘，而不是适应安卓底层提供的键盘
  - driver.get_screenshot_as_file()
  - shake       摇一摇
  - lock           
  - unlock
- 重要的appium 操作：
  - 元素查找、click() 点击、quit() start、swipe()
  - TouchAction() 单个手指操作都可以用 TouchAction, press, move,
  - MultiAction() 多指操作
  - back()
  - page_source 获取源代码， 判断里面有没有目标内容：如  if "漂流瓶" in driver.page_source:...

#  混合应用 Hybrid App

现在大量存在混合应用，纯原生的应用已经很少了；混合页面把H5页面放在原生组件webview中。

webview是原生应用的一种控件，还有其他控件如ImageView、TextView等等。webview能做到和web页面的交互

- 常用跨平台开发的技术框架
  - Cordova Apache  ： 
  - React Native，简称RN     facebook出的。facebook曾修改了React Native的开源协议，搞得国内用这个框架的人人自危，后来weex火了起来
  - Ionic
  - Flutter          
    - 谷歌出的，是最接近原生的技术，响应速度很快，性能优秀；很多互联网巨头都开始用这个，闲鱼是第一批使用的。在一个页面的H5网页的表现很接近原生，不容易区分
    - weex、React Native都是通过JS中间层来使用webview的
  - Weex            阿里出的混合应用开发框架，基于vue.js
  - Adobe Phonegap

- 判断是不是H5页面：

  - 查看类是不是webview（可以使用UIautomator、appium inspector、weditor等工具）
  - web特有：返回键×，进度条（有些原生应用也有进度条）

- uiautomatorviewer等不能定位到webview里面的HTML元素，需要借助其他工具，需要在apk源码设置开启webview调试模式。

  - ==**chrome://inspect/#devices**==：会自动检查连接的手机的webview页面，需要vpn
  - [HTTP1.1/404]解决：1. 开启电脑vpn全局模式。2. [Android端浏览器版本和电脑版本不匹配](https://www.cnblogs.com/matric/p/10407783.html)，[下载地址](http://npm.taobao.org/mirrors/chromedriver/)
  - uc-devtools：默认需要管理vpn代理

- 测试Web app的前提：

  - 需要让开发在apk源码开启webview调试模式。

  - 在webview中操作元素需要chromedriver.exe，其[版本要和webview的版本匹配](https://www.jianshu.com/p/b96755bf4916?tdsourcetag=s_pctim_aiomsg)，而不是电脑浏览器版本

    ```python
    desired_capbilities = {
        chromedriverExecutableDir:r"filepath"  # 指定chromedriver的路径自动查找合适的
        # chromedriverExecutable:r"filepath/chromedriver_for_87.0.4280.20_in_mac.exe"}  # 指定文件
    ```

    

- 测试步骤：操作H5页面需要先切换到对应的上下文环境

  - 定位到原生应用控件并点击组件
  - 切换webview的上下文：进入web页面
    - 切换到指定上下文环境：driver.switch_to.context(context)，
    - 默认：driver.switch_to.context(None)
  - uctools定位web页面并操作web元素
  - （appium操作web页面）
  - 切换回原生页面

- ```python
  # toast 的xpath定位
  # 1. xpath,   '//*[contains(@text, "手机号码或密码不能为空")]'
  # 2. xpath toast的固定表示  '//*[//android.widget.Toast]'
  # TODO: Toast 定位如果要用显示等待
  # toast定位的显式等待只能用 presence, 不能用 visiblve（因为会自动消失）
  el = driver.find_element(By.XPATH, '//*[contains(@text, "手机号码或密码不能为空")]')
  print(el.text)
  ```

# 获取toast：

```python
# toast 的xpath定位
# 1. xpath '//*[contains(@text, "手机号码或密码不能为空")]'  需要传参
# 2. xpath toast的固定表示 '//*[//android.widget.Toast]' 不用传参，在不知toast文本情况下更适用
# TODO: Toast 定位如果要用显示等待
# toast定位的显式等待只能用 presence, 不能用 visiblve（因为会自动消失）
el = driver.find_element(By.XPATH, '//*[contains(@text, "手机号码或密码不能为空")]')
print(el.text)
```

# App自动化框架搭建

```
## 步骤
- 框架搭建（目录结构）
- 路径依赖：进入某个界面需要经过的路径，在PO设计模式下可以封装到该界面的类里<-->web：一个url一个页面

## 测试用例的执行步骤（写代码，如何编写自动化测试用例）
- 准备测试用例
- 手工测试步骤
- 封装页面行为
- 自动化用例编写

    """
    测试步骤：
        0， 导航页面点击我的柠檬
        1， 进入登录页面
        2， 在登录页面点击头像 （点击头像页面和用户名密码输入页面可以被当成一个页面。
            都和某个功能相关，用户管理功能
        ）
        3， 在登录页面输入用户名和密码登录
        4， 断言。


        1, 手工执行流程，得到所有的 locator, 复制在这
        2， 封装页面行为， PO
            多界面共用元素可封装进同一个类：底部三个按键->通用按键：
            class NavPage(BasePage):
            	my_locator=(MobileBy.ID,"xxxx")
            	tiku_locator =(MobileBy.ID,"xxx")
            	home_locator = (MobileBy.ID,"xxx")
            	
            def click_my() click_tiku()  click_home()
            
    """
可以切换的内容：
1. switch_context上下文切换


```

# 微信小程序
- 微信小程序

  - 是一个 H5页面，测试微信小程序即测试一个混合应用的H5页面
    
    - 要注意上下文切换，切换到 web 环境

  - 微信小程序环境：腾讯X5内核

      - 类似于web的前端环境可以是chromium内核，小程序的前端环境是X5内核
      - X5内核是腾讯基于chrome内核上进行的封装

  - 确定小程序进程名：

      - 微信有很多进程，每个小程序都运行在不同进程中

      - 获取前台运行的类，找到微信小程序的进程号，再adb shell ps 进程号，就可以找到小程序的进程名

          ```dos
          adb shell dumpsys activity top | findstr ACTIVITY  # 获取所有前台正在运行的类
            	ACTIVITY com.oneplus.opbackup/.CheckUpdateActivity2 7034584 pid=(not running)
            	ACTIVITY com.android.settings/.SubSettings 5af6213 pid=2239
            	ACTIVITY com.oppo.market/com.heytap.cdo.client.detail.ui.ProductDetailActivity d66d004 pid=9169
           	ACTIVITY net.oneplus.launcher/net.oneplus.quickstep.RecentsActivity 238c432 pid=2951
            	ACTIVITY net.oneplus.h2launcher/.Launcher 7d10df9 pid=2965
          	ACTIVITY com.tencent.mm/.ui.LauncherUI 49c73ca pid=30192
            	ACTIVITY com.tencent.mm/.plugin.appbrand.ui.AppBrandUI 343bc6d pid=30386    # .plugin.xxxxx微信的
          adb shell ps 30386
          	USER           PID  PPID     VSZ    RSS WCHAN            ADDR S NAME
          	u0_a132      30386   851 9592176 380944 SyS_epoll_wait      0 S com.tencent.mm:appbrand0
          ```

      - 指定小程序的webview的进程名称：微信里有多个环境，需要确定目标小程序的环境名

          ```
          desired_caps['chromeOptions']={'androidProcess':'com.tencent.mm:appbrand0'}
          ```

      

      - 其他：
        - 一个小程序里可能有多个handle，但是都放在同一页面里

        ```python
        # 一个根据源码里的文本确定目标handle的方法
        for handle in hs：
        	driver.switch_to.window(handle)
          	print("切换到窗口：", handle)
          	time.s;eep(3)
          	if driver.page_source.find("柠檬班") != -1
            	break
        ```

        - 小程序的webview版本要和chromedriverExecutableDir指定的chromedriver版本匹配
          - 71版本的chromedriver.exe挺稳定的

- 测试环境准备：

- 安装x5内核：可以直接安装qq浏览器
  - 打开x5内核调试模式：
      - 微信7.0-：访问debugx5.qq.com  >信息>TBS setting>TBS内核Inspector调试功能
      - 微信7.0+对H5页面的x5内核开关需强制开启：否则uc dev-tool 等外部工具无法找到元素
          - 访问 http://debugmm.qq.com/?forcex5=true    可以强制使用x5内核
          - 再访问  http://debugx5.qq.com 打开tbs 调试
  - 注意：需要使用真机，模拟器（win是x86架构，很难操作）需要转换为ARM架构环境：arm架构转化器：在x86架构的模拟器上再安装一个arm架构的模拟器





# Root

真机最好root，避免出现一些环境问题

- 可以使用xposed



- 工作中要更熟练使用adb、定位工具(uia..qppium ins..weditor..)
- 常用操作需要按分层思路封装到basepage
- 灵活运用appium官方文档
- 接口和web的一些可以优化的地方
  - 接口自动化-->只是一个框架，不适合直接给没有基础的新人使用。后续可以考虑发展成一个平台，也就是UI化
  - 接口测试的执行效率--> 使用的是单线程，对于特殊的接口比如需要等一段时间的接口，会造成堵塞-->可以考虑并发、或者分布式处理
  - 分析接口响应速度慢的原因：性能测试，性能分析，要有架构设计的能力
  - web自动化 ==> UI化、稳定性、
  - selenium-ide插件——可以直接录制、生成代码。xpath chrome插件
- 常用知识：装饰器、迭代器、生成器
- 找怎样的工作（自动化、测开、外包）
- 面试技巧

