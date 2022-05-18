# Benchmark Metric Object Detection Models

### @nabang1010 - SANSlab



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

class conf top left width height

0 0.94 821 169 26 53
0 0.99 794 172 25 57


ground truth file  image_1.txt

class top left width height

0 1039 98 17 38
0 758 176 29 56

```
## Format Video performance metric

```
predict file vid_1.txt:

frame class conf top left width height

1 0 0.94 0.133594 0.861574 0.076563 0.243519
1 0 0.99 0.277865 0.756019 0.054688 0.219444
2 0 0.96 0.541667 0.431481 0.066667 0.118519
2 0 0.94 0.666146 0.526389 0.101042 0.150926

ground truth file vid1_txt:

frame class top left width height

1 0 0.133594 0.861574 0.076563 0.243519
1 0 0.277865 0.756019 0.054688 0.219444
2 0 0.541667 0.431481 0.066667 0.118519
2 0 0.666146 0.526389 0.101042 0.150926

```

## Usage

|Argument|Description|Dest|Default|
| ------ | --------- | -- | ----- | 
| `-h`,`--help` | show this help message and exit |  |  | 
| `-pred`,`--pred_path` | prediciton folder path | pred_path |  | 
| `-gt`,`--gt_path` | ground truth folder path | gt_path |  | 
| `-pred_format`,`--pred_format` | prediction format (txt, json, xml) | pred_format |  | 
| `-gt_format`,`--gt_format` | gt format (txt, json, xml) | gt_format |  | 
| `-iou`,`--iou` | calculate IOU - Intersection Over Union | cal_IOU | Flase | 
| `-precision`,`--precision` | calculate Precision | cal_Precision | Flase | 
| `-recall`,`--recall` | calculate Recall | cal_Recall | False | 
| `-ap`,`--ap` | calculate Average Precision | cal_AP | False | 
| `-map`,`--map` | calculate mean Average Precision | cal_mAP | False | 
| `-ffpi`,`--ffpi` | calculate False Positive Per Image | cal_FFPI | False | 
| `-mr`,`--mr` | calculate Miss Rate | cal_MR | False | 
| `-graph`,`--graph` | draw graph | draw_graph | False | 


## Metric

### Precision

`precision = TP/(TP+FP)`

* `TP`: True Positive - Correct detection of the model
* `FP`: False Positive - Incorrect detection of the model
  
### Recall

`recall = TP/(TP+FN)` 

* `TP`: True Positive - Correct detection of the model
* `FN`: False Negative - Ground truth not detected 
### TO DO:
- [ ] Build 
<!-- - [ ] Calculate IOU -->
- [ ] Calculate Precision
- [ ] Calculate Recall
- [ ] Calculate AP
- [ ] Calculate mAP
- [ ] Calculate FFPI
- [ ] Calculate MR
