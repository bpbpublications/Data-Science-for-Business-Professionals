from sklearn.model_selection import train_test_split
X_train_num, X_val_num, y_train_num, y_val_num = train_test_split(X_n, y_n, test_size=0.3, random_state=1)


# Bernoulli
from sklearn.naive_bayes import BernoulliNB
clf = BernoulliNB()
clf.fit(X_train_num, y_train_num)

from sklearn import metrics
from sklearn.metrics import mean_squared_error
prediction_train = clf.predict(X_val_num)
mat_n = metrics.confusion_matrix(y_val_num, prediction_train)
mat_n
print (metrics.accuracy_score(y_val_num, prediction_train))

# Baseline accuracy
1-(sum(y_val_num)/len(y_val_num))
# sum(prediction_train)

def models(l):
    # Counting the occurence of each word in the corpus
    from sklearn.feature_extraction.text import CountVectorizer
    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(l)
    count_vect.get_feature_names()
    X_matrix= X_train_counts.todense()

    y = np.array(data_train1['target'])

    # Creating the train and test split
    from sklearn.model_selection import train_test_split
    X_train_m, X_val_m, y_train_m, y_val_m = train_test_split(X_train_counts, y, test_size=0.3, random_state=1)

    #Multinomial

    from sklearn.naive_bayes import MultinomialNB
    clf = MultinomialNB().fit(X_train_m, y_train_m)
    labels_m = clf.predict(X_val_m)

    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import accuracy_score
    mat_m = confusion_matrix(y_val_m, labels_m)

    # Bernoulli
    # Changing the data to binary to input BernoulliNB
    x_train_b1 = X_train_counts.todense()
    X_train_counts_ber = np.where(x_train_b1 >=1 ,1,0)

    # Creating the train and test split for bernoulli
    from sklearn.model_selection import train_test_split
    X_train_b, X_val_b, y_train_b, y_val_b = train_test_split(X_train_counts_ber, y, test_size=0.3, random_state=1)

    from sklearn.naive_bayes import BernoulliNB
    clf = BernoulliNB().fit(X_train_b, y_train_b)
    labels_b = clf.predict(X_val_b)

    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import accuracy_score
    mat_b = confusion_matrix(y_val_b, labels_b)
    print ('Confusion matrix:',mat_b)
    print ('Accuracy using BernoulliNB:',accuracy_score(y_val_b, labels_b))


    print ('Confusion matrix:',mat_m)
    print ('Accuracy using MultinomialNB:',accuracy_score(y_val_m, labels_m))
