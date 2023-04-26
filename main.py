from textblob import TextBlob
import graphics as gp
import auth, os

def searchCommentsAndAnalize(reddit, topic):
    # Buscar os 100 comentários mais recentes em um subreddit específico
    subreddit = reddit.subreddit(topic)
    comments = subreddit.comments(limit=100)
    
    # Analisar o sentimento de cada comentário e armazenar os resultados em listas
    sentiment = []
    text = []
    for comment in comments:
        texto = comment.body
        blob = TextBlob(texto)
        _sentiment = blob.sentiment.polarity
        sentiment.append(_sentiment)
        text.append(texto)
    return  sentiment, text

def initApplications(topic, key_words):
    try:
        reddit = auth.authenticate()
        sentiment, text = searchCommentsAndAnalize(reddit, topic)
        gp.barGraphic(sentiment)
        gp.pizzaGraphic(sentiment)
        gp.histogram(sentiment)
        gp.lineGraphic(sentiment)
        gp.dipersionGraphic(sentiment, text)
        gp.warmthGraphic(key_words, text)
    except Exception as e: print(e)
    
def help():
    clear_screen()
    print(" ________________________________________________________________")
    print("| For the algorithm to work as expected you have to:")
    print("| I.  Type a topic name without whitespace")
    print("| II. Type more than two keywords separated by spaces")
    print("|")
    print("|            Made by gabrielsants")
    print("|")
    print("| Type anything to return to main program.")
    print("|_________________________________________________________________\n\n$>. ",end="")
    input()

def clear_screen():
    pass
    if(os.name == "posix"):
        os.system('clear')
    else:
        os.system('cls')
            
if __name__ == "__main__":
    while True:
        clear_screen()
        print(" _______________________________________________________")
        print("| Welcome to the SentimentPolarity Application")
        print("| Type !h for help")
        print("| Type !e to exit the program")
        print("| Type !s to start the program")
        print("|_______________________________________________________\n\n$>. ",end="")
        choice = input()
        if(choice == "!h"):
            help()
        elif(choice == "!e"):
            break
        elif(choice == "!s"):
            clear_screen()
            print("Please provide a topic name that you want to search:\n$>. ",end="")
            topic = input()
            print("Please provide some keywords:\n$>. ",end="")
            key_words = input().split()
            initApplications(topic, key_words)
    
