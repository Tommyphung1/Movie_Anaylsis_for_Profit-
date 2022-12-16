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
3. Which director/s have the best record in making high quality movies? <br>
The main aspect we care about is whether or not a movie is profitable. 
Biggest indicator are popular movies so we will be looking at past popular movies and comparing the budget they spent and their gross box office
This may give insight to what type of movie makes them popular and inturn profitable. We first need to show the correlation between popular movie and profit as we will see later that a 'profitable' movie are always the most popular if we consider the scale of the movie. Investors would be more willing to invest if there is a certain guarentee on the movie's success. 

## **Data Understanding**
Their are several dataset are will be pulled together to support the claim we will be making.  <br>
[The Movie DB](https://www.themoviedb.org/) has data their popularity as well as a useful column, genre ID. All other attributes such as release data are not being used in this analysis. There was a helpful [forum](https://www.themoviedb.org/talk/5daf6eb0ae36680011d7e6ee) that explains the genre id to their respective genres. <br>
[The Numbers](https://www.themoviedb.org/talk/5daf6eb0ae36680011d7e6ee) will be providing the profit and budget of the movies which can be sorted and filtered out to see how these movies perform, whether they are popular or highly rated. <br>
[IMDB](https://www.imdb.com/) has an extensive database that contains movies, rating and people who worked on the movie. For this project, we will be specifically seeing the impact of movies based on their directors. <br>

## Methods
The Movie DB needed to be cleaned with the proper format to take the list of genre. Once it was sorted by popularity and cleaned out of duplicates, the top and worst movies are extracted for analysis. Functions help count the amount a single genre appear in the dataset
The Numbers needed the ratio to be added to the set and for each of the grosses it supplied. Comparing the movies genre and their ratios, will show us which genre is profitable. We can then compare the two datas to see if they corralate. 
IMBD will have the data grouped by directors and their movies average ratings to see which directors are consistently making high quality movie. We will use the top movies to have a clean example for the director that made previous made a popular movie in the past. 

## Results
The top genres from the top movies are action, adventure, sci-fi and fantasy while the worst genres are documentary, horror, thriller and comedy. Drama is in a grey area that was found in the top and worst genres for the list of movies. 
![The Worst and Best genre](https://github.com/Tommyphung1/Project1/blob/21d2a3cde350bf1c2cea1f7d3c798be8e6582f6f/pictures/Best%20and%20Worst%20Genre.PNG)

Production Cost vs Ratio and World Gross Box Office <br>
![Production Budget vs Ratio](https://github.com/Tommyphung1/Project1/blob/21d2a3cde350bf1c2cea1f7d3c798be8e6582f6f/pictures/Budget%20Graphs.png)

There are exemplary directors whom have movies in our top list of movies. Not only do they have made several films with an average rating of 7 and above, but also experienced with at least 5 movies produced. 
![The Best Directors](https://github.com/Tommyphung1/Project1/blob/21d2a3cde350bf1c2cea1f7d3c798be8e6582f6f/pictures/Top%20Ten%20Directors%20and%20Their%20movies.PNG)

List Of directors
1. Anthony Russo
2. Byron Howard
3. Chris Williams
4. Dean DeBlois
5. James Gunn 
6. Peter Ramsey
7. Taika Waititi

## Conclusion
In order for the highest possiblity of making a successful movie, it is recommended for the movie to have these attributes.
**The movie should have one or a combination of action, adventure, sci-fi or fantasy with a limited drama.** Documentaries should be avoided and keep thriller and horror to a minimum <br>
**The movie's budget has a slight positive relationship with gross box office.** Ratios are hard to interpret due to the metris being in the millions, making smaller production budget appear inflatted.
**One of the listed directors should be managing if possible.** The list contains the most positive rated and experience directors <br>

Although genre would be easy to adapt in a movie, budget and directors aren't as flexible. Budget are usually finite and there wasn't any conclusive evidence stating whether a low budget movie would lead to a profitable movie but rather a higher budget is more likely to get a profitable movie. 
In the future, it would be an interesting concept to see if leading actors would benifit a movie's profit and see whether a desirable actor is worth the cost to be in a movie to justify it. High demand would potential result in a higher budget. 


## Next Steps
This project primary focus on attributes before movie production such as budget, genre and directors. A movie is a multi-step process and we should look into aspects such as:
+ **Leading actors and their affect on a movie popularity or profit.** High profile actors may boost sales but might not justify the wage if over budget.
+ **Perhaps there is a combination of genre that may result in the best movie for the audience.** Many genres overlap, like action and adventure, which could be more popular than action horror. This could be analysis with the current data we have. 
+ **Seeing whether or not, new directors are performing better than old directors.** There were several movies that have been sequelized and newer directors making highly rated movies. Analysing this may give us insight on whether or not, newer talents should be producing movies instead of the experience director we recommended. 
## For More Information

Please review our full analysis in [Jupyter Notebook](./movie_code.ipynb) or the [presentation](./Phase_1_Project_Presentation.pdf).

For any additional questions, please contact **Tommy Phung, phungtommy109@gmail.com**

## Repository Structure

```
├── __init__.py                         <- .py file that signals to python these folders contain packages
├── README.md                           <- The top-level README for reviewers of this project
├── movie_code.ipynb                    <- Narrative documentation of analysis in Jupyter notebook
├── Project_1.pdf                       <- PDF version of project presentation
├── resources
│   ├── __init__.py                     <- .py file that signals to python these folders contain packages
│   ├── visualizations.py               <- .py script to create finalized versions of visuals for project
│   ├── data_preparation.py             <- .py script used to pre-process and clean data
│   └── eda_notebook.ipynb              <- Notebook containing data exploration
├── picture                             <- Graphs and plots created by code
└── ZippedData                          <- Original Code from Websites
```
