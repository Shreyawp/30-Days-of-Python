''' JavaScript Object Notation '''
import json

people_str = '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-2469",
            "emails": ["johnsmith@bogusemail.com", "john.smith@workmail.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-3563",
            "emails": null,
            "has_license": true
        }
    ]
}
'''
data = json.loads(people_str)
print(data)
print(type(data))
''' 
####################### OUTPUT ##########################
{'people': [{'name': 'John Smith', 'phone': '615-2469', 'emails': ['johnsmith@bogusemail.com', 'john.smith@workmail.com'], 'has_license': False}, {'name': 'Jane Doe', 'phone': '560-3563', 'emails': None, 'has_license': True}]}
<class 'dict'>
##########################################################
'''

print(data['people'])
print(type(data['people']))
''' 
####################### OUTPUT ##########################
[{'name': 'John Smith', 'phone': '615-2469', 'emails': ['johnsmith@bogusemail.com', 'john.smith@workmail.com'], 'has_license': False}, {'name': 'Jane Doe', 'phone': '560-3563', 'emails': None, 'has_license': True}]
<class 'list'>
##########################################################
'''

for person in data['people']:
    print(person)
''' 
####################### OUTPUT ##########################
{'name': 'John Smith', 'phone': '615-2469', 'emails': ['johnsmith@bogusemail.com', 'john.smith@workmail.com'], 'has_license': False}
{'name': 'Jane Doe', 'phone': '560-3563', 'emails': None, 'has_license': True}
##########################################################
'''

for person in data['people']:
    print(person['name'])
''' 
####################### OUTPUT ##########################
John Smith
Jane Doe
##########################################################
'''

# delete phone from dict of each person
for person in data['people']:
    del person['phone']

new_str = json.dumps(data, indent=2, sort_keys=True)
print(new_str)
''' 
####################### OUTPUT ##########################
{
  "people": [
    {
      "emails": [
        "johnsmith@bogusemail.com",
        "john.smith@workmail.com"
      ],
      "has_license": false,
      "name": "John Smith"
    },
    {
      "emails": null,
      "has_license": true,
      "name": "Jane Doe"
    }
  ]
}
##########################################################
'''

with open('./data/states.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'], state['abbreviation'])

''' 
####################### OUTPUT ##########################
Alabama AL
Alaska AK
Arizona AZ
Arkansas AR
California CA
Colorado CO
##########################################################
'''

for state in data['states']:
    del state['area_codes']

with open('./data/new_states.json', 'w') as f:
    json.dump(data, f, indent=2)


import requests

response = requests.get('https://open.er-api.com/v6/latest/USD')
data = response.text
#print(data)

data_src = json.loads(data)

print(json.dumps(data_src, indent=2))
''' 
####################### OUTPUT ##########################
{
  "result": "success",
  "provider": "https://www.exchangerate-api.com",
  "documentation": "https://www.exchangerate-api.com/docs/free",
  "terms_of_use": "https://www.exchangerate-api.com/terms",
  "time_last_update_unix": 1753660951,
  "time_last_update_utc": "Mon, 28 Jul
##########################################################
'''

print("Total number of country rates: ", len(data_src['rates']))
# >> Total number of country rates:  163

# for currency,rate in data_src['rates'].items():
#     print(currency, rate)
# OR
for currency in data_src['rates']:
    rate = data_src['rates'][currency]
    print(currency, rate) 
''' 
####################### OUTPUT ##########################
USD 1
AED 3.6725
AFN 68.603716
ALL 83.43285
AMD 384.018282
##########################################################
'''
usd_rates = {}
for currency in data_src['rates']:
    rate = data_src['rates'][currency]
    usd_rates[currency] = rate

print(f"50 USD = %.2f EUR" %(50 * usd_rates['EUR']))
# >> 50 USD = 43.03225 EUR
print(f"50 USD = %.2f INR" %(50 * usd_rates['INR']))
# >> 50 USD = 4336.49 INR
