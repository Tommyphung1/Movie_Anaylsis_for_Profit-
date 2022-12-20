# Project 1 Movie Analysis

**Authors**: Tommy Phung

## **Overview**
Microsoft is planning to start making movies and we are tasked to give the new department movie recommendations to help them start. We will look at movie genres, popularity, production budget, domestic gross, foreign gross, and director's movie rankings from various websites to back our claims. The top movies are ranked and their genres are totaled to see if we can correlate genres and popularity. **The results show a distinct popularity in action, adventure, sci-fi, and fantasy as well as a poor performance in documentary, horror, thriller, and comedy.** These genres were both profitable and successful.  <br>
**Production budget has a small influence on their world gross box office with a 1:2 ratio of dollars returned for every dollar spent.** A created variable ended up being a bad metric to determine success. <br>
Lastly, with the top movies from the previous data, **we can determine the best director to produce the movie**. IMDB provides the individual performance of the directors to see if they already have high-performing movies from The Movie DB. Picking from the top-rated directors will give another advantage to the movie's success.

## **Business Understanding**
1. What aspects of a movie are the most profitable?
2. Does a higher production budget results in a profitable movie?
3. Which director/s has the best record in making high-quality movies? <br>
The main aspect we care about is whether or not a movie is profitable. 
We will be looking at past popular movies and comparing the budget they spent and their gross box office. 
This may give insight into what type of movie makes them popular and in turn profitable. We first need to show the correlation between popular movie and profit as we will see later that a 'profitable' movie are not always the most popular if we consider the scale of the movie. Investors would be more willing to invest if there is a certain guarantee of the movie's success. 

## **Data Understanding**
There are several datasets are will be pulled together to support the claim we will be making.  <br>
[The Movie DB](https://www.themoviedb.org/) has data on their popularity as well as a useful column, genre ID. All other attributes such as release data are not being used in this analysis. There was a helpful [forum](https://www.themoviedb.org/talk/5daf6eb0ae36680011d7e6ee) that explains the genre id to their respective genres. <br>
[The Numbers](https://www.themoviedb.org/talk/5daf6eb0ae36680011d7e6ee) will be providing the profit and budget of the movies which can be sorted and filtered out to see how these movies perform, whether they are popular or highly rated. <br>
[IMDB](https://www.imdb.com/) has an extensive database that contains movies, ratings, and people who worked on the movie. For this project, we will be specifically seeing the impact of movies based on their directors. <br>

This project aims to present Microsoft with recommendations for the production of a movie that would lead to the most profitable movie.
We will look at movie genre, popularity, production budget, domestic gross, foreign gross, and director ranking. 
The top movies are ranked and their genres are totaled to see if we can see a trend. The results show a distinct popularity in action, adventure, sci-fi, and fantasy 
as well as a poor performance in documentary, horror, thriller, and comedy.  <br>
We created another measurement, ratios for production budget and their domestic gross and foreign gross. Strictly speaking, a ratio of over 1 is a net profit for the movie so I tried to find the most optimal budget to guarantee the highest likely profit, ie the greatest ratio. Lastly, with the top movies from the previous data, we can determine the best director to produce the movie. IMDB provides the individual performance of the directors to see if they already have high-performing movies from The Movie DB. Picking from the top-rated directors will give another advantage to the movie's success. 

## Methods
The Movie DB needed to be cleaned with the proper format to take the list of the genres. Once it was sorted by popularity and cleaned out of duplicates, the top and worst movies are extracted for analysis. Functions help count the amount a single genre appears in the dataset
The Numbers needed the ratio to be added to the set and for each of the grosses it supplied. Comparing the movies genre and their ratios will show us which genre is profitable. We can then compare the two datasets to see if they correlate. 
IMBD will have the data grouped by directors and their movie average ratings to see which directors are consistently making a high-quality movies. We will use the top movies to have a clear example of the director that made previously made a popular movie in the past. 

## Results
The top genres from the top movies are action, adventure, sci-fi, and fantasy while the worst genres are documentary, horror, thriller, and comedy. Drama is in a grey area that was found in the top and worst genres for the list of movies. 
![The Worst and Best genre](./pictures/Best%20and%20Worst%20Genre.PNG)

Production Cost vs Ratio and World Gross Box Office <br>
![Production Budget vs Ratio](./pictures/Budget%20Ratio%20and%20World%20Gorss.JPG)

We should only consider directors with the most experience and have movies in the top 100 movies list. Not only do they have made several films with an average rating of 7 and above but also experienced with at least 5 movies produced. 
![The Best Directors](./pictures/Top%20Ten%20Directors%20and%20Their%20movies.PNG)

List Of directors
1. Anthony Russo
2. Byron Howard
3. Chris Williams
4. Dean DeBlois
5. James Gunn 
6. Peter Ramsey
7. Taika Waititi

## Conclusion
For the highest possibility of making a successful movie, it is recommended for the movie have these attributes.
**The movie should have one or a combination of action, adventure, sci-fi, or fantasy with a limited drama.** Documentaries should be avoided and keep thriller and horror to a minimum. **The movie's budget has a slightly positive relationship with the gross box office.** Ratios are hard to interpret due to the metric being in the millions, making smaller production budgets appear inflated. **One of the listed directors should be managing if possible.** The list contains the most positively rated and experienced directors <br>

Although genre would be easy to adapt in a movie, budget and directors aren't as flexible. Budgets are usually finite and there wasn't any conclusive evidence stating whether a low-budget movie would lead to a profitable movie but rather a higher budget is more likely to get a profitable movie. 
In the future, it would be an interesting concept to see if leading actors would benefit a movie's profit and see whether a desirable actor is worth the cost to be in a movie to justify it. High demand would potentially result in a higher budget. 

## Next Steps
This project primarily focuses on attributes before movie production such as budget, genre, and directors. A movie is a multi-step process and we should look into aspects such as:
+ **Leading actors and their effect on a movie's popularity or profit.** High-profile actors may boost sales but might not justify the wage if over budget.
+ **Perhaps there is a combination of a genre that may result in the best movie for the audience.** Many genres overlap, like action and adventure, which could be more popular than action horror. This could be analyzed with the current data we have. 
+ **Seeing whether or not, there are other measures of success.** Merch sold, and the number of movies in a series may be some examples of success. 
## For More Information

Please review our full analysis in [Jupyter Notebook](./movie_code.ipynb) or the [presentation](./presentation.pdf).

For any additional questions, please contact **Tommy Phung, phungtommy109@gmail.com**

## Repository Structure

```                  
├── README.md                           <- The top-level README for reviewers of this project
├── movie_code.ipynb                    <- Narrative documentation of analysis in Jupyter notebook
├── presentation.pdf                    <- PDF version of project presentation
├── resources
│   ├── __init__.py                     <- .py file that signals to python these folders contain packages
│   ├── visualizations.py               <- .py script to create finalized versions of visuals for the project
│   ├── data_preparation.py             <- .py script used to pre-process and clean data
│   └── eda_notebook.ipynb              <- Notebook containing data exploration
├── picture                             <- Graphs and plots created by code
└── ZippedData                          <- Original Code from Websites
```
