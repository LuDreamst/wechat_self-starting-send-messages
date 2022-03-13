import pyautogui
import time

# 每个pyautogui指令的间隔时间
pyautogui.PAUSE = 1.0


# 图片识别定位函数
def location(png):
    icon = pyautogui.locateOnScreen(png)
    if icon is not None:
        center = pyautogui.center(icon)
        return center
    else:
        time.sleep(6)  # 考虑软件的加载时间，无法识别时延时6秒
        icon = pyautogui.locateOnScreen(png)
        center = pyautogui.center(icon)
        return center


target0 = location('wechat.png')
pyautogui.doubleClick(target0[0], target0[1])
time.sleep(2)

target1 = location('jinruweixin.png')
pyautogui.click(target1[0], target1[1])

target2 = location('myself.png')
pyautogui.click(target2[0], target2[1])

target3 = location('typearea.png')
# 避免点击过快，模拟鼠标移动
pyautogui.moveTo(target3[0], target3[1], duration=0.8)
pyautogui.click()
pyautogui.typewrite('Hello world!')  # 仅支持英文

# 点击发送表情包
# target3 = location('emoji.png')
# pyautogui.moveTo(target3[0], target3[1], duration=0.8)
# pyautogui.click()
#
# target4 = location('se.png')
# pyautogui.moveTo(target4[0], target4[1], duration=0.8)
# pyautogui.click()

# 模拟鼠标点击“发送”功能
target5 = location('send.png')
pyautogui.moveTo(target5[0], target5[1], duration=0.8)
pyautogui.click()
