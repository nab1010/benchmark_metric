
import argparse
import glob, os
from re import L
import sys
import cv2

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
    def __init__(self, box_class_name, conf, top, left, width, height):
        # self.idBbox = idBbox
        self.box_class_name = box_class_name
        self.conf = float(conf)
        self.top = float(top)
        self.left = float(left)
        self.width = float(width)
        self.height = float(height)

class bboxGt:
    def __init__(self, box_class_name, top, left, width, height):
        # self.idBbox = idBbox
        self.box_class_name = box_class_name
        self.top = float(top)
        self.left = float(left)
        self.width = float(width)
        self.height = float(height)
        self.used = False

class classData:
    
    def __init__(self, class_name):
        self.class_name = class_name
        self.TP = 0
        self.FP = 0
        self.FN = 0
        self.AP = 0

    def TP_up(self):
        self.TP += 1
    
    def FP_up(self):
        self.FP += 1
    
    def FN_up(self):
        self.FN += 1

class benchmarkData:
    def __init__(self, list_class):
        self.list_class = list_class
        self.class_arr = []
        self.mAP = 0

    def add_class(self, classData):
        self.class_arr.append(classData)


        

# class classProject:



def check_same_class(bboxA, bboxB):
    if bboxA.box_class_name == bboxB.box_class_name:
        return 1, bboxA.box_class_name
    else:
        return 0, bboxA.box_class_name

    



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
    # print("w, h", w, h)
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

def visual_bbox(image, boxA, boxB, color_box): #================================
    if color_box == 'green':
        image = cv2.rectangle(image, (int(boxA.top), int(boxA.left)), (int(boxA.top + boxA.height), int(boxA.left + boxA.width)), (0, 255, 0), 1)
        image = cv2.rectangle(image, (int(boxB.top), int(boxB.left)), (int(boxB.top + boxB.height), int(boxB.left + boxB.width)), (0, 125, 0), 1)
    else:    
        image = cv2.rectangle(image, (int(boxA.top), int(boxA.left)), (int(boxA.top + boxA.height), int(boxA.left + boxA.width)), (0, 0,255), 1)
        image = cv2.rectangle(image, (int(boxB.top), int(boxB.left)), (int(boxB.top + boxB.height), int(boxB.left + boxB.width)), (0, 0,125), 1)
        
    return image


def cal_Precision(args):
    list_class = ['0','1','2','3']
    iou_thresh = 0.5


    listGtFiles = load_gt_file(args) 
    listPredFiles = load_pred_file(args) 
    # print(benchmark_data.class_arr)

    
    benchmark_data = benchmarkData(list_class)                                                      # create benchmark_data class

    for class_name in benchmark_data.list_class:                                        
        new_class = classData(class_name)                                                           # create class data
        benchmark_data.add_class(new_class)                                                         # add all class to benchmark_data


    for i, fileGt in enumerate(sorted(listGtFiles)):                                               # each file .txt
        print(fileGt, sorted(listPredFiles)[i])
        listLinesGt = read_txt_file(fileGt)
        listLinesPred = read_txt_file(sorted(listPredFiles)[i])
        
        image_path = sorted(listPredFiles)[i][:-3] + "jpg" 
        # print(image_path)
       
        image = cv2.imread(image_path) 



        for lineGt in listLinesGt:                                                                      # each grouth truth box
            classNameB, topB, leftB, heightB, widthB = lineGt.split(' ')
            best_iou = 0
            for linePred in listLinesPred:                                                                  # each prediction box
                classNameA, confA, topA, leftA, heightA, widthA = linePred.split(' ')
                # print(classNameA, confA, topA, leftA, widthA, heightA)
                lineBboxPred = bboxPred(classNameA, confA, topA, leftA, widthA, heightA)
                lineBboxGt = bboxGt(classNameB, topB, leftB, widthB, heightB)

                # print(linePred, ' - ', lineGt)
                check, class_name_same = check_same_class(lineBboxPred, lineBboxGt)
                
                
                
                if check:          #each class
                    countTP = 0
                    countFP = 0
                
                    # print("same class")
                    iou = cal_IOU(lineBboxPred, lineBboxGt)
                    if iou > 0:
                        if iou > best_iou:
                            best_iou = iou
                            gt_match = lineBboxGt
                            pred_match = lineBboxPred
                            lineBboxGt.used = True

                        if iou >= iou_thresh:
                            image = visual_bbox(image, lineBboxPred, lineBboxGt, "green")
                            
                            for i in range (len(benchmark_data.class_arr)):
                                # print(classData)
                                if benchmark_data.class_arr[i].class_name == class_name_same:
                                    benchmark_data.class_arr[i].TP_up()
                                print("TP: ", benchmark_data.class_arr[i].TP, "\t - class: ",benchmark_data.class_arr[i].class_name, "\t - iou: ", iou)
                        else:
                            image = visual_bbox(image, lineBboxPred, lineBboxGt, "red")
                            for i in range (len(benchmark_data.class_arr)):
                                # print(classData)
                                if benchmark_data.class_arr[i].class_name == class_name_same:
                                    benchmark_data.class_arr[i].FP_up()
                                print("FP: ", benchmark_data.class_arr[i].FP, "\t - class: ",benchmark_data.class_arr[i].class_name, "\t - iou: ", iou)
                            
        print(benchmark_data.class_arr[0].TP/(benchmark_data.class_arr[0].TP+ benchmark_data.class_arr[0].FP))
        cv2.imshow('image', image)
        cv2.waitKey(0)        
    # cv2.imshow('image', image)
        


            


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





