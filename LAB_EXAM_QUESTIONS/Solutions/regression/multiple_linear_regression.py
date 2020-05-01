'''
problem 8: Linear Data regression
'''

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from regression.map_utils import scatter_plot
from regression.map_utils import heat_map

wine_data = pd.read_csv('winequality-red.csv')
# Clean data for None
wine_data = wine_data.dropna()
corr_matrix = wine_data.corr()
#heat_map(corr_matrix)
print("Correlation values for the best case scenario")
print(corr_matrix['quality'].sort_values(ascending=False)[1:4])
print("Correlation values for the worst case scenario")
print(corr_matrix['quality'].sort_values(ascending=True)[:3])


def prediction_with_best_features():
    # considering the best features.
    features = pd.DataFrame(wine_data, columns=['alcohol', 'sulphates', 'citric acid'])
    results = wine_data['quality']
    train_features, test_features, train_results, test_results_actuals = train_test_split(features, results,
                                                                                          random_state=42,
                                                                                          test_size=0.33)
    linear_regression = LinearRegression()
    model = linear_regression.fit(train_features, train_results)
    test_results_predicted = model.predict(test_features)

    print('r squared for best correlated features:', r2_score(test_results_actuals, test_results_predicted))
    print('RMSE for best correlated features: ', mean_squared_error(test_results_actuals, test_results_predicted))

    scatter_plot(test_results_predicted, test_results_actuals, 'Predicted Price', 'Actual Price',
                 'Linear Regression Model (Best Correlated features')


def prediction_with_all_features():
    # considering the best features.
    features = wine_data.drop(['quality'], axis=1)
    results = wine_data['quality']
    train_features, test_features, train_results, test_results_actuals = train_test_split(features, results,
                                                                                          random_state=42,
                                                                                          test_size=0.33)
    linear_regression = LinearRegression()
    model = linear_regression.fit(train_features, train_results)
    test_results_predicted = model.predict(test_features)

    print('r squared for best correlated features:', r2_score(test_results_actuals, test_results_predicted))
    print('RMSE for all features: ', mean_squared_error(test_results_actuals, test_results_predicted))

    scatter_plot(test_results_predicted, test_results_actuals, 'Predicted Price', 'Actual Price',
                 'Linear Regression Model (all features)')


prediction_with_best_features()
prediction_with_all_features()
