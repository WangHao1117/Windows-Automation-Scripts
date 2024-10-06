import subprocess
# Part 3
# 查找FFmpeg安装位置，前提需要在环境配置后

def check_ffmpeg_installation():
    result = subprocess.run(['where', 'ffmpeg'], stdout=subprocess.PIPE, text=True)
    if result.returncode == 0:
        print("FFmpeg is installed:", result.stdout.strip())
    else:
        print("FFmpeg is not installed or not found in PATH.")

check_ffmpeg_installation()