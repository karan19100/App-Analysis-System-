# App-Analysis-System

<img src="https://www.xda-developers.com/files/2017/01/androidinstantapps.png" width="500" >

#### Determining the scope and success of an android app for Google Play Store using Machine Learning in Python.

## Overview
The Play Store apps data has enormous potential to drive app-making businesses to success. Actionable insights can be drawn for developers to work on and capture the Android market! The model uses machine learning in python language.
The model will be providing insights to the App developers regarding various factors which would affect the success of the app and its scope in the market. The data set used is of Play Store for apps of different categories and through the information drawn from that, predictive analysis can be given which would help the android developers.

## Motivation 

Users download apps for various usage purposes. Given that paid service is usually better at offering pleasant experience, and that free apps are more accesible to everyone, what are the user opinions towards these apps?

More specifically, the following questions are of interest:

- What category of apps should a developer target for bursting onto the scene?
- How do the app ratings differ between paid and free apps in general?
- Does size of an app affect its popularity and rating?
- How do paid apps fare against free apps in terms of populariy and sentiment?
- Are there any categories where the differences are statistically significant?
- How are the differences distributed across different app categories?

To expore answers to the above questions, I narrawed the context to Google Play Store and conducted data analysis on the Kaggle dataset  [Google Play Store](https://www.kaggle.com/lava18/google-play-store-apps/home).

### Learning Objective
The following points were the objective of the project . If you are looking for all the following points in this repo then i have not covered all in this repo.  (The main intention was to create an end-to-end ML project.)  
- Data gathering 
- Descriptive Analysis 
- Data Visualizations 
- Data Preprocessing 
- Data Modelling 
- Model Evaluation 

### Detail about the Dataset
The data set used by the model provides all the necessary information for apps of various categories.
The attributes of the data set are:
1.	App: Application name
2.	Category: Category the app belongs to
3.	Rating: Overall user rating of the app (as when scraped)
4.	Reviews: Number of user reviews for the app (as when scraped)
5.	Size: Size of the app (as when scraped)
6.	Installs: Number of user downloads/installs for the app (as when scraped)
7.	Type: Paid or Free
8.	Price: Price of the app (as when scraped)
9.	Content Rating: Age group the app is targeted at - Children / Mature 21+ / Adult
10.	Genres: An app can belong to multiple genres (apart from its main category). For eg, a musical family game will belong to Music, Game, Family genres.
11.	Last Updated: Date when the app was last updated on Play Store (as when scraped)
12.	Current Ver: Current version of the app available on Play Store (as when scraped)
13.	Android Ver: Min required Android version (as when scraped)

### Technologies Used  
![](https://forthebadge.com/images/badges/made-with-python.svg) 

[<img target="_blank" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/scikit-learn/scikit-learn.png" width=90>
<img target="_blank" src="https://github.com/ditikrushna/End-to-End-Diabetes-Prediction-Application-Using-Machine-Learning/blob/master/Resource/numpy.png" width=120>
<img target="_blank" src="https://github.com/ditikrushna/End-to-End-Diabetes-Prediction-Application-Using-Machine-Learning/blob/master/Resource/pandas.jpeg" width=120>

### Project Folder Structure
```
DataAnalysis4GooglePlayStore
                 |---- App Analysis system.ipynb (The code file for data analysis)
                 |---- Report.html               (Report about the detail data)
                 |---- main.py                   (code for generating report in html)
                 |---- googleplaystore.csv          (data file)
                 |---- README.md                   (readme file)
                 
```

### Initial Findings from Analysis

- Maximum Number of Apps in the Store are from the "Family' and 'Game' Category.
- Most of the Apps hold a rating of above 4.0 easily.
- A total of 271 Apps have 5.0 Rating.
- The most famous Apps like WhatsApp, Facebook and Instagram are the most reviewed Apps.
- 93% of the Apps are free in the Play Store.
- Apps related to Education, LifeStyle and Tools seem to fetch full Ratings.

### Results<a name="results"></a>

1. A Developer should target categories which have high demand but lack of quality apps like Entertainment and Travel.
2. Users don't usually care about app size, but lighter apps do have higher average rating. Most of the top rated apps are light.
3. Paid apps are not much downloaded by users. Whenever possible users opt for free alternatives.
4. Reviews of free apps often contain words like bugs, problems and ads. However, such words are not present in reviews of paid apps. Since, both types of apps have similar ratings, we can say that people tend to critize free apps more than paid apps.
5. Developer should opt for a business model which is not fully paid (as it will lead to less downloads), and not fully adsupported as well (which leads to lower ratings). A sweet spot between both is having ads in free version and an option for user to remove those by paying a premium.


###  Made with &nbsp;❤️ by  [Karan Shah](https://github.com/karan19100) , [Shreyans Suraliya](https://github.com/ssuraliya)

