# Machine Learning Game Sales Project

## Games Dataset - [kaggle link](https://www.kaggle.com/datasets/gregorut/videogamesales?resource=download)
<hr>

## Description:
Utilizing kaggle's dataset of games and game sales, program will create a prediction on how many sales a given example game could sell based on few important features.

## Operation scheme

First, after importing the data from the csv file, we start analyzing our dataset.

Here we see the 5 best selling games from our dataset:
<img src="[Assets/icon.png](https://github.com/PKrystian/DataSetGames_Project/blob/master/Photos/1.PNG)" width="200">

Now we check for irregularities through plotbox:
![plotbox](https://github.com/PKrystian/DataSetGames_Project/blob/master/Photos/2.PNG "plotbox")
We can see that below 1995 there are only single game records, later after analysis we will remove them.

Here is the heatmap of columns with correlation. We can see their little degree of connections.
![heatmap](https://github.com/PKrystian/DataSetGames_Project/blob/master/Photos/3.png "heatmap")

After analyzing the dataset, we start removing unnecessary information. At the beginning we rename the columns for aesthetic reasons, later we remove unnecessary ones, e.g. Name or Rank. Then we delete individual data, including games released before 1995.
Now we check how does plotbox look after cleaning:
![plotbox2](https://github.com/PKrystian/DataSetGames_Project/blob/master/Photos/4.PNG "plotbox2")

Now we normalize the data through one hot encoder function.
Here's how our dataset looks like now.
![top52](https://github.com/PKrystian/DataSetGames_Project/blob/master/Photos/5.PNG "top52")

After cleaning the data, we can start training the model, we have chosen PCA, which will reduce the number of data only to the most important.
Here's how our weight graph looks like.
![pca](https://github.com/PKrystian/DataSetGames_Project/blob/master/Photos/6.PNG "pca")
We see a low degree of importance of the data, which means that our data does not have a sufficiently large correlation with the Global sales.
After training the model, we obtained a percentage result with a degree of: 0.0422979797979798

## Conclusion:
Based on the results of trained models, we can conclude that we have too little correlating information in our Dataset. The changes that we can apply include increasing the data range or adding new columns along a greater correlation with sales (e.g. game budget).
