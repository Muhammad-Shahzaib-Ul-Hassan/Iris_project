from load_data import load_iris_data
from visualize import scatter_plot, histograms, boxplot, pairplot, correlation_heatmap

def main():
    df = load_iris_data()

    #================================
    # PRINTING SHAPE AND COLUMN NAMES
    #================================
    print("1. SHAPE OF THE DATASET:", df.shape)
    print("\n2. COULUMN NAMES:", df.columns)

    #================================
    # PRINTING FIRST 5 ROWS OF THE DATASET
    #================================
    print("\n3. FIRST 5 ROWS OF THE DATASET:")
    print(df.head())

    #================================
    # PRINTING DATA TYPES OF EACH COLUMN
    #================================
    print("\n4. DATA TYPES OF EACH COLUMN:")
    print(df.info())

    #================================
    # PRINTING STATISTICAL SUMMARY OF THE DATASET
    #================================
    print("\n5. STATISTICAL SUMMARY OF THE DATASET:")
    print(df.describe())

    #-------EXTRA: CHECKING FOR MISSING VALUES-------#

    #================================
    # CHECKING FOR MISSING VALUES  
    #================================
    print("\n6. CHECKING FOR MISSING VALUES:")
    print(df.isnull().sum())

    #================================
    # CALLING VISUALIZATION FUNCTIONS   
    #================================

    #-----SCATTER PLOT-----#
    scatter_plot(df)
    #-----HISTOGRAMS-----#
    histograms(df)
    #-----BOXPLOT-----#
    boxplot(df)
    #-----PAIRPLOT (ADVANCED VISUALIZATION)-----#
    pairplot(df)
    #-----CORRELATION HEATMAP (ADVANCED VISUALIZATION)-----#
    correlation_heatmap(df)
if __name__ == "__main__":
    main()


# from load_data import load_iris_data
# from visualize import scatter_plot, histograms, boxplot

# def main():
#     df = load_iris_data()


#     print(df.head())
#     print(df.info())
#     print(df.describe())

#     scatter_plot(df)
#     histograms(df)
#     boxplot(df)

# if __name__ == "__main__":
#     main()