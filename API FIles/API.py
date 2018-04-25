import requests

try:
    r = requests.get('https://restcountries.eu/rest/v2/currency/inr')
    if r.status_code == 200:
        response = r.json()
        # Validate details for Bhutan
        if response[0]['name'] == 'Bhutan':
            if response[0]['capital'] != 'Thimphu':
                print('Capital did not match')
            if response[0]['region'] != 'Asia':
                print('Region did not match')
            if response[0]['population'] != 775620:
                print('Population did not match')
            if response[0]['currencies'][0]['code'] != 'BTN' or response[0]['currencies'][0]['name'] != 'Bhutanese ngultrum' or response[0]['currencies'][0]['symbol'] != 'Nu.':
                print('Currency BTN did not match')
            if response[0]['currencies'][1]['code'] != 'INR' or response[0]['currencies'][1]['name'] != 'Indian rupee' or response[0]['currencies'][1]['symbol'] != '₹':
                print('Currency INR did not match')
        else:
            print('1st country is not Bhutan')
        # Validate details for India
        if response[1]['name'] == 'India':
            if response[1]['capital'] != 'New Delhi':
                print('Capital did not match')
            if response[1]['region'] != 'Asia':
                print('Region did not match')
            if response[1]['population'] != 1295210000:
                print('Population did not match')
            if response[1]['currencies'][0]['code'] != 'INR' or response[1]['currencies'][0]['name'] != 'Indian rupee' or response[1]['currencies'][0]['symbol'] != '₹':
                print('Currency INR did not match')
        else:
            print('2nd country is not India')
        # Validate details for Zimbabwe
        if response[2]['name'] == 'Zimbabwe':
            if response[2]['capital'] != 'Harare':
                print('Capital did not match')
            if response[2]['region'] != 'Africa':
                print('Region did not match')
            if response[2]['population'] != 14240168:
                print('Population did not match')
            if response[2]['currencies'][0]['code'] != 'BWP' or response[2]['currencies'][0]['name'] != 'Botswana pula' or response[2]['currencies'][0]['symbol'] != 'P':
                print('Currency BWP did not match')
            if response[2]['currencies'][1]['code'] != 'GBP' or response[2]['currencies'][1]['name'] != 'British pound' or response[2]['currencies'][1]['symbol'] != '£':
                print('Currency GBP did not match')
            if response[2]['currencies'][2]['code'] != 'CNY' or response[2]['currencies'][2]['name'] != 'Chinese yuan' or response[2]['currencies'][2]['symbol'] != '¥':
                print('Currency CNY did not match')
            if response[2]['currencies'][3]['code'] != 'EUR' or response[2]['currencies'][3]['name'] != 'Euro' or response[2]['currencies'][3]['symbol'] != '€':
                print('Currency EUR did not match')
            if response[2]['currencies'][4]['code'] != 'INR' or response[2]['currencies'][4]['name'] != 'Indian rupee' or response[2]['currencies'][4]['symbol'] != '₹':
                print('Currency INR did not match')
            if response[2]['currencies'][5]['code'] != 'JPY' or response[2]['currencies'][5]['name'] != 'Japanese yen' or response[2]['currencies'][5]['symbol'] != '¥':
                print('Currency JPY did not match')
            if response[2]['currencies'][6]['code'] != 'ZAR' or response[2]['currencies'][6]['name'] != 'South African rand' or response[2]['currencies'][6]['symbol'] != 'Rs':
                print('Currency ZAR did not match')
            if response[2]['currencies'][7]['code'] != 'USD' or response[2]['currencies'][7]['name'] != 'United States dollar' or response[2]['currencies'][7]['symbol'] != '$':
                print('Currency ZAR did not match')
        else:
            print('3rd country is not Zimbabwe')       
    else:
        print('Unable to get the response')
except Exception as e:
    print(e)