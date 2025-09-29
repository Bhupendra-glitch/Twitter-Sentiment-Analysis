# Twitter-Sentiment-Analysis

This project performs sentiment analysis on tweets to classify them as positive, negative, or neutral. It uses machine learning/NLP techniques to preprocess text, extract features, and build a predictive model for sentiment classification.

DataSet: https://www.kaggle.com/datasets/yasserh/twitter-tweets-sentiment-dataset

## Problem Statement

The ability to analyze user sentiment through tweets and comments can provide significant value to companies during product launches. By understanding customer behavior and incorporating sentiment analysis, companies can gain insights from user feedback. This empowers them to make informed decisions, take necessary actions, and improve overall revenue by addressing customer concerns and making targeted improvements accordingly.

<img width="275" height="184" alt="image" src="https://github.com/user-attachments/assets/2576f80d-0654-4da6-98c1-1aa485f9694e" />

## Machine Learning & Data Science

Our approach involves utilizing machine learning techniques and text extraction to predict the sentiment of a given text, determining whether it is positive or negative. Initially, we will analyze the text and examine the various words present within it. Once we have a comprehensive understanding of the text, we will proceed with the machine learning analysis, employing deep neural networks. The output from this analysis will be utilized in subsequent machine learning operations to generate predictions regarding the sentiment of the text, specifically determining whether it is positive or negative.


## Natural Language Processing (NLP)

We would be using the natural language processing that is required when doing the machine learning analysis. Performing the natural language processing ensures that the words that are present are converted into mathematical vectors that are used for different machine learning models for prediction. Once the mathematical vectors are converted into different vectors, they are given for the machine learning models for prediction respectively. Therefore, with the features that are present in the text along with some newly created features, the machine learning, and deep learning models would be using those techniques and ensures that they are getting the best outputs respectively.


## Vectorizers

It is important to use vectorizers that are important for machine learning. Therefore, a given text which is in the form of a string is converted into a vectorial representation which is what is being used by machine learning models for prediction. Below are some of the vectorizers that were used in the process of converting a text into a mathematical representation.


## Exploratory Data Analysis (EDA)
After performing exploratory data analysis, it could be seen based on the results that there is a comparatively more number of neutral sentences compared to either positive or negative sentiments. With the use of word clouds, it could be seen that words such as good, awesome, and great were used most frequently. On the contrary, it could be seen for the negative word cloud that words such as hate, sorry and sad were used most frequently.

We have an image depicting a dataframe and a list of features. We will utilize the 'text' feature as input and consider the 'sentiment' feature as our target variable. Our goal is to predict the likelihood of a text being categorized as positive, negative, or neutral.

<img width="678" height="183" alt="image" src="https://github.com/user-attachments/assets/7be9a1a5-1e61-488a-9218-fbb1fe8f951d" />

The countplot below illustrates that the majority of texts are classified as neutral sentiment, while the count of negative and positive texts is comparatively lower. This indicates a higher prevalence of neutral sentiments in the dataset.

<img width="589" height="432" alt="image" src="https://github.com/user-attachments/assets/fd6dcc4e-ca4c-4025-9083-e175ba06c723" />

Wordcloud gives a good representation by the presence of words based on their size. In other words, more frequent words appear in higher size as compared to others. Words such as "Good" and "Love" are used most often in the positive tweets

<img width="826" height="818" alt="image" src="https://github.com/user-attachments/assets/ed9e8ad3-129f-4c06-9571-b80482aba3f4" />

The wordcloud provided showcases negative tweets within the dataset. Notably, recurring words like "miss" and "suck" are prevalent, indicating their significance in identifying negative sentiment.

<img width="826" height="818" alt="image" src="https://github.com/user-attachments/assets/bfab4fc6-7a36-4629-ac29-b0d406d42743" />

## Hyperparameter Tuning

In our project, after gaining a comprehensive understanding of various machine learning models, we will proceed with hyperparameter tuning. This crucial step aims to select optimal hyperparameters that can yield the best results for each specific model. By carefully selecting these hyperparameters, we can enhance the accuracy and performance of our machine learning models. Our objective is to explore and grasp the influence of different hyperparameters on the models and how they impact the outcomes for various problem statements. Ultimately, we aim to apply these optimized machine learning models in a production environment, leveraging their capabilities to achieve the desired results.

## Results

The observed discrepancy between the training loss and the test loss suggests the presence of overfitting in the data. Despite this, the model could still be utilized for predictions, considering its potential ability to generalize well on unseen test data, despite its exceptionally strong performance on the training data.

**Thanks**













