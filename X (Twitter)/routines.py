import warnings
from datetime import datetime

import pandas as pd
import requests


def create_headers(bearer_token):
    """
    Create the autorization header
    """
    headers = {"Authorization": f"Bearer {bearer_token}"}
    return headers

def create_url(query, start_date, end_date, max_results = 10):
    """
    Create the endpoint with query and all parameters and expected returns
    """
    #Change to the endpoint you want to collect data from. We need data from all Twitter:
    search_url = "https://api.twitter.com/2/tweets/search/all"
    query_params = {'query': query,
                    'start_time': start_date,
                    'end_time': end_date,
                    'max_results': max_results,
                    'expansions':   'author_id,referenced_tweets.id,in_reply_to_user_id,geo.place_id',
                    'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    'user.fields': 'id,location,name,username,created_at,description,public_metrics,verified',
                    'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                    'next_token': {}}
    return (search_url, query_params)

def connect_to_endpoint(url, headers, params, next_token = None):
    """
    Make the query and get response. If we have a next token query, the fetch will be
    the next page with the query token
    """
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json(), response.status_code

def format_dates(date):
    """
    Correct format for create ulr functions
    """
    try:
        date = datetime.strptime(date,'%d/%m/%Y')
    except ValueError:
        raise ValueError("Incorrect data format, should be dd/MM/YYYY")
    date = datetime.strftime(date,'%Y-%m-%dT%H:%M:%S.000Z')
    return date

def make_query(yes_words, not_words, or_groups, extra_query = ''):
    """
    Return a well formated query for twitter.
    yes_words: the words that the tweed need.
    not_words: the not contained words.
    extra_query: additional string.
    """
    full_query = ''
    # Concat yes words:
    if yes_words:
        yes_words = format_phrases(set(yes_words))
        yes_query = ' '.join(yes_words)
        full_query += yes_query
    # Concat not words:
    if not_words:
        not_words = format_phrases(set(not_words))
        not_query = ' '.join({'-'+word for word in not_words})
        full_query += ' ' + not_query
    if extra_query:
        full_query += ' ' + extra_query
    # Group and concat OR words:
    if or_groups:
        for group in or_groups:
            curr_group = format_phrases(set(group))
            curr_or_query = ' OR '.join(curr_group)
            full_query += ' (' + curr_or_query + ')'   
    if len(full_query) > 1024:
        raise Exception(f"Query exeeds character limit: Your query has {len(full_query)} characters. Limit is 1024")
    return full_query

def format_phrases(list_expressions):
    """
    If there is a phrase instead of word, sourrounded by " "
    """
    new_expressions = []
    for expresion in list_expressions:
        if len(expresion.split()) >1:
            new_expressions.append("\"" + expresion + "\"")
        else:
            new_expressions.append(expresion)
    return new_expressions

def merge_tweets_user_data(response):
    """
    Merge tweet data and user data usin author_id key
    """
    tweet_data = pd.json_normalize(response['data'])
    users_data = pd.json_normalize(response['includes']['users'])
    rename_cols_users = {'location':'author_location',
                        'public_metrics':'author_public_metrics',
                        'created_at':'account_created_at',
                        'name':'author_name',
                        'id':'author_id',
                        'verified':'account_verified',
                        'username':'account_username',
                        'description':'account_description',
                        'public_metrics.followers_count':'followers_count',
                        'public_metrics.following_count':'following_count',
                        'public_metrics.tweet_count':'tweet_count',
                        'public_metrics.listed_count':'listed_count',
                        }

    rename_cols_tweets = {'public_metrics.retweet_count':'retweet_count',
                        'public_metrics.reply_count':'reply_count',
                        'public_metrics.like_count':'like_count',
                        'public_metrics.quote_count':'quote_count',
                        }

    tweet_data.rename(columns = rename_cols_tweets, inplace=True)
    users_data.rename(columns = rename_cols_users, inplace=True)

    merged_df = pd.merge(tweet_data,users_data,on='author_id')
    return merged_df
