import os
import random
import shutil

# 定义路径
train_images_path = './imgs/train'
train_labels_path = './data/yolo/train'
val_images_path = './imgs/val'
val_labels_path = './data/yolo/val'

# 创建 val 目录
os.makedirs(val_images_path, exist_ok=True)
os.makedirs(val_labels_path, exist_ok=True)

# 获取所有训练集图像文件名（不包括扩展名）
train_images = [os.path.splitext(f)[0] for f in os.listdir(train_images_path) if f.endswith('.jpg')]

# 随机选择 5% 的图像文件
val_images = random.sample(train_images, int(len(train_images) * 0.05))

# 将选中的图像和对应的标签文件复制到 val 目录
for image in val_images:
    image_path = os.path.join(train_images_path, image + '.jpg')
    label_path = os.path.join(train_labels_path, image + '.txt')
    
    if os.path.exists(image_path) and os.path.exists(label_path):
        # 复制图像文件
        shutil.copy(image_path, os.path.join(val_images_path, image + '.jpg'))
        # 复制标签文件
        shutil.copy(label_path, os.path.join(val_labels_path, image + '.txt'))
    else:
        print(f"File not found: {image_path} or {label_path}")

print(f'Copied {len(val_images)} images and their labels to validation set.')