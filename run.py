"""This program creates a new song with lyrics in the style of your 2 favorite artist(s).
It prompts you to enter two urls(for the two artists you want to mix) from the website wwww.azlyrics.com
then uses a Markov Chain algorithim to mix up the text from the two files. Finally the result is formatted 
to look like new written lyrics."""

from markov_python_module.cc_markov import MarkovChain
from fetch_data import fetch_song

def add_songs():
	n = int(input("How many songs would you like to mix? "))
	for i in range(n):
		mc.add_string(fetch_song())

mc = MarkovChain()
add_songs()
markov_list = mc.generate_text(360)
i = 0
while i < 360:
	print(" ".join(markov_list[i:i + 5]))
	i += 6
	if i % 90 == 0:
		print("\n")



