import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier


class ModelTester:
    def __init__(self, categorical_columns: [str], file_name: str, target_column: str):
        dataframe = pd.read_table(file_name, delimiter=',')

        target = dataframe[[target_column]]
        features = dataframe.drop([target_column] + categorical_columns, axis=1)

        for categorical in categorical_columns:
            categorical_dummies = pd.get_dummies(dataframe[categorical], prefix=categorical)
            features = pd.concat((features, categorical_dummies), axis=1)

        features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.1)

        scaler = StandardScaler()
        self.features_train_scaled = pd.DataFrame(scaler.fit_transform(features_train, target_train))
        self.features_test_scaled = pd.DataFrame(scaler.transform(features_test))
        self.target_train_scaled = pd.DataFrame(scaler.fit_transform(target_train))
        self.target_test_scaled = pd.DataFrame(scaler.transform(target_test))

        label_encoder = LabelEncoder()
        self.target_train_scaled = label_encoder.fit_transform(self.target_train_scaled)
        self.target_test_scaled = label_encoder.fit_transform(self.target_test_scaled)

    def _run_model_get_accuracy(self, model) -> float:
        model.fit(self.features_train_scaled, self.target_train_scaled)

        prediction = model.predict(self.features_test_scaled)

        accuracy = accuracy_score(self.target_test_scaled, prediction)
        return accuracy

    def test_decision_tree_accuracy(self) -> float:
        model = DecisionTreeClassifier()
        return self._run_model_get_accuracy(model)

    def test_xgb_classifier_accuracy(self) -> float:
        model = XGBClassifier()
        return self._run_model_get_accuracy(model)

    def test_logistic_regression_accuracy(self) -> float:
        model = LogisticRegression()
        return self._run_model_get_accuracy(model)


def main():
    file_name = 'titanic_prepared.csv'
    categorical_columns = ['sex']
    target_column = 'label'

    model_tester = ModelTester(categorical_columns, file_name, target_column)

    decision_tree_accuracy = model_tester.test_decision_tree_accuracy()
    print(f'Decision tree accuracy: {decision_tree_accuracy}')

    xgb_accuracy = model_tester.test_xgb_classifier_accuracy()
    print(f'XGBoost accuracy: {xgb_accuracy}')

    logistic_regression_accuracy = model_tester.test_logistic_regression_accuracy()
    print(f'Logistic regression accuracy: {logistic_regression_accuracy}')


main()
