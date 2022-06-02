alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
gedecodeerdwoord = ''
woord = input('Typ het woord dat gedecodeerd moet worden:')
for letter in woord:
    gedecodeerdwoord += ' '
    for i in range(len(alphabet)):
        if letter.upper() == alphabet[i]:
            for b in range(10):
                i += 1
                if i > len(alphabet) - 1:
                    i = 0
            gedecodeerdwoord += alphabet[i].lower()
print(gedecodeerdwoord)
