import os
import shutil

# Part 1

def create_folders(base_path):
    # 定义操作名称，可按需求用例进行修改
    operations = [
       "首次登录", "杀进程重进", "首次进入P2P会话", "首次进入群会话", "首次进入服务号", "双击录制语音消息", 
       "创建群组", "邀请人进群", "发送消息-文本", "发送消息-图片", "发送消息-图文", "发送消息-视频", "双击录制语音消息", 
       "创建群组", "加入群组", "邀请人进群", "@人", "语音通话", "视频通话", "会议语音通话", "发起会议", "加入会议", 
       "快速切换会话", "拍摄", "相册", "文件", "pin", "收藏", "表情回应", "点击搜索", "搜索联系人", "搜索群", "搜索消息", 
       "切换tab", "加入群组", "@人", "点击头像", "点击+号", "进入眼界大开", "眼界大开-进入话题", "P2P语音通话", "视频通话", 
       "语音通话(右上角加号)", "发起会议", "加入会议", "创建日程", "进入日程详情", "取消日程", "进入代办", "添加代办", 
       "删除代办", "标记为完成", "设置提醒", "编辑提醒", "删除提醒", "查看日历", "添加日程", "编辑日程", "删除日程", 
       "分享日程", "查看共享日程", "接受共享日程邀请", "拒绝共享日程邀请", "退出共享日程", "屏蔽消息", "解除屏蔽", 
       "举报不良信息", "查看举报记录", "处理举报结果", "设置隐私", "编辑隐私设置", "查看隐私设置", "删除隐私设置", 
       "备份聊天记录", "恢复聊天记录", "导出聊天记录", "导入聊天记录", "清空聊天记录", "查找聊天记录", "筛选聊天记录", 
       "搜索聊天记录", "标记未读消息", "标记已读消息", "全部已读", "删除聊天", "退出聊天", "置顶聊天", "取消置顶", 
       "消息免打扰", "取消免打扰", "置底聊天", "取消置底", "置顶群组", "取消置顶群组", "置顶联系人", "取消置顶联系人", 
       "置顶消息", "取消置顶消息", "置顶日程", "取消置顶日程", "置顶代办", "取消置顶代办", "发送文件", "接收文件", 
       "查看文件", "删除文件", "转发文件", "保存文件到本地", "从本地上传文件", "下载文件", "在线预览文件", "编辑文件名", 
       "删除文件名", "重命名文件", "复制文件链接", "粘贴文件链接", "分享文件链接", "撤销文件分享", "设置文件权限", 
       "修改文件权限", "查看文件权限", "删除文件权限", "添加文件描述", "编辑文件描述", "删除文件描述", "查看文件描述", 
       "分享文件描述", "查看文件描述", "下载文件描述", "上传文件描述", "设置文件描述质量", "修改文件描述质量", 
       "查看文件描述质量", "删除文件描述质量","添加好友","删除好友","查看好友资料","编辑好友备注","将好友移至黑名单",
       "从黑名单中移除好友","发送好友请求","接受好友请求","拒绝好友请求","查看好友请求记录","编辑群资料","删除群",
       "转让群主","接受群主转让","拒绝群主转让","查看群成员列表","添加群成员","删除群成员","查看群公告","编辑群公告",
       "删除群公告","设置入群问题","编辑入群问题","删除入群问题","查看入群申请记录","审批入群申请","拒绝入群申请",
       "查看已通过的入群申请","查看被拒绝的入群申请","查看待审批的入群申请","语音转文字","编辑转换后的文字",
       "删除转换后的文字","保存转换后的文字","分享转换后的文字"
    ]
    
    # 创建所有副本文件夹和所有主文件夹
    copy_folder_path = os.path.join(base_path, "所有副本")
    main_folder_path = os.path.join(base_path, "所有主文件")
    if not os.path.exists(copy_folder_path):
        os.mkdir(copy_folder_path)
    if not os.path.exists(main_folder_path):
        os.mkdir(main_folder_path)
    
    # 遍历操作名称，创建主文件夹和副本文件夹
    for i, operation in enumerate(operations, start=1):
        main_folder = f"{i}-{operation}"
        copy_folder = f"{i}-{operation}-副本"
        
        # 创建主文件夹
        main_folder_path_full = os.path.join(base_path, main_folder)
        if not os.path.exists(main_folder_path_full):
            os.mkdir(main_folder_path_full)
        
        # 创建副本文件夹
        copy_folder_path_full = os.path.join(base_path, copy_folder)
        if not os.path.exists(copy_folder_path_full):
            os.mkdir(copy_folder_path_full)
        
        # 移动副本文件夹到“所有副本”文件夹中
        shutil.move(copy_folder_path_full, os.path.join(copy_folder_path, copy_folder))
    
    # 移动剩下的所有文件夹到“所有主文件”文件夹中
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)
        if os.path.isdir(item_path) and item != "所有副本" and item != "所有主文件":
            shutil.move(item_path, os.path.join(main_folder_path, item))
    
    # 在每个主文件夹中创建6个空子文件夹
    for main_folder in os.listdir(main_folder_path):
        main_folder_full_path = os.path.join(main_folder_path, main_folder)
        # 可根据需求修改子文件夹的数量，如需要9个子文件夹，即：for i in range(1, 10)
        for i in range(1, 7):
            child_folder_path = os.path.join(main_folder_full_path, str(i))
            if not os.path.exists(child_folder_path):
                os.mkdir(child_folder_path)

    print("所有文件夹已创建并整理完成。")

# 指定基本路径
base_path = r"E:\Python脚本测试"
create_folders(base_path)
