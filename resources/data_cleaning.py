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

def clean_df(df_column):
    changed_df = df_column.map(lambda x: x.strip('$'))
    changed_df = changed_df.map(lambda x: x.replace(',',''))  
    changed_df = changed_df.astype('int64')
    return changed_df

def clean_genre(df_column):
    #Strip and normalize the genre id list
    cleaned = ((df_column['genre_ids'].map(lambda x: x.strip('[]')).map(lambda x: x.replace(' ', ''))).map(lambda x: x.split(',')))  
    return cleaned

def cat_ratio (ratio):
    if ratio < 1:    #Less than 1 is a 0 - negative profit
        return 0
    elif ratio < 2:    #Between 1 and 2
        return 1
    elif ratio < 3:    #Between 2 and 3
        return 2
    else:   #Greater than 3
        return 3    