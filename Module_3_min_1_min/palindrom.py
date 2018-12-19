word = input('please write some word\n')
if word == word[::-1]:
    print('This word is palindrom')
else:
    print('It"s a pity, but word isn"t palindrom')