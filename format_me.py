OUTPUT_PREFIX = 'Result'

input_number = 42

modulo = input_number % 2

if modulo:
    result = 'odd'
else:
    result = 'even'

print(f'{OUTPUT_PREFIX}: number {input_number} is {result}, since division remainder is {modulo}.')