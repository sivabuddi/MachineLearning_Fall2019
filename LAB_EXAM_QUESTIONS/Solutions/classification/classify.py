from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB


def support_vector_machine(x_train, y_train, x_test):
    '''
    Function : Support Vector Machine Classification
    :param x_train:
    :param y_train:
    :param x_test:
    :return:
    '''
    svc_linear = SVC(kernel='linear')
    svc_linear.fit(
        x_train,
        y_train
    )
    y_test = svc_linear.predict(x_test)
    acc_svc = round(svc_linear.score(x_train, y_train) * 100, 2)
    print("linear svm accuracy is:", acc_svc)
    ################
    svc_rbf = SVC(kernel='rbf')
    svc_rbf.fit(
        x_train,
        y_train
    )
    y_test = svc_rbf.predict(x_test)
    acc_svc = round(svc_rbf.score(x_train, y_train) * 100, 2)
    print("rbf kernel svm accuracy is:", acc_svc)


def nearest_neighbor(x_train, y_train, x_test):
    '''
    Function: Nearest Neighbhor classification
    :param x_train:
    :param y_train:
    :param x_test:
    :return:
    '''
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(x_train, y_train)
    Y_pred = knn.predict(x_test)
    Y_prob = knn.predict_proba(x_test)
    acc_knn = round(knn.score(x_train, y_train) * 100, 2)
    print("KNN accuracy is:", acc_knn)


def bayes_classifier(x_train, y_train, x_test):
    '''
    Function : Naive Bayes Classifier
    :param x_train:
    :param y_train:
    :param x_test:
    :return:
    '''
    gauss = GaussianNB()
    gauss.fit(
        x_train,
        y_train
    )

    y_pred = gauss.predict(x_test)
    acc_knn = round(gauss.score(x_train, y_train) * 100, 2)
    print("Bayes Classifier accuracy is:", acc_knn)
