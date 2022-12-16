import pandas as pd    #Help visualize the data

# Convert the genre id to names for understanding purposes
convert = {'28' : 'Action', '12': 'Adventure', '35': 'Comedy', '99': 'Documentary', 
           '18': 'Drama', '14': 'Fantasy', '27': 'Horror', '878' : 'Sci-Fi', '53' : 'Thriller',
           '16': 'Animation', '80' : 'Crime', '10751' : 'Family','14':'Fantasy',
           "36" : 'History','27': 'Horror', '10402':'Music', '9648':'Mystery',
           '10749':'Romance','10770': 'TV Movie','10752': 'War','37':'Western', '': "NULL" }


# Function count all the genre and group them
def count_genre(df_list):
    genre_count = {}    #https://www.themoviedb.org/talk/5daf6eb0ae36680011d7e6ee
    for genre in df_list['genre_ids']:    #Take the list of genre ids
        for ids in genre:    #For each element in the list, multiple genre for one movie
            if(genre_count.get(convert[ids])):    #Check if it exists,
                genre_count[convert[ids]] += 1    #Convert the ID and add 1 to counter
            else:
                genre_count[convert[ids]] = 1
    return sorted(genre_count.items(), key = lambda x: x[1], reverse=True)    #Return the list sorted by the most popular genre

#Function strips a string number with $ and ,'s into an integer
def clean_df(df_column):
    changed_df = df_column.map(lambda x: x.strip('$'))
    changed_df = changed_df.map(lambda x: x.replace(',',''))  
    changed_df = changed_df.astype('int64')
    return changed_df

#Funtcion changes the genre column full of strings and change them into a list of genre id
def clean_genre(df_column):
    #Strip and normalize the genre id list
    cleaned = ((df_column['genre_ids'].map(lambda x: x.strip('[]')).map(lambda x: x.replace(' ', ''))).map(lambda x: x.split(',')))  
    return cleaned

#Catorgize movie from their ratios. Not used in final version
def cat_ratio (ratio):
    if ratio < 1:    #Less than 1 is a 0 - negative profit
        return 0
    elif ratio < 2:    #Between 1 and 2
        return 1
    elif ratio < 3:    #Between 2 and 3
        return 2
    else:   #Greater than 3
        return 3    
    
###    Function that takes the data frame, takes the movie name if they are also in the top movie list    ###
def list_of_movies(df_list, top_list):
    movie_list = []    #Make a empty list
    for name in df_list:    #For each movie in the list    
        for top in top_list:    #Check if any of the most popular list are in the second list
            if(name == top):    #If match
                movie_list.append(name)     #Add the list
    return movie_list      

def find_min_max(data):
    
    IQR = data.quantile(.75) - data.quantile(.25)
    min_out = data.median() - (IQR*1.5)
    max_out = data.median() + (IQR*1.5)
    if (min_out > data.min()):
        print('Min Outlier: ', min_out)
    if (max_out < data.max()):
        print('Max Outlier: ', max_out)
    
    return [min_out if min_out > 0 else 0, max_out]
    #Determine a reasonable range of budget that gives the most benifical ratio possible

#IQR = df_2['prod_world_ratio'].quantile(.75) - df_2['prod_world_ratio'].quantile(.25)
#min_out = df_2['prod_world_ratio'].median() - IQR*1.5
#max_out = df_2['prod_world_ratio'].median() + IQR*1.5

#outlier_removed = df_2.loc[df_2['prod_world_ratio'] < 6.607385548232989]
#outlier_removed['prod_world_ratio'].describe()
#scat_x = outlier_removed['production_budget'].loc[outlier_removed['prod_world_ratio'] > 1]
#scat_y = outlier_removed['prod_dom_ratio'].loc[outlier_removed['prod_world_ratio'] > 1]
#outlier_removed['prod_world_ratio'].median()
#outlier_removed['production_budget'].quantile(.75)
