
import argparse
import glob, os
import sys


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

def check_path(args):
    if not os.path.exists(args.pred_path) and not os.path.exists(args.gt_path):
        errorMessage = "[ERROR]: Folder prediction: " + args.gt_path + " and folder gt: "  + args.gt_path +  " not exist"
        sys.exit(errorMessage)
    elif not os.path.exists(args.pred_path):
        errorMessage = "[ERROR]: Folder prediction: " + args.pred_path + " not exist"
        sys.exit(errorMessage)
    elif not os.path.exists(args.gt_path):
        errorMessage = "[ERROR]: Folder ground truth: " + args.gt_path + " not exist"
        sys.exit(errorMessage)

def check_format(args):
    listFormat = ["txt", "xml ", "json"]
    checkPredFormat = False
    for typeFormat in listFormat:
        if args.pred_format == typeFormat:
            checkPredFormat = True
    if not checkPredFormat:
        errorMessage = "Format prediciton [" + args.pred_format + "] not suport"
        sys.exit(errorMessage)
    checkGtFormat = False
    for typeFormat in listFormat:
        if args.gt_format == typeFormat:
            checkGtFormat = True
    if not checkGtFormat:
        errorMessage = "Format ground truth [" + args.gt_format + "] not suport"
        sys.exit(errorMessage)



class bboxPred:
    def __init__(self, className, conf, top, left, width, height):
        # self.idBbox = idBbox
        self.className = className
        self.conf = float(conf)
        self.top = float(top)
        self.left = float(left)
        self.width = float(width)
        self.height = float(height)

class bboxGt:
    def __init__(self, className, top, left, width, height):
        # self.idBbox = idBbox
        self.className = className
        self.top = float(top)
        self.left = float(left)
        self.width = float(width)
        self.height = float(height)



def check_same_class(bboxA, bboxB):
    if bboxA.className == bboxB.className:
        return 1
    else:
        return 0
    

def cal_overlap(x1, w1, x2, w2):
    r1 = x1 + w1
    r2 = x2 + w2
    if(x1 > x2):
        left = x1
    else:
        left = x2
    if(r1 < r2):
        right = r1
    else:
        right = r2
    return right - left
         
def cal_box_intersection(boxA, boxB):
    w = cal_overlap(boxA.left, boxA.width, boxB.left, boxB.width)
    h = cal_overlap(boxA.top, boxA.height, boxB.top, boxB.height)
    print("w, h", w, h)
    if((w < 0) or (h < 0)):
        return 0
    areaOverlap = w * h
    return areaOverlap

def cal_box_union(boxA, boxB):
    interArea = cal_box_intersection(boxA, boxB)
    return (boxA.width*boxA.height + boxB.width*boxB.height) - interArea


def cal_IOU(boxA, boxB):
    I = cal_box_intersection(boxA, boxB)
    U = cal_box_union(boxA, boxB)
    if ((I == 0) or (U == 0)):
        return 0
    else:
        return I/U


def visual_bbox(boxA, boxB):
    return 0

def cal_Precision(args):
    listGtFiles = load_gt_file(args) 
    listPredFiles = load_pred_file(args) 


    for i, fileGt in enumerate(sorted(listGtFiles)):               #each file .txt
        print(fileGt, sorted(listPredFiles)[i])
        listLinesGt = read_txt_file(fileGt)
        listLinesPred = read_txt_file(sorted(listPredFiles)[i])
        


        for linePred in listLinesPred:
            for lineGt in listLinesGt:
                classNameA, confA, topA, leftA, widthA, heightA = linePred.split(' ')
                classNameB, topB, leftB, widthB, heightB = lineGt.split(' ')
                lineBboxPred = bboxPred(classNameA, confA,topA, leftA, widthA, heightA)
                lineBboxGt = bboxGt(classNameB, topB, leftB, widthB, heightB)

                # print(linePred, ' - ', lineGt)
                if check_same_class(lineBboxPred, lineBboxGt):          #each class
                    countTP = 0
                    countFP = 0
                
                    print("same class")
                    iou = cal_IOU(lineBboxPred, lineBboxGt)
                    print("IoU", iou)
                
                
        


            


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


    




def load_pred_file(args):
    filePath = args.pred_path + "/*."  + args.pred_format 
    files =  glob.glob(filePath)
    return files

def load_gt_file(args):
    filePath = args.gt_path + "/*." + args.gt_format 
    files =  glob.glob(filePath)
    return files


def read_txt_file(file):
    TXTFileData = open(file, 'r')
    lines = TXTFileData.read().splitlines()
    return lines







def main():
    args = parser()

    check_path(args)

    check_format(args)

    if args.cal_Precision:
        cal_Precision(args)
    # print(args.pred_path)
    
    # print(listPredFiles)
    # print(listGtFiles)
    
    
    return 0



if __name__ == '__main__':
    main()





