import time


def searcher(list, search):
    initial = time.time()
    scores = []
    for sentence in list:
        words = sentence.split()
        searchL = str(search).split()
        score = 0
        for word in words:
            for wrd in searchL:
                if word == wrd:
                    score += 1
        if score != 0:
            scores.append(f"{score}, {sentence}")
    sortedSentScore = sorted(scores, reverse=True)
    print(f"{len(sortedSentScore)} Results found({time.time() - initial} seconds)")
    for items in sortedSentScore:
        item = items.split(",")
        print(f"{item[1]}")


if __name__ == '__main__':
    sentences = ["python is a good", "this is snake",
                 "harry is a good boy", "Subscribe to code with harry"]
    query = input("Enter the text You want to search: ")
    searcher(sentences, query)
