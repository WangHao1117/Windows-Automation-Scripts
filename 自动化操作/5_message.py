from pywinauto import Application
import time
""" Part 5 """
# 此代码文件测试的目标为竞品，非网易POPO。可根据需求修改下方的应用程序，效果以及功能无差别
# 运行此代码前，需要确保钉钉和p2p对话界面已经打开
def send_dingtalk_message(app, message):
    try:
        # 切换到钉钉窗口
        dingtalk = app.window(title_re=".*钉钉.*")
        dingtalk.set_focus()
        time.sleep(2)

        # 输入消息
        dingtalk.type_keys(message)
        time.sleep(1)  # 等待一段时间，确保消息已经输入完毕

        # 发送消息
        dingtalk.type_keys('{ENTER}')
        print(f"已发送消息: {message}")

    except Exception as e:
        print(f"发送消息时发生错误: {e}")

def main():
    message = "Hello, this is a test message from my script."  # 要发送的消息
    max_duration = 3600  # 最大运行时间，例如1小时（3600秒）
    interval = 30  # 发送消息的间隔时间（秒）

    # 启动或连接到钉钉应用
    app = Application(backend='uia').connect(title_re=".*钉钉.*")

    start_time = time.time()
    while (time.time() - start_time) < max_duration:
        send_dingtalk_message(app, message)
        time.sleep(interval)

    print("达到最大运行时间，脚本自动终止")

if __name__ == "__main__":
    main()
