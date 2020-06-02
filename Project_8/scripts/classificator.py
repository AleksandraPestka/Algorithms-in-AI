''' Classify data from XML file using DBSCAN clustering algorithm. '''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import KernelPCA

from preprocessing import XML_to_dict, dict_to_dataframe

def remove_outliers(df):
    numeric_columns = ['num_contrib', 'year', 'num_pages']
    z_scores = stats.zscore(df[numeric_columns])
    filtered_entries = (np.abs(z_scores) < 3).all(axis=1)
    new_df = df[filtered_entries]
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
    ax.set_xlabel('PCA 1st component')
    ax.set_ylabel('PCA 2nd component')
    plt.show()

def clustering(df):
    # get the numerical values
    num_vals = df[[col for col in df_cleaned.columns if col!='title']].values
    
    print(f'[INFO] Reducing dimensions to 2D using PCA ')
    pca = KernelPCA(n_components=2, kernel='rbf')
    data_2D = pca.fit_transform(num_vals)
    #print(f'[INFO] Explained variance ratio: {pca.explained_variance_ratio_}')

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

    plot2D_data(data_2D, labels)
    plot3D_data(df_cleaned, labels)