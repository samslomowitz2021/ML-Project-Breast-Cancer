# Indruction


The incidence of breast cancer in women is the second highest behind skin cancer. The median age of diagnosis is 62. On average, 1 in 8 women will develop breast cancer in the USA. Death by breast cancer ranks second in women behind lung cancer. Further, 3.8 million patients overcome breast cancer as survivors. 

# Data Source
<br>
Breast Cancer Dataset from Kaggle:
https://www.kaggle.com/datasets/sarahvch/breast-cancer-wisconsin-prognostic-data-set

## Discussion 
<br>
Breast cancer get much needed attention, yet tool to eradicate the surge in incidence per year are much needed. I decided to better understand the disease by delving into machine learning tools like classification methods in supervised learning. I found the top two marker for disease classification were concave points worst and perimeter worst. According to UC Irvine Machine Learning Repository, concave points worst is a cellular nucleus metric that approximates the number of concave portions of a “digitized image of a fine needle aspirate (FNA) of a breast mass” (UC Irvine ML Repository).

Logistic Regression out-performed Random Forest and K Nearest Neighbors (KNN) as well as Support Vector Classifier (SVC).
<br>
The logistic regression model was optimized by selecting the top 4 absolute value correlations scores for the diagnosis of breast cancer (binary: malignant or benign). Since logistic regression is a linear function, the extraneous dummy variable was dropped. 
In conclusion, higher values of concave points worst, perimeter worst, concave points mean, and radius worst led to higher classification value of breast cancer. Machine learning remains a vital tool to better understand cancer diagnosis and prognosis. 
<br>
## References
<li>1. About Breast Cancer: https://www.cancer.org/cancer/breast-cancer/about/how-common-is-breast-cancer.html</li>
<li>2. ML on this data set: https://medium.com/swlh/simple-machine-learning-model-on-breast-cancer-dataset-c1a013b594ad </li>
<li> 3. Explaination of this data set: https://archive-beta.ics.uci.edu/ml/datasets/breast+cancer+wisconsin+diagnostic </li>
<li>4. More Data Exploration on this data set: https://towardsdatascience.com/building-a-simple-machine-learning-model-on-breast-cancer-data-eca4b3b99fa3 </li>
<li>5. Breast Cancer ML Literature: https://www.hindawi.com/journals/jhe/2022/4365855/ </li>
