def largest(l):
    largest_word = max(l, key=len)
    smallest_word = min(l, key=len)
    largest_words = [word for word in l if len(word) == len(largest_word)]
    smallest_words = [word for word in l if len(word) == len(smallest_word)]
    
    return largest_words, smallest_words

s = "it is a  string with laargest and smallest word."
l = s.split()
largest_words, smallest_words = largest(l)

if len(largest_words) > 1 or len(smallest_words) > 1 :
    print(-1)
else:
    print("The largest word:", largest_words[0])
    print("\n")
    print("The smallest word:", smallest_words[0])


    