import matplotlib.pyplot as plt
import seaborn as sns

#================================
# SCATTER PLOT FUNCTION
#================================
def scatter_plot(df):
    sns.scatterplot(data = df , x ="sepal.length", y = "sepal.width", hue = "variety")
    plt.title("Scatter Plot of Sepal Length vs Sepal Width")
    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")
    plt.show()

#================================
# HISTOGRAMS FUNCTION
#================================
def histograms(df):
    df.hist(figsize=(10,8))
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.suptitle("Histograms of Iris Dataset Features")
    plt.show()

#================================
# BOXPLOT FUNCTION
#================================
def boxplot(df):
    sns.boxplot(data=df)
    plt.title("Boxplot of Iris Dataset Features")
    plt.xlabel("Features")
    plt.ylabel("Value")
    plt.show()

#--------SOME ADVANCED VISUALIZATION FUNCTIONS BELOW--------#

#================================
# PAIRPLOT FUNCTION
#================================
def pairplot(df):
    sns.pairplot(df,hue = "variety")
    plt.title("Pairplot of Iris Dataset Features")
    plt.xlabel("Features")
    plt.ylabel("Features")
    plt.show()

#================================
# CORRELATION HEATMAP FUNCTION
#================================
def correlation_heatmap(df):
    plt.figure(figsize = (8,6))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
    plt.title("Correlation Heatmap of Iris Dataset Features")
    plt.xlabel("Features")
    plt.ylabel("Features")
    plt.show()



# import matplotlib.pyplot as plt
# import seaborn as sns

# def scatter_plot(df):
#     sns.scatterplot(data=df, x='sepal_length', y='sepal_width', hue='species')
#     plt.show()

# def histograms(df):
#     df.hist(figsize=(10,8))
#     plt.show()

# def boxplot(df):
#     sns.boxplot(data=df)
#     plt.show()