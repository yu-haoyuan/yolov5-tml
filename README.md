# HNU Data Mining

这是22届数据挖掘课程期末作业第二组的yolov5版本的复现

## 实现步骤
前提:自行准备魔法访问

##### 1.原论文与数据的获取

这是原论文的地址,请通过湖大登录获得ieee的文章获取权限
  https://ieeexplore.ieee.org/document/9991806


这是原仓库的地址,用于开源数据集的获取
  https://github.com/freds0/PTL-AI_Furnas_Dataset


##### 2.数据集的准备

在实现之前,我们要准备好yolov5格式的数据集

在第1步中提到的原仓库中找到Download PTL-AI Furnas Dataset here.
点击下载

下载之后你会看到这种格式

  furnas_dataset_v0.07
    ├── .ipynb_checkpoints
    ├── data
    |   ├──coco
    |   ├──csv
    |   |──xml
    |   |──yolo
    |   │   ├── test
    │   │   ├── train
    │   │   └── val
    ├── imgs
    │   ├── test
    │   ├── train
    │   └── val
    ├── output
    └── utils
将imgs和data中的yolo文件复制到一个新文件夹中,新文件夹由你命名,我的为tmlData
  tmlData
    ├── images
    │   ├── test
    │   ├── train
    │   └── val
    └── labels
        ├── test
        ├── train
        └── val
          