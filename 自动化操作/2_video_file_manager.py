import os
import shutil

# Part 2

def rename_videos(copy_folder_path):
    for folder_name in os.listdir(copy_folder_path):
        folder_path = os.path.join(copy_folder_path, folder_name)
        if os.path.isdir(folder_path):
            print(f"正在重命名文件夹 '{folder_name}' 中的视频文件...")
            for i, video_file in enumerate(sorted(os.listdir(folder_path)), start=1):
                old_video_path = os.path.join(folder_path, video_file)
                new_video_name = f"{i}-{video_file}"
                new_video_path = os.path.join(folder_path, new_video_name)
                os.rename(old_video_path, new_video_path)
            print(f"文件夹 '{folder_name}' 中的视频文件重命名完成。")

def copy_and_rename_videos(copy_folder_path, main_folder_path):
    for folder_name in os.listdir(main_folder_path):
        folder_path = os.path.join(main_folder_path, folder_name)
        if os.path.isdir(folder_path):
            copy_folder_name = folder_name + "-副本"
            copy_folder_path_full = os.path.join(copy_folder_path, copy_folder_name)
            if os.path.isdir(copy_folder_path_full):
                print(f"正在复制并重命名文件夹 '{copy_folder_name}' 中的视频文件到 '{folder_name}'...")
                for i, video_file in enumerate(sorted(os.listdir(copy_folder_path_full)), start=1):
                    video_path = os.path.join(copy_folder_path_full, video_file)
                    video_index = str(i)
                    new_video_name = f"{video_index}.MOV"
                    new_video_path = os.path.join(folder_path, new_video_name)
                    shutil.copy(video_path, new_video_path)
                print(f"文件夹 '{copy_folder_name}' 中的视频文件复制并重命名到 '{folder_name}' 完成。")
                print()

def main():
    base_path = r"E:\Python脚本测试"  # 文件夹所在的总路径，此路径包含所有副本和所有主文件
    copy_folder_path = os.path.join(base_path, "所有副本")
    main_folder_path = os.path.join(base_path, "所有主文件")

    rename_videos(copy_folder_path)
    copy_and_rename_videos(copy_folder_path, main_folder_path)
    print("视频文件的重命名和复制操作已成功完成。")

if __name__ == "__main__":
    main()
