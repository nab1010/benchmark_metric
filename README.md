# Benchmark Metric Object Detection

***@nabang1010***

***SANSlab***


```

├── example
│   ├── json
│   │   └── predict_example.json
│   └── txt
├── gitPush.sh
├── ObjectDetection
│   └── benchmark.py
├── README.md
├── README_metric_benchmark.pdf
└── requirements.txt
```

# Format Image performance metric

```
predict file image_1.txt:

class conf bbox_x bbox_y bbox_w bbox_h

0 0.94 0.133594 0.861574 0.076563 0.243519
0 0.99 0.277865 0.756019 0.054688 0.219444

```
# Format Video performance metric

```
predict file vid_1.txt:

frame class conf bbox_x bbox_y bbox_w bbox_h

1 0 0.94 0.133594 0.861574 0.076563 0.243519
1 0 0.99 0.277865 0.756019 0.054688 0.219444
2 0 0.96 0.541667 0.431481 0.066667 0.118519
2 0 0.94 0.666146 0.526389 0.101042 0.150926

```

benchmark_metric

### TO DO8
- [ ] Calculate IOU
- [ ] Calculate Precision
- [ ] Calculate Recall
- [ ] Calculate AP
- [ ] Calculate mAP
- [ ] Calculate FFPI
- [ ] Calculate MR
