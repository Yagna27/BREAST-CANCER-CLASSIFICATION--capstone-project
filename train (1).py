from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory
def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()

    run = Run.get_context()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

    # TODO: Create TabularDataset using TabularDatasetFactory
    # Data is located at:
    # "https://archive.ics.uci.edu/ml/machine-learning-databases/00451/dataR2.csv"

    path_train = "https://archive.ics.uci.edu/ml/machine-learning-databases/00451/dataR2.csv"
    ds = TabularDatasetFactory.from_delimited_files(path=path_train)
    data=ds.to_pandas_dataframe().dropna()
    y=data['Classification']
    x=data
    x.drop("Classification", inplace=True, axis=1)
    # TODO: Split data into train and test sets.

    ### YOUR CODE HERE ###
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.261)

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    run.log("average_precision_score_weighted", np.float(accuracy))

if __name__ == '__main__':
    main()
