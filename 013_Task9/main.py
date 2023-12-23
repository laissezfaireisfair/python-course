from ModelTester import ModelTester


def main():
    file_name = 'titanic_prepared.csv'
    categorical_columns = ['sex']
    target_column = 'label'
    most_important_features_count = 2

    tester = ModelTester(categorical_columns, file_name, target_column)

    decision_tree_accuracy, most_important_features = tester.test_decision_tree_accuracy(
        most_important_features_count)
    print(f'Decision tree accuracy: {decision_tree_accuracy:.3f}')
    important_features_str = ', '.join(most_important_features)
    print(f'Most important features: {important_features_str}')

    xgb_accuracy = tester.test_xgb_classifier_accuracy()
    print(f'XGBoost accuracy: {xgb_accuracy:.3f}')

    logistic_regression_accuracy = tester.test_logistic_regression_accuracy()
    print(f'Logistic regression accuracy: {logistic_regression_accuracy:.3f}')

    tester_for_important = ModelTester(categorical_columns, file_name, target_column, most_important_features)

    decision_tree_accuracy_important_only, _ = tester_for_important.test_decision_tree_accuracy(
        most_important_features_count)
    print(f'Decision tree IMPORTANT FEATURES ONLY accuracy: {decision_tree_accuracy_important_only:.3f}')


main()
