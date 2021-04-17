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

Hyperparameter Tuning:-

Being a classification problem, I used Logistic Regression whose hyperparameters are tuned using the following configuration.

The hyperparameters to be tuned are:

Learning Rate - It controls how quickly the model is adapted to the problem. It has a small positive value, often in the range between 0.0 and 1.0.
Maximum Iterations - It is the maximum number of iterations that Regression Algorithm can perform.
Bandit Policy
Bandit policy is based on slack factor/slack amount and evaluation interval. Bandit terminates runs where the primary metric is not within the specified slack factor/slack amount compared to the best performing run. Unlike Truncation policy it doesn't calculate primary metric for all runs only to delete a percentage of them, but termminate it as soon as the primary metric doesn't satisfy slack amount, omitting unnecessary baggage. It also omits the need to calculate running Median, making it less computationally cumbersome unlike MedianStoppingPolicy.

Random Parameter Sampling
Random sampling supports discrete and continuous hyperparameters. In random sampling, hyperparameter values are randomly selected from the defined search space. It supports early termination of low-performance runs. Unlike other methods, this gives us a wide exploratory range, which is good to do when we don't have much idea about the parameters. It can also be used do an initial search with random sampling and then refine the search space to improve results.

Herein, we provide hyperdrive a search space to check for parameters, for learning rate I started with a very small search space of 0.02 to 0.05, where I got a very small value for my primary metric (which actually had to be maximised), and the maximum iterations were the least number provided. Attempt 2 Results

So I increased --C to be in the range 0.09 - 0.15 and added 50 to the choices of maximum iterations, and received the following.

below image shows the parameter selection
<img src="capstoneprojectscreenshot/Screenshot (675).png"/>

below image shows the run details of the hyder drive and run completion
<img src="capstoneprojectscreenshot/Screenshot (677).png"/>

below image shows the run id ,target cluster,status
<img src="capstoneprojectscreenshot/Screenshot (678).png"/>

below image shows the best run id,its parameters and outcome and saving of that model
<img src="capstoneprojectscreenshot/Screenshot (680).png"/>
Hereby I may observe information about the parameters generated by the best run along with its run id.
## Screen Recording<a name="sr"></a>
<a href="https://youtu.be/uyE_AfXgdjM">YouTube Video Link</a> contains the Working model of project.

## Standout Suggestions
Enabled Logging in my deployed Web App
I've enabled logging, by means of the logs.py file, which fetches the webservice from its name and the displays its logs.
