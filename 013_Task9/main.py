import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


def load_and_scale(categorical_columns: [str], file_name: str, target_column: str) \
        -> (pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame):
    dataframe = pd.read_table(file_name, delimiter=',')

    target = dataframe[[target_column]]
    features = dataframe.drop([target_column] + categorical_columns, axis=1)

    for categorical in categorical_columns:
        categorical_dummies = pd.get_dummies(dataframe[categorical], prefix=categorical)
        features = pd.concat((features, categorical_dummies), axis=1)

    features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.1)

    scaler = StandardScaler()
    features_train_scaled = pd.DataFrame(scaler.fit_transform(features_train, target_train))
    features_test_scaled = pd.DataFrame(scaler.transform(features_test))
    target_train_scaled = pd.DataFrame(scaler.fit_transform(target_train))
    target_test_scaled = pd.DataFrame(scaler.transform(target_test))
    return features_train_scaled, features_test_scaled, target_train_scaled, target_test_scaled


def main():
    file_name = 'titanic_prepared.csv'
    categorical_columns = ['sex']
    target_column = 'label'

    features_train_scaled, features_test_scaled, target_train_scaled, target_test_scaled \
        = load_and_scale(categorical_columns, file_name, target_column)

    print(pd.concat((features_test_scaled, target_test_scaled), axis=1))

    # TODO: Learn models and check accuracy

    pass


main()
