import string
def count_word(text):
    marks=[',','.','?','!',';',':',"'"]
    for i in marks:
        text=text.replace(i,'')
    words=text.split()
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word]=1
        else:
            word_count[word]+=1
    sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
    for word, count in word_count.items():
        print(f"{word} -> {count}")
