''' Classify data from XML file using DBSCAN clustering algorithm. '''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from scipy import stats
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from preprocessing import XML_to_dict, dict_to_dataframe

def remove_outliers(df):
    numeric_columns = ['num_contrib', 'year', 'num_pages']
    z_scores = stats.zscore(df[numeric_columns])

    # remove rows with values > 3 * std
    filtered_entries = (np.abs(z_scores) <= 3).all(axis=1)
    new_df = df[filtered_entries]

    # remove rows with num_pages > 100
    new_df = df[df.num_pages<100]
    return new_df

def plot3D_data(df, labels=None):
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.scatter3D(df['num_contrib'], df['year'], df['num_pages'], c=labels)
    ax.set_xlabel('number of contributors')
    ax.set_ylabel('year')
    ax.set_zlabel('number of pages')
    plt.show()

def plot2D_data(data, labels=None):
    fig = plt.figure()
    ax = plt.axes()
    ax.scatter(data[:, 0], data[:,1], c=labels)
    ax.set_xlabel('feature 1')
    ax.set_ylabel('feature 2')
    plt.show()

def plot_year_distribution(df, col_name, xlabel, bins=100):
    ax = plt.figure().gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.hist(df[col_name], bins=bins)
    plt.ylabel('number of publications')
    plt.xlabel(xlabel)
    plt.show()

def clustering(df):
    # get the numerical values
    num_vals = df[[col for col in df_cleaned.columns if col!='title']].values
    
    # reduce data to 2 dims
    data_2D = num_vals[:, :2]

    # standardize each column (feature) 
    print(f'[INFO] Standarization of features')
    data_2D = StandardScaler().fit_transform(data_2D)

    # compute DBSCAN
    print(f'[INFO] Clusterization using DBSCAN algorithm')
    db = DBSCAN(eps=0.5, min_samples=10).fit(data_2D)
    labels = db.labels_

    return data_2D, labels

if __name__ == '__main__':
    dict_list = XML_to_dict('../data/dataset publications - ready.xml')
    df = dict_to_dataframe(dict_list)
    df_cleaned = remove_outliers(df)

    # data visualization
    plot3D_data(df_cleaned)

    data_2D, labels = clustering(df_cleaned)

    # Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise_ = list(labels).count(-1)

    print(f'Estimated number of clusters: {n_clusters_}')
    print(f'Estimated fraction of noise points: {(n_noise_/len(labels)):.2f}')

    # plot clusters in 2D and 3D
    plot2D_data(data_2D, labels)
    plot3D_data(df_cleaned, labels)

    plot_year_distribution(df_cleaned, 'year', 'year of publication')
    plot_year_distribution(df_cleaned, 'num_contrib', 'number of contributors')
    plot_year_distribution(df_cleaned, 'num_pages', 'number of pages', bins=10)
