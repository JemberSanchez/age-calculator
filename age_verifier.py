name = input('Whats your name?') 
age = int(input('How old are you?'))
if age < 13:
 print(f'im sorry, {name}, you cant register.')
elif age < 18:
 print(f'{name}, You can register with adult permission.')
elif age < 65: 
 print(f'{name}, You can register freely.')
else:
 print(f'{name}, Do you need help registering?')