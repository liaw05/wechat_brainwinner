# wechat_brainwinner
最近在参加微信“头脑王者”的小游戏，发现比答题速度比别人慢，就想着做个小程序帮助答题。
![image](https://github.com/liaw05/wechat_brainwinner/blob/master/temp/screenshot.png?raw=true)  

#原理说明  
---
1. 将手机点击到《头脑王者》小程序界面  
2. 用 ADB 工具获取当前手机截图，并用 ADB 将截图 pull 上来  
    adb shell screencap -p /sdcard/autojump.png  
    adb pull /sdcard/autojump.png .  
3. 调用tesseract-ocr进行问题与答案识别  
4. 通过 python requests 模块在百度网上搜索，通过对题目答案记频来确定答案
5. 通过 ADB 工具点击自动快速手机屏幕  
    adb shell input tap x y

#程序说明  
---
1. resoures文件中包含各个功能模块 
2. temp中为截屏图片
3. tools中包含adb工具包和所需 python 模块清单。

