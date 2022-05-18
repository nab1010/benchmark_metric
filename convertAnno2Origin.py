import glob, os
import cv2



def convert2original(image, x, y, w, h):

    image_h, image_w, __ = image.shape

    orig_x       = int(x * image_w)
    orig_y       = int(y * image_h)
    orig_width   = int(w * image_w)
    orig_height  = int(h * image_h)

    bbox_converted = (orig_x, orig_y, orig_width, orig_height)

    return bbox_converted




def main():
    gtPath = "/home/nab/Desktop/Benchmark_Metric_Object_Detection/example/gt"
    annoPath = "/home/nab/Desktop/Benchmark_Metric_Object_Detection/anno"
    os.chdir(annoPath)
    for file in glob.glob("*.txt"):
        print(file[0:9])
        gtFilePath = gtPath + '/' + file
        annoFilePath = annoPath + '/' + file
        imageFilePath = annoPath + '/' + file[0:9] + ".jpg"
        image = cv2.imread(imageFilePath)
        gtFile =  open(gtFilePath, 'w')
        annoData  = open(annoFilePath, 'r')
        lines = annoData.read().splitlines()
        for line in lines:
            classId, bbox_x, bbox_y, bbox_w, bbox_h = line.split(' ')
            x, y, w, h = convert2original(image, float(bbox_x), float(bbox_y), float(bbox_w), float(bbox_h))
            newLine = classId + ' ' + str(int(x - w / 2.)) + " " + str(int(y - h / 2.)) + " " + str(w) + " " + str(h) + "\n"
            # print(newLine)
            gtFile.write(newLine)
    gtFile.close()    





if __name__ == '__main__':
    main()
