# 使用指南

## 环境设置
- 确保Python环境已安装。
- 根据需要下载并安装FFmpeg。

## 脚本运行顺序
1. **创建文件夹结构**：
   - 首先运行[`1_create_file.py`](自动化操作/1_create_file.py)创建必要的文件夹结构。

2. **上传视频文件**：
   - 使用爱思助手上传视频文件到指定的副本文件夹。

3. **视频文件整理和重命名**：
   - 运行[`2_video_file_manager.py`](自动化操作/2_video_file_manager.py)进行视频文件的整理和重命名。

4. **提取视频帧**：
   - 运行[`3_findFFmpeg.py`](自动化操作/3_findFFmpeg.py)检查FFmpeg。
   - 确认FFmpeg安装后，执行[`4_extract_frames.py`](自动化操作/4_extract_frames.py)提取视频帧。

6. **性能监控**：
   - 使用性能狗测试工具，并运行[`5_message.py`](自动化操作/5_message.py)进行性能监控。

7. **文件清理**：
   - 如遇错误或需求变更，使用[`delete_file.py`](自动化操作/delete_file.py)进行文件清理。
   
