# import plotly
# from plotly.offline import iplot, init_notebook_mode
# from plotly import tools
# import plotly.graph_objs as go
# init_notebook_mode(connected=True)

#string of lyrics
lyrics = "Ah, Ba Ba Ba Ba Barbara Ann Ba Ba Ba Ba Barbara Ann Oh Barbara Ann Take My Hand Barbara Ann You Got Me Rockin' And A-Rollin' Rockin' And A-Reelin' Barbara Ann Ba Ba Ba Barbara Ann ...More Lyrics... Ba Ba Ba Ba Barbara Ann Ba Ba Ba Ba Barbara Ann"

#list of lyrics
list_of_lyrics = lyrics.split(' ')

print(list_of_lyrics)
print("\n", len(list_of_lyrics))

#unique set of words to make the keys of the dictionary and the x-axis labels
unique_words = set(list_of_lyrics)

print("\n", unique_words)
print("\n", len(unique_words))

#create dictionary for word count
word_histogram = dict.fromkeys(unique_words, 0)

for word in list_of_lyrics:
  word_histogram[word] += 1

print("\n", word_histogram)

# trace = {'type': 'bar', 'x': list(unique_words), 'y': list(word_histogram.values())}
 
# plotly.offline.iplot({'data': [trace]})