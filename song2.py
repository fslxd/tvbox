import subprocess
import os

def split_songs_by_silence(input_file, output_dir):
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 使用ffmpeg根据静音部分分割歌曲
    command = f"ffmpeg -i {input_file} -af afade=t=in:st={0}:d=2,afade=t=out:st={0}:d=2 {os.path.join(output_dir, '%03d.mp3')}"
    subprocess.call(command, shell=True)

# 示例用法
input_file = "123.mp4"
output_dir = "split_songs"
split_songs_by_silence(input_file, output_dir)
