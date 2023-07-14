<font face = "华文中宋">

# HuBMAP-Competition

HuBMAP - Hacking the Human Vasculature Competition Respository

## Usage 

- 使用以下命令从 kaggle 上下载数据集

```bash
cd ./data
python download.py
```

> 因为原始数据集实在太大，因此不 push 到仓库中，而是由用户自行下载。
>
> 以上命令会将数据集下载到 `/data/` 文件夹下，然后你需要将这个数据集重命名为 `dataset` 来使得 `gitignore` 文件生效，防止 push 代码时将整个数据集 push 到仓库中。


## About the Competition 

### 基本生物学原理

- 别理 VCCF
- 别看太长的专业资料
- 这些都和我们没关系
- 需要的所有生物学知识都罗列如下：
  
#### 微循环是什么

微循环包括微动脉、后微动脉和毛细血管前括约肌、微静脉。在我们这个项目中，我们需要研究的主要部分是：微动脉，微静脉和毛细血管。因此，我们甚至可以不严格地近似认为：本项目研究的微循环 = 微动脉 + 微静脉 + 毛细血管。

微循环的示意图如下（以肠系膜微循环模式图为例）：

<center><img src = ./images/1.png width=50%></center>

#### 题目给出的样本是怎么得到的

题目给出的一个样本如下所示：

<center><img src = ./images/2.png width=35%></center>

这实际上是血管的组织切片，直白些，就是血管的横截面染色图。你可以想象它可能是用以下切割方法得到的：

<center><img src = ./images/3.png width=60%></center>

通过这样的横切，就形成了染色切面图中的形状，根据某个医学专业同学的提示：

- 微动脉圆圈规则，壁厚腔小。
- 微静脉圆圈不一定规则，壁薄腔大。
- 毛细血管则较难辨识。

本题并不具体要求到区分各种血管类型，它只要求找到血管的位置。

### 问题描述 (What To Do)

- 对**微血管结构**(包括毛细血管、微动脉和微静脉)进行**分段**。
- 需要根据数据集中给出的人类肾组织切片图像创建一个机器学习模型。
  - 模型输入：`.tif` 图像，见数据集描述。
  - 模型处理：医学图像语义分割模型。
  - 模型输出：一行，见评估方法描述。

### 数据集描述

#### `polygons.jsonl` 文件

`polygons.jsonl` 就相当于传统机器学习项目中的标注数据。`jsonl` 是一种优化的 `json` 格式，它的每一行代表一个 item，即对于一张图片的注释。

对于一张图片的注释包含以下内容：

- `id`：每张图片对应的 ID 
- `annotations`：

- 所有 `.tif` 类型的图像宽高都是 512，存放在 `./data/dataset/test` 和 `./data/dataset/train` 两个文件夹中。
- `annotations`：对于图片的注释，这是一个列表，列表的每个元素表示识别到的一个实例，这些实例都有 `type` 和 `coordinates` 两个属性
  - `type`：包括 `blood_vessel` 和 `glomerulus` 两种类型： 
    - `blood_vessel`：血管类型。本次任务需要检测出所有血管的 `mask`。
    - `glomerulus`：肾小球类型。肾小球类型不应该被我们的模型识别，我们的分割结果不应该包括它。
    - `unsure`：即使是专家也不能确定的类型，忽略。
  - `coordinates`：多边形的每个点的坐标。

> 多边形和 mask 的关系
>
> 多边形（一个 n*2 的数组）实际上就表示一个 mask 的边界，所谓 mask，一般就是一个 0/1 值的数组，数组中标志为 1 的位置表示存在目标，数组中标志为 0 的位置表示不存在目标：
>
> 多边形标注示例如下所示：
>
> <center><img src = ./images/4.png width=60%></center>
>
> mask 标注示例如下所示：
>
> <center><img src = ./images/5.png width=60%></center>
>
> 下面的函数能实现多边形和 mask 的转换：
>
> ```python
> def poly2mask(points, width, height):
>   mask = np.zeros((width, height), dtype=np.int32)
>   obj = np.array([points], dtype=np.int32)
>   cv2.fillPoly(mask, obj, 1)
>   return mask
> ```

#### `tile_meta.csv`

包括每张图片的源数据，有以下属性：

- `source_wsi`：这张图片来自哪个 WSI 
- `{i|j}`：这张图片在 WSI 上的位置
- `dataset`：该图片来自哪个数据集

#### `wsi_data.csv`

包含每个 WSI 的提取来源信息。

### 数据集预处理方法

### 评估方法描述

阈值为 0.6 的 IoU 评估方法。

### 相关研究

医疗图像分割综述：

CV 图像分割问题综述：


