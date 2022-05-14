








import argparse


def parser():
    parser = argparse.ArgumentParser(description="Benchmark Metric Object Detection")
    parser.add_argument("--", type=str, default="",
                        help="video path")
    parser.add_argument("--output_image_path", type=str, default="",
                        help="output image path")
    parser.add_argument("--output_label_path", type=str, default="",
                        help="output label data path")
    parser.add_argument("--num_frame_per_cut", type=int, default=5,
                        help="number frames per cut")
    parser.add_argument("--weight_path", type=str, default="yolov4.weights",
                        help="yolo weights path")
    parser.add_argument("--config_path", type=str, default="./cfg/yolov4.cfg",
                        help="path to config file")
    parser.add_argument("--data_file", type=str, default="./cfg/coco.data",
                        help="path to data file")
    parser.add_argument("--thresh", type=float, default=.5,
                        help="remove detections with confidence below this value")
    return parser.parse_args()



def cal_IOU():
    return 0

    
def cal_IOU():
    return 0
def cal_IOU():
    return 0
def cal_IOU():
    return 0











def main():
    args = parser()
    return 0



if __name__ == '__main__':
    main()





