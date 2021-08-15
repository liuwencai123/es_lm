import streamlit as st
import pickle
import numpy as np
import pandas as pd
import numpy as np
import pandas as pd
import sklearn
import json
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import random
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from xgboost import XGBClassifier
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
import sklearn.model_selection as model_selection
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import AgglomerativeClustering
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from imblearn.over_sampling import RandomOverSampler

#应用标题
st.title('A machine learning-based predictive model for predicting lung metastasis in patients with Ewing’s sarcoma')

# conf
st.sidebar.markdown('## Variables')
#Age = st.sidebar.slider("Age", 1, 99, value=25, step=1)
#Laterality = st.sidebar.selectbox('Laterality',('Left','Right','Other'),index=0)
T = st.sidebar.selectbox("T stage",('T1','T2','T3','TX'))
N = st.sidebar.selectbox("N stage",('N0','N1','NX'))
surgery = st.sidebar.selectbox("Surgery",('No','Yes'),index=0)
#Radiation = st.sidebar.selectbox("Radiation",('No','Yes'),index=0)
#Chemotherapy = st.sidebar.selectbox("Chemotherapy",('No','Yes'),index=0)
Bone_metastases = st.sidebar.selectbox("Bone metastases",('No','Yes'))
#Lung_metastases = st.sidebar.selectbox("Lung metastases",('No','Yes'))

# str_to_int

map = {'Left':0,'Right':1,'Other':2,'T1':0,'T2':1,'T3':2,'TX':3,'N0':0,'N1':1,'NX':2,'No':0,'Yes':1,}
#Age =map[Age]

T =map[T]
N =map[N]
surgery =map[surgery]
#Radiation =map[Radiation]
#Chemotherapy =map[Chemotherapy]
Bone_metastases =map[Bone_metastases]
#Lung_metastases =map[Lung_metastases]

# 数据读取，特征标注
thyroid_train = pd.read_csv('train.csv', low_memory=False)
thyroid_train['Lung.metastases'] = thyroid_train['Lung.metastases'].apply(lambda x : +1 if x==1 else 0)
#thyroid_test = pd.read_csv('test.csv', low_memory=False)
#thyroid_test['BM'] = thyroid_test['BM'].apply(lambda x : +1 if x==1 else 0)
features = ['T','N','surgery','Bone.metastases',]
target = 'Lung.metastases'

#处理数据不平衡
ros = RandomOverSampler(random_state=12, sampling_strategy='auto')
X_ros, y_ros = ros.fit_resample(thyroid_train[features], thyroid_train[target])

#XGB = XGBClassifier(random_state=32,max_depth=3,n_estimators=36)
#XGB.fit(X_ros, y_ros)
RF = sklearn.ensemble.RandomForestClassifier(n_estimators=21,criterion='entropy',max_features='log2',max_depth=5,random_state=12)
RF.fit(X_ros, y_ros)


sp = 0.5
#figure
is_t = (RF.predict_proba(np.array([[T,N,surgery,Bone_metastases]]))[0][1])> sp
prob = (RF.predict_proba(np.array([[T,N,surgery,Bone_metastases]]))[0][1])*1000//1/10

#st.write('is_t:',is_t,'prob is ',prob)
#st.markdown('## is_t:'+' '+str(is_t)+' prob is:'+' '+str(prob))

if is_t:
    result = 'High Risk'
else:
    result = 'Low Risk'
if st.button('Predict'):
    st.markdown('## Risk grouping for LM:  '+str(result))
    if result == 'Low Risk':
        st.balloons()
    st.markdown('## Probability of LM:  '+str(prob)+'%')
#st.markdown('## The risk of bone metastases is '+str(prob/0.0078*1000//1/1000)+' times higher than the average risk .')

#排版占行



st.title("")
st.title("")
st.title("")
st.title("")
#st.warning('This is a warning')
#st.error('This is an error')

#st.info('Information of the model: Auc: 0.874 ;Accuracy: 0.851 ;Sensitivity(recall): 0.750 ;Specificity :0.868 ')
#st.success('Affiliation: The First Affiliated Hospital of Nanchang University, Nanchnag university. ')





