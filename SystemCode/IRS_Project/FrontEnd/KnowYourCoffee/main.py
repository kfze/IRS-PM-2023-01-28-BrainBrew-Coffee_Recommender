# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


from flask import Flask, render_template, url_for, request
import requests
import json
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


@app.route('/products')
def products():
    return render_template('products.html')


@app.route('/store')
def store():
    return render_template('store.html')


@app.route('/recommendation', methods=['POST', 'GET'])
def recommend():
    url = "http://localhost:8899/recommendCoffee"
    if request.method == 'POST':
        timeOfDay = request.form.get('timeOfDay')
        coffeeType = request.form.get('coffee-type')
        flavour = request.form.getlist('flavour')
        fruitType = request.form.getlist('fruitExpend')
        # origin = request.form.get('origin')
        json_data = {"timeOfDay": timeOfDay, "coffee-type": coffeeType, "flavour": flavour, "fruitType": fruitType}
        headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
        response = requests.post(url, json=json_data, headers=headers)
        apiresponse = response.json()
        return render_template('products.html', CoffeeRecommend1=apiresponse['Recommendations'][0]['name'], CoffeeDescription1=apiresponse['Recommendations'][0]['cuppingNotes'], CoffeeFor1=apiresponse['Recommendations'][0]['recommendedFor'], CoffeeOrigin1=apiresponse['Recommendations'][0]['origin'],
                               CoffeeRecommend2=apiresponse['Recommendations'][1]['name'], CoffeeDescription2=apiresponse['Recommendations'][1]['cuppingNotes'], CoffeeFor2=apiresponse['Recommendations'][1]['recommendedFor'], CoffeeOrigin2=apiresponse['Recommendations'][1]['origin'],
                               CoffeeRecommend3=apiresponse['Recommendations'][2]['name'], CoffeeDescription3=apiresponse['Recommendations'][2]['cuppingNotes'], CoffeeFor3=apiresponse['Recommendations'][2]['recommendedFor'], CoffeeOrigin3=apiresponse['Recommendations'][2]['origin'])
    
        #return apiresponse


if __name__ == '__main__':
    app.run(debug=True)

    app.jinja_env.auto_reload = True
