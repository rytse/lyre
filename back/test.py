from lnlp import parse_sentance

(e, d, a) = parse_sentance('There\'s a fire at McDonalds.', 38.9097, -77.0433)
print(f'Emergency: {e}\nDispatch: {d}\nAddress: {a}\n\n')

(e, d, a) = parse_sentance('I need a helo sent to McDonalds.', 38.9097, -77.0433)
print(f'Emergency: {e}\nDispatch: {d}\nAddress: {a}\n\n')

(e, d, a) = parse_sentance('I have a guy that needs medivac from Starbucks.', 39.051600, -77.174820)
print(f'Emergency: {e}\nDispatch: {d}\nAddress: {a}\n\n')
