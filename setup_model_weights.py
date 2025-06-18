import os
import urllib.request

# 创建保存目录
os.makedirs('./saved_models/u2net', exist_ok=True)

# 下载函数
def download(url, save_path):
    print(f"Downloading from {url}...")
    urllib.request.urlretrieve(url, save_path)
    print(f"Saved to {save_path}")

# u2net.pth - 高清版，176MB，适用于毛发级抠图
u2net_url = 'https://huggingface.co/luannd/u2net/resolve/main/u2net.pth'
u2net_path = './saved_models/u2net/u2net.pth'

download(u2net_url, u2net_path)
