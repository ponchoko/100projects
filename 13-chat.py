def main():
    user = input("ask me a question")

    responses = {
        "How are you?":"I'm good",
        "How old are you?":"10",
        "What is you fav colour?":"blue"
        }
    
    try:
        user in responses
        print(responses[user])
        exit
    except:
        print("Ask a different qn")  
main()