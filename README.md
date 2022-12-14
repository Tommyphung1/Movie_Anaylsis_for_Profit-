
The three main questions to answer for stake holders.

Overview
Present business stakeholder with recommendations for the production of a movie that would lead to the most profitable movie.
We will look through the data and determine the usable data and remove or ignore unusable data.

Business Understanding
1. What aspect of a movie are the most profitable
2. Does higher production budget influence to a profitable movie?
3. Which director/s have the best record in making high quality movies?
The main aspect we care about is whether or not a movie is profitable. 
Biggest indicator are popular movies so we will be looking at past popular movies and comparing the budget they spent and their gross box office
This may give insight to what type of movie makes them popular and inturn profitable

Data Understanding 
Sources are as follow:
The Movie DB - - https://www.themoviedb.org/
    Genre ID Conversion -  https://www.themoviedb.org/talk/5daf6eb0ae36680011d7e6ee
    Data used: Genre and Popularity
The Numbers - https://www.the-numbers.com/
    Data Used: Production Budget, Domestic Gross, Foreign Gross
IMBD - https://www.imdb.com/
    Data Used: Director Name, Number of Movies, Average Ratings


![data_pictures/Best and Worst Genre.PNG ]



df_1 is looking into The Movie DB 
The file is mostly data about rating and populating.
We will make the corralation with popularity to what genre the movie are taged as.
There are some cleaning that needs to be done, such as the index column and the duplicat data.
The website have genre id to organize them -
    Found on a forum for each of the Id numbers.
    Used for clarity in genre. 
Next was to find the most used genre for the top movies as well as the most used for the worst performed movies
Some movie have no genre (Further research suggest that these movie are too short
