name = input('whats your name?:')
current_age = int(input('your age now?:'))
current_year = 2025 
future_year = int(input('in what year do you want to know your age?:'))
future_age = current_age + (future_year - current_year)                
print(f'{name},In the year {future_year} you will be {future_age} years old.')