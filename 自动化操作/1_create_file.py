import os
import shutil

# Part 1

def create_folders(base_path):
    # 定义操作名称
    operations = [
        "拍摄", "相册", "文件"
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
base_path = r"E:\实习内容\Python脚本测试\测试顺序"
create_folders(base_path)