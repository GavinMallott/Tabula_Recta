def interpret_hex_to_acii(hex):
	if hex == '30': return '0'
	if hex == '31': return '1'
	if hex == '32': return '2'
	if hex == '33': return '3'
	if hex == '34': return '4'
	if hex == '35': return '5'
	if hex == '36': return '6'
	if hex == '37': return '7'
	if hex == '38': return '8'
	if hex == '39': return '9'

	if hex == '41': return 'A'
	if hex == '42': return 'B'
	if hex == '43': return 'C'
	if hex == '44': return 'D'
	if hex == '45': return 'E'
	if hex == '46': return 'F'
	if hex == '47': return 'G'
	if hex == '48': return 'H'
	if hex == '49': return 'I'
	if hex == '4A': return 'J'
	if hex == '4B': return 'K'
	if hex == '4C': return 'L'
	if hex == '4D': return 'M'
	if hex == '4E': return 'N'
	if hex == '4F': return 'O'
	if hex == '50': return 'P'
	if hex == '51': return 'Q'
	if hex == '52': return 'R'
	if hex == '53': return 'S'
	if hex == '54': return 'T'
	if hex == '55': return 'U'
	if hex == '56': return 'V'
	if hex == '57': return 'W'
	if hex == '58': return 'X'
	if hex == '59': return 'Y'
	if hex == '5A': return 'Z'

	if hex == '61': return 'a'
	if hex == '62': return 'b'
	if hex == '63': return 'c'
	if hex == '64': return 'd'
	if hex == '65': return 'e'
	if hex == '66': return 'f'
	if hex == '67': return 'g'
	if hex == '68': return 'h'
	if hex == '69': return 'i'
	if hex == '6A': return 'j'
	if hex == '6B': return 'k'
	if hex == '6C': return 'l'
	if hex == '6D': return 'm'
	if hex == '6E': return 'n'
	if hex == '6F': return 'o'
	if hex == '70': return 'p'
	if hex == '71': return 'q'
	if hex == '72': return 'r'
	if hex == '73': return 's'
	if hex == '74': return 't'
	if hex == '75': return 'u'
	if hex == '76': return 'v'
	if hex == '77': return 'w'
	if hex == '78': return 'x'
	if hex == '79': return 'y'
	if hex == '7A': return 'z'

	if hex == '20': return ' '
	if hex == '21': return '!'
	if hex == '22': return '"'
	if hex == '23': return '#'
	if hex == '24': return '$'
	if hex == '25': return '%'
	if hex == '26': return '&'
	if hex == '27': return "'"
	if hex == '28': return '('
	if hex == '29': return ')'
	if hex == '2A': return '*'
	if hex == '2B': return '+'
	if hex == '2C': return ','
	if hex == '2D': return '-'
	if hex == '2E': return '.'	
	if hex == '2F': return '/'

	if hex == '3A': return ':'
	if hex == '3B': return ';'
	if hex == '3C': return '<'
	if hex == '3D': return '='
	if hex == '3E': return '>'
	if hex == '3F': return '?'
	if hex == '40': return '@'

	if hex == '5B': return '['
	if hex == '5C': return "\\"
	if hex == '5D': return ']'
	if hex == '5E': return '^'
	if hex == '5F': return '_'
	if hex == '60': return '`'

	if hex == '7B': return '{'
	if hex == '7C': return '|'
	if hex == '7D': return '}'
	if hex == '7E': return '~'



def interpret_ascii_to_hex(ascii):
	if ascii == '0': return '30'
	if ascii == '1': return '31'
	if ascii == '2': return '32'
	if ascii == '3': return '33'
	if ascii == '4': return '34'
	if ascii == '5': return '35'
	if ascii == '6': return '36'
	if ascii == '7': return '37'
	if ascii == '8': return '38'
	if ascii == '9': return '39'

	if ascii == 'A': return '41'
	if ascii == 'B': return '42'
	if ascii == 'C': return '43'
	if ascii == 'D': return '44'
	if ascii == 'E': return '45'
	if ascii == 'F': return '46'
	if ascii == 'G': return '47'
	if ascii == 'H': return '48'
	if ascii == 'I': return '49'
	if ascii == 'J': return '4A'
	if ascii == 'K': return '4B'
	if ascii == 'L': return '4C'
	if ascii == 'M': return '4D'
	if ascii == 'N': return '4E'
	if ascii == 'O': return '4F'
	if ascii == 'P': return '50'
	if ascii == 'Q': return '51'
	if ascii == 'R': return '52'
	if ascii == 'S': return '53'
	if ascii == 'T': return '54'
	if ascii == 'U': return '55'
	if ascii == 'V': return '56'
	if ascii == 'W': return '57'
	if ascii == 'X': return '58'
	if ascii == 'Y': return '59'
	if ascii == 'Z': return '5A'

	if ascii == 'a': return '61'
	if ascii == 'b': return '62'
	if ascii == 'c': return '63'
	if ascii == 'd': return '64'
	if ascii == 'e': return '65'
	if ascii == 'f': return '66'
	if ascii == 'g': return '67'
	if ascii == 'h': return '68'
	if ascii == 'i': return '69'
	if ascii == 'j': return '6A'
	if ascii == 'k': return '6B'
	if ascii == 'l': return '6C'
	if ascii == 'm': return '6D'
	if ascii == 'n': return '6E'
	if ascii == 'o': return '6F'
	if ascii == 'p': return '70'
	if ascii == 'q': return '71'
	if ascii == 'r': return '72'
	if ascii == 's': return '73'
	if ascii == 't': return '74'
	if ascii == 'u': return '75'
	if ascii == 'v': return '76'
	if ascii == 'w': return '77'
	if ascii == 'x': return '78'
	if ascii == 'y': return '79'
	if ascii == 'z': return '7A'

	if ascii == ' ': return '20'
	if ascii == '!': return '21'
	if ascii == '"': return '22'
	if ascii == '#': return '23'
	if ascii == '$': return '24'
	if ascii == '%': return '25'
	if ascii == '&': return '26'
	if ascii == "'": return '27'
	if ascii == '(': return '28'
	if ascii == ')': return '29'
	if ascii == '*': return '2A'
	if ascii == '+': return '2B'
	if ascii == ',': return '2C'
	if ascii == '-': return '2D'
	if ascii == '.': return '2E'
	if ascii == '/': return '2F'

	if ascii == ':': return '3A'
	if ascii == ';': return '3B'
	if ascii == '<': return '3C'
	if ascii == '=': return '3D'
	if ascii == '>': return '3E'
	if ascii == '?': return '3F'
	if ascii == '@': return '40'

	if ascii == '[': return '5B'
	if ascii == "\\": return '5C'
	if ascii == ']': return '5D'
	if ascii == '^': return '5E'
	if ascii == '_': return '5F'
	if ascii == '`': return '60'

	if ascii == '{': return '7B'
	if ascii == '|': return '7C'
	if ascii == '}': return '7D'
	if ascii == '~': return '7E'	

	