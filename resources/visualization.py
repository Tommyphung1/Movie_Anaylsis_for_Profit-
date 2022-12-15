import matplotlib.pyplot as plt
import sqlite3 as sql   #for the db file
import pandas as pd    #Help visualize the data

def genre_comparison(title, data1, data2, data3):
    fig , ax = plt.subplots(2,2, figsize =(15, 10))
    x, y = zip(*data1)
    x2, y2 = zip(*data2)
    x3, y3 = zip(*data3)

    fig.suptitle(title, fontsize=15)
    ax[0,0].barh(x,y, color = 'red', label = 'Over 1')
    ax[0,0].legend();
    ax[0,0].set_title('Most Popular Genre Based on Ratio: >1');
    ax[0,0].set_xlabel('Frequency')
    ax[0,0].set_ylabel('Genre')
    ax[0,0].set_xlim([0,60])

    ax[0,1].barh(x2,y2, color = 'blue',label = 'Over 2')
    ax[0,1].legend();
    ax[0,1].set_title('Most Popular Genre Based on Ratio: >2');
    ax[0,1].set_xlabel('Frequency')
    ax[0,1].set_ylabel('Genre')
    ax[0,1].set_xlim([0,60]);
    
    ax[1,0].barh(x3,y3, color = 'green', label = 'Over 3')
    ax[1,0].legend();
    ax[1,0].set_title('Most Popular Genre Based on Ratio: >3');
    ax[1,0].set_xlabel('Frequency')
    ax[1,0].set_ylabel('Genre')
    ax[1,0].set_xlim([0,60]);

    ax[1,1].barh(x,y, color = 'red', label = 'Over 1');
    ax[1,1].barh(x2,y2,  color = 'blue', label = 'Over 2');
    ax[1,1].barh(x3,y3,  color = 'green', label = 'Over 3');
    ax[1,1].legend();
    ax[1,1].set_title('Most Popular Genre Based on Ratio');
    ax[1,1].set_xlabel('Frequency')
    ax[1,1].set_ylabel('Genre')
    ax[1,1].set_xlim([0,60]);
    
#Plot the most popular movie genre     
def worst_and_best(top, worst):    
    
    x, y = zip(*top)    #Seperate the tuple into movie and count
    x2,y2 = zip(*worst)

    fig, ax = plt.subplots(1,2, figsize = (20,10))
    colors1 = ['red' if genre in x2[0:5] else 'green' for genre in x]    #Red for genre in the worst genre list
    colors2 = ['cyan' if genre in x[0:5] else 'black' for genre in x2]    #Cyan for genre in the top genre list

    ax[0].barh(x,y, color = colors1);
    ax[0].set_xlabel("Frequency");
    ax[0].set_ylabel("Genre");
    ax[0].set_title("Best Genre from Top 100 Movies");
    ax[0].legend(["Good Tags"]);

    ax[1].barh(x2,y2, color = colors2);
    ax[1].set_xlabel("Frequency");
    ax[1].set_ylabel("Genre");
    ax[1].set_title("Worst Genre from Worst 100 Movies");
    ax[1].legend(["Bad Tags"]);
    
def top_genre(_list):
    ax = plt.subplot()
    x, y = zip(*_list)
    ax.barh(x,y, color = 'red');
    ax.set_title('Most Popular Genre - All Movies');
    ax.set_xlabel('Frequency');
    ax.set_ylabel('Genre');

def read_sql(conn):    
    return pd.read_sql(
        """SELECT persons.primary_name AS 'Director Name', COUNT(movie_id) AS 'Number of Movies'
        FROM movie_ratings
        JOIN movie_basics
            USING (movie_id)
        JOIN directors
            USING (movie_id)
        JOIN persons
            USING (person_id)
        GROUP BY persons.primary_name
        LIMIT 5
        """, conn)

def top_directors(conn):
    return pd.read_sql("""SELECT primary_title, persons.primary_name, COUNT(movie_id), AVG(averagerating)
    FROM movie_ratings
    JOIN movie_basics
        USING (movie_id)
    JOIN directors
        USING (movie_id)
    JOIN persons
        USING (person_id)
    GROUP BY primary_title
    HAVING AVG(averagerating) > 6.332729 AND COUNT(movie_id) > 5

    ORDER BY AVG(averagerating) DESC
    """, conn)
    
def top_dir_and_movies(conn):
    return pd.read_sql("""SELECT primary_title AS 'Movie Title'
                ,persons.primary_name AS 'Director Name'
                , COUNT(movie_id) AS 'Number of Movies' 
                ,AVG(averagerating) AS 'Average Movie Ratings'
                FROM movie_ratings
                JOIN movie_basics
                    USING (movie_id)
                JOIN directors
                    USING (movie_id)
                JOIN persons
                    USING (person_id)
                WHERE primary_title IN ('Spider-Man: Into the Spider-Verse','Avengers: Infinity War','How to Train Your Dragon','Guardians of the Galaxy','Zootopia',
                                        'Thor: Ragnarok','A Star Is Born','Captain America: Civil War','Big Hero 6', 'Guardians of the Galaxy Vol. 2',
                                        'Spider-Man: Homecoming','Ant-Man','Iron Man 3','Aquaman','Ant-Man and the Wasp','Logan','Ralph Breaks the Internet',
                                        'X-Men: Apocalypse','Thor','Thor: The Dark World','Beauty and the Beast','Kong: Skull Island',
                                        'Pirates of the Caribbean: Dead Men Tell No Tales',
                                        'Justice League','Batman v Superman: Dawn of Justice','The Mule')
                GROUP BY primary_title
                HAVING AVG(averagerating) > 6.332729 AND COUNT(movie_id) > 5

                ORDER BY AVG(averagerating) DESC
                LIMIT 10
                """, conn)

def graph_budgets(data):
    
    
    fig, ax = plt.subplots(1,2, figsize = (15, 5))
    ax[0].scatter(data['production_budget'], data['prod_world_ratio']);
    ax[0].set_xlabel('Production Budget');
    ax[0].set_ylabel('Ratio');
    ax[0].set_title('Budget vs Ratio');
    
    
    ax[1].scatter(data['production_budget'], data['worldwide_gross']);
    ax[1].set_xlabel('Production Budget');
    ax[1].set_ylabel('World Gross');
    ax[1].set_title('Budget vs Foreign Gross');
    
    ax[1].plot([0,400000000], [0,2000000000] ,color = 'red');
    
    #df1_and_2.plot.scatter('production_budget', 'worldwide_gross')
#plt.plot([0,400000000], [0,2000000000] ,color = 'red');
#df1_and_2.plot.scatter('production_budget', 'prod_world_ratio');
