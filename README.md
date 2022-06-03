# Benchmark Metric Object Detection Models

### @nabang1010 - SANSlab


```
    0,0 ------> x (width)
     |      _________________________________ 
     |     |                                 |
     |     |   (Left,Top)                    |
     |     |       *_________                |
     |     |       |         |               |
     v     |       |   bbox  |               | 
     y     |       |_________|               |
  (height) |                 *               |
           |           (Right,Bottom)        |
           |_________________________________|
```




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

<class> <conf> <top> <left> <width> <height>

0 0.94 821 169 26 53
0 0.99 794 172 25 57
___________________________________________________

ground truth file  image_1.txt

<class> <top> <left> <width> <height>

0 1039 98 17 38
0 758 176 29 56

```
## Format Video performance metric

```
predict file vid_1.txt:

<frame> <class> <conf> <top> <left> <width> <height>

1 0 0.94 781 143 25 57
1 0 0.99 1127 457 57 146
2 0 0.96 950 252 217 126
2 0 0.94 538 608 98 217

ground truth file vid1_txt:

<frame> <class> <top> <left> <width> <height>

1 0 1064 117 21 47
1 0 704 379 62 133
2 0 975 690 280 383
2 0 538 608 98 217

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

`IoU --> TP, FP, FN --> Prec, Recall --> AP --> mAP` 

### Precision

`precision = TP/(TP+FP)`

* `TP`: True Positive - Correct detection of the model
* `FP`: False Positive - Incorrect detection of the model




  
### Recall

`recall = TP/(TP+FN)` 

* `TP`: True Positive - Correct detection of the model
* `FN`: False Negative - Ground truth not detected 



### Popular object detection methods

|Method|Benchmark Dataset|Metric|
| ------ | --------- | ----- | 
|**CornerNet**|COCO|`AP@[.5:.05:.95]`; `AP@50`; `AP@75`; <code>AP<sub>S</sub></code>; <code>AP<sub>M</sub></code>; <code>AP<sub>L</sub></code>|
|**EfficientDet**|COCO|`AP@[.5:.05:.95]`; `AP@50`; `AP@75`; `AP@75`|
|**Fast R-CNN**|PASCAL VOC 2007, 2010, 2012|`AP`; `mAP (IoU=0.50)`|
|**Faster R-CNN**|PASCAL VOC 2007, 2012|`AP`; `mAP (IoU=0.50)`|
|**Faster R-CNN**|COCO|`AP@[.5:.05:.95]`; `AP@50`|
|**R-CNN**|PASCAL VOC 2007, 2010, 2012|`AP`; `mAP (IoU=0.50)`|
|**RFB Net**|PASCAL VOC 2007|`mAP (IoU=0.50)`|
|**RFB Net**|COCO|`AP@[.5:.05:.95]`; `AP@50`; `AP@75`; <code>AP<sub>S</sub></code>; <code>AP<sub>M</sub></code>; <code>AP<sub>L</sub></code>|
|**RefineDet**|PASCAL VOC 2007, 2012|`mAP (IoU=0.50)`|
|**RefineDet**|COCO|`AP@[.5:.05:.95]`; `AP@50`; `AP@75`; <code>AP<sub>S</sub></code>; <code>AP<sub>M</sub></code>; <code>AP<sub>L</sub></code>|
|**RentinaNet**|COCO|`AP@[.5:.05:.95]`; `AP@50`; `AP@75`; <code>AP<sub>S</sub></code>; <code>AP<sub>M</sub></code>; <code>AP<sub>L</sub></code>|
|**R-FCN**|PASCAL VOC 2007, 2012|`mAP (IoU=0.50)`|
|**R-FCN**|COCO|`AP@[.5:.05:.95]`; `AP@50`; <code>AP<sub>S</sub></code>; <code>AP<sub>M</sub></code>; <code>AP<sub>L</sub></code>|
|**SSD**|PASCAL VOC 2007, 2012|`mAP (IoU=0.50)`|
|**SSD**|COCO|`AP@[.5:.05:.95]`; `AP@50`; `AP@75`; <code>AP<sub>S</sub></code>; <code>AP<sub>M</sub></code>; <code>AP<sub>L</sub></code>; <code>AR<sub>1</sub></code>; <code>AR<sub>10</sub></code>; <code>AR<sub>100</sub></code>; <code>AR<sub>S</sub></code>; <code>AR<sub>M</sub></code>; <code>AR<sub>L</sub></code>|
|**SSD**|ImageNet|`mAP (IoU=0.50)`|
|**YOLOv1**|PASCAL VOC 2007, 2012|`AP`; `mAP (IoU=0.50)`|
|**YOLOv1**|Picasso|`AP`; `mAP (IoU=0.50)`|
|**YOLOv1**|People-Art|`AP`; `mAP (IoU=0.50)`|
|**YOLOv2**|PASCAL VOC 2007, 2012|`AP`; `mAP (IoU=0.50)`|
|**YOLOv2**|COCO|`AP@[.5:.05:.95]`; `AP@50`; `AP@75`; <code>AP<sub>S</sub></code>; <code>AP<sub>M</sub></code>; <code>AP<sub>L</sub></code>; <code>AR<sub>1</sub></code>; <code>AR<sub>10</sub></code>; <code>AR<sub>100</sub></code>; <code>AR<sub>S</sub></code>; <code>AR<sub>M</sub></code>; <code>AR<sub>L</sub></code>|
|**YOLOv3**|COCO|`AP@[.5:.05:.95]`; `AP@50`; `AP@75`; <code>AP<sub>S</sub></code>; <code>AP<sub>M</sub></code>; <code>AP<sub>L</sub></code>; <code>AR<sub>1</sub></code>; <code>AR<sub>10</sub></code>; <code>AR<sub>100</sub></code>; <code>AR<sub>S</sub></code>; <code>AR<sub>M</sub></code>; <code>AR<sub>L</sub></code>|
|**YOLOv4**|COCO|`AP@[.5:.05:.95]`; `AP@50`; `AP@75`; <code>AP<sub>S</sub></code>; <code>AP<sub>M</sub></code>; <code>AP<sub>L</sub></code>|
|**YOLOv5**|COCO|`AP@[.5:.05:.95]`; `AP@50`|



* `AP@[.5:.05:.95]`: 
* `AP@50`:
* `AP@75`: 
* `AP`:
* `mAP (IoU=0.50)`:
* <code>AP<sub>S</sub></code>: Average Precision for small object: area < 32<sup>2</sup>
* <code>AP<sub>M</sub></code>: Average Precision for medium object: 32<sup>2</sup> < area < 96<sup>2</sup>
* <code>AP<sub>L</sub></code>: Average Precision for large object: area > 96<sup>2</sup>
* <code>AR<sub>1</sub></code>: Average Recall given 1 detection per image
* <code>AR<sub>10</sub></code>: Average Recall given 10 detections per image
* <code>AR<sub>100</sub></code>: Average Recall given 100 detections per image
* <code>AR<sub>S</sub></code>: Average Recall for small object: area < 32<sup>2</sup>
* <code>AR<sub>M</sub></code>: Average Recall for medium object: 32<sup>2</sup> < area < 96<sup>2</sup>
* <code>AR<sub>L</sub></code>: Average Recall for large object: area > 96<sup>2</sup>




### TO DO:

- [ ] **Calculate Precision**  --Pending--
- [ ] Calculate Recall
- [ ] Calculate AP
- [ ] Calculate mAP
- [ ] Calculate FFPI
- [ ] Calculate MR
