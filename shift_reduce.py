gram = {
	"S":["IF b THEN s ELSE a","(IF b THEN a"]
}
starting_terminal = "S"
inp = "IF b THEN (IF b THEN b) ELSE b$"

stack = "$"
print(f'{"Stack": <40}'+"|"+f'{"Input Buffer": <30}'+"|"+f'Parsing Action')
print(f'{"-":-<100}')

while True:
	action = True
	i = 0
	while i<len(gram[starting_terminal]):
		if gram[starting_terminal][i] in stack:
			stack = stack.replace(gram[starting_terminal][i],starting_terminal)
			print(f'{stack: <40}'+"|"+f'{inp: <30}'+"|"+f'Reduce S->{gram[starting_terminal][i]}')
			i=-1
			action = False
		i+=1
	if len(inp)>1:
		stack+=inp[0]
		inp=inp[1:]
		print(f'{stack: <40}'+"|"+f'{inp: <30}'+"|"+f'Shift')
		action = False
	if inp == "$" and stack == ("$"+starting_terminal):
		print(f'{stack: <40}'+"|"+f'{inp: <30}'+"|"+f'Accepted')
		break

	if action:
		print(f'{stack: <40}'+"|"+f'{inp: <30}'+"|"+f'Rejected')
		break
