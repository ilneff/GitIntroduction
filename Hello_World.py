import Levenshtein as LV
from pyWords import words as MyDictionary


def Find_Min_Edit_Distance_Word(given_word):
	Min_Edit_Dist = len(given_word)
	suggested_word = given_word

	for word in MyDictionary:
		edit_dist = LV.Edit_Distance(given_word, word)

		if edit_dist < Min_Edit_Dist:
			Min_Edit_Dist = edit_dist
			suggested_word = word

	return suggested_word


def main():
	
	Exit_Program = False

	try:
		while not(Exit_Program):
	
			print 'Hello! I am here to help you write sentences!\nType a sentence you would like help with.\nTo quit, type !!! or press ctrl-C at any time.\nSentence:'
			sentence = raw_input()
			if '!!!' in sentence:
				Exit_Program = True
			else:
				words = sentence.strip()[:-1].split(' ')
				punct = sentence.strip()[-1]
				suggested_sentence = ''

				for word in words:
					suggested_sentence = suggested_sentence + Find_Min_Edit_Distance_Word(word) + ' '

				suggested_sentence = suggested_sentence[:-1] + punct

				print 'Is this what you meant to say?'
				confirmation = raw_input(suggested_sentence + '\n(Y/N): ')

				if confirmation.upper() == 'Y':
					print 'Yay! I\'m happy I could help :)'
				else:
					print 'Shoot :( Maybe next time.'

				print '\n'

	
	except:
		pass

	print '\nSee you next time!\n'


main()