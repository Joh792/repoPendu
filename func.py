import os
import sys
import pickle
import data
import random


"""
Remplacable par le debut de cette fonction pour verifier l'existence du fichier :
 

    if os.path.exists(nom_fichier_scores): # Le fichier existe

        # On le récupère

        fichier_scores = open(nom_fichier_scores, "rb")

        mon_depickler = pickle.Unpickler(fichier_scores)

        scores = mon_depickler.load()

        fichier_scores.close()

    else: # Le fichier n'existe pas

        scores = {}

    return scores
"""
def check_name():
	print("Enter your name please :")
	name = input().lower()
	if name.isalnum() or len(name)<2:
		return name
	else:
		print('Invalid name')		
		check_name()

def read_scores(s):
	try :
		with open('scores', 'rb') as score:
			pickle_score = pickle.Unpickler(score)
			get_scores = pickle_score.load()
			if s in get_scores:
				return get_scores[s]
			else:
				get_scores[s]=0
				return get_scores[s]	
	except :
		with open('scores', 'wb') as score:
			pickle_score = pickle.Pickler(score)
			scores = {s: 0}
			pickle_score.dump(scores)	
			return 0

def set_score(name, s):
	with open('scores', 'wb') as score:
		pickle_score = pickle.Pickler(score)
		pickle_score.dump({name : s})

def set_word(d_word):
	word = d_word[random.randrange(len(d_word))]
	return word
	
def check_letter(word, letter, hide_word):
	if len(letter)==1 and letter in word: 
		for i in range(0,len(word)):
			if letter == word[i]:
				hide_word[i] = word[i]
		return 0, hide_word
	else:
		if word == letter:
			return 1, hide_word

		else:
			return -1, hide_word



