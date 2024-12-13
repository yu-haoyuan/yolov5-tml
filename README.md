# HNU Data Mining

这是22届数据挖掘课程期末作业第二组的yolov5版本的复现

## 实现步骤
前提:自行准备魔法访问

##### 1.原论文与数据的获取

这是原论文的地址,请通过湖大登录获得ieee的文章获取权限

    https://ieeexplore.ieee.org/document/9991806


这是原仓库的地址,用于开源数据集的获取

    https://github.com/freds0/PTL-AI_Furnas_Dataset

##### 2.环境的准备

首先测试是否能运行yolov5,可以直接运行detect.py然后检查是否出现runs文件
如果出现且exp中有bus.jpg和zidane.jpg的检测结果图片,证明配置成功

##### 3.数据集的准备

在实现之前,我们要准备好yolov5格式的数据集和对应的配置yaml文件

首先我们准备数据集

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
      │   │   
      ├── imgs
      │   ├── test
      │   ├── train
      │   
      ├── output
      └── utils

由于这里没用val文件无法适应yolo的格式,这里提供了一个简单的脚本datafix.py来提供val集,可以自行设置路径完成val文件的生成,生成之后将val文件加入到如下步骤

将imgs和data中的yolo文件以及自行生成的val文件复制移动到一个新文件夹中,新文件夹由你命名,我的为tmldata

    tmldata
      ├── images
      │   ├── test
      │   ├── train
      │   └── val
      └── labels
          ├── test
          ├── train
          └── val

然后将文件夹tmldata移动到如下位置
    yolov5-tml
      ├── data
           ├── tmldata
                ├── images
                │   ├── test
                │   ├── train
                │   └── val
                └── labels
                    ├── test
                    ├── train
                    └── val


然后我们准备.yaml配置文件,这里由于内容比较长直接在对应位置配置好了,建议了解一下这部分是如何工作的
    yolov5-tml
      ├── data
      │   ├── tml.yaml

到这里,我们的数据集准备部分就完成了

##### 4.yolov5对应parser命令行的更改

这里为了方便,直接对源文件中的parser中的参数进行更改,这里正确的用法应该是在命令行中运行的过程时执行,我更改的部分为

    parser.add_argument("--cfg", type=str, default="models/yolov5s.yaml", help="model.yaml path")
    parser.add_argument("--data", type=str, default=ROOT / "data/tml.yaml", help="dataset.yaml path")
    parser.add_argument("--epochs", type=int, default=100, help="total training epochs")
    parser.add_argument("--batch-size", type=int, default=4, help="total batch size for all GPUs, -1 for autobatch")


--cfg为采用预训练模型,这里我们可以到yolov5的源库中进行下载
    https://github.com/ultralytics/yolov5
这里根据自己显卡配置选择模型,参数越大效果越好(可能)
这里我下载的是yolov5s模型,下载完成后将yolov5s.pt放置在
    yolov5-tml
      ├── yolov5s.pt
即为和train.py同级的文件夹下

--data为文件参数的路径,改为我们设置的data/tml.yaml
--epochs为训练轮数,这里采用默认值100
--batch-size由你的显卡参数自行设置,越大越好

(实际上这里的正确用法应该是)
    python train.py --data data/tml.yaml --batch-size 4

当执行python train.py没有报错后,可能会运行几个小时进行训练
其中会出现wandb的配置,这里可以进行忽略

如果训练完毕且正确,你会在runs文件夹下面看见train--exps文件
点开最后一个exp,你会发现weightd中有best.pt,这就是你训练好的模型

##### 5.训练完毕后进行推理

找到文件下的val.py文件,这里和训练同理进行偷懒
这里运用的是你训练好的模型进行推理

    parser.add_argument("--data", type=str, default=ROOT / "data/tml.yaml", help="dataset.yaml path")
    parser.add_argument("--weights", nargs="+", type=str, default=ROOT / "runs/train/exp8/weights/best.pt", help="model path(s)")

注意对应参数的更改,然后执行python val.py