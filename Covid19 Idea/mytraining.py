import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

## produces random shuffeld numberss
def data_split(data,ratio):
    np.random.seed(42)
    shuffled = np.random.permutation(len(data))
    test_set_size = int(len(data)*ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[test_set_size:]
    return data.iloc[train_indices],data.iloc[test_indices]



if __name__ == '__main__':
    df = pd.read_csv("data.csv")
    train, test = data_split(df, 0.2)
    X_train = train[['fever', 'bodyPain', 'age', 'ruunyNose', 'diffBreath']].to_numpy()
    X_test = test[['fever', 'bodyPain', 'age', 'ruunyNose', 'diffBreath']].to_numpy()
    Y_train = train[['infectionProb']].to_numpy().reshape(2000, )  # reshape(1,-1)
    Y_test = test[['infectionProb']].to_numpy().reshape(499, )
    clf = LogisticRegression()
    clf.fit(X_train, Y_train)
    #using a pickle to dump the training module
    file = open("model.pkl",'wb')
    #dumping the data into pickle file
    pickle.dump(clf,file)
    file.close()


    # #Code for inference
    # input_features = [102, 1, 12, -1, 0]  # this gives the probablity of % getting the percentage
    # clf.predict_proba([input_features])[0][1]
