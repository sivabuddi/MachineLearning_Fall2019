"""
problem 5 :
a. Perform exploratory data analysis on the data set (like Handling null values, removing  the  features
not  correlated  to  the  target  class,  encoding  the categorical features, ...)
b. Apply the three classification algorithms Naïve Bayes, SVM and KNN on thechosen data set and report
which classifier gives better result.
"""
import pandas as pd
import seaborn as sns
from classification.classify import support_vector_machine
from classification.classify import bayes_classifier
from classification.classify import nearest_neighbor

train_data = pd.read_csv("./train.csv")
test_data = pd.read_csv("./test.csv")

# Converting Sex into 1 or 0 as we would require numericals to analysis.
train_data['Sex'] = train_data['Sex'].map({"male": 0, "female": 1})
test_data['Sex'] = test_data['Sex'].map({"male": 0, "female": 1})

train_data['Embarked'] = train_data['Embarked'].map({"S": 0, "Q": 1, "C": 2})
test_data['Embarked'] = test_data['Embarked'].map({"S": 0, "Q": 1, "C": 2})

# Dropping Passenger ID as its not relavant.
train_data = train_data.drop(['PassengerId', 'Cabin'], axis=1)
test_data = test_data.drop(['PassengerId', 'Cabin'], axis=1)

##Analyze by pivoting features ---> the higher the number means more correlation with the target
print(train_data[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Survived',
                                                                                                ascending=False))
print(
    train_data[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False))
print(train_data[["SibSp", "Survived"]].groupby(['SibSp'], as_index=False).mean().sort_values(by='Survived',
                                                                                              ascending=False))
print(train_data[["Parch", "Survived"]].groupby(['Parch'], as_index=False).mean().sort_values(by='Survived',
                                                                                              ascending=False))

corr_matrix = train_data.corr()
print(corr_matrix)

sns.heatmap(corr_matrix, xticklabels=corr_matrix.columns, yticklabels=corr_matrix.columns, annot=True)
print("Correlation values for the best case scenario")
print(corr_matrix['Survived'].sort_values(ascending=False)[1:4])
print("Correlation values for the worst case scenario")
print(corr_matrix['Survived'].sort_values(ascending=True)[:3])

# Dropping Passenger ID as its not relavant.
train_data = train_data.drop(['Pclass', 'Age', 'SibSp', 'Name', 'Ticket'], axis=1)
test_data = test_data.drop(['Pclass', 'Age', 'SibSp', 'Name', 'Ticket'], axis=1)

train_data = train_data.dropna()
test_data = test_data.dropna()

x_train = train_data.drop(['Survived'], axis=1)
y_train = train_data['Survived']

support_vector_machine(x_train, y_train, test_data)
bayes_classifier(x_train, y_train, test_data)
nearest_neighbor(x_train, y_train, test_data)
