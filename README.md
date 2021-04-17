# BREAST CANCER CLASSIFICATION
I used an external dataset i.e. <a href="https://archive.ics.uci.edu/ml/machine-learning-databases/00451/dataR2.csv">Breast Cancer Risk Classification dataset</a> in our Machine Learning Workspace, and trained the model using different tools available in the Microsoft Azure Workspace. I created two models, one using Automated ML module by Microsoft Azure and one Logistic Regression model whose hyperparameters are tuned using Hyperdrive. I compared their performance on the basis of their respective Weighted Average Precision Score wherein the score of the Voting Ensemble model created by AutoML was found to be 0.8883 and the Logistic Regression model as 0.4783. Furthermore, I deploy the better performing model i.e. clearly the Voting Ensemble model as a web service using the Azure ML Framework.



Following flow diagram depicts the process.
<br>
<br>

<img src="capstoneprojectscreenshot/capstone-diagram.png"/>

# BREAST CANCER 

Breast cancer is cancer that develops from breast tissue.[7] Signs of breast cancer may include a lump in the breast, a change in breast shape, dimpling of the skin, fluid coming from the nipple, a newly inverted nipple, or a red or scaly patch of skin.[1] In those with distant spread of the disease, there may be bone pain, swollen lymph nodes, shortness of breath, or yellow skin.
Risk factors for developing breast cancer include being female, obesity, a lack of physical exercise, alcoholism, hormone replacement therapy during menopause, ionizing radiation, an early age at first menstruation, having children late in life or not at all, older age, having a prior history of breast cancer, and a family history of breast cancer.

<img src="capstoneprojectscreenshot/capstone-diagram.png"/>

# DATASET 

There are 10 predictors, all quantitative, and a binary dependent variable, indicating the presence or absence of breast cancer.
The predictors are anthropometric data and parameters which can be gathered in routine blood analysis.
Prediction models based on these predictors, if accurate, can potentially be used as a biomarker of breast cancer.

# TASK
Our task is to classify the data wheather she as a Breast cancer using the data given

# Automated ML
I used the following setting for my automl experiment.

Since we're working on a small dataset, about 30 mins should be enough to reach the best performing model, and that is why we set experiment_timeout_minutes as 30.
Since our Compute has 4 nodes we're going for 4 max_concurrent_iterations.
In order to minimise overfitting we're using 3 Cross Validation (n_cross_validations).
Since we're working with medical data, accuracy is of utmost importance, hence we choose it as the primary_metric.Automated ML
I used the following setting for my automl experiment.

below image shows the automl-indivial -experiment details

<img src="capstoneprojectscreenshot/Screenshot (664).png"/>

below image show the automl-rundetails-widget

<img src="capstoneprojectscreenshot/Screenshot (665).png"/>

below image shows the run id -bestmodel

<img src="capstoneprojectscreenshot/Screenshot (666).png"/>

below image shows the best run model download

<img src="capstoneprojectscreenshot/Screenshot (667).png"/>

below images shows the deployment-download of models
<img src="capstoneprojectscreenshot/Screenshot (668).png"/>
<img src="capstoneprojectscreenshot/Screenshot (669).png"/>

below image shows that deployment was success and healthy and also swagger url and score url
<img src="capstoneprojectscreenshot/Screenshot (670).png"/>

below image shows the endpoint with the json pay load
<img src="capstoneprojectscreenshot/Screenshot (671).png"/>

below images shows the excuetion and outcome of logs.py which enables the application insights
<img src="capstoneprojectscreenshot/Screenshot (672).png"/>
enabled application insight
<img src="capstoneprojectscreenshot/Screenshot (673).png"/>
Finally service deletion
<img src="capstoneprojectscreenshot/Screenshot (674).png"/>

# HYPER-DRIVE 
