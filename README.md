# Project 1 Movie Analysis

**Authors**: Tommy Phung

## **Overview**
Present business stakeholder with recommendations for the production of a movie that would lead to the most profitable movie.
We will look at movie genre, popularity, production budget, domestic gross, foreign gross and director ranking. 
The top movies are ranked and their genre are totaled to see if we can see a trend. The results shows a district popularity to action, adventure, sci-fi and fantasy 
as well as a poor performance to documentry, horror, thriller and comedy.  <br>
We created another measurement, ratios for production budget and their domestic gross and foreign gross. Strictly speaking, a ratio of over 1 is a net profit for the movie so I tried find the most optimal budget to garentee the highest likely profit, ie the greatest ratio. Lastly, with the top movies from the previous data, we can determine the best director to produce the movie. IMDB provide the individual performance of the directors to see if they already have high performing movies from The Movie DB. Picking from the top rated directors will give another advangate for the movie success. 

## **Business Understanding**
1. What aspect of a movie are the most profitable
2. Does higher production budget influence to a profitable movie?
3. Which director/s have the best record in making high quality movies?
The main aspect we care about is whether or not a movie is profitable. 
Biggest indicator are popular movies so we will be looking at past popular movies and comparing the budget they spent and their gross box office
This may give insight to what type of movie makes them popular and inturn profitable. All of these questions are to make sure that a movie start off at the right foot to lead to a successful box office. 

## **Data Understanding** <br>
Sources are as follow: 
### **The Movie DB** - https://www.themoviedb.org/  <br>
Genre ID Conversion -  https://www.themoviedb.org/talk/5daf6eb0ae36680011d7e6ee <br>
Data used: Genre and Popularity
Description: By using popularity, we can quickly determine the best and worst movie as well as their used genre tags. 
### **The Numbers** - https://www.the-numbers.com/ <br>
Data Used: Production Budget, Domestic Gross, Foreign Gross
Decsription: A database with the production budget and gross income based on the movie. We can determine the best budget to profit ratio for all movies
### **IMBD** - https://www.imdb.com/ <br>
Data Used: Director Name, Number of Movies, Average Ratings
Description: A database that have data on directors and other aspects of a movie. By grouping directors and their works, we can see which would be benifical to have to direct the movie. 

## Methods
The Movie DB needed to be cleaned with the proper format to take the list of genre. Once it was sorted by popularity and cleaned out of duplicates, the top and worst movies are extracted for analysis. Functions help count the amount a single genre appear in the dataset
The Numbers needed the ratio to be added to the set and for each of the grosses it supplied. Comparing the movies genre and their ratios, will show us which genre is profitable. We can then compare the two datas to see if they corralate. 
IMBD will have the data grouped by directors and their movies average ratings to see which directors are consistently making high quality movie. We will use the top movies to have a clean example for the director that made previous made a popular movie in the past. 

## Data Analysis




### Visual 1 
![The Worst and Best genre](https://github.com/Tommyphung1/Project1/blob/master/data_pictures/Best%20and%20Worst%20Genre.PNG)
**Figure 1.** The top 10 best genre for the top 100 movies (left) as well as the 10 worst genre from the worst 100 movies in The Movie DB.
![Production Budget vs Ratio] ()
![Best Directors] () 
### **Q1. What aspect of a movie are the most profitable?** <br>
A1. The best genre a movie can have would be:
1. Action
2. Adventure
3. Sci-fi
4. Fantasy

### **Q2. Does higher production budget influence to a profitable movie?** <br>
A2. There is a reasonable range of production budget that would lead to a higher probablity of success. <br>
That ranges from $20,000,000 and $42,000,000  <br>

### **Q3. Which director/s have the best record in making high quality movies?** <br>
A3. There are several directors that have made movies in the past that were both popular and profitable
1. Anthony Russo
2. Byron Howard
3. Chris Williams
4. Dean DeBlois
5. James Gunn 
6. Peter Ramsey
7. Taika Waititi

## Conclusion
The give a movie the best chances to success, we would suggest making a fictional story that has action or adventure aspect. The budget should be roughly $20,000,000 but not more that $42,000,000. Lastly, the movie should have one of the listed directors manage the movie.
Although genre would be easy to adapt in a movie, budget and directors aren't as flexible. Budget are usually finite and there wasn't any conclusive evidence stating whether a low budget movie would lead to a profitable movie but rather a higher budget is more likely to get a profitable movie. 
In the future, it would be an interesting concept to see if leading actors would benifit a movie's profit and see whether a desirable actor is worth the cost to be in a movie to justify it. High demand would potential result in a higher budget. 

## For More Information

Please review our full analysis in [our Jupyter Notebook](./dsc-phase1-project-template.ipynb) or our [presentation](./DS_Project_Presentation.pdf).

For any additional questions, please contact **Tommy Phung, phungtommy109@gmail.com**

## Repository Structure

Describe the structure of your repository and its contents, for example:

```
├── __init__.py                         <- .py file that signals to python these folders contain packages
├── README.md                           <- The top-level README for reviewers of this project
├── movie_code.ipynb                    <- Narrative documentation of analysis in Jupyter notebook
├── Project_1.pdf         <- PDF version of project presentation
├── code
│   ├── __init__.py                     <- .py file that signals to python these folders contain packages
│   ├── visualizations.py               <- .py script to create finalized versions of visuals for project
│   ├── data_preparation.py             <- .py script used to pre-process and clean data
│   └── eda_notebook.ipynb              <- Notebook containing data exploration
├── data _picture                       <- Both sourced externally and generated from code
└── data                                <- Both sourced externally and generated from code
```