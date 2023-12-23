import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier


class ModelTester:
    def __init__(self, categorical_columns: [str], file_name: str, target_column: str, features_override: [str] = None):
        dataframe = pd.read_table(file_name, delimiter=',')
        dataframe.drop(columns=dataframe.columns[0], axis=1, inplace=True)

        target = dataframe[[target_column]]
        features = dataframe.drop([target_column] + categorical_columns, axis=1)

        for categorical in categorical_columns:
            categorical_dummies = pd.get_dummies(dataframe[categorical], prefix=categorical)
            features = pd.concat((features, categorical_dummies), axis=1)

        if features_override is not None:
            features = features[features_override]

        self.features_train, self.features_test, self.target_train, self.target_test = train_test_split(features,
                                                                                                        target,
                                                                                                        test_size=0.1)

    def _run_model_get_accuracy(self, model) -> float:
        model.fit(self.features_train, self.target_train.values.ravel())

        prediction = model.predict(self.features_test)

        accuracy = accuracy_score(self.target_test, prediction)
        return accuracy

    def test_logistic_regression_accuracy(self) -> float:
        model = LogisticRegression(max_iter=400)  # Max iter set to suppress warning (monkey see monkey do)
        return self._run_model_get_accuracy(model)

    def test_decision_tree_accuracy(self, most_important_features_count: int) -> (float, [str]):
        model = DecisionTreeClassifier()
        accuracy = self._run_model_get_accuracy(model)

        importance = model.feature_importances_
        importance_sort_indices = np.argsort(importance)
        features = np.array(self.features_train.columns)
        features_sorted = features[importance_sort_indices]
        if features.size < most_important_features_count:
            most_important_features = features
        else:
            most_important_features = features_sorted[-1 * most_important_features_count:]

        return accuracy, most_important_features

    def test_xgb_classifier_accuracy(self) -> float:
        model = XGBClassifier()
        return self._run_model_get_accuracy(model)
