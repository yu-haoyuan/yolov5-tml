# HNU Data Mining

这是22届数据挖掘课程期末作业第二组的yolov5版本的复现

## 实现步骤
- [HNU Data Mining](#hnu-data-mining)
    前提:自行准备魔法访问

##### 1.原论文与数据的获取

    这是原论文的地址,请通过湖大登录获得ieee的文章获取权限
    https://ieeexplore.ieee.org/document/9991806


    这是原仓库的地址,用于开源数据集的获取
    [freds0/PTL-AI_Furnas_Dataset：PTL-AI Furnas 数据集：使用航空图像进行输电线路故障检测的公共数据集 --- freds0/PTL-AI_Furnas_Dataset: PTL-AI Furnas Dataset: A Public Dataset for Fault Detection in Power Transmission Lines Using Aerial Images](https://github.com/freds0/PTL-AI_Furnas_Dataset)


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
          
    


## 安装

1. 克隆仓库：
    ```bash
    git clone https://github.com/your-username/awesome-project.git
    ```
2. 安装依赖：
    ```bash
    cd awesome-project
    npm install
    ```

## 使用说明

