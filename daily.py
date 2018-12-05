import os, time

def fight_pic():
    while True:
        time.sleep(1)
        os.system('adb shell input tap 100 1500')

def switch():
    os.system('adb shell input swipe 300 1000 800 1000')    # 向右滑动
    os.system('adb shell input tap 120 1845')    # 点击设置
    os.system('adb shell input tap 500 300')    # 点击账号管理
    os.system('adb shell input tap 500 1350')    # 切换帐号
    time.sleep(1)
    os.system('adb shell input tap 95 150')    # 返回设置
    os.system('adb shell input tap 95 150')    # 返回主界面
    os.system('adb shell input swipe 800 1000 300 1000')    # 向左滑动

def like():
    os.system('adb shell input tap 500 450')    # 进入聊天界面
    os.system('adb shell input tap 1010 130')
    os.system('adb shell input tap 500 400')
    time.sleep(2)
    for i in range(0, 10):
        os.system('adb shell input tap 950 1380')
        time.sleep(1)
    time.sleep(1)
    os.system('adb shell input tap 105 140')
    os.system('adb shell input tap 105 140')
    os.system('adb shell input tap 50 150')

def qlike():    # 该函数未测试
    for i in range(0, 6):
        switch()
        like()

def signin(x, y):
    ins = 'adb shell input tap ' + str(x) + ' ' + str(y)
    time.sleep(1)
    os.system(ins)    # 进入群 这里有点小瑕疵 输入法会自己弹出来
    # 解决方法:将输入法设置为浮动键盘
    os.system('adb shell input tap 1010 1853')    # 进入应用第一页
    os.system('adb shell input swipe 800 1500 400 1500')    # 进入应用第二页
    os.system('adb shell input tap 650 1700')    # 进入签到页面
    time.sleep(2)
    os.system('adb shell input tap 1000 125')    # 签到确定
    time.sleep(1)
    os.system('adb shell input tap 95 150')

def sigin5():
    signin(500, 450)    # 第一个群签到
    signin(500, 650)    # 第二个群签到
    signin(500, 850)    # 第三个群签到
    signin(500, 1050)    # 第四个群签到
    signin(500, 1250)    # 第五个群签到

if __name__ == '__main__':
    # 准备工作:设置浮动输入法键盘 QQ在主界面
    # 全部完成需要4分钟20秒
    sigin5()    # 40秒时间即可完成
    qlike()    # 3分钟半多的时间
    switch()    # 返回主帐号

