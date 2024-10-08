import os
import cv2
import subprocess
""" Part 4 """
# 视频解码 转图片                
# 若更换设备，检查是否安装了ffmpeg，安装后，配置环境变量，使用cmd，输入ffmpeg -version，显示版本号，说明配置成功
#  ！！注：环境配置成功后，需要重启电脑，才可以正常运行此脚本

def convert_video_to_images(video_path, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 使用ffmpeg命令行工具来提取视频帧
    print(f"正在处理视频：{video_path}")
    cmd = [
        'ffmpeg',  # 可使用绝对路径代替
        '-i', video_path,
        '-r', '120',  # 根据视频的实际帧率设置
        '-q:v', '2',
        '-f', 'image2',
        os.path.join(output_folder, '%04d.jpg')   # 以4位数的形式排序+命名
    ]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    print(f"视频帧已保存到：{output_folder}")
    print()

def main(base_dir):
    # 遍历主文件夹中的所有子文件夹
    for main_folder in os.listdir(base_dir):
        main_folder_path = os.path.join(base_dir, main_folder)
        if os.path.isdir(main_folder_path):
            print(f"进入主文件夹：{main_folder_path}")
            # 遍历子文件夹内的所有视频文件
            for video_file in os.listdir(main_folder_path):
                if video_file.lower().endswith(".mov"):
                    video_path = os.path.join(main_folder_path, video_file)
                    video_filename_without_ext = os.path.splitext(video_file)[0]
                    output_folder = os.path.join(main_folder_path, video_filename_without_ext)
                    convert_video_to_images(video_path, output_folder)

    print("所有视频处理完成。")

# 指定基本路径（存储重命名后的视频文件的所在路径）
base_dir = r"E:\Python脚本测试\所有主文件"   # 会遍历所有主文件中的子文件夹
main(base_dir)
