import praw

def authenticate():
    # Autenticação na API do Reddit
    reddit = praw.Reddit(
        client_id='your_client_id',
        client_secret='your_client_secret',
        user_agent='your_user_agent'
    )
    return reddit