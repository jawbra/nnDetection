import pickle
import pandas as pd
import matplotlib as pyplot



path = '/home/brandtj/Data/brandtj/nnDetection/models/Task00_roi_main_pathology/RetinaUNetV001_D3V001_3dlr1/fold0/test_predictions/WKAOfNzyFMo$RY2pk8rHxco_boxes.pkl'

with open(path, 'rb') as f:
    data = pickle.load(f)

print(data['pred_boxes'][0])

