
# ---
# name: currency-converter
# description: |
#
#   ### Description
#   Converts a value to another currency using the https://exchangeratesapi.io API.
#
#   ### Sample Usage
#
#   =FLEX(":team/currency-convert",A10,\$A$1,\$A$2)
#   =FLEX(":team/currency-convert",A10,\$A$1,\$A$2,"2019-01-31)
#   =FLEX(":team/currency-convert",100,"USD","EUR","2019-01-31")
#
#   ### Syntax
#
#   FLEX(":team/currency-convert", amt, cur1, cur2, [date])
#
#   Property | Type | Description
#   ---------- | ---------- | ----------
#   `amt` | number | The value to convert from one currency to another
#   `cur1` | string | The currency to convert from (e.g. "USD", "EUR")
#   `cur2` | string | The currency to convert to (e.g. "USD", "EUR")
#   `[date]` | string | (optional) The exchange rate date in YYYY-DD-MM format.
#
# deployed: true
# ---


import json
import requests
from datetime import *
from cerberus import Validator
from collections import OrderedDict

# main function entry point
def flexio_handler(flex):
    result = getresult(flex)
    flex.output.write(result)

def getresult(flex):

    # get the input
    input = flex.input.read()
    try:
        input = json.loads(input)
        if not isinstance(input, list): raise ValueError
    except ValueError:
        raise ValueError

    # define the expected parameters and map the values to the parameter names
    # based on the positions of the keys/values
    params = OrderedDict()
    params['amt'] = {'required': True, 'type': 'number'}
    params['cur1'] = {'required': True, 'validator': validate_currency, 'coerce': lambda s: s.upper()}
    params['cur2'] = {'required': True, 'validator': validate_currency, 'coerce': lambda s: s.upper()}
    params['date'] = {'required': False, 'type': 'date', 'coerce': lambda s: datetime.strptime(s, '%Y-%m-%d')}
    input = dict(zip(params.keys(), input))

    # validate the mapped input against the validator
    # if the input is valid return an error
    v = Validator(params, allow_unknown = True)
    input = v.validated(input)
    if input is None:
        raise ValueError

    try:

        date = 'latest';
        if 'date' in input.keys():
            date = input['date'].strftime('%Y-%m-%d')

        if input['cur1'] == input['cur2']:
            return input['amt']

        url = 'https://api.exchangeratesapi.io/'+date+'?base=' + input['cur1']
        response = requests.get(url)
        rates = response.json()['rates']

        conversion_rate = rates[input['cur2']]
        return input['amt']*conversion_rate

    except:
        raise RuntimeError


def validate_currency(field, value, error):

    currency_types = [
        'CAD','HKD','ISK','PHP','DKK','HUF','CZK','GBP','RON','SEK',
        'IDR','INR','BRL','RUB','HRK','JPY','THB','CHF','EUR','MYR',
        'BGN','TRY','CNY','NOK','NZD','ZAR','USD','MXN','SGD','AUD',
        'ILS','KRW','PLN'
    ]
    if any(value in c for c in currency_types):
        return

    error(field, 'is an invalid currency type')
