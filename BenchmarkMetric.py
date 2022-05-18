
import argparse


def parser():
    parser = argparse.ArgumentParser(description="Benchmark Metric Object Detection")
    parser.add_argument("-pred","--pred_path",
                        dest="pred_path",
                        type=str, 
                        default="",
                        help="prediction folder path")
    parser.add_argument("-gt","--gt_path", 
                        dest="gt_path",
                        type=str, 
                        default="",
                        help="ground truth folder path")
    parser.add_argument("-pred_format","--pred_format", 
                        dest="pred_format",
                        type=str, 
                        default="",
                        help="type prediction file")
    parser.add_argument("-gt_format","--gt_format", 
                        dest="gt_format",
                        type=str, 
                        default="",
                        help="type ground truth file")
    parser.add_argument("-iou","--iou",
                        dest="cal_IOU", 
                        default=False,
                        help="calculate IOU - Intersection Over Union")
    parser.add_argument("-precision","--precision", 
                        dest="cal_Precision",
                        default=False,
                        help="calculate Precision")
    parser.add_argument("-recall","--recall", 
                        dest="cal_Recall",
                        default=False,
                        help="calculate Recall")
    parser.add_argument("-ap","--ap",
                        dest="cal_AP", 
                        default=False,
                        help="calculate Average Precision")
    parser.add_argument("-map","--map", 
                        dest="cal_mAP",
                        default=False,
                        help="calculate mean Average Precision")
    parser.add_argument("-ffpi","--ffpi",
                        dest="cal_FFPI", 
                        default=False,
                        help="calculate False Positive Per Image")
    parser.add_argument("-mr","--mr",
                        dest="cal_MR",
                        default=False,
                        help="calculate Miss Rate")
    parser.add_argument("-graph","--graph",
                        dest="draw_graph", 
                        default=False,
                        help="draw graph")
    return parser.parse_args()



# def cal_IOU(boxGt, boxPred):
#     float I = cal_box_intersection(boxGt, boxPred)
#     float U = cal_box_union(boxGt, boxPred)
#     if ((I == 0) or (U == 0)):
#         return 0
#     else:
#         return I/U
         
# def cal_box_intersection(boxA, boxB):
#     return 0

# def cal_box_union():
#     return 0






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


def loadTXTFile(args):
    
    return 0








def main():
    args = parser()
    print(args.pred_path)
    
    
    return 0



if __name__ == '__main__':
    main()





