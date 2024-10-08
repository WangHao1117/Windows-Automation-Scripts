import os
import shutil


def delete_files_in_folder(folder_path):
    # 遍历文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for file in files:
            # 构建完整的文件路径
            file_path = os.path.join(root, file)
            # 删除文件
            os.remove(file_path)
            print(f"已删除文件：{file_path}")

        # 如果需要删除空文件夹，可以取消注释下面的代码
        # for dir in dirs:
        #     dir_path = os.path.join(root, dir)
        #     shutil.rmtree(dir_path)
        #     print(f"已删除空文件夹：{dir_path}")

    print(f"文件夹 '{folder_path}' 中的所有文件已被删除。")

if __name__ == "__main__":
    # 指定要清空的文件夹路径
    # folder_to_clear = r"D:\Test\test\测试\所有主文件\1-拍摄"
    folder_to_clear = r"E:\Python脚本测试"   # 删除此路径下的子文件
    delete_files_in_folder(folder_to_clear)
