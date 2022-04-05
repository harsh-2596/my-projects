import json
import requests


def speak(url):

    from win32com.client import Dispatch
    speake = Dispatch("SAPI.SpVoice")
    speake.Speak(url)


if __name__ == '__main__':

    category = input("Select a Category From the Following-:\n"
                     "business entertainment general health-science sports technology: ")
    i = 1
    while i>0:

        link = f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey=06eb1d9dcb32476997c0bec92701485b"
        y = requests.get(url=link)
        # print(y.status_code)
        parsed = json.loads(y.content)
        # print(y.content["MLB Lockout"])
        # print(parsed)
        # print(parsed["articles"])
        title = parsed["articles"]
        # print(title)

        title2 = title[i-1]
        print(f'Headline: {title2["title"]}')
        speak(title2["title"])
        print(f'Content: {title2["description"]}')
        speak(title2["description"])
        # print(title2["content"])
        # speak(title2["content"])
        choice = input("Type Next to Listen to the next news:\n"
                       "Change to Change The Category \n"
                       " E for Exit: ")

        if choice == "change" or choice == "Change" or choice == "CHANGE":
            category = input("Select a Category From the Following-:\n"
                             "business entertainment general health-science sports technology: ")
        elif choice == "e" or choice == "E" or choice == "quit":
            exit()
        elif choice == "next" or choice == "Next" or choice == "NEXT":
            i += 1
