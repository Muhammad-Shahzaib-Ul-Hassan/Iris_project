import pandas as pd
import seaborn as sns
# ==================================
# THIS FUNCTION IS FOR DATA LOADING FROM IRIS DATASET
# ==================================
def load_iris_data():
    #================================
    # LOADING THE IRIS DATASET
    #================================
    #df = sns.load_dataset('iris')
    #--------------OR----------------
    df = pd.read_csv("iris.csv")
    return df