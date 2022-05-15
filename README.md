# Benchmark Metric Object Detection Models

**@nabang1010 - SANSlab**



## Format Image performance metric

```
├── prediction
│   ├── image_1.txt
│   ├── image_2.txt
│   └── image_3.txt
└── gt
    ├── image_1.txt
    ├── image_2.txt
    └── image_3.txt

```

```
predict file image_1.txt:

class conf bbox_x bbox_y bbox_w bbox_h

0 0.94 0.133594 0.861574 0.076563 0.243519
0 0.99 0.277865 0.756019 0.054688 0.219444


ground truth file  image_1.txt

class bbox_x bbox_y bbox_w bbox_h

0 0.133594 0.861574 0.076563 0.243519
0 0.277865 0.756019 0.054688 0.219444

```
## Format Video performance metric

```
predict file vid_1.txt:

frame class conf bbox_x bbox_y bbox_w bbox_h

1 0 0.94 0.133594 0.861574 0.076563 0.243519
1 0 0.99 0.277865 0.756019 0.054688 0.219444
2 0 0.96 0.541667 0.431481 0.066667 0.118519
2 0 0.94 0.666146 0.526389 0.101042 0.150926

ground truth file vid1_txt:

frame class bbox_x bbox_y bbox_w bbox_h

1 0 0.133594 0.861574 0.076563 0.243519
1 0 0.277865 0.756019 0.054688 0.219444
2 0 0.541667 0.431481 0.066667 0.118519
2 0 0.666146 0.526389 0.101042 0.150926

```

## Guide

|Argument|Description|Dest|Default|
| ------ | --------- | -- | ----- | 
| `-h`,`--help` | show this help message and exit |  |  | 




### TO DO:
- [ ] Build 
- [ ] Calculate IOU
- [ ] Calculate Precision
- [ ] Calculate Recall
- [ ] Calculate AP
- [ ] Calculate mAP
- [ ] Calculate FFPI
- [ ] Calculate MR
