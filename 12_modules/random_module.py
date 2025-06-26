import random

# random() method - generates random value between 0 and 1
value = random.random()
print(value)
# >> 0.467527645149853

# uniform() method - generates random floating point num between given num range
value = random.uniform(1, 10)
print(value)
# >> 6.986557762968738

# randint() method - generates random integer num  between given range
value = random.randint(0,1)  # example of coin: Heads - 1, Tails - 0
print(value)
# >> 1

# choice() method - select one random value from given sequence
greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola'] 
value = random.choice(greetings)
print(value + ', Eric!')
# >> Hey, Eric!

# choices() - select more than one or k random value from given sequence 
# example: one ball has chance of landing in one of the color pockets 
colors = ['Red', 'Black' ,'Green']
results = random.choices(colors, k=10)
print(results)
# >> ['Red', 'Black', 'Black', 'Red', 'Green', 'Red', 'Black', 'Red', 'Red', 'Red']

# weight attribute for likeliness of each item in sequence
results = random.choices(colors, weights=[18, 18 ,2], k=10)
print(results)
# >> ['Black', 'Red', 'Black', 'Red', 'Black', 'Black', 'Red', 'Red', 'Red', 'Black']

# shuffle() - to shuffle sequence
# Example : deck of playing cards
deck = list(range(1,53))
random.shuffle(deck)
print(deck)
# >> [44, 18, 23, 40, 38, 16, 51, 8, 32, 19, 10, 3, 49, 36, 24, 33, 39, 30, 9, 47, 45, 34, 41, 25, 21, 28, 2, 7, 13, 27, 31, 35, 52, 29, 6, 15, 37, 22, 42, 12, 46, 20, 11, 17, 1, 26, 4, 5, 43, 48, 14, 50]

# sample() - to generate k unique samples
hand = random.sample(deck, k=5)
print(hand)
# >> [49, 1, 20, 39, 17]


# Example: create random names with their details 
first_name = ['Harry', 'Ron', 'Hermione', 'Ginny', 'Neville', 'Luna', 'Percy', 'Lucas', ]
last_name = ['Potter', 'Weasley', 'Granger', 'Longbottom', 'Lovegood', 'Jackson', 'Malfoy']

street_names = ['Daigon Valley', '4th Avenue', 'Main Street', 'Oak', 'Park', 'Pine', 'Elm']
cities = ['Metropolis', 'South Park', 'Manhattan', 'Sunnydale', 'Metropolis', 'Alantis']
states = ['AL', 'AR', 'CA', 'DN', 'GA', 'FL', 'HI', 'IN', 'YM', 'AU']

for num in range(5):
    first = random.choice(first_name)
    last = random.choice(last_name)

    phone = f'{random.randint(100, 999)}-555-{random.randint(1000, 9999)}'

    street_num = random.randint(100, 999)
    street = random.choice(street_names)
    city = random.choice(cities)
    state = random.choice(states)
    zip_code = random.randint(10000, 99999)
    address = f'{street_num} {street} St., {city} {state} {zip_code}'

    email = first.lower() + last.lower() + '@xyzmail.com'

    print(f'{first} {last}\n{phone}\n{address}\n{email}\n')


''' 
####################### OUTPUT ##########################
Percy Weasley
636-555-3190
300 Park St., Sunnydale IN 96185
percyweasley@xyzmail.com

Percy Granger
893-555-3049
569 Main Street St., Sunnydale IN 58757
percygranger@xyzmail.com

Ginny Granger
469-555-9326
349 Daigon Valley St., Metropolis CA 66417
ginnygranger@xyzmail.com

Neville Lovegood
226-555-1114
524 Park St., Sunnydale HI 30471
nevillelovegood@xyzmail.com

Neville Malfoy
989-555-6177
721 4th Avenue St., Sunnydale AL 84968
nevillemalfoy@xyzmail.com

##########################################################
'''
