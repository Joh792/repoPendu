import os
import func
import data

used_letter = []
hide_word = []
game = True
star = '*'
life = data.life

name = func.check_name() 
print("Hello {0}, you got {1} points".format(name,func.read_scores(name)))

word_to_find = func.set_word(data.words).lower()
word_to_find.split()

for i in range(0, len(word_to_find)):
	hide_word.append('*')

while game:
	print("Enter a new char :")
	letter = input().lower()		
	print('Alrady used letters : {}'.format(''.join(used_letter)))
	if len(letter) > 1:
		if letter == word_to_find:
			print('Congratulations {}, you beat the game'.format(name))
			score = func.read_scores(name)
			func.set_score(name,score+1)
			game = False
		else:
			life -= 1
			print('Your remaining number of lifes is {}'.format(life))
			if life == 0:
				print('Sorry you lost :(')
				game = False
	else:
		if letter not in used_letter:
			used_letter.append(letter)
			my_i, hide_word= func.check_letter(word_to_find,letter,hide_word)
			if my_i >-1: 
				if star not in hide_word:
					print('Congratulations {}, you beat the game'.format(name))
					score = func.read_scores(name)
					func.set_score(name,score+1)
					game = False
				print(''.join(hide_word))
			else:
				print(''.join(hide_word))
				life -= 1
				print('Your remaining number of lifes is {} \n'.format(life))
				if life == 0:
					print('Sorry you lost :(')
					game = False

