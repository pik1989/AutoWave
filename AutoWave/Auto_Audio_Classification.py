import sklearn
import xgboost
import lightgbm
from sklearn.utils import all_estimators
from sklearn.base import ClassifierMixin
from sklearn import preprocessing
import time
from sklearn.metrics import recall_score,precision_score,roc_auc_score,f1_score,accuracy_score
import numpy as np
import pandas as pd
import tqdm
from sklearn.model_selection import train_test_split


import warnings
warnings.filterwarnings("ignore")

def label_encode(label_data:list):
    label_encodder = preprocessing.LabelEncoder()
    label_encodder.fit(label_data)
    label_data_encode = label_encodder.transform(y)
    return label_data_encode, label_encodder

CLASSIFIERS = [est for est in all_estimators() if issubclass(est[1], ClassifierMixin)]

removed_classifiers = [
    ("DummyClassifier", sklearn.dummy.DummyClassifier),
    ("ClassifierChain", sklearn.multioutput.ClassifierChain),
    ("ComplementNB", sklearn.naive_bayes.ComplementNB),
    (
        "GradientBoostingClassifier",
        sklearn.ensemble.GradientBoostingClassifier,
    ),
    (
        "GaussianProcessClassifier",
        sklearn.gaussian_process.GaussianProcessClassifier,
    ),
    (
        "HistGradientBoostingClassifier",
        sklearn.ensemble._hist_gradient_boosting.gradient_boosting.HistGradientBoostingClassifier,
    ),
    ("MLPClassifier", sklearn.neural_network.MLPClassifier),
    ("LogisticRegressionCV", sklearn.linear_model.LogisticRegressionCV),
    ("MultiOutputClassifier", sklearn.multioutput.MultiOutputClassifier),
    ("MultinomialNB", sklearn.naive_bayes.MultinomialNB),
    ("OneVsOneClassifier", sklearn.multiclass.OneVsOneClassifier),
    ("OneVsRestClassifier", sklearn.multiclass.OneVsRestClassifier),
    ("OutputCodeClassifier", sklearn.multiclass.OutputCodeClassifier),
    (
        "RadiusNeighborsClassifier",
        sklearn.neighbors.RadiusNeighborsClassifier,
    ),
    ("VotingClassifier", sklearn.ensemble.VotingClassifier),
    ("StackingClassifier",sklearn.ensemble._stacking.StackingClassifier)
]

for i in removed_classifiers:
    CLASSIFIERS.pop(CLASSIFIERS.index(i))

CLASSIFIERS.append(("XGBClassifier", xgboost.XGBClassifier))
CLASSIFIERS.append(("LGBMClassifier", lightgbm.LGBMClassifier))

CLASSIFIERS = dict(CLASSIFIERS)

def Auto_Audio_Classification_Ml(X,Y,test_size):
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, shuffle = True)
    dic =  {"Model":[],"Acuracy":[],"Sensitivity":[],"Precision":[],"F-Score":[],"ROC_AUC":[],'Time':[]}
    for name, model_new in tqdm.tqdm(CLASSIFIERS.items()):
        start = time.time()
        model = model_new()
        try:
            model.fit(np.array(X_train), np.array(y_train))
            predict_test = model.predict(np.array(X_test))
        except Exception as exception:
            print("Invalid Classifier(s) : "+name)
            print(f"Error Code: {exception}")
            continue
        Accuracy = accuracy_score(y_test,predict_test,normalize=True)
        Sensitivity = recall_score(y_test,predict_test,average="weighted")
        #ROC_AUC = roc_auc_score(y_test,predict_test, average="weighted",multi_class='ovr')
        try:
            roc_auc = roc_auc_score(y_test,predict_test,multi_class='ovo')
            dic["ROC_AUC"].append(roc_auc)
        except Exception as exception:
            roc_auc = None
            #print("ROC AUC couldn't be calculated for " + name)
            #print(exception)
            dic["ROC_AUC"].append(roc_auc)
        Precision =  precision_score(y_test,predict_test,average="weighted")
        FScore =  f1_score(y_test,predict_test,average="weighted")
        dic["Model"].append(name)
        dic["Acuracy"].append(Accuracy)
        dic["Sensitivity"].append(Sensitivity)
        dic["Precision"].append(Precision)
        dic["F-Score"].append(FScore)
        dic["Time"].append(time.time() - start)
    final_data = pd.DataFrame(dic)
    print("==================================================================")
    print("Best Model Sorted By Accurcy")
    print("==================================================================")
    final_data = final_data.sort_values(by='Acuracy',ascending=False).reset_index(drop=True)
    if all(x is None for x in dic["ROC_AUC"]):
        final_data = final_data.sort_values(by='Acuracy',ascending=False).reset_index(drop=True).drop(['ROC_AUC'],axis=1)
    return final_data