#!/usr/bin/env python

import sys

productions = set()
puzzle = 'MI';

def print_rules():
	print ''
	print 'Rule I:   If you possess a string whose last letter is \'I\' you can add'
	print '          on a \'U\' at the end.'
	print 'Rule II:  Suppose you have "Mx", you may add "Mxx" to your collection.'
	print 'Rule III: If "III" occurs in one of the strings in your collection you may'
	print '          make a new string with "U" in place of "III".'
	print 'Rule IV:  If "UU" occurs inside one of your strings, you can drop it.'
	print ''
	
def print_help():
	print ''
	print 'Following commands are available:'
	print '  h    show this list of commands'
	print '  q    quit'
	print '  s    to show the rules'
	print '  r    start over'
	print '  p    print all strings you produced'
	print '  1    apply rule I if possible'
	print '  2    apply rule II if possible'
	print '  3    apply rule III if possible'
	print '  4    apply rule IV if possible'
	print ''

print 'You are about to enjoy some time experimenting with a formal system called'
print 'MIU-system. It\'s words consist only of the letters \'M\', \'I\' and \'U\''
print 'and there are four rules to apply to those words/strings:'
print_rules()
print 'You will be given the string "MI", which you must transform to "MU" using'
print 'the above rules.'

print_help()

while puzzle is not 'MU':
	cmd = raw_input('Enter a character and press enter: ')

	if cmd is 'h':
		print_help()
	elif cmd is 'q':
		exit(0)
	elif cmd is 's':
		print_rules()
	elif cmd is 'p':
		print ''
		print 'Strings you produced:' + ' '.join(item for item in productions)
		print ''
	else:
		if cmd is 'r':
			puzzle = 'MI'
		elif cmd is '1':
			if puzzle[-1] is 'I':
				puzzle += 'U'
		elif cmd is '2':
			puzzle += puzzle[1:]
		elif cmd is '3':
			puzzle = puzzle.replace('III', 'U')
		elif cmd is '4':
			puzzle = puzzle.replace('UU', '')
		else:
			print 'Sorry, I did not understand that command. Enter \'h\' for a list of commands.'
			continue
		print 'You produced the string "' + puzzle + '"'
		productions.add(puzzle)

print 'Congratulations, you solved the MU-puzzle!'
