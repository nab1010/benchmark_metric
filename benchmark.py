








import argparse


def parser():
    parser = argparse.ArgumentParser(description="Benchmark Metric Object Detection")
    parser.add_argument("--pred_path", type=str, default="",
                        help="prediction folder path")
    parser.add_argument("--gt_path", type=str, default="",
                        help="ground truth folder path")
    parser.add_argument("--type_pred_file", type=str, default="",
                        help="type ground truth file")
    parser.add_argument("--type_gt_file", type=int, default=5,
                        help="type prediction file")
    parser.add_argument("--iou", default=False,
                        help="calculate IOU - Intersection Over Union")
    parser.add_argument("--precision", default=False,
                        help="calculate Precision")
    parser.add_argument("--recall", default=False,
                        help="calculate Recall")
    parser.add_argument("--ap", default=False,
                        help="calculate Average Precision")
    parser.add_argument("--map", default=False,
                        help="calculate mean Average Precision")
    parser.add_argument("--ffpi", default=False,
                        help="calculate False Positive Per Image")
    parser.add_argument("--mr", default=False,
                        help="calculate Miss Rate")
    parser.add_argument("--graph", default=True,
                        help="draw graph")
    return parser.parse_args()



def cal_IOU():
    return 0


def cal_Precision():
    return 0


def cal_Recall():
    return 0
def cal_AP():
    return 0
def cal_mAP():
    return 0
def cal_FFPI():
    return 0
def cal_MR():
    return 0











def main():
    args = parser()
    print(args)
    
    
    return 0



if __name__ == '__main__':
    main()



1

