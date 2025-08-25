# This script does some basic data processing such as removing duplicates, transforming the target column into a column containing two labels, one hot encoding, and an 80-20 split to produce training and test datasets.

import argparse
import os
import warnings
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelBinarizer, KBinsDiscretizer
from sklearn.preprocessing import PolynomialFeatures
from sklearn.compose import make_column_transformer

from sklearn.exceptions import DataConversionWarning

warnings.filterwarnings(action="ignore", category=DataConversionWarning)


columns = [
    "sex",
    "length",
    "diameter",
    "height",
    "whole_weight",
    "shucked_weight",
    "viscera_weight",
    "shell_weight",
    "rings"
]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-test-split-ratio", type=float, default=0.3)
    args, _ = parser.parse_known_args()

    input_data_path = os.path.join("/opt/ml/processing/input", "abalone_data.csv")

    # Downloading the data from S3 into a Dataframe
    df = pd.read_csv(input_data_path)
    df = pd.DataFrame(data=df, columns=columns)

    # Dropping the duplicates
    df.drop_duplicates(inplace=True)

    # Split the dataset into 80-20 train and test datasets
    split_ratio = args.train_test_split_ratio
    X_train, X_test, y_train, y_test = train_test_split(
        df.drop("rings", axis=1), df["rings"], test_size=split_ratio, random_state=0
    )

    # Running preprocessing and feature engineering transformations
    train_features = X_train
    test_features = X_test

    # Saving Train and Test processed data to output locations
    train_features_output_path = os.path.join("/opt/ml/processing/train", "train_features.csv")
    train_labels_output_path = os.path.join("/opt/ml/processing/train", "train_labels.csv")

    test_features_output_path = os.path.join("/opt/ml/processing/test", "test_features.csv")
    test_labels_output_path = os.path.join("/opt/ml/processing/test", "test_labels.csv")

    pd.DataFrame(train_features).to_csv(train_features_output_path, header=False, index=False)

    pd.DataFrame(test_features).to_csv(test_features_output_path, header=False, index=False)

    y_train.to_csv(train_labels_output_path, header=False, index=False)

    y_test.to_csv(test_labels_output_path, header=False, index=False)