import pandas as pd
import datetime
import time
import pickle
import numpy as np

class ModelHelper():
    def __init__(self):
        pass

    def makePredictions(self, concave_points_worst_bins, perimeter_worst_bins, concave_points_mean_bins, radius_worst_bins):
        concave_points_worst_bins_A=0
        concave_points_worst_bins_B=0
        concave_points_worst_bins_C=0
        concave_points_worst_bins_D=0

        perimeter_worst_bins_A=0
        perimeter_worst_bins_B=0
        perimeter_worst_bins_C=0
        perimeter_worst_bins_D=0

        concave_points_mean_bins_A=0
        concave_points_mean_bins_B=0
        concave_points_mean_bins_C=0
        concave_points_mean_bins_D=0

        radius_worst_bins_A=0
        radius_worst_bins_B=0 
        radius_worst_bins_C=0
        radius_worst_bins_D=0


     
         # parse pclass
        if (concave_points_worst_bins == "A"):
            concave_points_worst_bins_A = 1
        elif (concave_points_worst_bins == "B"):
            concave_points_worst_bins_B = 1
        elif (concave_points_worst_bins == "C"):
            concave_points_worst_bins_C = 1
        elif (concave_points_worst_bins == "D"):
            concave_points_worst_bins_D = 1
        else:
            pass

        # parse embarked
        if (perimeter_worst_bins == "A"):
            perimeter_worst_bins_A = 1
        elif (perimeter_worst_bins == "B"):
            perimeter_worst_bins_B = 1
        elif (perimeter_worst_bins == "C"):
            perimeter_worst_bins_C = 1
        elif (perimeter_worst_bins == "D"):
            perimeter_worst_bins_D = 1
        else:
            pass

        if (concave_points_mean_bins == "A"):
            concave_points_mean_bins_A = 1
        elif (concave_points_mean_bins == "B"):
            concave_points_mean_bins_B = 1
        elif (concave_points_mean_bins == "C"):
            concave_points_mean_bins_C = 1
        elif (concave_points_mean_bins == "D"):
            concave_points_mean_bins_D = 1
        else:
            pass

        if (radius_worst_bins == "A"):
            radius_worst_bins_A = 1
        elif (radius_worst_bins == "B"):
            radius_worst_bins_B = 1
        elif (radius_worst_bins == "C"):
            radius_worst_bins_C = 1
        elif (radius_worst_bins == "D"):
            radius_worst_bins_D = 1
        else:
            pass


     

       

        
        input_pred = [[concave_points_worst_bins_B,concave_points_worst_bins_C, concave_points_worst_bins_D, perimeter_worst_bins_B, perimeter_worst_bins_C,perimeter_worst_bins_D, concave_points_mean_bins_B,concave_points_mean_bins_C, concave_points_mean_bins_D,radius_worst_bins_B, radius_worst_bins_C, radius_worst_bins_D]]

        filename = 'finalized_model.sav'
        reg_load = pickle.load(open(filename, 'rb'))
        

        X = np.array(input_pred)
        preds = reg_load.predict_proba(X)
        preds_singular = reg_load.predict(X)

        return preds_singular[0]