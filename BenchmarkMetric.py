
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

class bboxPred:
    def __init__(self, idBbox, className, conf, top, left, width, height):
        self.idBbox = idBbox
        self.className = className
        self.conf = conf
        self.top = top
        self.left = left
        self.width = width
        self.height = height


def checkSameClass(bboxPred, bboxGt):
    classNameBboxPred = bboxPred.split(' ')[0]
    classNameBboxGt = bboxGt.split(' ')[0]
    if classNameBboxPred == classNameBboxGt:
        return 1
    else:
        return 0
    

# def checkOverLap(bboxA, bboxB):
#     topA, leftA, widthA, heightA = bboxA.split(' '):
#     topB, leftB, widthB, heightB = bboxB.split(' '):




def cal_Precision(args):
    listGtFiles = loadGtFile(args)
    listPredFiles = loadPredFile(args)

    for filePred in listPredFiles:
        listLinesPred = readTXTFile(filePred)
        for linePred in listLinesPred:
            print(linePred)




    for fileGt in listGtFiles:
        listLinesGt = readTXTFile(fileGt)
        for lineGt in listLinesGt:
            print(lineGt)


            
    for linePred in listLinesPred:
        for lineGt in listLinesGt:
            # print(linePred, ' - ', lineGt)
            checkSameClass(linePred, lineGt)
            


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

def checkPath(args):
    if not os.path.exists(args.pred_path) and not os.path.exists(args.gt_path):
        errorMessage = "[ERROR]: Folder prediction: " + args.gt_path + " and folder gt: "  + args.gt_path +  " not exist"
        sys.exit(errorMessage)
    elif not os.path.exists(args.pred_path):
        errorMessage = "[ERROR]: Folder prediction: " + args.pred_path + " not exist"
        sys.exit(errorMessage)
    elif not os.path.exists(args.gt_path):
        errorMessage = "[ERROR]: Folder gt: " + args.gt_path + " not exist"
        sys.exit(errorMessage)

def checkFormat(args):
    listFormat = ["txt", "xml ", "json"]
    checkPredFormat = False
    for typeFormat in listFormat:
        if args.pred_format == "txt" or args.pred_format == "xml" or args.pred_format == "json":
            checkPredFormat = True

    




def loadPredFile(args):
    filePath = args.pred_path + "/*."  + args.pred_format 
    files =  glob.glob(filePath)
    return files

def loadGtFile(args):
    filePath = args.gt_path + "/*." + args.gt_format 
    files =  glob.glob(filePath)
    return files

def readTXTFile(file):
    TXTFileData = open(file, 'r')
    lines = TXTFileData.read().splitlines()
    return lines







def main():
    args = parser()
    checkPath(args)
    checkFormat(args)
    if args.cal_Precision:
        cal_Precision(args)
    # print(args.pred_path)
    
    # print(listPredFiles)
    # print(listGtFiles)
    
    
    return 0



if __name__ == '__main__':
    main()





